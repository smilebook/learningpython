import sys
import base64
orgfile = open('failorg.txt', 'r')
tarfile = open('targetdata.txt','w')
orgdata = orgfile.read()
orgfile.close()
dataItemList = []
checklist = ['Version=', 'From=', 'Time=', 'AverageSpeed=', 'DoneSize=', 'DoneTime=', 'DownHeader=', 'DownloadProtocol=', 'DownloadURL=', 'IEVersion=', 'LastStartTime=', 'StartTime=', 'StopCount=', 'Log=', 'PcCode=', 'PcCode2=', 'OSVersion=', 'cookies=', 'ip=', 'MainFlow=', 'P2SFirst=Connect=', 'P2SFlow=']   
for orgDataItem in orgdata.split('\tArray\n'):
	dataItem = []
	for i in range(len(checklist)):
		beg = orgDataItem.find(checklist[i])
		end = orgDataItem.find(' ',beg)
		if beg != -1 and end != -1:
			dataItem.append(orgDataItem[beg+len(checklist[i]):end])
#	print dataItem
	dataItemList.append(dataItem)
	tarfile.writelines(dataItem)
tarfile.close()

