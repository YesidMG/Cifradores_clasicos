import sys
import os

# Agregar la carpeta padre al path para importar desde la raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Algorithms.encryptionAlgorithms import cesar, polibio, transposicion
from Algorithms.decryptionAlgorithms import cesar_decrypt, polibio_decrypt, transposicion_decrypt

def print_header(title):
    """Imprime un encabezado formateado."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_cesar_algorithm():
    """Pruebas interactivas del algoritmo César."""
    print_header("PRUEBAS - ALGORITMO CÉSAR")
    
    test_cases = [
        ("hola", "clave", "lax"),
        ("Hola Mundo", "clave", "strict"),
        ("prueba123", "test", "lax"),
        ("a", "b", "lax"),
    ]
    
    for mensaje, clave, modo in test_cases:
        try:
            print(f"\n📝 Mensaje: '{mensaje}'")
            print(f"🔑 Clave: '{clave}'")
            print(f"📋 Normalización: {modo}")
            
            cifrado = cesar(mensaje, modo, clave)
            print(f"🔐 Cifrado: {cifrado}")
            
            descifrado = cesar_decrypt(cifrado, clave)
            print(f"🔓 Descifrado: {descifrado}")
            
            match = mensaje.lower().replace(" ", "") if modo == 'strict' else mensaje.lower()
            print(f"✓ Reversible: {match == descifrado or mensaje.lower() == descifrado}")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_polibio_algorithm():
    """Pruebas interactivas del algoritmo Polibio."""
    print_header("PRUEBAS - ALGORITMO POLIBIO")
    
    test_cases = [
        ("hola", "lax"),
        ("abc", "lax"),
        ("Hola Mundo", "strict"),
        ("123", "lax"),
    ]
    
    for mensaje, modo in test_cases:
        try:
            print(f"\n📝 Mensaje: '{mensaje}'")
            print(f"📋 Normalización: {modo}")
            
            cifrado = polibio(mensaje, modo)
            print(f"🔐 Cifrado: {cifrado}")
            
            descifrado = polibio_decrypt(cifrado, modo)
            print(f"🔓 Descifrado: {descifrado}")
            
            print(f"✓ Reversible: {mensaje.lower() == descifrado}")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_transposicion_algorithm():
    """Pruebas interactivas del algoritmo Transposición."""
    print_header("PRUEBAS - ALGORITMO TRANSPOSICIÓN")
    
    test_cases = [
        ("hola", "ab", "Par"),
        ("hola", "abc", "Impar"),
        ("abcd", "xy", "Par"),
        ("prueba", "clave", "Impar"),
    ]
    
    for mensaje, clave, tipo in test_cases:
        try:
            print(f"\n📝 Mensaje: '{mensaje}'")
            print(f"🔑 Clave: '{clave}' (largo {tipo})")
            
            cifrado = transposicion(mensaje, 'lax', clave)
            print(f"🔐 Cifrado: {cifrado}")
            
            descifrado = transposicion_decrypt(cifrado, clave)
            print(f"🔓 Descifrado: {descifrado}")
            
            print(f"✓ Reversible: {mensaje.lower() == descifrado}")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_combined_algorithms():
    """Pruebas de algoritmos combinados."""
    print_header("PRUEBAS - ALGORITMOS COMBINADOS")
    
    mensaje = "mensaje secreto"
    clave = "miLlave"
    
    try:
        print(f"\n📝 Mensaje original: '{mensaje}'")
        print(f"🔑 Clave: '{clave}'")
        
        # Prueba 1: César + Polibio
        print("\n--- Combinación 1: César + Polibio ---")
        paso1 = cesar(mensaje, 'lax', clave)
        paso2 = polibio(paso1, 'lax')
        print(f"Paso 1 (César): {paso1}")
        print(f"Paso 2 (Polibio): {paso2}")
        
        # Prueba 2: César + Polibio + Transposición
        print("\n--- Combinación 2: César + Polibio + Transposición ---")
        paso1 = cesar(mensaje, 'lax', clave)
        paso2 = polibio(paso1, 'lax')
        paso3 = transposicion(paso2, 'lax', clave)
        print(f"Paso 1 (César): {paso1}")
        print(f"Paso 2 (Polibio): {paso2}")
        print(f"Paso 3 (Transposición): {paso3}")
        
        # Desencriptar en orden inverso
        print("\n--- Desencriptación (orden inverso) ---")
        d3 = transposicion_decrypt(paso3, clave)
        d2 = polibio_decrypt(d3, 'lax')
        d1 = cesar_decrypt(d2, clave)
        print(f"Paso 1 inverso (Transposición): {d3}")
        print(f"Paso 2 inverso (Polibio): {d2}")
        print(f"Paso 3 inverso (César): {d1}")
        print(f"\n✓ Reversible: {mensaje.lower() == d1}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def test_edge_cases():
    """Pruebas de casos extremos."""
    print_header("PRUEBAS - CASOS EXTREMOS")
    
    test_cases = [
        ("", "clave", "Mensaje vacío"),
        ("a", "b", "Un solo carácter"),
        ("aaaa", "b", "Caracteres repetidos"),
        ("!@#$", "clave", "Caracteres especiales"),
        ("MAYUSCULAS", "clave", "Letras mayúsculas"),
        ("123456", "clave", "Solo números"),
    ]
    
    for mensaje, clave, descripcion in test_cases:
        try:
            print(f"\n📌 {descripcion}")
            print(f"   Mensaje: '{mensaje}'")
            
            if mensaje:  # Solo probar si no está vacío
                cifrado = cesar(mensaje, 'lax', clave)
                descifrado = cesar_decrypt(cifrado, clave)
                print(f"   Cifrado: {cifrado}")
                print(f"   Descifrado: {descifrado}")
                print(f"   ✓ OK")
            else:
                print(f"   ⚠ Omitido (mensaje vacío)")
        except Exception as e:
            print(f"   ❌ Error: {e}")

def main():
    """Menú principal de pruebas."""
    print("\n" + "=" * 70)
    print("  SUITE DE PRUEBAS INTERACTIVAS - CIFRADO Y DESCIFRADO")
    print("=" * 70)
    
    while True:
        print("\n📋 MENÚ DE PRUEBAS:")
        print("  1. Pruebas César")
        print("  2. Pruebas Polibio")
        print("  3. Pruebas Transposición")
        print("  4. Pruebas Combinadas")
        print("  5. Casos Extremos")
        print("  6. Ejecutar todas las pruebas")
        print("  0. Salir")
        
        opcion = input("\n👉 Selecciona una opción: ").strip()
        
        if opcion == '1':
            test_cesar_algorithm()
        elif opcion == '2':
            test_polibio_algorithm()
        elif opcion == '3':
            test_transposicion_algorithm()
        elif opcion == '4':
            test_combined_algorithms()
        elif opcion == '5':
            test_edge_cases()
        elif opcion == '6':
            test_cesar_algorithm()
            test_polibio_algorithm()
            test_transposicion_algorithm()
            test_combined_algorithms()
            test_edge_cases()
            print("\n✓ Todas las pruebas completadas")
        elif opcion == '0':
            print("\n¡Hasta luego!")
            break
        else:
            print("\n❌ Opción no válida")

if __name__ == '__main__':
    main()