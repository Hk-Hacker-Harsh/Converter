import time

import os


if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


print("Thank you, for using my project.")
time.sleep(1.5)
print("Created By: Hk Hacker (a.k.a.  HARSH KHANDAL)")



while True:
    time.sleep(1.5)

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


    def hexadec():          #hexadecimal to decimal
        hexdec = input("Enter Hexadecimal Value (Space Sep.) : ")
        hexdeclst = list(hexdec.split())
        hexdeclst2=[]

        for i in hexdeclst:
            hexdeclst2.append(int(i, 16))

        print(hexdeclst2)
        return hexdeclst2

    def morseencode():      #encode morse code
        morseen=input("Enter Morse Code in terms of 0s(.) & 1s(-) & /s(SPACE) : ")

        morenlst=list(morseen.split())
        morenlst2=[]
        morenstr=""
        
        for i in morenlst:
            match i:
                case '01':
                    morenlst2.append('a')

                case '1000':
                    morenlst2.append('b')
                
                case '1010':
                    morenlst2.append('c')

                case '100':
                    morenlst2.append('d')

                case '0':
                    morenlst2.append('e')

                case '0010':
                    morenlst2.append('f')

                case '110':
                    morenlst2.append('g')

                case '0000':
                    morenlst2.append('h')

                case '00':
                    morenlst2.append('i')

                case '0111':
                    morenlst2.append('j')

                case '101':
                    morenlst2.append('k')

                case '0100':
                    morenlst2.append('l')
                
                case '11':
                    morenlst2.append('m')

                case '10':
                    morenlst2.append('n')

                case '111':
                    morenlst2.append('o')

                case '0110':
                    morenlst2.append('p')

                case '1101':
                    morenlst2.append('q')

                case '010':
                    morenlst2.append('r')

                case '000':
                    morenlst2.append('s')

                case '1':
                    morenlst2.append('t')

                case '001':
                    morenlst2.append('u')

                case '0001':
                    morenlst2.append('v')

                case '011':
                    morenlst2.append('w')

                case '1001':
                    morenlst2.append('x')

                case '1011':
                    morenlst2.append('y')

                case '1100':
                    morenlst2.append('z')

                case '11111':
                    morenlst2.append('0')

                case '01111':
                    morenlst2.append('1')

                case '00111':
                    morenlst2.append('2')

                case '00011':
                    morenlst2.append('3')

                case '00001':
                    morenlst2.append('4')

                case '00000':
                    morenlst2.append('5')

                case '10000':
                    morenlst2.append('6')

                case '11000':
                    morenlst2.append('7')

                case '11100':
                    morenlst2.append('8')

                case '11110':
                    morenlst2.append('9')

                case '010101':
                    morenlst2.append('.')

                case '110011':
                    morenlst2.append(',')

                case '111000':
                    morenlst2.append(':')

                case '001100':
                    morenlst2.append('?')

                case '011110':
                    morenlst2.append('\'')

                case '100001':
                    morenlst2.append('-')

                case '10010':
                    morenlst2.append('/')

                case '101101':
                    morenlst2.append(')')

                case '10110':
                    morenlst2.append('(')

                case '010010':
                    morenlst2.append('"')

                case '10001':
                    morenlst2.append('=')

                case '01010':
                    morenlst2.append('+')

                case '011010':
                    morenlst2.append('@')

                case '/':
                    morenlst2.append(' ')

                case _ :
                    print("Invalid Morse. Please Enter a Correct one.")

        print(morenlst2)
        print(morenstr.join(morenlst2))

        return morenlst2

    def bindec():           #binary to decimal
        bindec = input("Enter Binary (Space Sep.) :")
        bindeclst2 = []
        bindeclst = bindec.split()

        
        for i in bindeclst:
            bindeclst2.append(int(i, 2))
        
        print(bindeclst2)

        return bindeclst2
        
    def decascii():         #Decimal to ascii
        decascii = input("Enter Decimal Value (Space Sep.) : ")

        decasciilst = []
        decasciilst2 = []
        decasciilst=decascii.split()

        for i in decasciilst:
            decasciilst2.append(chr(int(i)))

        print(decasciilst2)
        return decasciilst2

    def octdec():               #octal to decimal
        octdec = input("Enter Octal Value (Space Sep.) : ")
        octdeclst2 = []
        octdeclst = octdec.split()

        for i in octdeclst:
            octdeclst2.append(int(i, 8))

        print(octdeclst2)

        return octdeclst2

    def asciidec():             #ascii to decimal

        asciidec = input("Enter ASCII Value (Space Sep.) : ")

        asciideclst = []
        asciideclst2 = []
        asciideclst=asciidec.split()

        for i in asciideclst:
            asciideclst2.append(ord(i))

        print(asciideclst2)
        return asciideclst2

    def decbin():               #Decimal to binary
        decbin = input("Enter Decimal Value :")
        decbinlst2 = []
        decbinlst3 = []
        decbinlst = decbin.split()

        for i in decbinlst: 
            i = int(i)
            while i > 0:   
                decbinlst2.append(i%2)
                i = i//2

            decbinlst2.reverse()
            merge = ''.join(map(str, decbinlst2))
            decbinlst3.append(merge)
            decbinlst2=[]
        print(decbinlst3)
        return decbinlst3

    def decoct():                  #Decimal to octal
        decoct = input("Enter Decimal Value :")
        decoctlst2 = []
        decoctlst3 = []
        decoctlst = decoct.split()

        for i in decoctlst: 
            i = int(i)
            while i > 0:   
                decoctlst2.append(i%8)
                i = i//8

            decoctlst2.reverse()
            merge = ''.join(map(str, decoctlst2))
            decoctlst3.append(merge)

            decoctlst2=[]

        print(decoctlst3)
        return decoctlst3

    def morsedecode():           #Morse Decode
        moralp = input("Enter Value : ")
        morlst=[]
        morstr=""
        moralp = list(moralp)

        for i in moralp:
            for j in i:
                match j:
                    case "A" | "a":
                        morlst.append('01')
                    case "B" | "b":
                        morlst.append('1000')
                    case "C" | "c":
                        morlst.append('1010')
                    case "D" | "d":
                        morlst.append('100')
                    case "E" | "e":
                        morlst.append('0')
                    case "F" | "f":
                        morlst.append('0010')
                    case "G" | "g":
                        morlst.append('110')
                    case "H" | "h":
                        morlst.append('0000')
                    case "I" | "i":
                        morlst.append('00')
                    case "J" | "j":
                        morlst.append('0111')
                    case "K" | "k":
                        morlst.append('101')
                    case "L" | "l":
                        morlst.append('0100')
                    case "M" | "m":
                        morlst.append('11')
                    case "N" | "n":
                        morlst.append('10')
                    case "O" | "o":
                        morlst.append('111')
                    case "P" | "p":
                        morlst.append('0110')
                    case "Q" | "q":
                        morlst.append('1101')
                    case "R" | "r":
                        morlst.append('010')
                    case "S" | "s":
                        morlst.append('000')
                    case "T" | "t":
                        morlst.append('1')
                    case "U" | "u":
                        morlst.append('001')
                    case "V" | "v":
                        morlst.append('0001')
                    case "W" | "w":
                        morlst.append('011')
                    case "X" | "x":
                        morlst.append('1001')
                    case "Y" | "y":
                        morlst.append('1011')
                    case "Z" | "z":
                        morlst.append('1100')
                    case "0":
                        morlst.append('11111')
                    case "1":
                        morlst.append('01111')
                    case "2":
                        morlst.append('00111')
                    case "3":
                        morlst.append('00011')
                    case "4":
                        morlst.append('00001')
                    case "5":
                        morlst.append('00000')
                    case "6":
                        morlst.append('10000')
                    case "7":
                        morlst.append('11000')
                    case "8":
                        morlst.append('11100')
                    case "9":
                        morlst.append('11110')
                    case " ":
                        morlst.append('/')
                    case ".":
                        morlst.append('010101')
                    case ",":
                        morlst.append('110011')
                    case ":":
                        morlst.append('111000')
                    case "?":
                        morlst.append('001100')
                    case "'":
                        morlst.append('011110')
                    case "-":
                        morlst.append('100001')
                    case "/":
                        morlst.append('10010')
                    case "(":
                        morlst.append('10110')
                    case ")":
                        morlst.append('101101')
                    case "\"":
                        morlst.append('010010')
                    case "=":
                        morlst.append('10001')
                    case "+":
                        morlst.append('01010')
                    case "@":
                        morlst.append('011010')
        print(morlst)
        for i in morlst:
            morstr = morstr + i
            morstr = morstr + " "
        print(morstr)
        return morstr, morlst

    def dechex():           #Decimal to hexadecimal
        dechex = input("Enter Decimal Value :")
        dechexlst2 = []
        dechexlst3 = []
        dechexstr = ""
        dechexlst = dechex.split()

        for i in dechexlst: 
            i = int(i)
            while i > 0:   
                if i%16 <= 9:
                    dechexlst2.append(i%16)
                    
                if i%16 >= 9:
                    match i%16:
                        case 10:
                            dechexlst2.append("A")
                        case 11:
                            dechexlst2.append("B")
                        case 12:
                            dechexlst2.append("C")
                        case 13:
                            dechexlst2.append("D")
                        case 14:
                            dechexlst2.append("E")
                        case 15:
                            dechexlst2.append("F")
                i = i//16

            merge = ''.join(map(str, dechexlst2))
            dechexlst3.append(merge)

            dechexlst2=[]

        for i in dechexlst3:
            dechexstr = dechexstr + i + " "

        print(dechexlst3)
        print(dechexstr)

        return dechexlst3 , dechexstr


    print(''' Select Any One:
        1. Binary to Decimal
        2. Octal to Decimal
        3. Hexadecimal to Decimal
        4. ASCII to Decimal
        5. Morse Encode
        6. Morse Decode
        7. Decimal to ASCII
        8. Decimal to Hexadecimal
        9. Decimal to Octal
        10. Decimal to Binary
    ''')


    choice = int(input("Enter Your choice : 1/2/3/4/5/6/7/8/9/10 : "))

    match choice:
        case 1:
            while True:
                bindec()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 2:
            while True:
                octdec()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 3:
            while True:
                hexadec()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 4:
            while True:
                asciidec()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")
                
        case 5:
            while True:
                morseencode()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 6:
            while True:
                morsedecode()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 7:
            while True:
                decascii()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 8:
            while True:
                dechex()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case 9:
            while True:
                decoct()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!") 

        case 10:
            while True:
                decbin()
                aga=input("Do You Want To Run it Again? Y/N : ")
                if aga=="Y" or aga =="y":
                    pass
                elif aga=="N" or aga=="n":
                    break
                else:
                    print("Error!! Incorrect Choice!")

        case _:
            print("Error!! Incorrect choice!!")


    print()
    again=input("Go To Main Menu?? ('N' to Exit) Y/N : ")

    if again=='Y' or again=='y':
        pass
    elif again=='N' or again=='n':
        print("Exiting!!!")
        time.sleep(2)
        break




    #This code is written in Python language by Hk (Harsh Khandal) Hacker..... Available on Github too.