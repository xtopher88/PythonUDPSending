import sys
import socket
import csv
import time


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def main(args):

    file_name = "test1.csv"
    num_loops = 1
    ip_address = "127.0.0.1"
    ip_port = 8080

    num_args = len(args)
    if num_args > 1:
        file_name = args[0]
    if num_args > 2:
        num_loops = args[1]
    if num_args > 3:
        ip_address = args[2]
    if num_args > 3:
        ip_port = args[3]

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    for i in range (num_loops):
        with open(file_name) as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True,delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                print row
                byte1 = 0
                byte2 = 0
                for key in ['v1', 'v2', 'v3', 'v4', 'v5']:
                    byte1 = (byte1 << 1) + (int(row[key]) & 0x1)
                print [byte1, byte2]
                sock.sendto(bytearray([byte1, byte2]), (ip_address, ip_port))
                time.sleep(float(row['time']))

    sock.close()




if __name__ == "__main__":
    main(sys.argv[1:])
