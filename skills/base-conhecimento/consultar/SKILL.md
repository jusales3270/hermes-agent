---
name: consultar-base-conhecimento
description: Consultar a base de conhecimento da empresa (documentos e planilhas enviados pelos departamentos via dashboard). Use SEMPRE que precisar de dados reais do negocio — numeros financeiros, listas de maquinas/produtos, relatorios, vendas, estoque, RH.
platforms: [linux]
---

# Base de Conhecimento da Empresa

Dados reais do negocio que os departamentos enviaram pelo dashboard. Os arquivos foram convertidos em Markdown e indexados num servico HTTP interno chamado Docling, acessivel em http://docling:3002.

## REGRA CRITICA

Os arquivos NAO estao no seu sistema de arquivos local. NAO use search_files, ls, find ou read_file para procura-los. A base e acessada SOMENTE via HTTP, usando a ferramenta terminal com Python urllib (curl e barrado pelo scan de seguranca).

Antes de afirmar qualquer numero, fato ou detalhe do negocio, CONSULTE a base. Nunca invente. Se nao houver documento que sustente a resposta, diga isso claramente. Sempre cite o arquivo e o departamento de onde tirou a informacao.

## Metodo principal: BUSCA SEMANTICA (/search)

Para a maioria das perguntas, use a busca semantica. Ela retorna apenas os trechos relevantes a pergunta — rapido e eficiente. Prefira SEMPRE este metodo em vez de ler o arquivo inteiro.

Execute via terminal (ajuste a query e o department):

    python3 -c "import urllib.request,json; body=json.dumps({'query':'quantos tornos CNC existem','department':'financeiro','match_count':5}).encode(); req=urllib.request.Request('http://docling:3002/search',data=body,headers={'Content-Type':'application/json'},method='POST'); print(urllib.request.urlopen(req,timeout=60).read().decode())"

Parametros:
- query: a pergunta em linguagem natural (o que voce quer encontrar)
- department: financeiro, vendas, compras, rh, estoque ou geral. Use null para buscar em todos.
- match_count: quantos trechos retornar (5 e um bom padrao)

A resposta traz uma lista de trechos (content) com a similaridade. Use esses trechos para responder.

## Quando listar os documentos disponiveis (/list)

Se precisar saber o que existe na base:

    python3 -c "import urllib.request; print(urllib.request.urlopen('http://docling:3002/list').read().decode())"

## Quando ler um documento inteiro (/read)

Use SOMENTE quando precisar do documento completo (ex: gerar um relatorio que cobre tudo). Para perguntas pontuais, prefira /search.

    python3 -c "import urllib.request,urllib.parse; d=urllib.parse.quote('financeiro'); f=urllib.parse.quote('NOME DO ARQUIVO.md'); print(urllib.request.urlopen('http://docling:3002/read?department='+d+'&file='+f).read().decode())"

## Analisar e responder

Com os trechos em maos, responda citando a fonte (arquivo + departamento). Cruze dados de multiplos departamentos quando fizer sentido — esse cruzamento e seu maior valor.

## Departamentos

financeiro, vendas, compras, rh, estoque, geral
