import argparse
import sys
from Algorithms.encryptionAlgorithms import cesar, polibio, transposicion
from Algorithms.decryptionAlgorithms import cesar_decrypt, polibio_decrypt, transposicion_decrypt

def validate_ciphers(cipher):
    """Valida que el cifrado sea válido."""
    valid_ciphers = {'cesar', 'c', 'polibius', 'p', 'transposition', 't'}
    if cipher not in valid_ciphers:
        raise argparse.ArgumentTypeError(
            f"❌ Error: '{cipher}' no es un algoritmo válido"
        )
    return cipher

def main():
    """Interfaz CLI para cifrado y descifrado."""
    
    parser = argparse.ArgumentParser(
        description="Aplicación de cifrado y descifrado con múltiples algoritmos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py --cipher c --mode enc --key "miLlave" --normalize lax
  python main.py --cipher c p t --mode enc --key "miLlave" --normalize lax
  python main.py --cipher p t --mode dec --normalize s
        """
    )
    
    # Flag: --cipher (1 a 3 cifradores sin repetir)
    parser.add_argument(
        '--cipher',
        nargs='+',
        required=True,
        type=validate_ciphers,
        help='1 a 3 Algoritmos de cifrado: cesar (c), polibius (p), transposition (t)'
    )
    
    # Flag: --mode (encriptación o desencriptación)
    parser.add_argument(
        '--mode',
        required=True,
        choices=['enc', 'dec'],
        help='Modo: enc (encriptar), dec (desencriptar)'
    )
    
    # Flag: --key (clave de cifrado)
    parser.add_argument(
        '--key',
        required=False,
        help='Clave para cifrado (requerida para César y Transposición)'
    )
    
    # Flag: --in (entrada: archivo o stdin)
    parser.add_argument(
        '--in',
        dest='input_file',
        default='stdin',
        help='Entrada: ruta de archivo o "stdin" para entrada estándar'
    )
    
    # Flag: --out (salida: archivo o stdout)
    parser.add_argument(
        '--out',
        dest='output_file',
        default='stdout',
        help='Salida: ruta de archivo o "stdout" para salida estándar'
    )
    
    # Flag: --normalize (normalización: strict o lax)
    parser.add_argument(
        '--normalize',
        choices=['strict', 's', 'lax', 'l'],
        default='lax',
        help='Normalización: strict (s) o lax (l)'
    )
    
    args = parser.parse_args()
    
    # Validar cantidad de cifradores (mínimo 1, máximo 3)
    if len(args.cipher) < 1 or len(args.cipher) > 3:
        print("❌ Error: Debes pasar entre 1 y 3 algoritmos")
        sys.exit(1)
    
    # Validar que no haya repetidos
    if len(set(args.cipher)) != len(args.cipher):
        print("❌ Error: No puede haber algoritmos repetidos")
        sys.exit(1)
    
    # Convertir flags cortos a completos
    cipher_map = {
        'c': 'cesar',
        'p': 'polibius',
        't': 'transposition'
    }
    
    ciphers = [cipher_map.get(c, c) for c in args.cipher]
    
    normalize_mode = 'strict' if args.normalize in ['s'] else 'lax'
    
    # Leer entrada
    try:
        if args.input_file.lower() == 'stdin':
            mensaje = input("Ingresa el mensaje: ").strip()
        else:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                mensaje = f.read().strip()
    except FileNotFoundError:
        print(f"❌ Error: No se encontró '{args.input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    # Procesar con cada cifrador en secuencia
    try:
        resultado = mensaje
        for cipher in ciphers:
            if cipher == 'cesar':
                if not args.key:
                    print("❌ César requiere --key")
                    sys.exit(1)
                resultado = cesar(resultado, normalize_mode, args.key) if args.mode == 'enc' \
                           else cesar_decrypt(resultado, args.key)
            
            elif cipher == 'polibius':
                resultado = polibio(resultado, normalize_mode) if args.mode == 'enc' \
                           else polibio_decrypt(resultado, normalize_mode)
            
            elif cipher == 'transposition':
                if not args.key:
                    print("❌ Transposición requiere --key")
                    sys.exit(1)
                resultado = transposicion(resultado, normalize_mode, args.key) if args.mode == 'enc' \
                           else transposicion_decrypt(resultado, args.key)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    # Escribir salida
    try:
        if args.output_file.lower() == 'stdout':
            print(f"\n✓ Resultado:\n{resultado}")
        else:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(resultado)
            print(f"✓ Guardado en '{args.output_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()