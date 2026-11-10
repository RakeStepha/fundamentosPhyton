"""validar que una contraseña tenga al menos 8 caracteres"""
#input= "1234567"
#output="introduce minimo 8 caracteres"
# while True:
#     input_pasword=input("ingrese contraseña:")
#     if len(input_pasword)<8:
#             print("introduce minimo 8 caracteres")
#     else:
#             print("contraseña valida")
#             break

# """ingresar un numero y crear una tabla de multiplicar hasta el 10"""
# #Input: 1
# #output: 1*1 =1,1x2,1*3,

while True:
       number=int(input("introduce un numero:"))
       i=1
       while i<=10:
              print(f"{number} * {i}={number *i}")
              i=i+1

       