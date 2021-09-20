#! /usr/bin/env python3

import requests as req
import os
import sys
import argparse
from os.path import exists

##TO-DO##
###HELP Section###
# Ask for client name acronym#
# set file name in Robots function
# Run Nikto##
##Run URLCrazy###
##Run EyeWitness##
##RunWAFW00F##
##Gobuster or Dirbuster##

# def Robots():

Domain = input("Enter the client FQDN:\n")
ClientAck = input("Enter Client Acronym:\n")


def robots():
    response = req.get(f'https://www.{Domain}/robots.txt')
    try:
        os.path.exists("{ClientAck}_Robots.txt")
    except True:
        f = open(f"{ClientAck}_Robots.txt", "x")
        f.write(response.text)

    # print(response.text)


def url_crazy():
    os.system("urlcrazy -p -f CSV -o {ClientAck}_urlcrazy.csv {Domain}")

def wafw00f():
    os.system("wafw00f {Domain}")


robots()
url_crazy()
wafw00f()
