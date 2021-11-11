"""
Code to generate messages and possible addresses

"""


def gen_message(name, company, position, internship):
    with open("message_template") as txt:
        msg = txt.read()
    first_name = (name.split(" "))[0]
    msg = msg.format(fname=first_name, fposition=position, fcompany=company, finternship=internship)
    return msg


def gen_addresses(name, company):
    possible_addresses = []
    first_name, last_name = (name.split(" "))  #firstname, lastname
    possible_addresses.append(
        first_name + "." + last_name + "@" + company + ".com")  #firstname.lastname@company.com
    possible_addresses.append(
        first_name[0] + last_name + "@" + company + ".com")  #first letter of firstnamelastname@company.com

    return possible_addresses


def gen_subject(internship, company):
    return internship + " at " + company
