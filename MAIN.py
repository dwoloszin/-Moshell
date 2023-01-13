from subprocess import Popen,PIPE
#process = Popen("powershell putty.exe f8059678@10.36.154.37:22 -pw Oss@202211",stdout=PIPE,stderr=PIPE,shell=True, universal_newlines=True)

process = Popen(['powershell', 'putty.exe','f8059678@10.36.154.37:22', '-pw', 'Oss@202211'],stdout=PIPE,stderr=PIPE,shell=True, universal_newlines=True)


stdout, stderr = process.communicate(timeout=6)
print(stderr)
 



