import datetime
import sys
import traceback

def log():
    
    f= open("error_log.txt","a")
    f.write("*"*80)
    f.write("\n"+str(datetime.datetime.now())+"\n")
    f.write(traceback.format_exc())
    f.close()   
    