meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "F": "Expresion de tristesa o de respeto"
            }

print("Bienvenidos al diccionario de palabras modernas")

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys(5):
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    print("Esta palabra no esta en el diccionario")
