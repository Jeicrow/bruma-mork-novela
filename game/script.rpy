# game/script.rpy

# --- Definiciones de Personajes ---

define b = Character("Bruma", color="#ffffff", what_color="#c8c8ff", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define k = Character("Koda", color="#ff9999", what_color="#ffcccc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define ar = Character("Ardan", color="#9999ff", what_color="#ccccff", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define j = Character("Jeicrow", color="#99ff99", what_color="#ccffcc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define v = Character("Valerius", color="#ffcc99", what_color="#ffddbb", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define vv = Character("Vampiro Vigía", color="#aaaaaa", what_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define v1 = Character("Vampiro 1", color="#aaaaaa", what_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define vvel = Character("Vampiro Veloz", color="#aaaaaa", what_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define viejo = Character("Viejo Vampiro", color="#aaaaaa", what_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")
define lidia = Character("Lidia", color="#ffff99", what_color="#ffffcc", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], kind=nvl, what_prefix="\"", what_suffix="\"")
define narrador = Character(None, color="#bbbbbb", what_color= "#dddddd", who_outlines=[ (2, "#000") ], what_outlines=[ (1, "#000") ], what_prefix="\"", what_suffix="\"")


# --- Definición de Imágenes ---

image bg ataud = "images/backgrounds/ataud.png"
image bg vias = "images/backgrounds/vias.png"
image bg bosque = "images/backgrounds/bosque.png"
image bg salon = "images/backgrounds/salon.png"
image bg habitacion bruma = "images/backgrounds/habitacion_bruma.png"
image bg lugar desertico = "images/backgrounds/lugar_desertico.png"

image bruma normal = "images/characters/bruma/bruma_normal.png"
image bruma triste = "images/characters/bruma/bruma_triste.png"
image bruma enojada = "images/characters/bruma/bruma_enojada.png"
image bruma sorprendida = "images/characters/bruma/bruma_sorprendida.png"
image bruma decidida = "images/characters/bruma/bruma_decidida.png"

image koda normal = "images/characters/koda/koda_normal.png"
image koda picara = "images/characters/koda/koda_picara.png"
image koda preocupada = "images/characters/koda/koda_preocupada.png"

image ardan arrogante = "images/characters/ardan/ardan_arrogante.png"
image ardan desden = "images/characters/ardan/ardan_desden.png"
image ardan furioso = "images/characters/ardan/ardan_furioso.png"

image jeicrow espalda = "images/characters/jeicrow/jeicrow_espalda.png"
image jeicrow serio = "images/characters/jeicrow/jeicrow_serio.png"
image jeicrow leve_sonrisa = "images/characters/jeicrow/jeicrow_leve_sonrisa.png"
image jeicrow reverencia = "images/characters/jeicrow/jeicrow_reverencia.png"

image valerius frio = "images/characters/valerius/valerius_frio.png"
image valerius desconfianza = "images/characters/valerius/valerius_desconfianza.png"

image vampiro_vigia = "images/characters/vampiro_vigia.png"
image vampiro1 = "images/characters/vampiro1.png"
image vampiro_veloz = "images/characters/vampiro_veloz.png"
image viejo_vampiro = "images/characters/viejo_vampiro.png"

image asaltante normal = "images/characters/asaltante/asaltante_normal.png"
image asaltante gigante = "images/characters/asaltante/asaltante_gigante.png"

image lidia normal = "images/characters/lidia/lidia_normal.png"
image lidia preocupada = "images/characters/lidia/lidia_preocupada.png"
image lidia furiosa = "images/characters/lidia/lidia_furiosa.png"

image cuervo colgante = "images/objects/cuervo_colgante.png"
image black_screen = Solid("#000000")


# --- Configuración de Estilos (NVL para pensamientos) ---

$ style.nvl_thought.size = 20
$ style.nvl_thought.font = "gui/font/dejavu-sans/DejaVuSans.ttf"  # Asegúrate de tener esta fuente
$ style.nvl_thought.color = "#ffffff"
$ style.nvl_thought.outlines = [(2, "#000000")]


# --- Inicio del Juego (Prólogo) ---

label start:
    play music "audio/ambiental.mp3" loop fadein 2.0  # Simplificado
    scene black_screen with dissolve
    narrador "Prólogo"
    narrador """¿Por qué sigo aquí? ¿Por qué sigo luchando? Cada amanecer es una agonía, cada noche una repetición de la misma desesperanza. Veo a mi alrededor, a mi clan, y no siento más que un vacío. Se ríen, se alimentan, se jactan de su poder, pero ¿de qué sirve el poder cuando no hay nada por lo que valga la pena usarlo?"""
    jump capitulo1


# --- Capítulo 1: Ecos en la Niebla ---

label capitulo1:
    scene bg ataud
    with dissolve
    show bruma normal at center
    with dissolve

    b "Otro día, otra cacería. ¿Realmente importa?"

    show lidia normal at left
    with moveinleft
    lidia "Miau... ¿Te preocupa la reunión de esta noche? Sabes que esos vampiros de sangre \"pura\" solo buscan una excusa para menospreciarnos."

    show bruma triste
    b "No es eso, Lidia. Es... todo. Siento que estoy atrapada en una pesadilla que nunca termina."
    hide lidia
    with moveoutright

    show koda normal at right
    with moveinright

    k "¡Bruma! ¿Lista para la \"diversión\"?"

    b "Supongo. ¿Y tú, Koda? ¿Emocionada por otra noche de fanfarronería y miradas de desprecio?"

    show koda picara
    k "Alguien tiene que mantener la cordura en este clan. Además, siempre hay una oportunidad para poner a esos engreídos en su lugar."
    hide koda

    show ardan arrogante at right
    with moveinright

    ar "Bruma, cariño, ¿ya estás lista? No querrás perderte la oportunidad de demostrar nuestra superioridad, ¿verdad?"

    show bruma enojada
    b "No te preocupes, Ardan. No dejaré que tu ego se sienta amenazado."

    show ardan desden
    narrador """Ardan la mira con desdén, pero no dice nada. Bruma siente un escalofrío. Ya no reconoce al vampiro del que una vez se enamoró. Solo queda un cascarón vacío, lleno de ambición y crueldad."""

    hide ardan
    hide bruma
    with dissolve

    # --- Escena 2: La Emboscada ---
    scene bg vias
    with dissolve
    show vampiro_vigia
    with dissolve
    vv "¡Allí! Un tren de carga. Y... puedo ver cápsulas. Contienen vampiros. Jóvenes, en su mayoría."

    hide vampiro_vigia
    show bruma normal
    with dissolve

    b "Malditos humanos..."

    show ardan arrogante at right
    with moveinright

    ar "Déjalos. No son de nuestra sangre. No vale la pena el riesgo."

    show vampiro1 at left
    with moveinleft

    v1 "Ardan tiene razón. Probablemente sean vampiros errantes, de todos modos."

    show bruma enojada
    b "¿Y qué si lo son? ¿Acaso no son vampiros? ¿No merecen vivir?"
    hide vampiro1

    show koda normal at left
    with moveinleft

    k "Estoy contigo, amiga. No podemos dejarlos a su suerte."
    hide koda

    show vampiro_veloz at left
    with moveinleft
    vvel "Yo también iré."

    show bruma decidida
    b "(Mirando a Ardan con desprecio). ¿Y tú? ¿Te quedarás aquí, lamiendo tus heridas imaginarias?"

    show ardan arrogante
    ar "Haz lo que quieras. Pero no esperes que te salve el trasero."
    hide ardan

    hide bruma
    hide vampiro_veloz
    with dissolve

    narrador "Bruma, Koda y el Vampiro Veloz se dirigen hacia el tren. La adrenalina corre por las venas de Bruma. Por primera vez en mucho tiempo, siente un propósito."
    $ renpy.music.stop(channel="ambiental")
    play music "audio/combate.mp3" loop fadein 2.0  # Simplificado
    #---Batalla ---
    "Aquí se narraría la batalla que se da en el tren, en contra de los soldados."

    # --- Escena 3: El Encuentro ---

    scene bg bosque
    with dissolve
    $ renpy.music.stop(channel="combate")
    play music "audio/ambiental.mp3" loop fadein 2.0  # Simplificado

    show jeicrow espalda at center
    with dissolve
    show bruma normal at left

    b "¿Qué...? ¿Dónde estoy?"

    j "Estás a salvo. Por ahora."

    b "¿Qué es esto?"

    j "Una planta medicinal. Acelera la curación. Y... bebe esto. Necesitas sangre."

    narrador "Bruma bebe con avidez, sintiendo cómo la vida regresa a su cuerpo. Mira a Jeicrow, que sigue de espaldas."
    show bruma normal
    b "¿Quién eres? ¿Por qué me ayudas?"

    narrador "Jeicrow permanece en silencio. La tensión se acumula."

    b "¿No vas a responder? ¿Acaso eres mudo?"

    j "No creo que hayas sido tan estúpida como para enfrentarte sola a un batallón de soldados armados."

    show bruma enojada
    b "¿Qué sabes tú? No me conoces. Y..."
    b "¿Mis compañeros... ¿dónde están?"

    j "Los ayudaste a escapar. Un acto noble, pero imprudente."
    b "¿Y tú qué sabes de nobleza? Solo eres un..."

    j "Me llamo Jeicrow. Y sé que perteneces al clan Mork. Llevas su marca en el cuello. Dicen que son un clan poderoso, pero también... despreciado."

    b "¿Y eso qué? ¿Me vas a juzgar por mi linaje?"

    show jeicrow serio at center
    with move

    j "Estaba buscando a alguien. Alguien que me fue arrebatado. Los cazadores de vampiros se la llevaron. Y entonces... te vi."

    b "¿Y qué hiciste?"

    j "Los maté. A todos los que pude. Te liberé y te traje aquí. El tren... ya no es un problema."

    show bruma sorprendida
    b "¿Tú solo? ¿Con esa espada?"

    j "Tengo mis métodos."

    narrador """Bruma lo estudia, sintiendo una mezcla de fascinación y desconfianza. Hay algo en él que la atrae, algo que la hace sentir... viva."""

    b "Gracias. Supongo."

    j "Debo irme."

    b "¿Me vas a dejar aquí? ¿Sola?"

    show jeicrow leve_sonrisa
    j """Eres fuerte, Bruma Mork. Ya no me necesitas. Además, tu clan no tardará en llegar. Puedo sentirlos."""
    show jeicrow reverencia
    narrador "Jeicrow se inclina en una reverencia. Bruma está a punto de hablar, pero él desaparece en un parpadeo."
    hide jeicrow
    with dissolve

    show bruma sorprendida
    b "Jeicrow..."

    narrador """Se queda sola, envuelta en el abrigo de Jeicrow, sintiendo su aroma y el eco de su presencia. La noche ya no parece tan vacía."""

    # --- Escena 4: El Regreso ---
    "Aqui se narra la llegada del clan Mork"

    # --- Escena 5: El Ataúd ---

    scene bg habitacion bruma
    with dissolve
    $ renpy.music.stop(channel="ambiental")
    play music "audio/ambiental.mp3" loop fadein 2.0  # Simplificado
    show bruma normal at center
    with dissolve
    show lidia normal at left
    with moveinleft

    lidia "Miau... ¿Qué te pasa, Bruma? Estás diferente."

    b "Conocí a alguien, Lidia. Alguien que... me hizo sentir algo que creía perdido."

    lidia "Miau... ¿Amor?"

    show bruma triste
    b "Tal vez. O tal vez solo sea otra ilusión."

    narrador """Cierra los ojos, recordando el rostro de Jeicrow, su voz, su mirada.
    La imagen se mezcla con los recuerdos de su pasado, de su abuela,
    de su madre, de la pérdida y el dolor.  Pero ahora, hay una chispa
    de esperanza. Una chispa que lleva el nombre de un cuervo."""

    jump capitulo2

# --- Capítulo 2: Sombras del Pasado, Susurros del Futuro ---
