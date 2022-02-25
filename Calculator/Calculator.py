
def main():
    import time
    print(' +  => Sabiranje\n -  => Oduzimanje\n *  => Mnozenje\n /  => Deljenje\n %  => Ostatak deljenja\n // => Deljenje celog broja\n ** => Eksponent')
    print('Izaberite funkciju: ')
    operacija= input()
    if operacija == '+':
        print('Prvi sabirak: ')
        psabirak = input()
        print('Drugi sabirak: ')
        dsabirak = input()
        zbir = str(int(psabirak) + int(dsabirak))
        print('Zbir ta dva broja je '+ zbir)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        else:
            quit
    elif operacija == '-':
        print('Prvi broj: ')
        umanjenik = input()
        print('Drugi broj: ')
        umanjilac = input()
        razlika = str(int(umanjenik) - int(umanjilac))
        print('Razlika ta dva broja je '+ razlika)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit
    elif operacija == '*':
        print('Prvi broj: ')
        pmnoz = input()
        print('Drugi broj: ')
        dmnoz = input()
        mnozenje = str(int(pmnoz) * int(dmnoz))
        print('Rezultat mnozenja ta dva broja je '+ mnozenje)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit
    elif operacija == '/':
        print('Prvi broj: ')
        deljenik = input()
        print('Drugi broj: ')
        delilac = input()
        deljenje = str(int(deljenik) / int(delilac))
        print('Rezultat mnozenja ta dva broja je '+ deljenje)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit
    elif operacija == '%':
        print('Prvi broj: ')
        post = input()
        print('Drugi broj: ')
        dost = input()
        ostatak = str(int(post) % int(dost))
        print('Ostatak pri deljenju ta dva broja je '+ ostatak)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit
    elif operacija == '//':
        print('Prvi broj: ')
        cbroj1 = input()
        print('Drugi broj: ')
        cbroj1 = input()
        cbroj = str(int(cbroj1) // int(cbroj1))
        print('Broj '+str(cbroj1)+' moze biti u '+str(cbroj1)+ ' ' + str(cbroj)+ ' puta')
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit
    elif operacija == '**':
        print('Prvi broj: ')
        broj = input()
        print('Drugi broj: ')
        eksp = input()
        ekspo = str(int(broj) ** int(eksp))
        print('Eksponent tog broja je  '+ ekspo)
        print()
        print('Da li hocete jos da racunate?')
        odgovor = input()
        if odgovor == "da":
            time.sleep(1)
            main()
        elif odgovor=="ne":
            quit

    else :
        print('----{ Pogresna operacija }----')
        main()


print('Ovo je moj prvi kalkulator u Python-u')
print('Mozete da koristite +, -, *, /, %, //, **')
main()
