class Spaceship:
    shape: 'oval'
    hyperdrive: 'Gravity Propelled'
    galaxy: 'Juilian 647'

    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "This spaceship is called the %s. An %s %s, created in the year %d." % (self.name, self.make, self.model, self.year)


Millenium_Falcon = Spaceship("Millenium Falcon", "Corellian Engineering Corporation", "YT-Series", 1300)

print(Millenium_Falcon)