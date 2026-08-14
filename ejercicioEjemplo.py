def invertir_frase(frase):
    # Caso base
    if len(frase) <= 1:
        return frase

    # Caso recursivo
    return invertir_frase(frase[1:]) + frase[0]


# Programa principal
frase = input("Digite una frase: ")

resultado = invertir_frase(frase)

print("Frase original:", frase)
print("Frase invertida:", resultado)