import string

def cifrar_letra(letra: str, clave: int) -> str:
    """
    Cifra una letra usando el cifrado César.
    
    Parámetros:
    letra (str): La letra a cifrar.
    clave (int): El número de desplazamiento para el cifrado.

    Retorna:
    str: La letra cifrada.
    """
    ABC: str = string.ascii_uppercase  # Obtener el alfabeto en mayúsculas
    idx_letra: int = ABC.index(letra)  # Obtener el índice de la letra en el alfabeto
    return ABC[(idx_letra + clave) % 26]  # Calcular y retornar la letra cifrada

def main():
    """
    Función principal del programa. Cifra algunas letras de ejemplo y las imprime.
    """
    print("BIENVENIDOS")  # Imprimir un mensaje de bienvenida
    # Cifrar y mostrar algunas letras con

