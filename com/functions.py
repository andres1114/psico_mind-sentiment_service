import os
import sys
import time

def verbose(**kwargs):

    if kwargs.get('outputMode') == 0:
        print("(" + time.strftime('%Y-%m-%d %H:%M:%S') + ") " + str(kwargs.get('outputMessage')))
    elif kwargs.get('outputMode') == 1:
        print("(" + time.strftime('%Y-%m-%d %H:%M:%S') + ") " + str(kwargs.get('outputMessage')))

        dir_path = os.path.dirname(os.path.abspath(__file__)) + "/logs/"
        file = open(dir_path + kwargs.get('logName') + '.log', 'a')
        file.write("(" + time.strftime('%Y-%m-%d %H:%M:%S') + ") " + str(kwargs.get('outputMessage')) + "\n")
        file.close()