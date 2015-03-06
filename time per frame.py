import os.path
import datetime
import glob
from tkinter.filedialog import askopenfilename

frameTimeArray = []
total = datetime.timedelta()
prev = None

fullpath = askopenfilename()
path = os.path.dirname(fullpath)
filename = (fullpath.split(path,))
filename = filename[1].rsplit('_',1)
glob_path = path + os.sep + filename[0] + '*'

def nice_time(td):
    timeDifference = str(td).split(':',3)
    
    if timeDifference[0] == '0':
        hours = ""
    elif timeDifference[0] == '1':
        hours = ("{time} hour, ".format(time=timeDifference[0]))
    else:
        hours = ("{time} hours, ".format(time=timeDifference[0]))

    if timeDifference[1] == '0':
        mins = ""
    elif timeDifference[1] == '1':
        mins = ("{time} minute".format(time=timeDifference[1]))
    else:
        mins = ("{time} minutes".format(time=timeDifference[1]))

    secondSplit = timeDifference[2].split('.')
    timeDifference[2] = secondSplit[0]
    if timeDifference[2] == '00':
        secs = ""
    elif timeDifference[2] == '1':
        secs = (" and {time} second".format(time=timeDifference[2]))
    else:
        secs = (" and {time} seconds".format(time=timeDifference[2]))

    return("{hours}{mins}{secs}").format(hours=hours, mins=mins, secs=secs)

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

for file in glob.iglob(glob_path):
    if prev == None:
        prev = modification_date(file)        
        continue
    timeDifference = modification_date(file)-prev
    frameTimeArray.append(timeDifference)
    total = total + timeDifference
    uniqueFile =  (file.split(path,))
    uniqueFile = uniqueFile[1].rsplit(os.sep,)
    print("frame {frame} took {nicetime} to render.".format(frame=uniqueFile[1], nicetime=nice_time(timeDifference)))
    prev = modification_date(file)

average = total/len(frameTimeArray)
print("The average frame render time was {average}.".format(average=nice_time(average)))
print("The total render time was {total}.")
print(total)
