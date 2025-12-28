# Archivo: variables.rpy
# Este archivo inicializa el estado del juego. 
# El uso de 'default' es fundamental para que el sistema de guardado y carga de Ren'Py
# rastree correctamente estos valores.

# Estado mental del protagonista (0-100)
default cordura = 100

# Lista de objetos obtenidos por el jugador
default inventario = []

# Seguimiento del progreso narrativo
default historia_capitulo = 1

# Flag para eventos específicos de la trama
default ha_visto_muerte = False
