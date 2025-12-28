label capitulo_1_inicio:

    # --- ESCENA 1: EL ATAÚD ---
    scene black
    with fade

    # Pensamientos (sin nombre)
    "¿Por qué sigo aquí? ¿Por qué sigo luchando?"
    "Cada amanecer es una agonía, cada noche una repetición de la misma desesperanza."
    "Veo a mi clan y no siento más que un vacío. ¿De qué sirve el poder cuando no hay nada por lo que valga la pena usarlo?"

    # Fondo: Habitación Gótica (Placeholder: Definiremos imágenes luego)
    # scene bg habitacion_gotica with dissolve 

    show bruma normal at center with dissolve
    
    bruma "Otro día, otra cacería. ¿Realmente importa?"

    # Entra Lidia (la gata)
    "Una elegante criatura blanca con ojos azules penetrantes se frota contra sus piernas."
    
    lidia "Miau... ¿Te preocupa la reunión de esta noche? Sabes que esos vampiros de sangre 'pura' solo buscan una excusa para menospreciarnos."

    bruma "No es eso, Lidia. Es... todo. Siento que estoy atrapada en una pesadilla que nunca termina."

    # Entra Koda
    show bruma at left with move
    show koda at right with dissolve

    koda "¡Bruma! ¿Lista para la 'diversión'?"
    
    bruma "Supongo. ¿Y tú, Koda? ¿Emocionada por otra noche de fanfarronería y miradas de desprecio?"

    koda "Alguien tiene que mantener la cordura en este clan. Además, siempre hay una oportunidad para poner a esos engreídos en su lugar."

    # Entra Ardan
    hide koda
    show ardan at right with dissolve

    ardan "Bruma, cariño, ¿ya estás lista? No querrás perderte la oportunidad de demostrar nuestra superioridad, ¿verdad?"

    # --- PEQUEÑA DECISIÓN DE JUGADOR ---
    menu:
        "Responder con frialdad":
            bruma "No te preocupes, Ardan. No dejaré que tu ego se sienta amenazado."
            $ cordura += 5 # Ganar un poco de control
        
        "Ignorarlo (Silencio)":
            "Bruma simplemente asiente, guardando su desprecio."
            
    "Ardan la mira con desdén. Ya no reconoces al vampiro del que una vez te enamoraste. Solo queda un cascarón vacío."

    # --- ESCENA 2: LA EMBOSCADA ---
    scene black with fade
    "Afueras de la ciudad. El esqueleto de hormigón devorado por la niebla."
    
    # scene bg vias_tren 
    
    show vigia at left
    vigia "¡Allí! Un tren de carga. Y... puedo ver cápsulas. Contienen vampiros. Jóvenes, en su mayoría."

    show bruma enojada at center
    bruma "Malditos humanos..."

    show ardan at right
    ardan "Déjalos. No son de nuestra sangre. No vale la pena el riesgo."

    v1 "Ardan tiene razón. Probablemente sean vampiros errantes."

    bruma "¿Y qué si lo son? ¿Acaso no son vampiros? ¿No merecen vivir?"

    hide vigia
    show koda at left
    koda "Estoy contigo, amiga. No podemos dejarlos a su suerte."

    # La batalla comienza (Transición rápida)
    hide ardan
    hide koda
    hide bruma
    
    "La adrenalina corre por tus venas. Por primera vez en mucho tiempo, sientes un propósito."
    
    # Efecto de sonido de batalla o pantalla roja podría ir aquí
    scene black with flash_oscuro
    "..."
    "Dolor..."
    "Oscuridad..."

    # --- ESCENA 3: EL ENCUENTRO ---
    scene bg bosque_noche with fade
    "Despiertas confundida. El fuego crepita a tu lado."

    show jeicrow sombra at center with dissolve
    # Nota: 'jeicrow sombra' podría ser una silueta oscura

    bruma "..."
    bruma "¿Qué...? ¿Dónde estoy?"

    desconocido "Estás a salvo. Por ahora."

    bruma "¿Qué es esto? (Señala la pasta viscosa en su herida)."

    desconocido "Una planta medicinal. Acelera la curación. Y... bebe esto. Necesitas sangre."

    "Bebes con avidez. La vida regresa a tu cuerpo."

    bruma "¿Quién eres? ¿Por qué me ayudas?"
    "El extraño permanece en silencio."
    
    bruma "¿No vas a responder? ¿Acaso eres mudo?"

    desconocido "No creo que hayas sido tan estúpida como para enfrentarte sola a un batallón de soldados armados."

    bruma "¿Qué sabes tú? No me conoces. Y... mis compañeros... ¿dónde están?"

    desconocido "Los ayudaste a escapar. Un acto noble, pero imprudente."

    bruma "¿Y tú qué sabes de nobleza? Solo eres un..."

    # Revelación del nombre
    $ nombre_misterioso = "Jeicrow"
    show jeicrow normal with dissolve 
    # Aquí mostraríamos la cara de Jeicrow

    jeicrow "Me llamo Jeicrow. Y sé que perteneces al clan Mork. Llevas su marca en el cuello."

    bruma "¿Y eso qué? ¿Me vas a juzgar por mi linaje?"

    "Se levanta y te mira a los ojos. Quedas hipnotizada por su belleza y su mirada penetrante."

    jeicrow "Estaba buscando a alguien. Alguien que me fue arrebatado. Los cazadores de vampiros se la llevaron. Y entonces... te vi."
    
    jeicrow "Los maté. A todos los que pude. Te liberé y te traje aquí. El tren... ya no es un problema."

    bruma "¿Tú solo? ¿Con esa espada?"

    jeicrow "Tengo mis métodos."

    "Hay algo en él que te atrae, algo que te hace sentir... viva."

    bruma "Gracias. Supongo."

    jeicrow "Debo irme."
    
    jeicrow "Eres fuerte, Bruma Mork. Ya no me necesitas. Además, tu clan no tardará en llegar. Puedo sentirlos."

    hide jeicrow with dissolve
    "Desaparece en un parpadeo."

    bruma "Jeicrow..."
    
    # Obtener objeto
    $ inventario.append("Abrigo de Jeicrow")
    "Te quedas envuelta en su abrigo, sintiendo su aroma. Has obtenido: {b}Abrigo de Jeicrow{/b}."

    # --- ESCENA 4: EL REGRESO ---
    scene black with fade
    "El clan Mork llega al bosque. Koda corre hacia ti, abrazándote con fuerza."

    # --- ESCENA 5: FINAL ---
    # scene bg habitacion_gotica 
    
    "De vuelta en tu habitación."
    show lidia at left
    
    lidia "Miau... ¿Qué te pasa, Bruma? Estás diferente."

    bruma "Conocí a alguien, Lidia. Alguien que... me hizo sentir algo que creía perdido."

    lidia "Miau... ¿Amor?"

    bruma "Tal vez. O tal vez solo sea otra ilusión."

    "Jeicrow... ¿Quién eres realmente? ¿Un salvador? ¿Un asesino? ¿O algo más?" 
    "No lo sé. Pero te encontraré. Y descubriré la verdad, cueste lo que cueste."

    return