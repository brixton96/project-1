# def mainMenu():



print('''Selamat datang di program Python 
      1. Integral
      2. Turunan
      3. Aritmatika
      4. Logaritma
      5. Translate
      6. Exit''')

def mainMenu():
    pilihan = int(input("Masukkan pilihan anda: "))
    if pilihan == '1':
        integral()
    elif pilihan == 2:
        turunan()
    elif pilihan == 3:
        aritmatika()
    elif pilihan == 4:
        logaritma()
    elif pilihan == 5:
        translate()
    elif pilihan == 6:
        exit()
    else:
        print("Pilihan tidak valid")
        mainMenu()

mainMenu()



def integral():
    pass


def turunan():
    pass

def aritmatika():
    pass


def logaritma():
    pass

def translate():
    pass

def exit():
    pilihan = int(input("Masukkan kembali pilihan anda: "))