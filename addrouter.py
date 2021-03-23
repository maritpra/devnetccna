#!/usr/bin/python3

import csv

addmore = "no"
addmore = input("Add more data?:\n 'yes' or 'no' ")
if addmore == 'yes':
    hostname = input("\nWhat is device name? ")
    ip = input("What is device ip address? ")
    location = input("What is the location? ")
    router = [hostname, location, ip]
    with open("routerlist.csv", "a") as data:
        csv_writer = csv.writer(data)
        csv_writer.writerow(router)
        