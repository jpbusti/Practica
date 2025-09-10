clientes = [{"id_cliente" : "1", "nombre" : "Juan", "apellido" : "Perez", "telefono" : "3123456789"},
           {"id_cliente" : "2", "nombre" : "Maria", "apellido" : "Gomez", "telefono" : "3123456786"},
           {"id_cliente" : "3", "nombre" : "Carlos", "apellido" : "Ramirez", "telefono" : "3123456787"}]

productos = [{"id_producto": "1", "nombre": "Laptop", "precio": "2500.00"},
             {"id_producto": "2", "nombre": "Mouse", "precio": "20.50"},
             {"id_producto": "3", "nombre": "Teclado", "precio": "45.00"},
             {"id_producto": "4", "nombre": "Monitor", "precio": "150.00"}]

ventas = [{"id_venta": "1", "id_cliente": "1", "id_producto": "1", "cantidad": "1"},
           {"id_venta": "2","id_cliente": "2", "id_producto": "2", "cantidad": "2"},
           {"id_venta": "3","id_cliente": "1","id_producto": "3","cantidad": "1"},
           {"id_venta": "4","id_cliente": "3","id_producto": "4","cantidad": "1"}]
class F:
    def write(self, filename, dictionary):
        enable = 1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys())
            for label in labels:
                f.write(label + ",")
            f.write("activo" + "\n")
            for a in dictionary:
                for d in a.values():
                    f.write(d )
                    f.write(",")
                f.write(str(enable)+"\n")
                
    def read(self, filename):
        with open(filename, "r", encoding = "utf-8") as f:
            for linea in f:
                print(linea.strip())
                
    def read(self, filename):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                for linea in f:
                    print(linea.strip())
        except FileNotFoundError:
            print ("El archivo no existe")
    
    def delete(self, filename, id):
        list = []
        with open(filename, "r", encoding = "utf-8") as f:
           list = f.readlines() 
        newlist = []
        for l in list:
            arr = l.strip().split(',')
            if str(arr[0]) == str(id):
                arr[len(arr) - 1] = "0"
                ll = ""
                count = 1
                for a in arr:
                    ll = ll + str(a)
                    if count  < len(arr):
                        ll = ll + ","
                    count += 1
                l = ll + "\n"
            newlist.append(l)
        self.write_array(filename, newlist)
                
    def write_array(self, filename, list):
        with open(filename, "w", encoding = "utf-8") as f:
            for l in list:
                f.write(l)
                
    def registrarcliente(self, clientes):
        nuevo_id = str(len(clientes) + 1)
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        cliente = {"id_cliente" : nuevo_id, "nombre" : nombre, "apellido" : apellido, "telefono" : telefono}
        clientes.append(cliente)
        
    def listarclientes(self, clientes):
        for cliente in clientes:
            print(cliente["nombre"] + " " + cliente["apellido"])
    
    def registrarpedido(self, pedidos):
        nuevo_id = str(len(pedidos) + 1)
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        pedido = {"id_producto" : nuevo_id, "nombre" : nombre, "precio": precio}
        pedidos.append(pedido)
        
    def registrarventa(self, ventas):
        nuevo_id = str(len(ventas) + 1)
        id_cliente = input("Ingrese el id del cliente: ")
        id_producto = input("Ingrese el id del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        venta = {"id_venta" : nuevo_id, "id_cliente" : id_cliente, "id_producto" : id_producto, "cantidad" : cantidad}
        ventas.append(venta)
        
    def listarventascliente():
        for c in clientes:
            if c["nombre"].lower() == nombre.lower():
                break
            
        id_cliente = c["id_cliente"]
        t = 0
        for v in ventas:
            if v["id_cliente"] == id_cliente:
                id_producto = v["id_producto"]
                cantidad = v["cantidad"]
                    
                for p in productos:
                    if p["id_producto"] == id_producto:
                        t += float(p["precio"]) * int(cantidad)
                        print(t)
                        break
        
    def ordenar_productos_por_precio(self, productos):
        n = len(productos)
        for i in range(n):
            for j in range(0, n - i - 1):
                precio_actual = float(productos[j]["precio"])
                precio_siguiente = float(productos[j + 1]["precio"])

                if precio_actual < precio_siguiente:
                    productos[j], productos[j + 1] = productos[j + 1], productos[j]
        
        print("Productos ordenados por precio (mayor a menor):")
        for producto in productos:
            print(f"ID: {producto['id_producto']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}")
f = F()
f.write("clientes.csv", clientes)
f.write("productos.csv", productos)
f.write("ventas.csv", ventas)

f.read("clientes.csv")
f.read("ventas.csv")
f.read("productos.csv")

        
while True:
    print("1. Registrar un cliente")
    print("2. Listar clientes")
    print("3. Eliminar un cliente")
    print("4. Registrar un producto")
    print("5. Guardar una venta")
    print("6. Listar las ventas realizadas por cliente")
    print("7. Salir")
    print("Seleccione una opción: ")
    op = input()
    if op == "1":
        F.registrarcliente("clientes.csv", clientes)
        f.write("clientes.csv", clientes)
    elif op == "2":
        F.listarclientes("clientes.csv", clientes)
    elif op == "3":
        print("Ingrese el ID del cliente a eliminar: ")
        id = input()
        f.delete("clientes.csv", id)
    elif op == "4":
        F.registrarpedido("productos.csv", productos)
        f.write("productos.csv", productos)
    elif op == "5":
        F.registrarventa("ventas.csv", ventas)
        f.write("ventas.csv", ventas)
    elif op == "6":
        nombre = input("Ingrese el nombre del cliente: ")        
        F.listarventascliente()
    elif op == "7":
        F.ordenar_productos_por_precio("productos.csv", productos)
        

    
        
        
        
    
   