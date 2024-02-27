birim = str(input("Birim giriniz: "))

if birim == 'c' :
    print("Derece giriniz : ")
    cel = float(input())
    fah = (cel * 1.8) + 32
    print("\nFahrenheit : ", fah)

elif birim == 'f' :
    print("Derece giriniz : ")
    fah = float(input())
    cel = (fah - 32) / 1.8
    print("\nCelcius : ", cel)


