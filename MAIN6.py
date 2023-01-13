import paramiko
from rich import print, pretty, inspect
import time
import pandas as pd
import config

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect(config.connectionIP,port=22,username=config.userName,password=config.passWd)


channel = ssh.invoke_shell()

channel_data = str()
kpi = str()

text_file = open("Output.txt", "w")



node = 'SI6036'

once = True
while True:
  if channel.recv_ready():
    dataInfo = str(channel.recv(9999).decode('utf8'))
    channel_data += dataInfo
    print(dataInfo)
    if 'Sector=' in dataInfo:
      kpi += dataInfo
  else:
    continue
  if channel_data.startswith('Last login:') and once:
    channel.send('cd moshell\n')
    channel.send('./moshell -v username=rbs,password=aeiSP#11 {}\n'.format(node))
    channel.send('lt all\n')
    channel.send('pmxet Sector=* AvgRssi$\n')
    channel.send('quit\n')
    time.sleep(5)
    once = False
  #print(channel_data)
  text_file.write(kpi)


#Stdout

'''
for line in stdout.readlines():
    print(line.replace('\n', ''))
'''


