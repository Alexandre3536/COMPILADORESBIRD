import tkinter as tk
from tkinter import filedialog
from docx import Document
import pdfplumber
import re
from collections import defaultdict

# Função para extrair linhas do documento
def extrair_linhas(caminho_arquivo):
    linhas = []
    if caminho_arquivo.endswith(".docx"):
        doc = Document(caminho_arquivo)
        for paragrafo in doc.paragraphs:
            for linha in paragrafo.text.split("\n"):
                linhas.append(linha)

    elif caminho_arquivo.endswith(".pdf"):
        with pdfplumber.open(caminho_arquivo) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    linhas.extend(texto.split("\n"))

    return linhas

# Função para processar o texto e criar a referência cruzada
def processar_texto(caminho_arquivo):
    linhas = extrair_linhas(caminho_arquivo)
    referencias = defaultdict(set)  # Dicionário para armazenar palavras e as linhas em que aparecem

    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, "Texto Numerado:\n\n")

    for i, linha in enumerate(linhas, start=1):
        resultado_texto.insert(tk.END, f"{i}: {linha}\n")

        # Extrai palavras ignorando pontuações e converte para minúsculas
        palavras = re.findall(r"\b[a-zA-ZÀ-ÖØ-öø-ÿ0-9']+\b", linha.lower())
        for palavra in palavras:
            referencias[palavra].add(i)

    # Ordena as palavras alfabeticamente
    palavras_ordenadas = sorted(referencias.keys())

    resultado_texto.insert(tk.END, "\nReferência Cruzada:\n\n")
    for palavra in palavras_ordenadas:
        linhas_ocorrencias = ", ".join(map(str, sorted(referencias[palavra])))
        resultado_texto.insert(tk.END, f"{palavra}: {linhas_ocorrencias}\n")

# Função para abrir o arquivo
def abrir_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Word", "*.docx"), ("Arquivos PDF", "*.pdf")])
    if caminho_arquivo:
        processar_texto(caminho_arquivo)

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Listagem Numerada com Referência Cruzada")

# Área de texto para exibir os resultados
resultado_texto = tk.Text(root, width=100, height=30)
resultado_texto.pack(pady=10)

# Botão para abrir o arquivo
abrir_btn = tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo)
abrir_btn.pack(pady=10)

# Executar o loop da interface gráfica
root.mainloop()
