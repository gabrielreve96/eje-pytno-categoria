"""
Podríamos comenzar con un programa que permita agregar productos al inventario, mostrar el inventario actual, y simular la compra de productos. 
"""





# menu_usuario_basico= input ( """
# 1-ver productos y comprar productos
# 2-ir al carrito de compras
# 3-mi perfil
# 4-historial de compras
# 6-salir 


# """)


# menu_admin =(  """
# 1-crear producto\n
# 2-eliminar producto\n
# 3-editar producto\n
# 4-ver todos los productos
# 5-ver todos los usuario creados
# 6-ver todos los usuarios mienbros\n
# 7-salir
 
# """)


carrito_compras=[]

articulos_tienda=[
    
    {   
        "orden_compra":1,
        "articulo":"vestido",
        "color":"rojo",
        "precio":"23$",
        "catidad":22
        
    },
       {
        "orden_compra":2,
        "articulo":"pantalon",
        "color":"verde",
        "precio":"23$",
        "catidad":22
        
    },
    {
        "orden_compra":3,
        "articulo":"gorra",
        "color":"rojo",
        "precio":"23$",
        "catidad":22
        
    },
    {
        "orden_compra":4,
        "articulo":"reloj",
        "color"
        :"rojo",
        "precio":"23$",
        "catidad":22
        
    },
             
    
]


def obetiendoRol(rol):
    return main_usuario_basico()






    
    
    
    

def main_usuario_basico():
    opcion= input( """
    1 -ver y comprar articulos
    2- eliminar un producto del carrito
    3-vaciar carrito de compras
    4 -ver carrito de compra

    """)
    return  swtich_casos_usuario_basico(opcion)
    
"""
usuo para usuario basico
"""
    
def ver_y_comprar_articulo():
    for articulo in articulos_tienda:
        print(articulo)
    
    seleccion_orden_compra = input("Por favor ingrese el número de orden de compra para añadir al carrito: ")
    seleccion = None
    for articulo in articulos_tienda:
        if str(articulo.get("orden_compra")) == seleccion_orden_compra:
            seleccion = articulo
            carrito_compras.append(seleccion)
            break
    
    if seleccion:
        print("===============EL PRODUCTO FUE AGREGADO CON EXITO====================🛒🛒🛒🛒🛒🛒")
        print(carrito_compras )
        main_usuario_basico()
        
    else:
        print("Error: No se encontró ningún artículo con ese número de orden de compra.")





def eliminar_un_pruducto_del_carrito():
    id_articulo = input("ingrese el nombre del articulo que desea eliminar")
    for articulos_agregados in carrito_compras:
        if articulos_agregados.get("articulo") == id_articulo:
           
            index=carrito_compras.index(articulos_agregados)
            carrito_compras.pop(index)
            
            print("=========PRODUCTO ELIMINADO CON EXITO ================")
            print(F"{articulos_agregados}")
            print(f"{carrito_compras} no hay articulos")
            main_usuario_basico()
            break;
        else:
            print("el producto no existe")
    
    
    
def vaciar_carrito_compras():
    confimacion=input("segura desea vaciar el carrito? 😒")
    if confimacion == "si":
        carrito_compras.clear()
        print("===========CARRITO VACIO=============🛒")
        print(carrito_compras)
        main_usuario_basico()
    else:
        print("operacion cancelada con exito")
        main_usuario_basico()
    





def ver_carrito_compras():
    if len(carrito_compras) > 0:
        tota_a_pagar=0
        for articulos in carrito_compras:
            tota_a_pagar+=int(articulos.get("precio").split("$")[0])
            print(f"========Algunos datos  cantidad de productos en el carrito  = {len(carrito_compras)}  Total a pagar = {tota_a_pagar}")
            print(f"articulos agregados ====>>>>>>>> {carrito_compras}")
            main_usuario_basico()
    else:
        print("actualmente no posee ningun articulo agregado al carrito")
        main_usuario_basico()








def swtich_casos_usuario_basico(argumento):
    sw = {
        1: ver_y_comprar_articulo,  # Sin paréntesis para pasar la referencia de la función
        2: eliminar_un_pruducto_del_carrito,  # Sin paréntesis para pasar la referencia de la función
        3:vaciar_carrito_compras,
        4:ver_carrito_compras
    }

    # Verificar si el argumento dado está en el diccionario
    if int(argumento) in sw:
        # Llamar a la función correspondiente
        return sw[int(argumento)]()
    else:
        return "Caso no válido"

# Ejemplo de uso


    
    


        
                

def interfaz_sesion(email, clave):
    usuarios = [
        
        {"email": "usuario@example.com", "clave_usuario": "usuario123", "rol": "basico"}
    ]

    def consultar_usuario():
        for usuario in usuarios:
            if usuario["email"] == email and usuario["clave_usuario"] == clave:
                 
                return {
                    "usuario":email,
                    "rol":usuario["rol"]
                }
        return {
             "usuario":False,
             "rol":False
        }

    return consultar_usuario

while True:
    email = input("Ingrese su email por favor: ")
    clave = input("Ingrese su clave por favor: ")
    sesion = interfaz_sesion(email, clave)()  # Llamamos a la función devuelta por interfaz_sesion

    if sesion.get('rol') != False:
        obetiendoRol(sesion.get("rol")) 
        break
    else:
        print("¡Credenciales incorrectas! Inténtelo de nuevo.")

    



                
                
       