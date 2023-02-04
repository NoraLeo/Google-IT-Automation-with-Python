#!/usr/bin/env python3

import os
import datetime
import reports
import emails

#read each .txt file

def getDesc(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    name_field = "Name: {}",format(lines[0])
    weight_field = "Weight: {}".format(lines[1])
    return "{}</br>{}</br></br>".format(name_field, weight_field)


def main():
    txt_dir = "/supplier-data/descriptions/"
    file_names = [txt_dir + f for f in os.listdir(txt_dir)]

    #report file
    report_file = "/tmp/processed.pdf"

    #report body
    report_body = ""
    for file in file_names:
        report_body += getDesc(file)

    #report title
    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        today.strftime("%B"), today.day, today.year)
    
    #generate report
    reports.generate_report(report_file, report_title, report_body)

    # generate & send email report:
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


if __name__ == "__main__":
    main()

    


