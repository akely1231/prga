sekundy = int(input("Kolik sekund? "))

minuty = sekundy // 60
zbytek = sekundy % 60
print(sekundy, "sekund je", minuty, "minut a", zbytek, "sekund.")

vek = int(input("Kolik je ti let? "))
dni = vek * 365
print("Jsi na světě zhruba", dni, "dní, tedy", dni * 24, "hodin.")
print("Za", 18 - vek, "let ti bude 18.")
