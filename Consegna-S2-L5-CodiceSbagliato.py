import datetime 

# Aggiunto testo di presentazione e istruzioni all'utente
print("\nCIAO! Sono un Assitente Virtuale!")
print("\nRi-scrivi una delle domande di seguito e sarò felice di rispondere OPPURE digita 'esci' per uscire.\n")

lista_domande=['Qual è la data di oggi?',
               'Che ore sono?',
               'Come ti chiami?'] # Aggiunto lista per comodità di codice per poter presentare le domande all'utente.

for indice, domanda in enumerate(lista_domande, start=1): # Aggiunto Ciclo FOR per stampare le domande nella lista in elenco
    print(f"{indice} - {domanda}\n")


def assistente_virtuale(comando):    
    if comando == lista_domande[0]:        
        oggi = datetime.date.today()  #Metodo corretto per chiamare metodo .today() della classe date del modulo datetime.
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    
    elif comando == lista_domande[1]:        
        ora_attuale = datetime.datetime.now().time() # Metodo corretto per chiamare il metodo .no() della classe .datetime del modulo .datetime + utilizo di .time() per indicare SOLO l'ora.          
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M") #Correzione segno strano tra %H e %M
    
    elif comando == lista_domande[2]:        
        risposta = "Mi chiamo Assistente Virtuale"
    
    else:        
        risposta = "Non ho capito la tua domanda."      
    
    return risposta 

while True:  # Mancavano i due punti
    comando_utente = input("\n\n[Domanda]: ") # Modificato in "Domanda" per preferenza stilistica.
    
    if comando_utente.lower() == "esci":        
        print("\nArrivederci!\n")        
        break
    else: # Mancava questo else + il print  per restituire il valore della funzione creata prima.
        print(assistente_virtuale(comando_utente)) 


# A parte gli errori di sintassi che ho indicato nei commenti mancavano alcune parti di codice per far si che il programma funzionasse correttamente (vedi else alla fine)
# Inoltre il programma era logicamente sbagliato in quanto non istruiva l'utente sulle sue capacità e su cosa/come gli si poteva chiedere.