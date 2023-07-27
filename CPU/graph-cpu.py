import matplotlib.pyplot as plt
import csv
import pandas as pandas
import numpy as np

data = pandas.read_csv("cpu.csv")
times = data["time"]
cpu1 = data["CPU1"]
cpu2 = data["CPU2"]
cpu3 = data["CPU3"]
cpu4 = data["CPU4"]
cpu5 = data["CPU5"]
cpu6 = data["CPU6"]
cpu7 = data["CPU7"]
cpu8 = data["CPU8"]

plt.style.use('ggplot')
plt.figure(figsize=(20, 10))
plt.plot(data.time, cpu1, label='cpu1')
plt.plot(data.time, cpu2, label='cpu2')
plt.plot(data.time, cpu3, label='cpu3')
plt.plot(data.time, cpu4, label='cpu4')
plt.plot(data.time, cpu5, label='cpu5')
plt.plot(data.time, cpu6, label='cpu6')
plt.plot(data.time, cpu7, label='cpu7')
plt.plot(data.time, cpu8, label='cpu8')
plt.gcf().autofmt_xdate()
plt.xlabel('time')
plt.ylabel('Usage')
plt.title("CPU Usage")
plt.legend()

# SAVE OR SHOW THE GRAPH

plt.savefig('cpu_usage.jpg', bbox_inches='tight')
#plt.show()
