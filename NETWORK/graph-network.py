import matplotlib.pyplot as plt
import csv
import pandas as pandas
import numpy as np

data = pandas.read_csv("bandwidthdata.csv")
times = data["time"]
download = data["download"]
upload = data["upload"]

plt.style.use('ggplot')
plt.figure(figsize=(20, 10))
plt.plot(data.time, data.download, label='download', color='r')
plt.plot(data.time, data.upload, label='upload', color='b')
plt.gcf().autofmt_xdate()
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title("internet speed")
plt.legend()

# SAVE OR SHOW THE GRAPH

#plt.savefig('networkgraph.jpg', bbox_inches='tight')
plt.show()
