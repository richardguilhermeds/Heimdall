<div align="center">

<img src="images\heimdall_readme.jpg" alt="Heimdall" width="640"/>

# 🛡️ Heimdall

**O guardião do Sistema Financeiro Nacional.**

*Na mitologia nórdica, Heimdall vigia o Bifröst e enxerga os nove reinos. Aqui, ele vigia o SFN e enxerga todos os bancos. Capital, liquidez, crédito e rentabilidade*.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![BACEN](https://img.shields.io/badge/Fonte-BACEN%20IF.data-0b3d91)
![License](https://img.shields.io/badge/License-MIT-22d3ee)

</div>

---

## Visão geral

**Heimdall** é um dashboard que consome dados públicos do Banco Central do Brasil e exibe as principais métricas regulatórias de bancos brasileiros, sempre acompanhadas dos limites regulatórios que as governam.

> *"Nenhuma instituição passa pela ponte sem ser vista."*

---

## ✨ Funcionalidades

| | Recurso | Descrição |
|---|---|---|
| 📊 | **Painel de Capital** | Índice de Basileia, CET1, Nível I, RWA e Alavancagem com *gauges* coloridos (verde / amarelo / vermelho) |
| 💧 | **Liquidez** | LCR e NSFR contra o piso de 100% |
| 🩺 | **Qualidade de crédito** | Inadimplência +90d, cobertura de PDD e distribuição por estágio (IFRS 9 / Res. 4.966) |
| 💰 | **Rentabilidade** | ROE, ROA, margem financeira (NIM) e índice de eficiência |
| ⚖️ | **Comparativo entre bancos** | Ranking e *heatmap* de métricas entre instituições do mesmo segmento prudencial |
| 🚨 | **Alertas regulatórios** | Destaque automático quando uma instituição fica abaixo do mínimo exigido |
| 📈 | **Série histórica** | Evolução trimestral dos índices (dados do IF.data desde 2000) |
| 📥 | **Exportação** | Relatórios em PDF e Excel das métricas selecionadas |

---

## 🌈 Identidade visual

A marca é construída sobre dois símbolos: **o olho que tudo vê** e o **Bifröst**, a ponte de arco-íris.

**Paleta: "Bifröst sobre Asgard noturna"**

| Cor | Hex | Uso |
|---|---|---|
| ⬛ Noite de Asgard | `#0b1120` | Fundo principal |
| 🟦 Azul vigília | `#38bdf8` | Destaques, ícones, links |
| 🟪 Violeta | `#7c3aed` | Início do gauge (risco baixo) |
| 🟦 Azul / Ciano | `#2563eb` → `#06b6d4` | Faixa intermediária |
| 🟧 Âmbar | `#f59e0b` | Atenção |
| 🟥 Vermelho | `#ef4444` | Abaixo do limite regulatório |
| ⬜ Branco gelo | `#f8fafc` | Texto principal |

**Tipografia:** *Georgia* (serifada, para o wordmark — peso institucional) + *Courier* (monoespaçada, para tags normativas) + uma sem-serifa limpa no corpo do app.

---

## 🏗️ Arquitetura

```
heimdall/
├── app.py                      # Entrada principal (Streamlit)
├── data/
│   ├── raw
│   └── processed
└── images/
    └── heimdall_readme.jpg
├── pages/
│   ├── 1_capital.py
│   ├── 2_liquidez.py
│   ├── 3_credito.py
│   ├── 4_rentabilidade.py
│   └── 5_comparativo.py
├── pipelines/
│   └── jobs/
    └── notebooks/

```

---

## 🔌 Fontes de dados

Todas públicas e gratuitas:

- **IF.data (BACEN)** — balanços, capital e liquidez por instituição
- **SGS (BACEN)** — séries temporais macroeconômicas
- **CVM** — demonstrações financeiras de bancos de capital aberto

---

## 📜 Aviso

Projeto **educacional / de portfólio**. As métricas são calculadas a partir de dados públicos e não constituem aconselhamento financeiro, regulatório ou de investimento.

---

<div align="center">

*Construído por Richard, cientista de dados apaixonado pelo mercado de crédito"

**Heimdall vê tudo. Bom proveito.**

⚡
</div>