import sys
import subprocess

if(len(sys.argy)<= 1);
    print("Ip address belum diberikan")
else:
    host_ip = sys.argv[1]
    status, result = subprocess.getstatusoutput("ping -c1" + host_ip)
    if(status == 0):
        print(f'host {host_ip} is UP')
    else:
        print(f'{host_ip} is DOWN')