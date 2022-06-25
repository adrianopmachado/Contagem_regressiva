import time

def contador(t):
    while t:
        minutos, segundos = divmod (t, 60)
        cronometro = '{:02d}:{:02d}'.format(minutos, segundos)
        print (cronometro, end="\r")
        time.sleep(1)
        t -= 1

    print('Tempo esgotado!')

t = input("Infome o tempo em segundos: ")

contador(int(t))