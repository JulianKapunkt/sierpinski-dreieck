from random import choice
import matplotlib.pyplot as plt

#Die 3 Eckpunkte 
a = [0, 0]
b = [250, 250]
c = [500, 0]

#Eine Liste der Eckpunkte, um mit random.choice 
#später einen zufällig aus der Liste auswählen zu könen
eckpunkte = [a,b,c]

#Die Listen der generierten Punkte. punkte_x[0] und punkte_y[0] ergeben 
#zusammen den Startpunkt
punkte_x = [50]
punkte_y = [50]


def berechne_punkte():
	"""Die Funktion wählt zufällig einen der drei Eckpunkte aus. 
	Danach wird die Entfernung der x und y Punkte zu dem Eckpunkt berechnet.
	Die Entfernung wird durch 2 geteilt.
	So wird der Punkt berechnet, der auf der Hälfte der Strecke zwischen 
	Eckpunkt und dem aktuellen Punkt liegt.
	Der Punkt wird zuletzt in punkte_x und punkte_y eingefügt."""

	for i in range(10000):

		ziel_punkt = choice(eckpunkte)
		print(f"Der ausgewählte Punkt ist: {ziel_punkt}")

		#wählt den letzten Eintrag der punkte_x aus
		abstand_x = ziel_punkt[0] - punkte_x[-1]
		print (f"Der Abstand auf der x Achse  zum ziel_punkt beträgt: {abstand_x}")

		abstand_y = ziel_punkt[1] - punkte_y[-1] 
		print (f"Der Abstand auf der y Achse  zum ziel_punkt beträgt: {abstand_y}")

		neuer_x_punkt = (abstand_x // 2) + punkte_x[-1]
		print (neuer_x_punkt)

		punkte_x.append(neuer_x_punkt)

		neuer_y_punkt = (abstand_y // 2) + punkte_y[-1]
		print (neuer_y_punkt)
		punkte_y.append(neuer_y_punkt)


berechne_punkte()
print (punkte_x)
print (punkte_y)

fig, ax = plt.subplots()
#ax.plot(x_coordinates, y_coordinates)
ax.scatter(punkte_x, punkte_y, s = 20)

plt.show()