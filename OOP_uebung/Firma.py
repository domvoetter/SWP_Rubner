from matplotlib import pyplot as plt
import numpy as np

class Firma:

    def __init__(self, firmenname):
        self.firmenname = firmenname
        self.abteilungen = []

    def __str__(self):
        return f"Firmenname: {self.firmenname} \
            Anzahl der Abteilungen: {len(self.abteilungen)}"

    def anzMitarbeiter(self):
        anz = 0
        for a in self.abteilungen:
            anz += len(a.mitarbeiter)
        print("Es gibt " + str(anz) + " Mitarbeiter in der Firma \n")

    def anzGruppenleiter(self):
        anz = 0
        for a in self.abteilungen:
            anz += len(a.gruppenleiter)
        print("Es gibt " + str(anz) + " Gruppebleiter in der Firma \n")
    
    def anzAbteilungen(self):
        print("Es gibt " + str(len(self.abteilungen)) + " Abteilung in der Firma \n")

    def groessteAbteilung(self):
        name = ""
        size = 0
        for a in self.abteilungen:
            if len(a.mitarbeiter) > size:
                size = len(a.mitarbeiter)
                name = a.abteilungsname
        print("Die Abteilung " + name + " hat die größte Mitarbeiterstärke \n")
    
    def frauenmaenner(self):
        anzmaenner = 0
        anzfrauen = 0
        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if m.geschlecht == "m":
                    anzmaenner += 1
                else:
                    anzfrauen += 1
        prozent = anzfrauen / anzmaenner * 100
        print("Der Prozentanteil Frauen zu Männer beträgt " + str(prozent) + "\n")

        circle_values = np.array([anzfrauen, anzmaenner])
        label = ["Frauen", "Maenner"]
        plt.pie(circle_values, labels = label, autopct='%1.2f%%')
        plt.show()
        