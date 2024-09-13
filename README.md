# RelayNetCommander

**RelayNetCommander** es una herramienta automatizada diseñada para realizar ataques de **NTLM Relay** aprovechando las conexiones de víctimas comprometidas. Utiliza **Ntlmralyx** y el protocolo **SOCKS** para detectar y explotar dispositivos vulnerables en la red.

## Características principales

- **Automatización del ataque NTLM Relay**: RelayNetCommander detecta automáticamente cuando uno o más dispositivos se ven comprometidos a través de un ataque NTLM Relay, gestionado mediante **Ntlmralyx**.
  
- **Carga de Netcat en el dispositivo víctima**: Una vez comprometido, la herramienta crea un directorio en el dispositivo de la víctima y sube un ejecutable de **Netcat** para establecer una puerta trasera persistente.

- **Creación de tareas programadas**: RelayNetCommander configura una tarea programada en el dispositivo víctima, la cual ejecuta un comando de Netcat cada minuto para mantener acceso constante a la máquina comprometida.

- **Puerta trasera persistente**: La combinación de tareas programadas y Netcat permite a un atacante mantener una conexión activa y persistente con los dispositivos comprometidos.

## Requisitos

- **Ntlmralyx**: Debe estar configurado y funcionando para realizar los ataques NTLM Relay.
- **SOCKS**: Es necesario para la interacción con los dispositivos víctimas.
- **Netcat**: Utilizado para establecer la conexión de puerta trasera en los dispositivos comprometidos.

## Uso

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/RelayNetCommander.git
    cd RelayNetCommander
    ```

2. Configura los parámetros de red y las rutas de acceso a **Ntlmralyx** y **Netcat**.

3. Ejecuta la herramienta:

    ```bash
    python relaynetcommander.py
    ```

RelayNetCommander escaneará automáticamente la red, detectará las víctimas comprometidas a través de NTLM Relay y desplegará la puerta trasera de manera automática.

---

### Aviso de responsabilidad

Esta herramienta está diseñada exclusivamente con fines educativos y de evaluación de seguridad. El uso de RelayNetCommander sin autorización puede ser ilegal y está prohibido. Los desarrolladores no son responsables del uso indebido de esta herramienta.

