def capitalize_first_letter(frase):
    """
    Recebe uma frase e retorna a mesma frase com a primeira letra em maiúscula.
    """
    if not frase:
        return ""  # Retorna uma string vazia se a frase for vazia
    else:
        return frase[0].upper() + frase[1:]
    
    frase_entrada = "olá, mundo!"
frase_saida = capitalize_first_letter(frase_entrada)
print(frase_saida)  # Saída: "Olá, mundo!"