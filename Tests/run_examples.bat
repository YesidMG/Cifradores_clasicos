@echo off
REM filepath: c:\Users\hp\OneDrive\Documentos\UPTC\9- Noveno semestre\Seguridad\taller 1 50\run_examples.bat
REM Script para ejecutar ejemplos rápidamente en Windows

setlocal enabledelayedexpansion

echo.
echo ====================================================
echo   EJEMPLOS DE EJECUCION - CIFRADO Y DESCIFRADO
echo ====================================================

:menu
echo.
echo MENU DE EJEMPLOS:
echo 1. Ver ayuda
echo 2. Encriptar con César (entrada por teclado)
echo 3. Encriptar desde archivo
echo 4. Desencriptar desde archivo
echo 5. Encriptar con Polibio
echo 6. Encriptar con Transposición
echo 7. Combinar 3 algoritmos
echo 8. Ejecutar pruebas unitarias
echo 9. Ejecutar pruebas interactivas
echo 0. Salir

set /p opcion="Selecciona una opción: "

if "%opcion%"=="1" goto ayuda
if "%opcion%"=="2" goto cesar_simple
if "%opcion%"=="3" goto cesar_archivo
if "%opcion%"=="4" goto desencriptar
if "%opcion%"=="5" goto polibio
if "%opcion%"=="6" goto transposicion
if "%opcion%"=="7" goto combinado
if "%opcion%"=="8" goto pruebas_unit
if "%opcion%"=="9" goto pruebas_inter
if "%opcion%"=="0" goto fin

echo Opción no válida
goto menu

:ayuda
echo.
echo Mostrando ayuda...
python main.py --help
pause
goto menu

:cesar_simple
echo.
echo === ENCRIPTAR CON CÉSAR ===
python main.py --cipher c --mode enc --key "miLlave" --normalize lax
pause
goto menu

:cesar_archivo
echo.
echo === ENCRIPTAR DESDE ARCHIVO ===
if not exist mensaje.txt (
    echo Creando archivo de prueba...
    (
        echo Este es un mensaje de prueba
        echo para cifrar con todos los algoritmos
    ) > mensaje.txt
)
echo Archivo creado: mensaje.txt
echo Encriptando...
python main.py --cipher c p t --mode enc --key "clave" --in mensaje.txt --out cifrado.txt --normalize lax
echo Archivo cifrado guardado en: cifrado.txt
type cifrado.txt
pause
goto menu

:desencriptar
echo.
echo === DESENCRIPTAR ===
if exist cifrado.txt (
    echo Desencriptando cifrado.txt...
    python main.py --cipher t p c --mode dec --key "clave" --in cifrado.txt --out descifrado.txt
    echo Archivo descifrado guardado en: descifrado.txt
    type descifrado.txt
) else (
    echo No existe archivo cifrado.txt
    echo Primero ejecuta la opción 3 para crear un archivo cifrado
)
pause
goto menu

:polibio
echo.
echo === ENCRIPTAR CON POLIBIO ===
python main.py --cipher p --mode enc --normalize lax
pause
goto menu

:transposicion
echo.
echo === ENCRIPTAR CON TRANSPOSICIÓN ===
python main.py --cipher t --mode enc --key "clave" --normalize lax
pause
goto menu

:combinado
echo.
echo === COMBINAR 3 ALGORITMOS ===
if not exist entrada.txt (
    echo Creando archivo de entrada...
    echo información secreta > entrada.txt
)
echo Encriptando con César + Polibio + Transposición...
python main.py --cipher c p t --mode enc --key "clave_fuerte" --in entrada.txt --out resultado_cifrado.txt --normalize lax
echo Archivo cifrado: resultado_cifrado.txt
type resultado_cifrado.txt
pause
goto menu

:pruebas_unit
echo.
echo === EJECUTANDO PRUEBAS UNITARIAS ===
python -m unittest test_algorithms.py -v
pause
goto menu

:pruebas_inter
echo.
echo === EJECUTANDO PRUEBAS INTERACTIVAS ===
python test_interactive.py
pause
goto menu

:fin
echo.
echo ¡Hasta luego!
exit /b 0