from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()


client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('10.36.154.37',port=22,username='f8059678',password='Oss@202211')

'''
stdin, stdout, stderr = client.exec_command('cd moshell')
print(type(stdin))
print(type(stdout))
print(type(stderr))
stdout1 = stdout.read().decode("utf8")
stderr1 = stderr.read().decode("utf8")
print(stdout1,stderr1)
'''
channel = client.invoke_shell()


channel_data = str()
host = str()
scrfile = str()

channel.send('cd moshell\n')
channel.send('./moshell SP3607;\n')
channel.send('lt all\n')  
print(channel.recv(9999))



'''
while true:
  if channel.recv_ready():
    channel_data += channel.recv_ready(9999)
  else:
    continue
  if  
'''









client.close()