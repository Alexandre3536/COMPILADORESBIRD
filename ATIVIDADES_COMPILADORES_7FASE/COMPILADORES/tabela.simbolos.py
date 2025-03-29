import tkinter as tk
from tkinter import messagebox


class TabelaSimbolos:
    def __init__(self):
        self.tabela = []

    def adicionar_simbolo(self, nome, valor, atributos=None):
        """Adiciona um símbolo (variável) à tabela de símbolos"""
        if atributos is None:
            atributos = {}
        
        # Verifica se o símbolo já existe na tabela
        if any(simbolo['nome'] == nome for simbolo in self.tabela):
            messagebox.showwarning("Aviso", f"O símbolo '{nome}' já existe na tabela.")
            return False
        
        simbolo = {'nome': nome, 'valor': valor, 'atributos': atributos}
        self.tabela.append(simbolo)
        return True

    def atualizar_valor(self, nome, valor):
        """Atualiza o valor de um símbolo já existente"""
        for simbolo in self.tabela:
            if simbolo['nome'] == nome:
                simbolo['valor'] = valor
                return True
        messagebox.showwarning("Aviso", f"O símbolo '{nome}' não foi encontrado na tabela.")
        return False

    def associar_atributo(self, nome, atributo, valor):
        """Associa um atributo a um símbolo existente"""
        for simbolo in self.tabela:
            if simbolo['nome'] == nome:
                simbolo['atributos'][atributo] = valor
                return True
        messagebox.showwarning("Aviso", f"O símbolo '{nome}' não foi encontrado.")
        return False

    def pesquisar_simbolo(self, nome):
        """Pesquisa um símbolo pelo nome e retorna seu valor e atributos"""
        for simbolo in self.tabela:
            if simbolo['nome'] == nome:
                return simbolo
        return None

    def ordenar_alfabeticamente(self):
        """Ordena a tabela de símbolos alfabeticamente pelo nome"""
        self.tabela.sort(key=lambda simbolo: simbolo['nome'])

    def exibir_tabela(self):
        """Exibe a tabela de símbolos"""
        if not self.tabela:
            messagebox.showinfo("Tabela de Símbolos", "A tabela está vazia.")
        else:
            tabela_str = "Tabela de Símbolos:\n"
            for simbolo in self.tabela:
                atributos = ", ".join([f"{k}: {v}" for k, v in simbolo['atributos'].items()])
                tabela_str += f"Nome: {simbolo['nome']}, Valor: {simbolo['valor']}, Atributos: {atributos}\n"
            messagebox.showinfo("Tabela de Símbolos", tabela_str)


# Funções da interface gráfica

def adicionar_simbolo():
    nome = entrada_nome.get()
    valor = entrada_valor.get()
    atributos = entrada_atributos.get()

    # Tratando o valor
    try:
        valor = eval(valor)  # Permite que o valor seja numérico ou string (com aspas)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro no valor fornecido: {str(e)}")
        return
    
    # Tratando atributos
    atributos_dict = {}
    if atributos:
        try:
            atributos_dict = eval(atributos)  # Converte o texto em um dicionário
            if not isinstance(atributos_dict, dict):
                raise ValueError("Atributos precisam ser passados como um dicionário.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar os atributos: {str(e)}")
            return

    if tabela.adicionar_simbolo(nome, valor, atributos_dict):
        messagebox.showinfo("Sucesso", f"O símbolo '{nome}' foi adicionado com o valor '{valor}'.")

def atualizar_valor():
    nome = entrada_nome_atualizar.get()
    valor = entrada_valor_atualizar.get()
    try:
        valor = eval(valor)  # Permite que o valor seja numérico ou string
        if tabela.atualizar_valor(nome, valor):
            messagebox.showinfo("Sucesso", f"O valor do símbolo '{nome}' foi atualizado para '{valor}'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro no valor fornecido: {str(e)}")

def associar_atributo():
    nome = entrada_nome_atributo.get()
    atributo = entrada_atributo.get()
    valor = entrada_valor_atributo.get()

    if tabela.associar_atributo(nome, atributo, valor):
        messagebox.showinfo("Sucesso", f"O atributo '{atributo}' foi associado ao símbolo '{nome}' com valor '{valor}'.")

def pesquisar_simbolo():
    nome = entrada_nome_pesquisa.get()
    simbolo = tabela.pesquisar_simbolo(nome)
    if simbolo:
        atributos = ", ".join([f"{k}: {v}" for k, v in simbolo['atributos'].items()])
        messagebox.showinfo("Símbolo Encontrado", f"Nome: {simbolo['nome']}\nValor: {simbolo['valor']}\nAtributos: {atributos}")
    else:
        messagebox.showinfo("Símbolo Não Encontrado", f"O símbolo '{nome}' não foi encontrado.")

def ordenar_tabela():
    tabela.ordenar_alfabeticamente()
    messagebox.showinfo("Tabela Ordenada", "A tabela foi ordenada alfabeticamente.")

def exibir_tabela():
    tabela.exibir_tabela()


# Criando a janela principal
janela = tk.Tk()
janela.title("Tabela de Símbolos")

# Criar a tabela de símbolos
tabela = TabelaSimbolos()

# Layout
tk.Label(janela, text="Nome do Símbolo:").grid(row=0, column=0, padx=10, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Valor do Símbolo:").grid(row=1, column=0, padx=10, pady=5)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Atributos (formato: {atributo: valor}):").grid(row=2, column=0, padx=10, pady=5)
entrada_atributos = tk.Entry(janela)
entrada_atributos.grid(row=2, column=1, padx=10, pady=5)

adicionar_button = tk.Button(janela, text="Adicionar Símbolo", command=adicionar_simbolo)
adicionar_button.grid(row=3, column=0, columnspan=2, pady=10)

# Atualizar o valor de uma variável existente
tk.Label(janela, text="Nome do Símbolo (para atualizar):").grid(row=4, column=0, padx=10, pady=5)
entrada_nome_atualizar = tk.Entry(janela)
entrada_nome_atualizar.grid(row=4, column=1, padx=10, pady=5)

tk.Label(janela, text="Novo Valor do Símbolo:").grid(row=5, column=0, padx=10, pady=5)
entrada_valor_atualizar = tk.Entry(janela)
entrada_valor_atualizar.grid(row=5, column=1, padx=10, pady=5)

atualizar_button = tk.Button(janela, text="Atualizar Valor", command=atualizar_valor)
atualizar_button.grid(row=6, column=0, columnspan=2, pady=10)

# Associar atributos
tk.Label(janela, text="Nome do Símbolo (para atributos):").grid(row=7, column=0, padx=10, pady=5)
entrada_nome_atributo = tk.Entry(janela)
entrada_nome_atributo.grid(row=7, column=1, padx=10, pady=5)

tk.Label(janela, text="Atributo:").grid(row=8, column=0, padx=10, pady=5)
entrada_atributo = tk.Entry(janela)
entrada_atributo.grid(row=8, column=1, padx=10, pady=5)

tk.Label(janela, text="Valor do Atributo:").grid(row=9, column=0, padx=10, pady=5)
entrada_valor_atributo = tk.Entry(janela)
entrada_valor_atributo.grid(row=9, column=1, padx=10, pady=5)

associar_button = tk.Button(janela, text="Associar Atributo", command=associar_atributo)
associar_button.grid(row=10, column=0, columnspan=2, pady=10)

# Pesquisar um símbolo
tk.Label(janela, text="Nome do Símbolo (para pesquisar):").grid(row=11, column=0, padx=10, pady=5)
entrada_nome_pesquisa = tk.Entry(janela)
entrada_nome_pesquisa.grid(row=11, column=1, padx=10, pady=5)

pesquisar_button = tk.Button(janela, text="Pesquisar Símbolo", command=pesquisar_simbolo)
pesquisar_button.grid(row=12, column=0, columnspan=2, pady=10)

# Ordenar a tabela
ordenar_button = tk.Button(janela, text="Ordenar Tabela Alfabeticamente", command=ordenar_tabela)
ordenar_button.grid(row=13, column=0, columnspan=2, pady=10)

# Exibir a tabela
exibir_button = tk.Button(janela, text="Exibir Tabela de Símbolos", command=exibir_tabela)
exibir_button.grid(row=14, column=0, columnspan=2, pady=10)

# Iniciar a interface gráfica
janela.mainloop()
