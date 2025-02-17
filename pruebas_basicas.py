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
    if letra in ABC:  # Verificar si la letra está en el alfabeto
        idx_letra: int = ABC.index(letra)  # Obtener el índice de la letra en el alfabeto
        return ABC[(idx_letra + clave) % 26]  # Calcular y retornar la letra cifrada
    else:
        return letra  # Retornar la letra sin cambios si no está en el alfabeto

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
        mensaje_cifrado += cifrar_letra(letra.upper(), clave)  # Cifrar cada letra y añadirla al mensaje cifrado
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
    if letra in ABC:  # Verificar si la letra está en el alfabeto
        idx_letra: int = ABC.index(letra)  # Obtener el índice de la letra en el alfabeto
        return ABC[(idx_letra - clave) % 26]  # Calcular y retornar la letra descifrada
    else:
        return letra  # Retornar la letra sin cambios si no está en el alfabeto

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
        mensaje_descifrado += descifrar_letra(letra.upper(), clave)  # Descifrar cada letra y añadirla al mensaje descifrado
    return mensaje_descifrado

def main():
    """
    Función principal del programa. Cifra y descifra ejemplos de mensajes.
    """
    print("BIENVENIDOS")  # Imprimir un mensaje de bienvenida
    
    # Cifrar "HOLA" con clave 3
    mensaje = "HOLA"
    clave = 3
    mensaje_cifrado = cifrar_mensaje(mensaje, clave)
    print(f"Cifrado de '{mensaje}' con clave {clave}: {mensaje_cifrado}")
    
    # Descifrar "CDE" con clave 5
    mensaje = "CDE"
    clave = 5
    mensaje_descifrado = descifrar_mensaje(mensaje, clave)
    print(f"Descifrado de '{mensaje}' con clave {clave}: {mensaje_descifrado}")
    
    # Probar con espacios y símbolos
    mensaje = "¡Hola Mundo!"
    clave = 3
    mensaje_cifrado = cifrar_mensaje(mensaje, clave)
    print(f"Cifrado de '{mensaje}' con clave {clave}: {mensaje_cifrado}")

if __name__ == "__main__":
    main()
