import os
import sys
from time import sleep

BK  = '\x1b[0;30m'
BL  = '\x1b[0;34m'
GN  = '\x1b[0;32m'
CY  = '\x1b[0;36m'
R   = '\x1b[0;31m'
PE  = '\x1b[0;35m'
BW  = '\x1b[0;33m'
LG  = '\x1b[0;37m'
DG  = '\x1b[1;30m'
LB  = '\x1b[1;34m'
LGN = '\x1b[1;32m'
LC  = '\x1b[1;36m'
LR  = '\x1b[1;31m'
LP  = '\x1b[1;35m'
Y   = '\x1b[1;33m'
W   = '\x1b[1;37m'
MN  = '\x1b[101m'
MS  = '\x1b[0m'

def menu():
    os.system('clear')
    print(LR + u'\u2554\u2550\u2550\u2557\u2554\u2550\u2550\u2557\u2554\u2550\u2550\u2557\u2554\u2550\u2557\u2554\u2550\u2550\u2557\u2554\u2550\u2557\u2554\u2550\u2557')
    print(LR + u'\u2551\u2550\u2550\u2563\u255a\u2557\u2554\u255d\u2551\u2554\u2557\u2551\u2551\u256c\u2551\u255a\u2557\u2554\u255d\u2551\u2566\u255d\u2551\u256c\u2551')
    print(W + u'\u2560\u2550\u2550\u2551\u2500\u2551\u2551\u2500\u2551\u2560\u2563\u2551\u2551\u2557\u2563\u2500\u2551\u2551\u2500\u2551\u2569\u2557\u2551\u2557\u2563')
    print(W + u'\u255a\u2550\u2550\u255d\u2500\u255a\u255d\u2500\u255a\u255d\u255a\u255d\u255a\u2569\u255d\u2500\u255a\u255d\u2500\u255a\u2550\u255d\u255a\u2569\u255d   ' + Y + 'v1')
    print(W + u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500')
    print(W + 'Author : Mr.iVx7')
    print(W + u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500')
    print(LGN + '{ ' + W + '1' + LGN + ' } ' + W + 'Package')
    print(LGN + '{ ' + W + '2' + LGN + ' } ' + W + 'Tampilan')
    print(LGN + '{ ' + W + '3' + LGN + ' } ' + W + 'Informasi')
    print('')
    print(LGN + '{ ' + W + '0' + LGN + ' } ' + W + 'Exit')
    print('')
    pilih = input(W + '[ ' + LR + 'Choice' + W + ' ] ' + LGN + u'\u2022>' + LC + '  ')
    if pilih == '1' or pilih == '01':
        play()
    elif pilih == '2' or pilih == '02':
        tampilan()
    elif pilih == '3' or pilih == '03':
        os.system('clear')
        info()
    elif pilih == '0' or pilih == '00':
        print(W + '')
        os.system('login')
    else:
        print('')
        print(W + 'Wrong Input !!')
        print('')
        asq = input(W + '[ ' + LR + 'Kembali' + W + ' ]')
        os.system('clear')
        menu()


def play():
    os.system('clear')
    print(LB + '[ ! ] Download Starting...')
    sleep(4)
    print(LR + '[ ! ] Please Dont Turn Off Your System..')
    sleep(4)
    print(W + ' ')
    os.system('apt update && apt upgrade && apt install curl && apt install git && apt install wget && pkg install python2 && pkg install python2 && pkg install root-repo && pkg install unstable-repo && pkg install x11-repo && apt install ruby && apt install cowsay && apt install clang && apt install apt install figlet && gem install lolcat && apt install neofetch && apt install openssh && apt install toilet && apt install nodejs && apt install mc')
    sleep(3)
    print(LGN + u'[ \u25cf ] Installing is Done..')
    print('')
    jas = input(W + '[ ' + LR + 'Kembali ' + W + ']')
    sleep(2)
    os.system('clear')
    menu()


def info():
    os.system('clear')
    print(LGN + u'\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac' + W + '' + Y + u'\u2726' + W + 'Informasi' + Y + u'\u2726' + LGN + u'\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac')
    sleep(2)
    print(W + '* Tools ini Adalah Tools Installer.. ')
    sleep(2)
    print('* Tools ini Tidak berbahaya sama sekali.. ')
    sleep(2)
    print('* Tools ini dibuat tanggal 6 / 9 / 2019..')
    sleep(2)
    print('* Tools ini Versi 1.0')
    sleep(2)
    print('* Github : https://github.com/ivx7 ')
    print(LGN + u'\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac')
    print('')
    hoq = input(W + '[ ' + LR + 'Kembali' + W + ' ]')
    os.system('clear')
    menu()


def tampilan():
    os.system('clear')
    os.system('bash v1.sh')
    os.system('clear')
    os.system('login')

menu()
