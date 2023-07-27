import datetime
import csv
import psutil



#c = psutil.cpu_percent(interval=1, percpu=True)
with open('cpu.csv', mode='w') as cpustats:
    csv_writer = csv.DictWriter(cpustats, fieldnames=['time', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8'])
    csv_writer.writeheader()
    while True:
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        time = datetime.datetime.now().strftime("%H:%M:%S")
        csv_writer.writerow({
            "CPU1": cpu[0],
            "CPU2": cpu[1],
            "CPU3": cpu[2],
            "CPU4": cpu[3],
            "CPU5": cpu[4],
            "CPU6": cpu[5],
            "CPU7": cpu[6],
            "CPU8": cpu[7],
            "time": time
        })
        cpustats.flush()
