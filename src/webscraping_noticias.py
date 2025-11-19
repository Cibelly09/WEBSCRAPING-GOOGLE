# -*- coding: utf-8 -*-
"""
Web Scraping de Notícias - Versão Premium
Autor: Cibelly Viegas
Descrição:
    Este script automatiza a busca, coleta e filtragem de notícias
    a partir do Google News, permitindo:
        - múltiplos termos de busca
        - captura de título, resumo, link e data relativa
        - filtro por palavras-chave
        - salvamento em CSV
"""

import requests
from bs4 import BeautifulSoup
import time
import csv


# -------------------------------------------------------------
# 1️⃣ Função principal de raspagem
# -------------------------------------------------------------
def buscar_noticias(termo):
    termo_formatado = termo.replace(" ", "+")
    url = f"https://www.google.com/search?q={termo_formatado}&tbm=nws&hl=pt-BR"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    resposta = requests.get(url, headers=headers)
    sopa = BeautifulSoup(resposta.text, "html.parser")

    resultados = []

    for item in sopa.find_all("div", class_="dbsr"):
        try:
            titulo = item.find("div", class_="JheGif nDgy9d").get_text()
            trecho = item.find("div", class_="Y3v8qd").get_text()
            link = item.a["href"]

            # Tentativa de captura de data relativa
            data_tag = item.find("span", class_="WG9SHc")
            data_relativa = (
                data_tag.span.text if data_tag and data_tag.span else "Data não informada"
            )

            resultados.append(
                {
                    "titulo": titulo,
                    "trecho": trecho,
                    "link": link,
                    "data": data_relativa,
                }
            )

        except AttributeError:
            continue

    return resultados


# -------------------------------------------------------------
# 2️⃣ Execução da busca para vários termos
# -------------------------------------------------------------
def coletar_varios_termos(lista_termos):
    todas = []
    for termo in lista_termos:
        print(f"\n🔍 Buscando por: {termo}")
        noticias = buscar_noticias(termo)
        todas.extend(noticias)
        time.sleep(2)  # reduz risco de bloqueio

    return todas


# -------------------------------------------------------------
# 3️⃣ Filtro por palavras-chave
# -------------------------------------------------------------
def filtrar_noticias(noticias, palavras_chave):
    filtradas = []

    for noticia in noticias:
        texto = (noticia["titulo"] + " " + noticia["trecho"]).lower()
        if any(p.lower() in texto for p in palavras_chave):
            filtradas.append(noticia)

    return filtradas


# -------------------------------------------------------------
# 4️⃣ Salvamento em CSV
# -------------------------------------------------------------
def salvar_csv(nome_arquivo, lista_noticias):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Trecho", "Link", "Data"])

        for n in lista_noticias:
            escritor.writerow([n["titulo"], n["trecho"], n["link"], n["data"]])

    print(f"\n✅ Arquivo '{nome_arquivo}' salvo com sucesso!")


# -------------------------------------------------------------
# 5️⃣ Execução completa (exemplo)
# -------------------------------------------------------------
if __name__ == "__main__":
    termos = [
        "tendências tecnologia 2025",
        "novidades inteligência artificial",
        "mercado digital inovação",
    ]

    noticias = coletar_varios_termos(termos)

    salvar_csv("noticias_coletadas.csv", noticias)

    # Filtragem opcional
    palavras = ["avanço", "mercado", "crescimento", "transformação"]
    filtradas = filtrar_noticias(noticias, palavras)

    salvar_csv("noticias_filtradas.csv", filtradas)

    print(f"\n🔎 Total coletadas: {len(noticias)}")
    print(f"🎯 Total filtradas: {len(filtradas)}")
