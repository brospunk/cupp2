import itertools
import string

nomi = []
anni = []
#suffissi = list(string.punctuation) + list(string.digits) + list(string.ascii_letters) + ['123']
suffissi = []
wordlist = set()

def inserisciNomi():
    global nomi
    print("[$] Inserisci stop per uscire")
    while True:
        a = str(input("[+] Inserisci nome: "))
        if a == 'stop':
            ribalta = input("[?] Vuoi aggiungere questi nomi invertiti? (si o no): ")
            if ribalta == 'si':
                l = [s[::-1] for s in (nomi)]
                print("[+] Aggiungendo parole INVERTIRE: ", l)
                nomi.extend(l)
            break
        else:
            nomi.append(a)

def inserisciAnni():
    global anni
    print("[$] Inserisci stop per uscire")
    while True:
        a = str(input("[+] Inserisci Anni: "))
        if a == 'stop':
            ribalta = input("[?] Vuoi aggiungere questi anni invertiti? (si o no): ")
            if ribalta == 'si':
                l = [s[::-1] for s in (anni)]
                print("[+] Aggiungendo parole INVERTIRE: ", l)
                anni.extend(l)
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
    print("[6] Caratteri più utilizzati")
    while True:
        try:
            choose = int(input("[?] Inserisci (-1 per dire di no): "))
            if choose == -1: break
            elif choose < 7 and choose >= 0:
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
    elif scegli_charset == 6: # Caratteri più utilizzati
        return list("-" + "_" + " " + string.ascii_letters + string.digits)
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
    global nomi, anni, suffissi, wordlist
    print("[...] Generando Wordlist")

    '''
    for r in range(2, len(nomi) + 1):  # da 2 nomi in su
        for combo in itertools.permutations(nomi, r):  # nomi distinti
            parola = ''.join(combo)
            print("Nomi: ", parola)
            wordlist.append(parola)
            '''
    
    # solo coppie di nomi distinti
    combo_nomi = list()
    for combo in itertools.permutations(nomi, 2):
        parola = ''.join(combo)
        combo_nomi.append(parola)
    
    nome_plus = []
    for nome in nomi:
        nome_plus.append(nome + nome)
    nomi = nomi + combo_nomi + nome_plus
    del combo_nomi # Puliamo la ram
    del nome_plus # Puliamo la ram
    print("Combo di nomi aggiunti: ", nomi)
    print("LUNGHEZZA totale Nomi: ", len(nomi))

    while nomi:
        nome = nomi.pop(0)
        print("LUNGHEZZA Nomi MANCANTI...  : ", len(nomi))
        print("LUNGHEZZA lista Wordlist... : ", len(wordlist))
        for anno in anni:
            for suff in suffissi:
                combinazioni = [
                    nome,
                    nome + anno,
                    nome + suff,
                    nome + anno + suff,
                    nome + suff + anno,
                    anno + anno,
                    anno + nome,
                    anno + suff,
                    anno + nome + suff,
                    anno + suff + nome,
                    suff + nome,
                    suff + anno,
                    suff + nome + anno,
                    suff + anno + nome
                ]
                while combinazioni:
                    parola = combinazioni.pop(0) # Liberiamo parte della memoria
                    if parola not in wordlist:
                        wordlist.add(parola)
                        

    print("[+] Lista dizionario creata!")
    #print("[...] Eseguendo Sort nel dizionario!")
    #wordlist = set(wordlist)
    print("LUNGHEZZA lista Wordlist... : ", len(wordlist))

def creaFileDizionario(nameFile):
    global wordlist
    '''
    with open(nameFile, 'w') as f:
        for parola in wordlist:
            f.write(parola + '\n')
    '''
    with open(nameFile, 'w') as f:
        cont, max = 0, len(wordlist)
        while wordlist:
            parola = wordlist.pop()  # rimuove e restituisce il primo elemento
            f.write(parola + '\n')
            #cont += 1
            #progress(cont, max)
            #print(f"\rSalvate: {cont}", end='', flush=True)
    print()

def progress(percent=0, max=100, width=45):
    left = width * percent // max
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent: .0f}%', sep='', end='', flush=True)


def main():
    global nomi, anni, suffissi, wordlist
    file_path_nome = input("[?] Inserisci nome del file per salvare il dizionario: ")

    inserisciNomi()
    if len(nomi) == 0: nomi.append('')
    print("*" * 30)

    inserisciAnni()
    if len(anni) == 0: anni.append('')
    print("*" * 30)
    
    inserisciSuffissi()
    if len(suffissi) == 0: suffissi.append('')
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
