# Análise de Dados — Gestão de Transporte de Cargas

Projeto em Python para análise de indicadores operacionais e financeiros de uma
operação de transporte de cargas (frete rodoviário): custos, receitas, margem,
ocupação da frota, prazos de entrega, avaliação de clientes e desempenho de motoristas.

## Estrutura do projeto

```
gestao_transporte_cargas/
├── gerar_dados.py          # Gera uma base simulada de 1.200 viagens (dados/cargas.csv)
├── analise.py              # Script principal: calcula KPIs, gera gráficos e relatório
├── requirements.txt        # Dependências do projeto
├── dados/
│   └── cargas.csv          # Base de dados (viagens/entregas)
├── graficos/                # Gráficos gerados em PNG
└── relatorios/
    └── relatorio_resumo.txt # Relatório-texto com todos os indicadores
```

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. (Opcional) Gere uma nova base de dados simulada:
   ```bash
   python3 gerar_dados.py
   ```
   Ou substitua `dados/cargas.csv` pelos seus dados reais, mantendo as mesmas colunas.

3. Rode a análise:
   ```bash
   python3 analise.py
   ```

Isso irá gerar 6 gráficos em `graficos/` e um relatório completo em
`relatorios/relatorio_resumo.txt`, além de imprimir o resumo no terminal.

## Colunas da base de dados (`dados/cargas.csv`)

| Coluna              | Descrição                                            |
|---------------------|-------------------------------------------------------|
| id_viagem           | Identificador único da viagem                         |
| data                | Data da viagem                                        |
| filial_origem       | Filial/origem da carga                                |
| destino             | Cidade de destino                                     |
| tipo_veiculo        | Van, Caminhão 3/4, Toco, Truck ou Carreta              |
| motorista           | Motorista responsável                                 |
| distancia_km        | Distância percorrida (km)                             |
| peso_kg             | Peso da carga transportada (kg)                       |
| capacidade_kg       | Capacidade máxima do veículo (kg)                     |
| ocupacao_pct        | % de ocupação da capacidade do veículo                |
| custo_combustivel   | Custo estimado de combustível (R$)                    |
| custo_pedagio       | Custo estimado de pedágio (R$)                        |
| custo_motorista     | Custo estimado de mão de obra (R$)                    |
| custo_total         | Soma dos custos (R$)                                  |
| frete_cobrado       | Valor do frete cobrado do cliente (R$)                |
| margem              | frete_cobrado - custo_total (R$)                      |
| tempo_previsto_h    | Tempo previsto de viagem (h)                          |
| tempo_real_h        | Tempo real de viagem (h)                              |
| atraso_h            | Horas de atraso (0 se no prazo)                       |
| status_entrega      | Entregue no prazo / com atraso / Cancelada / Em rota  |
| avaliacao_cliente   | Nota do cliente (1 a 5), quando aplicável              |

## Indicadores (KPIs) calculados

- Total de viagens, cancelamentos e % de entregas no prazo
- Distância total percorrida e peso total transportado
- Ocupação média da frota (uso da capacidade)
- Receita, custo e margem totais e por km
- Ranking de destinos por receita e margem
- Desempenho por tipo de veículo (ocupação, custo médio, margem média)
- Ranking de motoristas por avaliação e por índice de atrasos

## Gráficos gerados

1. Receita, custo e margem por mês (linha)
2. Distribuição do status das entregas (pizza)
3. Top 10 destinos por receita (barras)
4. Ocupação média por tipo de veículo, com linha de meta (barras)
5. Relação distância x custo total por viagem (dispersão)
6. Avaliação média dos clientes por mês (linha)

## Adaptando para dados reais

Basta substituir `dados/cargas.csv` por um arquivo com as mesmas colunas
(pode ter menos colunas — ajuste `analise.py` removendo os cálculos que
dependam de campos ausentes). O script `analise.py` não depende do gerador
de dados simulados.
