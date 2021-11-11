import csv
import generate as g
import sendEmail as s
import time
import smtplib
import ssl


# parses files first
with open("contacts_networking.csv") as file:
    reader = csv.reader(file)
    next(reader)  # skip first row

    your_address = "beardkoby@gmail.com"   # address to send emails from
    password = input("Type your password and press enter:")
    resume = "KBR.pdf"
    for name, company, position, internship in reader:
        msg = g.gen_message(name, company, position, internship)
        possible_addresses = g.gen_addresses(name, company)
        subject = g.gen_subject(internship, company)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(your_address, password)
            for address in possible_addresses:
                s.send_email(address, subject, msg, resume, server)
                time.sleep(5)
        print("Finished with " + name)
    print("Finished with all contacts!")




