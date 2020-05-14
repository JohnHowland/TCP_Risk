
class Player():
    def __init__(self, name, color, id):
        self.name = name
        self.color = color
        self.id = id  # player number
        self.counties = []  # List of tuple countries... {Country, num solders}

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_countries(self):
        return self.counties

    def set_countries(self, country_list):
        self.counties = country_list
