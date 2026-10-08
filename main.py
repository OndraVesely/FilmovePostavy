from datetime import datetime
with open("postavy.txt", "r", encoding="utf-8") as soubor, \
    open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
    for radek in soubor:
        udaje = radek.strip().split("#")
        jmeno = udaje[0]
        vek = int(udaje[1])
        pohlavi = udaje[2]
        zvire = udaje[3]
        promitani_filmu = datetime.strptime(udaje[4], '%Y-%m-%d')
        oblibenost = float(udaje[5])

        if oblibenost > 2.5:
            print(f"{jmeno}")
            print(f"{vek}")
            print(f"{pohlavi}")
            print(f"{zvire}")
            print(f"{promitani_filmu.strftime('%Y-%m-%d')}")
            print(f"{oblibenost}")
            print("--------------------")

            vystup.write(f"{jmeno}\t{vek}\t{pohlavi}\t{zvire}\t{promitani_filmu.strftime('%Y-%m-%d')}\t{oblibenost}\n")