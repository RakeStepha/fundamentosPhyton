
# users=[
# ["juan",25,"m","juan@email.com.pe"]
# ["Maria",30,"f","maria<@gmail.com.pe"]
# ["Ana",28,"m","ana@gmail.com.pe"]
# ["Pedro",35,"m","pedro@gmail.com.pe"]

# ]

# user_format={
#     "id":1,
#     "nombre":"Juan",
#     "edad":25,
#     "genero":"m",

# }
# new_users=[]
# # i=1
# for user in users:
#     user_dict={
#         "id": i,
#         "name":user[0],
#         "age":user[1],
#         "gender":user[2],
#         "email":user[3]

#     }
# i+=1
# new_users.append(user_dict)
# print(new_users)
vehiculo={
    "marca":"toyota",
    "modelo":"corolla",
    "año":2026,

}
"""modificar y agregar elementos"""
vehiculo["marca"]="honda"
vehiculo["color"]="rojo"
print(vehiculo)

del vehiculo["color"]
vehiculo.pop("año")
print(vehiculo)
"""metodos utiles"""
print(vehiculo.keys())#devuelve claves de diccionarios
print(vehiculo.values())#devuelve los valores del diccionario
print(vehiculo.items())#devuelve una lista de tuplas con las claves  y valores del diccionario
"""iterar sobre un diccionrio"""
for clave in vehiculo:
    print(clave,vehiculo[clave])

for clave,valor in vehiculo.items():
    print(clave,valor)
