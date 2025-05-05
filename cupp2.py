import itertools
import string

nomi = []
anni = []
#suffissi = list(string.punctuation) + list(string.digits) + list(string.ascii_letters) + ['123']
suffissi = []
wordlist = []

def inserisciNomi():
    global nomi
    print("[$] Inserisci stop per uscire")
    while True:
        a = str(input("[+] Inserisci nome: "))
        if a == 'stop':
            break
        else:
            nomi.append(a)

def inserisciAnni():
    global anni
    print("[$] Inserisci stop per uscire")
    while True:
        a = str(input("[+] Inserisci Anni: "))
        if a == 'stop':
            break
        else:
            anni.append(a)

def inserisciSuffissi():
    global suffissi
    print("[0] Caratteri Speciali, Lettere, Numeri")
    print("[1] Numeri")
    print("[2] Lettere")
    print("[3] Caratteri Speciali")
    print("[4] Lettere minuscole")
    print("[5] Lettere MAIUSCOLE")
    while True:
        try:
            choose = int(input("[?] Inserisci (-1 per dire di no): "))
            if choose == -1: break
            elif choose < 6 and choose >= 0:
                suffissi = charset(scegli_charset=choose)
                break
        except: continue
    print("*" * 30)

    print("[$] Inserisci stop per uscire")
    print("[$] Suffissi esistenti: ", suffissi)
    while True:
        suff = str(input("[+] Inserisci Suffissi: "))
        if suff == 'stop':
            break
        else:
            suffissi.append(suff)

def charset(scegli_charset=0):
    if scegli_charset == 0: # Tutto
        return list(string.punctuation) + list(string.digits) + list(string.ascii_letters) + ['123']
    elif scegli_charset == 1: # Solo numeri
        return list(string.digits)
    elif scegli_charset == 2: # Solo lettere
        return list(string.ascii_letters)
    elif scegli_charset == 3: # Solo caratteri speciali
        return list(string.punctuation)
    elif scegli_charset == 4: # Solo lettere minuscole
        return list(string.ascii_lowercase)
    elif scegli_charset == 5: # Solo lettere MAIUSCOLE
        return list(string.ascii_uppercase)
    return None

def generaSuffissi(lunghezza_min=1, lunghezza_max=None):
    global suffissi
    charset_list = suffissi
    if lunghezza_max is None:
        lunghezza_max = len(charset_list)
    for i in range(lunghezza_min, lunghezza_max + 1):
        print("[...] Generazione suffisso ", i)
        for combo in itertools.product(charset_list, repeat=i):
            suffissi.append(''.join(combo))
            #print("[+] Combinazione suffisso generata: ", suffissi[-1])
    print("[$] Fine generazione suffissi!")
    return suffissi


def generaWordlist():
    global nome, anni, suffissi, wordlist
    print("[...] Generando Wordlist")
    for nome in nomi:
        for anno in anni:
            for suff in suffissi:
                # Inizia con nomi
                wordlist.append(nome + nome)
                wordlist.append(nome + anno)
                wordlist.append(nome + suff)
                wordlist.append(nome + anno + suff)
                wordlist.append(nome + suff + anno)
                # Inizia con anni
                wordlist.append(anno + anno)
                wordlist.append(anno + nome)
                wordlist.append(anno + suff)
                wordlist.append(anno + nome + suff)
                wordlist.append(anno + suff + nome)
                # Inizia con suff
                wordlist.append(suff + nome)
                wordlist.append(suff + anno)
                wordlist.append(suff + nome + anno)
                wordlist.append(suff + anno + nome)
    print("[+] Lista dizionario creata!")
    print("[...] Eseguendo Sort nel dizionario!")
    wordlist = set(wordlist)

def creaFileDizionario(nameFile):
    global wordlist
    with open(nameFile, 'w') as f:
        for parola in wordlist:
            f.write(parola + '\n')

def main():
    global nomi, anni, suffissi, wordlist
    file_path_nome = input("[?] Inserisci nome del file per salvare il dizionario: ")

    inserisciNomi()
    print("*" * 30)
    inserisciAnni()
    print("*" * 30)
    inserisciSuffissi()
    print("*" * 30)
    generaSuffissi(lunghezza_max=2)
    print("*" * 30)

    generaWordlist()
    print("[...] Creando File: ", file_path_nome)
    creaFileDizionario(file_path_nome)
    print("[+] File creato: ", file_path_nome)


if "__main__" == main():
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Programma interrotto manualmente Ctrl+C")
