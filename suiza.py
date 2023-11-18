from matplotlib import pyplot as plt
desempleos = []
inflaciones = []
pibs = []
with open('desempleo_suiza.csv', 'r') as file:
	for linea in file.readlines()[1:]:
		desempleos.append(float(linea.split(',')[6]))
	file.close()

with open('inflacion_suiza.csv', 'r') as file:
	for linea in file.readlines()[1:]:
		inflaciones.append(float(linea.split(',')[6]))
	file.close()

with open('gdp_suiza.csv', 'r') as file:
	for linea in file.readlines()[1:]:
		pibs.append(float(linea.split(',')[6])/ 100000)

anos = range(2010, 2021)
plt.plot(anos, desempleos, label='Desempleo', color='blue')
plt.plot(anos, inflaciones, label='Inflacion', color='red')
plt.plot(anos, pibs, label='PIB (Mil Millones)', color='green')

plt.xticks(anos)


plt.title('Desempleo vs Inflacion vs PIB')

plt.legend()

plt.show()