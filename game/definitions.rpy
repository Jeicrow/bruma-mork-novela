# --- PERSONAJES PRINCIPALES ---
# Bruma: Color violeta pálido (melancolía/realeza caída)
define bruma = Character("Bruma Mork", color="#d4bbfb")

# Jeicrow: Color gris oscuro/negro (misterio y poder)
define jeicrow = Character("Jeicrow", color="#a6a6a6")

# --- PERSONAJES SECUNDARIOS ---
# Lidia: Azul claro (voz mental/espiritual)
define lidia = Character("Lidia", color="#aeeeff", who_suffix=" (Mente)")

# Koda: Naranja oscuro (energía/rebeldía)
define koda = Character("Koda", color="#ffbd80")

# Ardan: Rojo sangre (agresividad/arrogancia)
define ardan = Character("Ardan", color="#ff6b6b")

# --- EXTRAS ---
define vigia = Character("Vampiro Vigía", color="#aaaaaa")
define v_veloz = Character("Vampiro Veloz", color="#aaaaaa")
define v1 = Character("Vampiro 1", color="#aaaaaa")

# --- VARIABLES DE ESTADO PARA NOMBRES DESCONOCIDOS ---
# Esto permite que aparezca "???" antes de que se presente
default nombre_misterioso = "???"
define desconocido = Character("[nombre_misterioso]", color="#a6a6a6")

# Imágenes temporales (Placeholders)
image bg habitacion_gotica = Solid("#2b2b2b") # Gris oscuro
image bg bosque_noche = Solid("#051e05") # Verde muy oscuro
image bruma normal = Placeholder("girl")
image jeicrow normal = Placeholder("boy")
image ardan = Placeholder("boy")
image koda = Placeholder("girl")