import subprocess
import multiprocessing
import time

T1 = time.perf_counter()
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "8.8.8.8", "8.8.4.4"]
def check_host ():
    for x in hosts:
        status, result = subprocess.getstatusoutput("ping -c1" + x)
        if (status == 0):
            print(f'Host {x} is UP')
        else:
            print(f'Host {x} is DOWN')
Processes = []
for x in range(len(hosts)):
    P = multiprocessing.Process(target=check_host)
    P.start()
    Processes.append(P)
for process in Processes:
    process.join()
T2 = time.perf_counter()
print(f"selesai dalam : {round(T2-T1,2)} detik")