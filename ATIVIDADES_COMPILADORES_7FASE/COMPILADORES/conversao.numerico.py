import tkinter as tk
from tkinter import messagebox

def converter_para_decimal(valor, base):
    try:
        if base == 2:
            return int(valor, 2)
        elif base == 8:
            return int(valor, 8)
        elif base == 10:
            return int(valor)  # Para decimal já podemos converter diretamente
        elif base == 16:
            return int(valor, 16)
        else:
            raise ValueError("Base inválida. Deve ser 2, 8, 10 ou 16.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro ao converter: {e}")
        return None

def complemento_de_dois(numero, bits=8):
    """
    Converte um número negativo para complemento de dois, dado o número e o número de bits.
    """
    if numero < 0:
        # Convertendo o número positivo
        numero = abs(numero)
        binario = format(numero, f"0{bits}b")  # Binário com preenchimento
        # Invertendo os bits (1's para 0's e vice-versa)
        binario_invertido = ''.join('1' if x == '0' else '0' for x in binario)
        # Somando 1 ao número invertido
        complemento = bin(int(binario_invertido, 2) + 1)[2:].zfill(bits)
        return complemento
    else:
        return format(numero, f"0{bits}b")

def exibir_resultado(valor_decimal, base_saida, digitos=10):
    try:
        if base_saida == 2:
            # Se for negativo, usa complemento de dois
            if valor_decimal < 0:
                resultado = complemento_de_dois(valor_decimal, digitos)
            else:
                resultado = format(valor_decimal, f"0{digitos}b")
        elif base_saida == 8:
            resultado = format(valor_decimal, f"0{digitos}o")
        elif base_saida == 10:
            resultado = format(valor_decimal, f"{digitos}d")
        elif base_saida == 16:
            resultado = format(valor_decimal, f"0{digitos}X")
        else:
            raise ValueError("Base de saída inválida. Deve ser 2, 8, 10 ou 16.")
        return resultado
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro na formatação: {e}")
        return None

def calcular():
    # Obter os valores dos campos
    valor = entrada_valor.get()
    base_entrada = int(entrada_base_entrada.get())
    base_saida = int(entrada_base_saida.get())
    digitos = int(entrada_digitos.get())

    # Converter o valor para decimal
    valor_decimal = converter_para_decimal(valor, base_entrada)
    if valor_decimal is None:
        return  # Se houver erro, não faz mais nada

    # Exibir o resultado formatado
    resultado_formatado = exibir_resultado(valor_decimal, base_saida, digitos)
    if resultado_formatado is not None:
        resultado_label.config(text=f"Resultado: {resultado_formatado}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversão Numérica")

# Layout
tk.Label(janela, text="Digite um número:").grid(row=0, column=0, padx=10, pady=5)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Base de Entrada (2, 8, 10, 16):").grid(row=1, column=0, padx=10, pady=5)
entrada_base_entrada = tk.Entry(janela)
entrada_base_entrada.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Base de Saída (2, 8, 10, 16):").grid(row=2, column=0, padx=10, pady=5)
entrada_base_saida = tk.Entry(janela)
entrada_base_saida.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Número de Dígitos:").grid(row=3, column=0, padx=10, pady=5)
entrada_digitos = tk.Entry(janela)
entrada_digitos.grid(row=3, column=1, padx=10, pady=5)

# Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.grid(row=4, column=0, columnspan=3, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.grid(row=5, column=0, columnspan=3, pady=10)

# Iniciar a interface gráfica
janela.mainloop()