import tkinter as tk
from tkinter import filedialog
from docx import Document
import pdfplumber

# Função para extrair texto e contar as linhas corretamente
def extrair_linhas(caminho_arquivo):
    linhas = []

    if caminho_arquivo.endswith(".docx"):
        doc = Document(caminho_arquivo)
        for paragrafo in doc.paragraphs:
            for linha in paragrafo.text.split("\n"):  # Divide parágrafos em linhas reais
                linhas.append(linha)

    elif caminho_arquivo.endswith(".pdf"):
        with pdfplumber.open(caminho_arquivo) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    linhas.extend(texto.split("\n"))  # Divide o texto em linhas

    return linhas

# Função para abrir o arquivo e exibir o texto numerado
def abrir_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Word", "*.docx"), ("Arquivos PDF", "*.pdf")])
    if not caminho_arquivo:
        return

    linhas = extrair_linhas(caminho_arquivo)

    # Exibir as linhas numeradas
    resultado_texto.delete(1.0, tk.END)
    for i, linha in enumerate(linhas, start=1):
        resultado_texto.insert(tk.END, f"{i}: {linha}\n")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Listagem Numerada de Arquivo")

# Área de texto para exibir os resultados
resultado_texto = tk.Text(root, width=80, height=20)
resultado_texto.pack(pady=10)

# Botão para abrir o arquivo
abrir_btn = tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo)
abrir_btn.pack(pady=10)

# Executar o loop da interface gráfica
root.mainloop()
