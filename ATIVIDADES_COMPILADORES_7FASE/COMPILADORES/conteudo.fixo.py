import tkinter as tk
from tkinter import messagebox

# Tabela de palavras reservadas com descrições
palavras_reservadas_com_atributos = {
    'if': 'Condição de seleção (Execução condicional)',
    'else': 'Alternativa do if (Executa quando a condição do if falha)',
    'while': 'Estrutura de repetição (Enquanto a condição for verdadeira, repete)',
    'for': 'Estrutura de repetição com contador (Utiliza um contador para repetições)',
    'return': 'Retorna o valor de uma função',
    'int': 'Tipo de dado inteiro',
    'float': 'Tipo de dado flutuante',
    'char': 'Tipo de dado caractere',
    'void': 'Função sem valor de retorno'
}

# Função para realizar a pesquisa de uma palavra reservada
def pesquisar_palavra_reservada_com_atributo():
    palavra = entrada_palavra.get().strip()  # Obtém o texto da entrada
    if palavra in palavras_reservadas_com_atributos:
        # Se a palavra for encontrada, exibe o resultado
        resultado = f"A palavra '{palavra}' é uma palavra reservada.\nDescrição: {palavras_reservadas_com_atributos[palavra]}"
    else:
        # Se não for encontrada, exibe um aviso
        resultado = f"A palavra '{palavra}' NÃO é uma palavra reservada."
    
    # Exibe o resultado na área de texto
    texto_resultado.config(state=tk.NORMAL)  # Permite edição do campo de resultado
    texto_resultado.delete(1.0, tk.END)  # Limpa qualquer conteúdo anterior
    texto_resultado.insert(tk.END, resultado)  # Insere o novo resultado
    texto_resultado.config(state=tk.DISABLED)  # Desabilita a edição novamente

# Criando a janela principal
root = tk.Tk()
root.title("Pesquisa de Palavras Reservadas")
root.geometry("400x300")

# Título
titulo = tk.Label(root, text="Pesquisa de Palavras Reservadas", font=("Arial", 14))
titulo.pack(pady=10)

# Campo de entrada de texto para a palavra a ser pesquisada
entrada_palavra = tk.Entry(root, font=("Arial", 12), width=30)
entrada_palavra.pack(pady=10)

# Botão para pesquisar a palavra
botao_pesquisar = tk.Button(root, text="Pesquisar", font=("Arial", 12), command=pesquisar_palavra_reservada_com_atributo)
botao_pesquisar.pack(pady=10)

# Área de texto para mostrar o resultado da pesquisa
texto_resultado = tk.Text(root, font=("Arial", 12), height=6, width=35, wrap=tk.WORD, state=tk.DISABLED)
texto_resultado.pack(pady=10)

# Rodando a interface gráfica
root.mainloop()