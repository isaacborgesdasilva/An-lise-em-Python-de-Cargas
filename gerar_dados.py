# -*- coding: utf-8 -*-
"""
Gerador de dados simulados para o projeto de Gestão de Transporte de Cargas.
Cria uma base de viagens (entregas) com informações operacionais, financeiras
e de desempenho, salvando em dados/cargas.csv
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N = 1200  # número de viagens/registros

# --- Dimensões básicas -------------------------------------------------
filiais = ["Mossoró", "Natal", "Fortaleza", "João Pessoa", "Recife"]
destinos = [
    "Natal", "Fortaleza", "João Pessoa", "Recife", "Mossoró",
    "Assú", "Caicó", "Currais Novos", "Parnamirim", "Sousa"
]
tipos_veiculo = ["Van", "Caminhão 3/4", "Caminhão Toco", "Caminhão Truck", "Carreta"]
motoristas = [f"Motorista {i:02d}" for i in range(1, 21)]
status_entrega = ["Entregue no prazo", "Entregue com atraso", "Cancelada", "Em rota"]
status_pesos = [0.72, 0.18, 0.04, 0.06]

capacidade_kg = {
    "Van": 1500,
    "Caminhão 3/4": 3500,
    "Caminhão Toco": 6000,
    "Caminhão Truck": 14000,
    "Carreta": 27000,
}

custo_km_base = {
    "Van": 1.8,
    "Caminhão 3/4": 2.6,
    "Caminhão Toco": 3.4,
    "Caminhão Truck": 4.5,
    "Carreta": 6.2,
}

# --- Geração de datas ao longo de 12 meses -----------------------------
data_inicio = datetime(2025, 7, 1)
datas = [data_inicio + timedelta(days=int(d)) for d in np.random.randint(0, 365, N)]

# --- Montagem do dataframe ----------------------------------------------
registros = []
for i in range(N):
    filial = np.random.choice(filiais)
    destino = np.random.choice([d for d in destinos if d != filial])
    veiculo = np.random.choice(tipos_veiculo, p=[0.25, 0.25, 0.2, 0.2, 0.1])
    motorista = np.random.choice(motoristas)

    distancia_km = round(np.random.uniform(30, 850), 1)
    peso_kg = round(np.random.uniform(200, capacidade_kg[veiculo]), 1)
    ocupacao = round(peso_kg / capacidade_kg[veiculo] * 100, 1)

    custo_km = custo_km_base[veiculo] * np.random.uniform(0.9, 1.15)
    custo_combustivel = round(distancia_km * custo_km, 2)
    custo_pedagio = round(distancia_km * np.random.uniform(0.05, 0.15), 2)
    custo_motorista = round(distancia_km * np.random.uniform(0.3, 0.5), 2)
    custo_total = round(custo_combustivel + custo_pedagio + custo_motorista, 2)

    frete_cobrado = round(custo_total * np.random.uniform(1.15, 1.55), 2)
    margem = round(frete_cobrado - custo_total, 2)

    tempo_previsto_h = round(distancia_km / np.random.uniform(45, 65), 1)
    atraso_h = 0.0
    status = np.random.choice(status_entrega, p=status_pesos)
    if status == "Entregue com atraso":
        atraso_h = round(np.random.uniform(0.5, 8), 1)
    tempo_real_h = round(tempo_previsto_h + atraso_h, 1)

    avaliacao_cliente = None
    if status in ["Entregue no prazo", "Entregue com atraso"]:
        base_nota = 4.6 if status == "Entregue no prazo" else 3.3
        avaliacao_cliente = round(np.clip(np.random.normal(base_nota, 0.6), 1, 5), 1)

    registros.append({
        "id_viagem": f"V{i+1:05d}",
        "data": datas[i].strftime("%Y-%m-%d"),
        "filial_origem": filial,
        "destino": destino,
        "tipo_veiculo": veiculo,
        "motorista": motorista,
        "distancia_km": distancia_km,
        "peso_kg": peso_kg,
        "capacidade_kg": capacidade_kg[veiculo],
        "ocupacao_pct": ocupacao,
        "custo_combustivel": custo_combustivel,
        "custo_pedagio": custo_pedagio,
        "custo_motorista": custo_motorista,
        "custo_total": custo_total,
        "frete_cobrado": frete_cobrado,
        "margem": margem,
        "tempo_previsto_h": tempo_previsto_h,
        "tempo_real_h": tempo_real_h,
        "atraso_h": atraso_h,
        "status_entrega": status,
        "avaliacao_cliente": avaliacao_cliente,
    })

df = pd.DataFrame(registros)
df.sort_values("data", inplace=True)
df.to_csv("dados/cargas.csv", index=False, encoding="utf-8-sig")

print(f"Base gerada com sucesso: {len(df)} registros -> dados/cargas.csv")
print(df.head())
