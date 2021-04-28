import csv
import sys
import numpy as np
# sys.path.append("..")
# from estimator import Estimator
import matplotlib.pyplot as plt

# kDataPath = "C:/Users/24302/Desktop/Ceph混部数据/MAGI/data/history_ceph.csv"
# kModelPath = "/home/wcx/gitProject/MAGI/data_mcf_bzip_ceph2/model_ceph"
# kOutputPath = "/home/wcx/gitProject/MAGI/data_mcf_bzip_ceph2/ipc_contrast.csv"
# kLatPath = "/home/wcx/gitProject/MAGI/data_mcf_bzip_ceph2/lat.log"
kOutLatPath = "C:/Users/24302/Desktop/Ceph混部数据/MAGI/data/data_mcf_bzip_ceph2/lat.csv"
KOutIpcPath = "C:/Users/24302/Desktop/Ceph混部数据/MAGI/data/data_mcf_bzip_ceph2/ipc_contrast.csv"
'''
def parseIPC():
    datafile = open(kDataPath, "r")
    readRptr = csv.reader(datafile)
    oldIPC = []
    newIPC = []
    for dataline in readRptr:
        oldIPC.append(float(dataline[-1]) )
        tranX = dataline[:-1]
        e = Estimator(0.5, 'ceph')
        tranX = [float(i) for i in tranX]
        tipc = e.inference(tranX)
        newIPC.append(tipc)
    
    print("--------tranDone----------------")
    outfile = open(kOutputPath, "a", newline='')
    outWptr = csv.writer(outfile)
    tlen = min(len(oldIPC), len(newIPC))
    for i in range(tlen):
        # print([oldIPC[i],newIPC[i]])
        outWptr.writerow([oldIPC[i],newIPC[i]])
        # input()


    datafile.close()
    outfile.close()'''

'''def parseLat():
    # readfile = open(kLatPath, "r")
    objline = ''
    x = []
    with open(KOutIpcPath, "r") as r:
        line = r.readline()
        while line:
            if line.find("Average Latency(s):") != -1:
                objline = line
                x.append(float(objline.split()[2] ))
            line = r.readline()
    
    outfile = open(kOutLatPath, "a", newline='')
    outWptr = csv.writer(outfile)
    tlen = len(x)
    for i in range(tlen):
        # print([oldIPC[i],newIPC[i]])
        outWptr.writerow([x[i]])
        # input()
   ''' 

# 解析出来实时的latency
'''def parseLatTime():
    tfilepath = 'C:/Users/24302/Desktop/Ceph混部数据/MAGI/tools/干扰log.txt'
    lat = []
    with open(tfilepath, "r") as r:
        line = r.readline()
        while line:
            flat = line.find("lat")
            line = line.split()
            if len(line) < 8 or flat != -1:
                line = r.readline()
                continue
            lat.append(float(line[-1]) )
            line = r.readline()
    print(len(lat))
    print(lat[-1])
    tfilepath2 = 'C:/Users/24302/Desktop/Ceph混部数据/MAGI/tools/干扰lat.csv'
    toutfile = open(tfilepath2, "w", newline='')
    toutWptr = csv.writer(toutfile)
    for i in lat:
        toutWptr.writerow([i])
    toutfile.close()
'''

# 640:3920   6.125  lat裁掉10组‬  
# 241:4735   19.65  ipc裁掉10组
def plot():
    readfile = open(KOutIpcPath, "r")
    readRptr = csv.reader(readfile)
    oldIPC = []
    newIPC = []
    for dataline in readRptr:
        oldIPC.append(float(dataline[0]))
        newIPC.append((round(float(dataline[1]),2)))
    oldIPC = oldIPC[0:100]
    newIPC = newIPC[0:100]
    datalen = len(oldIPC)
    X = np.linspace(0, datalen, datalen)
    # X = np.arange(datalen)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(X, oldIPC, '--', label='old_ipc')
    plt.plot(X, newIPC, '--', label='new_ipc')
    plt.ylim(0.0)
    # plt.ylim(0.0)  # 这里筛去了10组
    plt.title("IPC Contrast")
    plt.xlabel("time")
    plt.ylabel("ipc")
    plt.legend()

    readfile = open(kOutLatPath, "r")
    readRptr = csv.reader(readfile)
    lat = []
    for dataline in readRptr:
        lat.append(float(dataline[0]))
    lat = lat[0:100]
    print(lat)
    tlen = len(lat)
    # print(tlen)
    X = np.arange(tlen)
    # print(X)
    plt.subplot(212)
    plt.plot(X, lat, "--", label="rand")
    plt.title("Rand Lat")
    plt.xlabel("time")
    plt.ylabel("lat")
    plt.ylim(0.0)
    plt.legend()
    # plt.plot()
    # plt.subplots_a    djust(hspace=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # parseIPC()
    # parseLat()
    # parseLatTime()
    plot()
        
