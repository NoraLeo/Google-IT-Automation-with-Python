#!/usr/bin/env python3


import shutil
import psutil
import socket
import emails

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free < 20

def check_cpu_usage():
    return psutil.cpu_percent(1) < 80


def check_memory_usage():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024
    return mem.available < THRESHOLD

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0
    
username = ""
disk = '/'
hostname= '127.0.0.1'
    
if check_cpu_usage():
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(username),
        "subject": "Error - CPU usage is over 80%",
        "body": "Please check your system and resolve the issue as soon as possible."
    }
    message = emails.generate_email_without_attachment(**content)
    emails.send_email(message)

elif check_disk_usage(disk):
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(username),
        "subject": "Error - Available disk space is less than 20%",
        "body": "Please check your system and resolve the issue as soon as possible."
    }
    message = emails.generate_email_without_attachment(**content)
    emails.send_email(message)

elif check_memory_usage():
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(username),
        "subject": "Error - Available disk space is less than 20%",
        "body": "Please check your system and resolve the issue as soon as possible."
    }
    message = emails.generate_email_without_attachment(**content)
    emails.send_email(message)

elif hostname_resolves(hostname) == 0:
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(username),
        "subject": "Error - localhost cannot be resolved to 127.0.0.1",
        "body": "Please check your system and resolve the issue as soon as possible."
    }
    message = emails.generate_email_without_attachment(**content)
    emails.send_email(message)

