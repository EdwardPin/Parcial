import re

texto = ("En el año 2025, 19 ingenieros construyen juntos. ¡Hola! ¿Te gusta la ingeniería? "
"El cielo técnico, las estrellas (★) brillan. 15 niños diseñan, 14.25 horas de trabajo. "
"Lista: regla, compás, plano. El costo es $70.10. ¿Sabías que el código #5566 es especial? "
"La vida es creación, @todos participan. El tiempo avanza, 16 días de proyecto. ¡Construye! "
"El número especial es 909. ¿Qué harías con 45.60 pesos? La respuesta está en la lista: "
"diseñar, calcular, crear. ¡Construye tu futuro! 100 palabras, 16 enteros, 3 decimales, 2 listas.")

enteros   = r"-?\b\d+\b"              
flotante  = r"-?\b\d+\.\d+\b"
booleano  = r"\b(True|False)\b"
string    = r'"([^"]*)"'              
listas = r"(?i)\blista:\s*([^\.\n]+)"  # Encuentra la palabra lista y continua HASTA el punto
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

