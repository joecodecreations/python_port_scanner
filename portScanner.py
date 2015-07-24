import socket
import time
print "starting port scan"

#initial reached value set to zero for no ports found yet
reached = "0"

#set the target host we will be port scanning
target = "192.168.0.47"

#start with port number
attempt = 0

#set the top port range to check
upperRange = 10000

#set the timeout for each port scanned
# Local network can be set as low as 0.0008
# Remote network should be set around 0.1000 but varies Play with this to increase speed and effectiveness
sessionTimeout = 0.0008

while attempt < upperRange:
        start = time.time()
        attempt=attempt+1
        print "Scanning Port: %d" %  attempt
        while 1==1:
                end = time.time()
                current = end-start
                #print "time : %d " % current
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(sessionTimeout)
                try:
                        s.connect((target, attempt))
                        #attempt=attempt+1
                        print "Port %d reachable" % attempt
                        if reached == "0":
                                reached = str(attempt)
                        else:

                                reached = reached+","+str(attempt)
                        break
                except socket.error as e:
                        #print "Error on connect: %s" % e
                        break


                s.close()
if reached != 0 :
        print "Ports Open: %s" % reached
else:
        print "No Ports Open"


