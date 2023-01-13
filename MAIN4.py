
from subprocess import Popen,PIPE
import time

process = Popen(['powershell', 'putty.exe','f8059678@10.36.154.37:22', '-pw', 'Oss@202211'],stdout=PIPE,stderr=PIPE,shell=False, universal_newlines=True)
time.sleep(5)
# Send commands to the shell as if they were read from a shell script
#process.stdin.write("./moshell SP2112\n")
process.stdin.send("cd moshell\n") 
#process.stdin.send("./moshell SP2112\n")   
#process.stdin.write("command2\n")
process.stdin.close()
# read out the answers, if needed
ans = process.stdout.read()
process.wait()
print(ans)  