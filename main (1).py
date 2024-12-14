class Bear:

    def __init__(self, type="Polar", color="White"):
        self.type = type
        self.color = color

    def bear_info(self):
        print("Bears can eat honey.")

    def bear_type(self):
        print("This bear is a", self.type)

    def bear_color(self):
        print("This bear is", self.color)


class Teddy:

    def __init__(self, name="Pushok", material="Cotton"):
        self.name = name
        self.material = material

    def teddy_info(self):
        print("Teddys are soft")

    def hug(self):
        print("Love you! <3")

    def teddy_name(self):
        print("This teddy is called", self.name)

    def teddy_material(self):
        print("This teddy is made of", self.material)


class TeddyBear(Bear, Teddy):

    def __init__(self,
                 name="Pushok",
                 material="Cotton",
                 color="White",
                 type="Polar"):
        self.type = type
        self.color = color
        self.name = name
        self.material = material

    pass


pushok = TeddyBear()
pushok.bear_color()
pushok.bear_type()
pushok.bear_info()
pushok.teddy_material()
pushok.teddy_info()
pushok.teddy_name()
pushok.hug()
