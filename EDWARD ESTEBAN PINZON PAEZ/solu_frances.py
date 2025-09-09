import re

texto = ("Bonjour! En 2025, 17 ingénieurs créent ensemble. Liste: règle, compas, plan. Le prix est de 68,30€. Les étoiles (★) brillent la nuit. 13 chats dessinent, 12 chiens calculent. Le code #7788 est spécial. 16 jours de projet, 10 jours de repos. @tous créent. Le numéro magique est 919. Que feriez-vous avec 48,80€? La réponse est dans la liste: dessiner, calculer, créer. Construisez votre avenir! 100 mots, 16 entiers, 3 décimaux, 2 listas.")

enteros   = r"-?\b\d+\b"              
flotante  = r"-?\b\d+\.\d+\b"
booleano  = r"\b(True|False)\b"
string    = r'"([^"]*)"'              
listas = r"(?i)\bliste:\s*([^\.\n]+)"  # Encuentra la palabra lista y continua HASTA el punto
palabras = r"[A-Za-zÁÉÍÓÚáéíóúÜüÑñ]+"   # lee el número declarado de palabras

resul_enteros = re.findall(enteros, texto)
resul_float   = re.findall(flotante, texto)
resul_bool    = re.findall(booleano, texto)
resul_string  = re.findall(string, texto)
resul_list    = re.findall(listas, texto)
resul_palabras = re.findall(palabras, texto, flags=re.IGNORECASE)

print("Los resultados encontrados fueron:")
print("0. Se encontraron:", len(resul_palabras), "palabras, siendo =", resul_palabras)
print("1. Se encontraron:", len(resul_enteros), "enteros, siendo =", resul_enteros)
print("2. Se encontraron:", len(resul_float), "flotantes, siendo =", resul_float)
print("3. Se encontraron:", len(resul_bool), "booleanos, siendo =", resul_bool)
print("4. Se encontraron:", len(resul_string), "strings, siendo =", resul_string)
print("5. Se encontraron:", len(resul_list), "listados, siendo =", resul_list)