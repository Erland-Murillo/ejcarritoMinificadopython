class ventas():
    def __init__(self, p_cliente):
        self.cliente = p_cliente
        self.producto = []
        self.precio = []
    def presentarse(self):
        print("******** {} ********").format(self.cliente)
        for i in self.producto:
            print(i)
            return "soy el cliente %s "%(self.cliente)

    def registrarcompra(self):
        print("gestion de compras")
        producto = input("digite el producto")
        self.producto.append(producto)
        print("producto {} registrado".format(producto))
        extra = input("desea registrar otro producto?: s/n: ")
        if(extra == "s"):
            self.registrarcompra()
        else:
            return "producto registrado"

    def menu(self):
            opciones = """
            Menu de la aplicacion:
            1.Presentarse
            2.Registrar Compra
                        """


juan = ventas("juan")
carolina = ventas("carolina")

print(juan.registrarCompra())