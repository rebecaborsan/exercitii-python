
while True:
    intrebare = input("Hei! Dă-mi un număr de la 3 la 10 (sau scrie 'stop'): ")

    if intrebare.lower() == "stop":
        print("Paa! 👋")
        break

    if not intrebare.isdigit():
        print("❌ Te rog să introduci un număr valid!")
        continue

    numar = int(intrebare)

    if numar < 3 and numar > 10:
        print("⚠️ Te rog scrie un număr între 3 și 10!")
        continue

    for i in range(numar, 0, -1):
        print(i)

    print("Start! 🚀\n")
    