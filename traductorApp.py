import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    """ Recibe una palabra como parametro, comprueba si existe y luego devuelve la descripción de la misma. """
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Te refieres a %s ? Presiona Y como si, o N como no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "La palabra no existe. Intente otra vez."
        else:
            return "No logramos entender tu palabra."
    else:
        return "La palabra no existe. Intente otra vez."

print('Hola!')
word = input("Escriba una palabra(en inglés): ")
print()
print('Tu palabra describe lo siguiente:')
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
