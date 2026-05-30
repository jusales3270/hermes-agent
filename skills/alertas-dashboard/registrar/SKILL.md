---
name: registrar-alerta-dashboard
description: Registrar um alerta no dashboard do BusinessOS para aparecer na Central de Alertas. Use sempre que o monitoramento detectar algo digno da atenção do dono.
platforms: [linux]
---

# Registrar Alerta no Dashboard

Quando o monitoramento detectar uma exceção que merece a atenção do dono, registre o alerta no dashboard além de avisar pelo canal de mensagens.

Esta skill traz um script pronto que faz isso de forma confiável. NAO monte requisicoes curl na mao — use o script.

## Como registrar

Execute o script via terminal, passando os argumentos nesta ordem: severity, titulo, descricao e departamento.

    python3 ~/skills/alertas-dashboard/registrar/registrar_alerta.py "danger" "Margem caiu para 12% em maio" "A margem despencou de 43% para 12% por causa de despesas fora do padrao. Lucro de apenas R$ 4.000." "financeiro"

## Argumentos

1. severity: "danger" para algo critico (lucro negativo, margem colapsando, risco imediato) ou "warning" para algo que merece atencao mas nao e grave (despesa fora do padrao, tendencia preocupante).
2. titulo: curto e direto, entre aspas.
3. descricao: explicacao com numeros concretos e o porque de importar, entre aspas.
4. departamento: financeiro, vendas, compras, rh, estoque ou geral.

## Confirmacao

A saida deve conter {"ok":true,...}. Se aparecer ERRO, o alerta nao foi registrado — nesse caso, avise o dono pelo canal de mensagens mesmo assim.
