import re

texto = ("Ciao! Nel 2025, 18 ingegneri progettano insieme. Lista: righello, compasso, piano. Il prezzo è €65,90. Le stelle (★) brillano sopra il progetto. 12 gatti disegnano, 11 cani calcolano. Il codice #9911 è speciale. 15 giorni di lavoro, 11 di riposo. @tutti progettano. Il numero magico è 929. Cosa faresti con 42,80€? La risposta è nella lista: disegnare, calcolare, creare. Costruisci il tuo futuro! 100 parole, 15 interi, 3 decimali, 2 listas.")

enteros   = r"-?\b\d+\b"              
flotante  = r"-?\b\d+\,\d+\b"
booleano  = r"\b(True|False)\b"
string    = r'"([^"]*)"'              
listas = r"(?i)\blista:\s*([a-zàèéìòù,\s]+)\."  # Encuentra la palabra lista y continua HASTA el punto 
#Se especificaron palabras a-z y especiales porque si lo dejo asi nomas, detecta la ultima como una lista por el mismo nombre.
palabras = r"[A-Za-zÁÉÍÓÚáàéèíìóòúùÜüÑñ]+"  # Lee desde la A-Z mayuscula, luego minuscula, y luego cada caracter especial (tilde, Ñ)

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