import tkinter as tk
from tkinter import messagebox
import re

# Funções de validação usando expressões regulares
def validar_binario_par(exp):
    return bool(re.match(r'^[01]*0$', exp))

def validar_palavra_binaria(exp):
    return bool(re.match(r'^[01]*00$', exp))

def validar_entre_aspas(exp):
    return bool(re.match(r'^".*"$', exp))

def validar_telefone_sc(exp):
    return bool(re.match(r'^\(4[7-9]\)\s9?\d{3,4}-\d{4}$', exp))

def validar_placa_veiculo(exp):
    return bool(re.match(r'^[A-Z]{3}-\d{4}$', exp))

def validar_email(exp):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com\.br|br|com)$', exp))

def validar_comentario_linha(exp):
    return bool(re.match(r'^//.*$', exp))

def validar_comentario_multiline(exp):
    return bool(re.match(r'/\*.*\*/$', exp))

# Função que valida com base na escolha
def validar():
    exp = entrada.get()
    tipo = tipo_validacao.get()

    if tipo == 'Binários Pares':
        valido = validar_binario_par(exp)
    elif tipo == 'Palavras Binárias com 00 no Final':
        valido = validar_palavra_binaria(exp)
    elif tipo == 'Strings entre Aspas':
        valido = validar_entre_aspas(exp)
    elif tipo == 'Telefone SC':
        valido = validar_telefone_sc(exp)
    elif tipo == 'Placas de Veículos':
        valido = validar_placa_veiculo(exp)
    elif tipo == 'Email':
        valido = validar_email(exp)
    elif tipo == 'Comentário de Linha':
        valido = validar_comentario_linha(exp)
    elif tipo == 'Comentário Multilinha':
        valido = validar_comentario_multiline(exp)
    else:
        messagebox.showerror("Erro", "Selecione um tipo de validação!")
        return

    if valido:
        resultado.config(text="Expressão válida!", fg="green")
    else:
        resultado.config(text="Expressão inválida!", fg="red")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)
    resultado.config(text="")

# Janela principal
root = tk.Tk()
root.title("Validador de Expressões Regulares")

# Caixa de entrada
entrada_label = tk.Label(root, text="Digite a expressão:")
entrada_label.pack()

entrada = tk.Entry(root, width=50)
entrada.pack()

# Opções de validação
tipo_validacao = tk.StringVar()
tipo_validacao.set("Escolha uma validação")

tipo_menu = tk.OptionMenu(root, tipo_validacao, 
                          "Binários Pares", 
                          "Palavras Binárias com 00 no Final", 
                          "Strings entre Aspas", 
                          "Telefone SC", 
                          "Placas de Veículos", 
                          "Email", 
                          "Comentário de Linha", 
                          "Comentário Multilinha")
tipo_menu.pack()

# Botão de validação
validar_button = tk.Button(root, text="Validar", command=validar)
validar_button.pack()

# Resultado da validação
resultado = tk.Label(root, text="", font=("Arial", 14))
resultado.pack()

# Botão de limpar
limpar_button = tk.Button(root, text="Limpar", command=limpar)
limpar_button.pack()

# Executar o programa
root.mainloop()