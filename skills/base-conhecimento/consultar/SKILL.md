---
name: consultar-base-conhecimento
description: Consultar a base de conhecimento da empresa (documentos e planilhas enviados pelos departamentos via dashboard). Use SEMPRE que precisar de dados reais do negócio — números financeiros, listas de máquinas/produtos, relatórios, vendas, estoque, RH.
platforms: [linux]
---

# Base de Conhecimento da Empresa

Dados reais do negócio que os departamentos enviaram pelo dashboard. Os arquivos foram convertidos em Markdown e ficam num serviço HTTP interno chamado Docling.

## REGRA CRÍTICA

Os arquivos NÃO estão no seu sistema de arquivos local. NÃO use search_files, ls, find ou read_file para procurá-los — eles NÃO estão no disco desta máquina.

A base é acessada SOMENTE via HTTP, no endereço http://docling:3002, usando a ferramenta terminal com curl.

Antes de afirmar qualquer número, fato ou detalhe do negócio, CONSULTE a base. Nunca invente. Se não houver documento que sustente a resposta, diga isso claramente. Sempre cite o arquivo e o departamento de onde tirou a informação.

## Passo 1 — Listar os documentos disponíveis

curl -s http://docling:3002/list

Retorna JSON com os arquivos e seus departamentos.

## Passo 2 — Ler um documento

Passe department e file como parâmetros de URL. Codifique espaços como %20:

curl -s "http://docling:3002/read?department=financeiro&file=NOME%20DO%20ARQUIVO.md"

O conteúdo Markdown vem no campo content.

## Passo 3 — Analisar e responder

Com o conteúdo, responda citando a fonte (arquivo + departamento). Cruze dados de múltiplos departamentos quando fizer sentido — esse cruzamento é seu maior valor.

## Departamentos

financeiro, vendas, compras, rh, estoque, geral
