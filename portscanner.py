#!/usr/bin/python3

import socket

# Prompt user to enter IP
userIP = input("Enter an IP address to scan: ")

# Lets the user know that the scan is in progress
print("-" * 60)
print("Scanning host", userIP)
print("-" * 60)

# Change filepath in accordance to personal system 
filePath = "/home/hackerman/PycharmProjects/"

# File path and filename can be altered as user sees fit
with open(filePath + "openPorts.txt", "a") as openPorts:
    openPorts.write("List of open ports on IP address " + userIP + "\n")

    totalPorts = 0

    try:
        # Reads all possible ports to find which are open for the given IP address
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connect_ex returns 0 upon success, or an appropriate ERRNO for anything else
            result = sock.connect_ex((userIP, port))
            if result == 0:
                # Write open ports to file
                openPorts.write("Port {}: 	 Open".format(port) + "\n")
                # Print open ports to terminal
                print("Port {}: 	 Open".format(port))
                totalPorts += 1
            sock.close()

    except KeyboardInterrupt:
        print("Ctrl+C input detected. Terminating program execution.")
        exit()

    except socket.gaierror:
        openPorts.write("ERROR: Hostname could not be resolved. Exiting.")
        print("ERROR: Hostname could not be resolved. Exiting.")
        exit()

    except socket.error:
        openPorts.write("ERROR: Unable to connect to address.")
        print("ERROR: Unable to connect to address.")
        exit()

    # Write total number of open ports for given IP to file
    openPorts.write("Number of open ports on " + userIP + ": " + str(totalPorts))
    # Printing the total number of open ports found for the user entered IP
    print("\nNumber of open ports on ", userIP, ": ", totalPorts, sep="")

    openPorts.write("\n\n")
