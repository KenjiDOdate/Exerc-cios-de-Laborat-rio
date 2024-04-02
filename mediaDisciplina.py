

provaI = float(input("\ninsira a nota da prova 1:\n"))
provaII = float(input("\ninsira a nota da prova 2:\n"))
trab = float(input("\n\n insira a nota do trabalho:\n"))
parti = float(input("\no valor da presença:\n"))

provaT = provaI + provaII

media = (provaT + (3*trab)+parti)/10

print(f"\n\nValor da media:\n{media}")