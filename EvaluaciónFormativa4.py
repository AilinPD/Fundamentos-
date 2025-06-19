turistas =  {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

while True:
    print('*** MENU PRINCIPAL ***\n' 
    '1.- Turistas por país.\n' \
    '2.- Turista por mes.\n' \
    '3.- Eliminar turista.\n' \
    '4.- Salir\n')
    
    try:
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1:
            pais = input("Ingrese país: ").lower()
            encontrados = []
            
            for datos in turistas.values():
                if datos[1].lower() == pais:
                    encontrados.append(datos[0])
            
            if len(encontrados) > 0:
                print(encontrados)
            else:
                print("No hay turistas de ese país.")
        
        elif opcion == 2:
            while True:
                try:
                    mes = int(input("Ingrese el mes a buscar: "))
                    if 1 <= mes <= 12:
                        break
                    else:
                        print("¡Error! El mes debe ser entre 1 y 12")
                except:
                    print("¡Error! Ingrese un número válido")
            
            total_turistas = len(turistas)
            turistas_mes = 0
            
            for datos in turistas.values():
                fecha = datos[2].split("-")  
                if int(fecha[1]) == mes:
                    turistas_mes += 1
            
            porcentaje = round((turistas_mes / total_turistas) * 100, 1)
            print(f"El porcentaje de turistas es: {porcentaje}%")
        
        elif opcion == 3:
            nombre = input("Ingrese nombre del turista a eliminar: ").lower()
            eliminado = False
            
           
            for id_turista, datos in list(turistas.items()):
                if datos[0].lower() == nombre:
                    del turistas[id_turista]
                    eliminado = True
            
            if eliminado:
                print("Turista eliminado con éxito.")
            else:
                print("Turista no encontrado. No se pudo eliminar.")
        
        elif opcion == 4:
            print("Programa terminado...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")
    
    except ValueError:
        print("Debe ingresar una opción válida!!")