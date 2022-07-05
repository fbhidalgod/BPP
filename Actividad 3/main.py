class Areas:
    """Clase para calcular las áreas de diferentes figuras geométricas

    Métodos:
    =========
    area_cuadrado:
        Método para calcular el área de un cuadrado
    area_triangulo:
        Método para calcular el área de un triángulo
    """
    def area_cuadrado(lado):
        """
            Función para calcular el área de un cuadrado

            Args:
                lado (int): Valor del lado del cuadrado
        """
        return lado*lado

    def area_triangulo(base, altura):
        """
            Función para calcular el área de un triángulo

            Args:
                base (int): Valor de la base del triángulo
                altura (int): Valor de la altura del triángulo
        """
        return (base*altura)/2

help(Areas)
