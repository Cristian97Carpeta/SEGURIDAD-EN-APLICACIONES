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

def cifrar_mensaje(mensaje: str, clave: int) -> str:
    """
    Cifra un mensaje completo usando el cifrado César.
    
    Parámetros:
    mensaje (str): El mensaje a cifrar.
    clave (int): El número de desplazamiento para el cifrado.

    Retorna:
    str: El mensaje cifrado.
    """
    mensaje_cifrado = ""  # Inicializar el mensaje cifrado como una cadena vacía
    for letra in mensaje:  # Recorrer cada letra del mensaje
        mensaje_cifrado += cifrar_letra(letra, clave)  # Cifrar cada letra y añadirla al mensaje cifrado
    return mensaje_cifrado

def descifrar_letra(letra: str, clave: int) -> str:
    """
    Descifra una letra usando el cifrado César.
    
    Parámetros:
    letra (str): La letra a descifrar.
    clave (int): El número de desplazamiento original usado para el cifrado.

    Retorna:
    str: La letra descifrada.
    """
    ABC: str = string.ascii_uppercase  # Obtener el alfabeto en mayúsculas
    idx_letra: int = ABC.index(letra)  # Obtener el índice de la letra en el alfabeto
    return ABC[(idx_letra - clave) % 26]  # Calcular y retornar la letra descifrada

def descifrar_mensaje(mensaje: str, clave: int) -> str:
    """
    Descifra un mensaje completo usando el cifrado César.
    
    Parámetros:
    mensaje (str): El mensaje a descifrar.
    clave (int): El número de desplazamiento original usado para el cifrado.

    Retorna:
    str: El mensaje descifrado.
    """
    mensaje_descifrado = ""  # Inicializar el mensaje descifrado como una cadena vacía
    for letra in mensaje:  # Recorrer cada letra del mensaje
        mensaje_descifrado += descifrar_letra(letra, clave)  # Descifrar cada letra y añadirla al mensaje descifrado
    return mensaje_descifrado

def main():
    """
    Función principal del programa. Cifra y descifra un mensaje de ejemplo.
    """
    print("BIENVENIDOS")  # Imprimir un mensaje de bienvenida
    mensaje = "INTER"  # Definir el mensaje a cifrar
    clave = 3  # Definir la clave de cifrado
    mensaje_cifrado = cifrar_mensaje(mensaje, clave)  # Cifrar el mensaje
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave)  # Descifrar el mensaje cifrado
    
    # Imprimir el mensaje original, el mensaje cifrado y el mensaje descifrado
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")

if __name__ == "__main__":
    main()





