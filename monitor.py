import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print("CPU:", cpu, "%")
    print("Memory:", memory, "%")
    print("------------------")

    time.sleep(2)
