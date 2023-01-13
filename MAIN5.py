import paramiko
import sys
import threading
import os
import time
#ssh.connect('10.36.154.37',port=22,username='f8059678',password='Oss@202211')
ip        = '10.36.154.37'
user      = 'f8059678'
passwd    = 'Oss@202211'
cmd = 'hostname'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
   ssh.connect(ip,username=user,password=passwd, timeout=5,allow_agent=False)
   print ("Connected to %s" % ip)
   time.sleep(5)
   output = ''
   connection = ssh.invoke_shell()
   transport = ssh.get_transport()
   transport.set_keepalive(30)
   if connection.send_ready():
      #print ("Channel is ready")
      connection.send(cmd)
   else:
      raise("Channel not ready!")
   buff=''
   while not buff.endswith('# '): # Checking for returned prompt
         resp = str(connection.recv(9999).decode('utf8'))
         buff += resp
   print (resp)
   #stdin, stdout, stderr = ssh.exec_command(cmd)
   #result = stdout.read().decode('ascii').strip("\n")
   #paramiko.util.log_to_file("filename.log")
   #print(result)
   ssh.close()
   #print result
except (paramiko.AuthenticationException,paramiko.SSHException) as message:
        print ("ERROR: SSH connection to "+ip+" failed: " +str(message))
        sys.exit(1)
 
#except paramiko.AuthenticationException:
#       print "[-] Authentication Exception! ..."
except paramiko.SSHException:
       print ("[-] SSH Exception! ...")