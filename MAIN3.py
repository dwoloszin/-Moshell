import paramiko
from rich import print, pretty, inspect
import time
import pandas as pd

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('10.36.154.37',port=22,username='f8059678',password='Oss@202211')
#ssh.connect('C:\Users\f8059678\Documents\WinFIOL\ChnFiles\OSS-3G 4G.chn')

channel = ssh.invoke_shell()

channel_data = str()
kpi = str()

text_file = open("Output.txt", "w")



node = ['SP2112','SP2107']

once = True
while True:
  for i in node:
    if channel.recv_ready():
      dataInfo = str(channel.recv(9999).decode('utf8'))
      channel_data += dataInfo
    else:
      continue
    if channel_data.startswith('Last login:'):
      if once:
        channel.send('cd moshell\n')
        once = True  
      channel.send('./moshell -v username=rbs,password=aeiSP#11 {}\n'.format(i))
      channel.send('lt all\n')
      channel.send('pmxet Sector=* AvgRssi$\n')
      channel.send('quit\n')
      time.sleep(5)
  print(channel_data)
  text_file.write(channel_data)









