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


print('*** MENU PRINCIPAL ***\n' 
'1.- Turistas por país.\n' \
'2.- Turista por mes.\n' \
'3.- Eliminar turista.\n' \
'4.- Salir\n')
    
while True:
    try:
        opcion= int(input ("ingrese su opcion "))
        if opcion == 1:
            pais= input("ingrese pais ").lower()
            if pais == "brasil":
                print("Joao Silva,Ana Santos ")
            elif pais == "argentina":
                print("Julian Martinez,Agustin Morales,Martin Fernandez,Sofia Gomez ")
            elif pais == "mexico":
                print("Carlos Garcia,Maria Lopez ")
            elif pais == "estados unidos":
                print("John Doe,Emily Smith,Michael Brown,Jessica Davis ")
            else:
                ("No hay turistas de ese pais")
          elif opcion == 2:
            mes= int(input("ingrese el mes a buscar"))
            
    except:
        print("Error Ingrese valores validos")

