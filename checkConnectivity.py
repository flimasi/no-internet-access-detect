import os
import time

startlog = time.time()

MINUTES = 1

def log():
    filename = "log/log.txt"
    f = open(filename, "w+")
    f.write(time.time().__str__())
    f.close()

def shutdown():
    os.system("shutdown now")

while True:
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        if time.time() - (60 * MINUTES) > startlog:
            print('its been ' + str(MINUTES) + ' minutes')
            log()
            shutdown()
            break
        pingstatus = "Network Error"
