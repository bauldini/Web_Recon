#!/usr/bin/env python3

import requests as req
import os
import argparse
from os.path import exists
from concurrent.futures import ThreadPoolExecutor

# Ask for client name acronym#
Domain = input("Enter the client FQDN:\n")
ClientAck = input("Enter Client Acronym:\n")


def robots():
    response = req.get(f'https://www.{Domain}/robots.txt')
    try:
        if not exists(f"{ClientAck}_Robots.txt"):
            with open(f"{ClientAck}_Robots.txt", "x") as f:
                f.write(response.text)
    except Exception as e:
        print(f"Error in robots function: {e}")


def url_crazy():
    os.system(f"urlcrazy -p -f CSV -o {ClientAck}_urlcrazy.csv {Domain}")


def wafw00f():
    os.system(f"wafw00f {Domain}")




def main():
    with ThreadPoolExecutor() as executor:
        future_robots = executor.submit(robots)
        future_url_crazy = executor.submit(url_crazy)
        future_wafw00f = executor.submit(wafw00f)

        # Wait for all threads to complete
        future_robots.result()
        future_url_crazy.result()
        future_wafw00f.result()


if __name__ == "__main__":
    main()
