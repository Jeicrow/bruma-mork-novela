# Archivo: script.rpy
# Este es el punto de entrada principal del motor Ren'Py.
# Siguiendo buenas prácticas, aquí solo se maneja el flujo inicial
# derivando la narrativa a archivos de capítulos específicos.

label start:
    # 1. Preparación de la escena
    stop music fadeout 1.0
    scene black
    with flash_oscuro

    # 2. Breve pausa dramática
    "..."
    "Todo comienza en el silencio..."

    # 3. Llamada al contenido narrativo externo
    # Usamos 'call' en lugar de 'jump' para que el flujo pueda regresar si es necesario.
    call capitulo_1_inicio

    return
