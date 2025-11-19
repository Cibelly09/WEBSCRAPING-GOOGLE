<div align="center">

# 📰🤖 WebScraping — Monitoramento Automático de Notícias  
Pipeline automatizado para coleta, filtragem e exportação de notícias utilizando Google News.

</div>

---

<div align="center">

## 🎯 Objetivo Geral

Demonstrar uma automação completa que realiza busca de notícias na web, extrai informações relevantes (título, trecho, link e data), aplica filtros temáticos e exporta o resultado para análises profissionais ou uso em pipelines.

</div>

---

<div align="center">

# 1️⃣ Coleta e Processamento das Notícias

## 🔍 Objetivo  
Extrair automaticamente notícias de múltiplas buscas no Google News, simulando um navegador real.

<br>

## 📌 Etapas Realizadas  
✔ Montagem dinâmica da URL de busca  
✔ Extração de título, trecho, link e data relativa  
✔ Identificação de notícias recentes  
✔ Tratamento de HTML com BeautifulSoup  
✔ Organização dos resultados em lista estruturada  

<br>

## 🖼️ Exemplos de Código  
*(Substitua as imagens abaixo pelas suas)*  

![Função Scraping](imgs/funcao_scraping.png)  
![Loop Buscas](imgs/loop_buscas.png)

</div>

---

<div align="center">

# 2️⃣ Filtragem de Notícias

## 🧪 Objetivo  
Selecionar apenas notícias relevantes com base em palavras-chave configuráveis.

<br>

## 📌 Etapas  
✔ Definição de lista de palavras-chave  
✔ Combinação de título + trecho  
✔ Busca por termos críticos (risco, desabamento, irregularidade etc.)  
✔ Lista final com apenas itens relevantes ao tema  

<br>

## 🖼️ Código da Filtragem  
![Filtro Keywords](imgs/filtro_keywords.png)

</div>

---

<div align="center">

# 3️⃣ Exportação dos Resultados

## 📦 Objetivo  
Gerar automaticamente o arquivo consolidado das notícias em formato CSV para BI e relatórios.

<br>

## 📌 Saída Final  
`noticias_construcao.csv` contendo:  

- Título  
- Trecho  
- Link  
- Data relativa  
- Termo de origem (busca que encontrou a notícia)

<br>

## 🖼️ Exportação  
![Export CSV](imgs/export_csv.png)

</div>

---

<div align="center">

# 4️⃣ Tecnologias Utilizadas

Python  
Requests  
BeautifulSoup  
Time  
CSV  

</div>

---

<div align="center">

# 🧩 5️⃣ Estrutura do Projeto

