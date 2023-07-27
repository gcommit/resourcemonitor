## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Demo](#demo)
* [Example](#example)


## General info
This little python script will measure your bandwidth and/or your CPU usage. 
You can visualize it with gnuplot or matplotlib.

## Technologies
Project is created with:
* Python
* Gnuplot (http://www.gnuplot.info)
* Matplotlib (https://matplotlib.org)
	
## Setup
###### Network Gnuplot 
```
$ mkdir -p $HOME/networkmonitor
$ cd $HOME/networkmonitor
$ git clone
$ pip3 install -r requirements.txt
$ python3 NETWORK/network_monitor.py
$ gnuplot NETWORK/liveplot.gnu
```
###### Network Matplotlib
```
$ mkdir -p $HOME/networkmonitor
$ cd $HOME/networkmonitor
$ git clone
$ pip3 install -r requirements.txt
$ python3 NETWORK/network_monitor.py
$ python3 NETWORK/graph-network.py
```
###### CPU Gnuplot 
```
$ mkdir -p $HOME/networkmonitor
$ cd $HOME/networkmonitor
$ git clone
$ pip3 install -r requirements.txt
$ python3 CPU/cpu_monitor.py
$ gnuplot liveplot.gnu
```
###### CPU Matplotlib
```
$ mkdir -p $HOME/networkmonitor
$ cd $HOME/networkmonitor
$ git clone
$ pip3 install -r requirements.txt
$ python3 CPU/cpu_monitor.py
$ python3 CPU/graph-cpu.py
```
## Demo
Just clone the repo and run the gnuplot. A prefilled CSV is already there
```
$ mkdir -p $HOME/networkmonitor
$ cd $HOME/networkmonitor
$ git clone
$ gnuplot CPU/liveplot.gnu / python3 CPU/graph-cpu.py
$ gnuplot NETWORK/liveplot.gnu / python3 NETWORK/graph-network.py
```

## Example
#### Network (live Gnuplot)
![networkgraph](https://github.com/gcommit/localmonitor/assets/18714033/fce8323b-2cdd-490a-adad-fff3fa504ee7)

#### CPU Usage (live Gnuplot)
![cpu_usage](https://github.com/gcommit/localmonitor/assets/18714033/bb36e1da-8526-4ef0-9cb3-701571df39f4)

#### Network
![networkgraph](https://user-images.githubusercontent.com/18714033/152780777-458d5941-ce2b-4697-be14-fd59a4137370.jpg)

#### CPU Usage
![cpu_usage](https://user-images.githubusercontent.com/18714033/152798312-fbea57c4-9e36-4da3-bb8f-0080dd7fe4d3.jpg)


