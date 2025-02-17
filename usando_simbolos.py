def cifrar_letra(letra: str, clave: int) -> str:
    """
    Cifra una letra usando el cifrado César.
    
    Parámetros:
    letra (str): La letra a cifrar.
    clave (int): El número de desplazamiento para el cifrado.

    Retorna:
    str: La letra cifrada.
    """
    ABC: str = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&'()*+,-./:;?<=>@[\\]^_`{|}~"  # Definir el alfabeto en formato AaBbCc...XxYyZz con símbolos
    if letra in ABC:  # Verificar si la letra está en el alfabeto
        idx_letra: int = ABC.index(letra)  # Obtener el índice de la letra en el alfabeto
        return ABC[(idx_letra + clave) % len(ABC)]  # Calcular y retornar la letra cifrada
    else:
        # Si la letra no está en el alfabeto (por ejemplo, un espacio o un signo de puntuación)
        return letra

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

def main():
    """
    Función principal del programa. Cifra un mensaje de ejemplo y lo imprime.
    """
    print("BIENVENIDOS")  # Imprimir un mensaje de bienvenida
    mensaje = "LLEGAMOS A INTER!"  # Definir el mensaje a cifrar
    clave = 3  # Definir la clave de cifrado
    mensaje_cifrado = cifrar_mensaje(mensaje, clave)  # Cifrar el mensaje
    print(f"Mensaje original: {mensaje}")  # Imprimir el mensaje original y el mensaje cifrado
    print(f"Mensaje cifrado: {mensaje_cifrado}")

if __name__ == "__main__":
    main()
