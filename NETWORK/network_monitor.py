import speedtest
import datetime
import csv

s = speedtest.Speedtest()

with open('bandwidthdata.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'download', 'upload'])
    csv_writer.writeheader()
    while True:
        download = round((round(s.download()) / 1048576), 2)
        upload = round((round(s.upload()) / 1048576), 2)
        time = datetime.datetime.now().strftime("%H:%M:%S")
        csv_writer.writerow({
            'download': download,
            "upload": upload,
            "time": time
        })
        speedcsv.flush()
        #time.sleep(30)
