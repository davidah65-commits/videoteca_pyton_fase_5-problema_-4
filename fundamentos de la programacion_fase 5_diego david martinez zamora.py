#creamosla matriz de la informacion de la videoteca, cada fila es una pelicula y cada columna es un atributo de la pelicula (titulo, año, calificacion, genero)
videoteca = [
    ["iception",2020,8.8,"ciencia ficcion"],
    ["interstellar",2014,8.6,"ciencia ficcion"],
    ["oppenheimer",2023,8.5,"drama"],
    ["the batman",2022,7.9,"accion"],
    ["the flash",2023,6.5,"accion"],
    ["the marvels",2023,6.2,"accion"],
    ["alicia en el pais de las maravillas",2010,7.6,"fantasia"]
]
#definimos la funsion para controlar los titulos segun los criterios 
def contar_peliculas_polpulares_y_recientes(matriz_peliculas,umbral_calificacion,año_limite):
    contador = 0 #incializamos el contador en cero
    #recorremos la matriz fila por fila
    for pelicula in matriz_peliculas:
      #extraemos los datos que nos interesan fila por fila 
      año = pelicula[1]
      calificacion = pelicula[2]    
      #evaluamos la logica del negocio (ambas condiciones deben cumplirse)
      if calificacion >= umbral_calificacion and año >= año_limite:
        contador += 1 #si se cumple la condicion, incrementamos el contador
    return contador
#definimos los umbrales para la prueba
calificacion_minima = 8.0
año_minimo = 2015   
#llamamos la funsion y guardamos el resultado
total_peliculas = contar_peliculas_polpulares_y_recientes(videoteca, calificacion_minima, año_minimo)
#mostramos la salida en la pantalla
print(f"resultados de la busqueda (calificacion>={calificacion_minima} y año>={año_minimo}): {total_peliculas}")
print(f"total de peliculas que cumplen los criterios: {total_peliculas}")
