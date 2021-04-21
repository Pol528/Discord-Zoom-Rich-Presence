import subprocess
from pypresence import *
import time
from colored import fg, bg, attr

rpc = Presence("832296309935308891")
rpc.connect()
print("%sZoom Rich presence has started! Made by Pol#6969 - https://github.com/Pol528/Discord-Zoom-Rich-Presence%s" % (fg(45), attr(0)))

running = False

def run_rpc():
    print("%sZoom has started, connecting Rich Presence!%s" % (fg(46), attr(0)))
    rpc.update(state="In a Zoom Meeting", large_image="logo", start=time.time())
    
def dc_rpc():
    print("%sZoom has been closed, disconnecting Rich Presence...%s" % (fg(1), attr(0)))
    rpc.clear()

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


while True:
    if process_exists("Zoom.exe") == True:
        if running == False:
            run_rpc()
            running = True
    
    else: 
        if running == True:
            dc_rpc()
            running = False
    time.sleep(1)