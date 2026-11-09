
while True:
    intrebare = input("Hei! Da-mi un numar de la 3 la 10 (sau scrie 'stop'): ")

    if intrebare.lower() == "stop":
        print("Paa! 👋")
        break

    if not intrebare.isdigit():
        print("❌ Te rog sa introduci un numar valid!")
        continue

    numar = int(intrebare)

    if numar < 3 and numar > 10:
        print("⚠️ Te rog scrie un numar intre 3 si 10!")
        continue

    for i in range(numar, 0, -1):
        print(i)

    print("Start! 🚀\n")
    