import csv
from dvd import DVListType
from linked_list import Linked_list
from customer import Customer
from bst import BSTnode


def load_data():
    dvd_data_file = open("dvd.csv","r")
    dvd_data_file.readline()
    for line in dvd_data_file:
        dvd_data = line.split(",")
        title = dvd_data[0]
        actors = dvd_data[1]
        producers = dvd_data[2]
        director = dvd_data[3]
        production_company = dvd_data[4]
        number_of_copies = int(dvd_data[5])
        dvd_object = DVListType(title,actors,producers, director, production_company, number_of_copies)
        dvd_list.add(dvd_object)

def add_dvd():
    name = input("Enter Movie name: ")
    actors =input("Enter the actors in / seperated: ")
    producers = input("Enter the producers(seperate by /): ")
    director = input("Enter the director: ")
    production_company = input("Enter the production company: ")
    number_of_copies = input("Enter the number of DVD copies ")
    new_dvd = DVListType(name, actors, producers, director, production_company, number_of_copies)
    dvd_list.add(new_dvd)
    print("\nNew DVD added\n")

def remove_dvd(title):
    found = False
    for dvd in dvd_list.iterate():
        if dvd.get_title() == title:
            found = True
            if found:
                dvd_list.remove(dvd)
                print("\nDVD removed successfully.\n")
    if not found:
        print("\nEntered DVD doesn't exist.\n")

def search_dvd(title):
  found = False
  for dvd in dvd_list.iterate():
      if dvd.get_title() == title:
        found = True
        if found:
            print("\nThe DVD info is as follows\n")
            print("============================\n")
            print(dvd)
  if not found:
    print("\nEntered DVD doesn't exist.\n")


def update_dvd(title):
    found = False
    for dvd in dvd_list.iterate():
        if dvd.get_title() == title:
            found = True
            if found:
                while True:
                    print("\nUpdate DVD details")
                    print("---------------------\n")
                    print("1) Update the Title:")
                    print("2) Update the actors: ")
                    print("3) Update producer:")
                    print("4) Update director:")
                    print("5) Update the production company:")
                    print("6) Update the number of compies:")
                    print("7) Exit\n")

                    option = input("Choose your option: ")
                    if option == '1':
                        updated_title = input("\nEnter a DVD title: ")
                        dvd.set_title(updated_title)
                        print("Title Updated.\n")
                    elif option == '2':
                        updated_actors = input("Enter the actors in / seperated: ")
                        dvd.set_actors(updated_actors)
                        print("Actors updated.\n")
                    elif option == '3':
                        updated_producers = input("Enter the producersin / seperated : ")
                        dvd.set_producers(updated_producers)
                        print("Producers Updated.\n")
                    elif option == '4':
                        updated_director = input("Enter the director: ")
                        dvd.set_director(updated_director)
                        print("Director name(s) has been updated.\n")
                    elif option == '5':
                        updated_production = input("Enter the production company name: ")
                        dvd.set_production_company(updated_production)
                        print("Production company name has been updated.\n")
                    elif option == '6':
                        updated_copies = int(input("Enter the new number of copies: "))
                        dvd.update_copies(updated_copies)
                        print("Number of copies Updated.\n")
                    elif option == '7':
                        admin_panel()

    if not found:
        print("\nDVD not exists.\n")


def show_all_dvd():
    print("All the DVD details are as follows"
          "================================")
    dvd_list.show()

def check_dvd_availability(title):
    found = False
    for dvd in dvd_list.iterate():
        if dvd.get_title() == title:
            found = True
            if found:
                print("\nDVD available")
                copies = dvd.get_number_of_copies()
                if copies > 0:
                     print(copies, " copies available.\n")
                else:
                    print("No available copies. \n")
    if not found:
        print("\nSearched DVD doesn't exist.\n")



def check_out_dvd(title):
    found = False
    for dvd in dvd_list.iterate():
        if dvd.get_title() == title:
            found = True
            if found:
                copies = dvd.get_number_of_copies()
                print('\n',copies, " copies available.")
                if copies > 0:
                    dvd.checkout_dvd()
                    updated_copies = dvd.get_number_of_copies()
                    print("DVD checked out.")
                    print('New number of copies :', updated_copies, '\n')
                else:
                    print("DVD sold out for borrowing.\n")
    if not found:
        print("\nSearched DVD doesn't exist.\n")


def check_in_dvd(title):
    found = False
    for dvd in dvd_list.iterate():
        if dvd.get_title() == title:
            found = True
            if found:
                copies = dvd.get_number_of_copies()
                print()
                print(copies, "copies available.\n")
                dvd.checkin_dvd()
                updated_copies = dvd.get_number_of_copies()
                print("DVD checked in.\n")
                print('New number of copies available :', updated_copies, '\n')

    if not found:
        print("\nSearched DVD doesn't exist.\n")


def show_all_titles():
  print("\nThe DVD titles are as follows \n"
        "======================\n")
  for dvd in dvd_list.iterate():
    dvd.print_title()
  print()



def add_customer():
    first_name = input("Enter Customer's first name: ")
    last_name = input("Enter Customer's last name: ")
    account_num = input("Enter Customer's account number: ")
    rented_dvd = input("Enter Customer's rented dvd: ")
    new_customer =Customer(first_name,last_name,account_num,rented_dvd)
    root.insert(new_customer)

def lookup_customer(account_num):
    existing_customer = Customer(None,None,account_num,None)
    data = root.search_node(existing_customer)
    if data:
        print("Customer details are as follows: \n"
              "=============================\n")
        print(data)


def show_customers():
    print("Customers details are as follows: \n"
          "================================\n")
    root.show_tree()

def update_customer_details(account_num):
    existing_customer = Customer(None,None,account_num,None)
    data = root.search_node(existing_customer)
    if data:
        while True:
            print("\nUpdate the Customer Details\n"
                  "===========================\n"
                  "(1) Update to new First Name: \n"
                  "(2) Update to new Last Name: \n"
                  "(3) Update to new Account Number: \n"
                  "(4) Update the list of rented DVDs: \n"
                  "(5) Quit\n")
            option =input("Chose an operation ")
            if option == '1':
                new_first_name = input("Enter the updated First name: ")
                data.set_first_name(new_first_name)
                print("First name updated.\n")
            elif option == '2':
                new_last_name = input("Enter the updated Last name: ")
                data.set_last_name(new_last_name)
                print("Last name updated.\n")
            elif option == '3':
                new_account_num = input("Enter the updated Account number: ")
                data.set_account_num(new_account_num)
                print("Account number updated.\n")
            elif option == '4':
                new_rented_dvds = input("Enter the new list of rented DVDs: ")
                data.set_rented_dvds(new_rented_dvds)
                print("Rented DVD list updated.\n")
            elif option == '5':
                admin_panel()

def admin_panel():
    while True:
        print("\nWelcome from the Admin Panel\n"
              "=============================\n"
              "(1) Add a new DVD\n"
              "(2) Remove an existing DVD\n"
              "(3) Search for an existing DVD\n"
              "(4) Update existing DVD details\n"
              "(5) View all DVD\n"
              "(6) Add a new Customer\n"
              "(7) Search for an existing customer\n"
              "(8) Update existing customer details\n"
              "(9) View all registered customers\n"
              "(10) Quit\n")

        option = input("Select your choice:")

        if option == '1':
            add_dvd()
        elif option == '2':
            remove_dvd(input("Enter the dvd title you wanna remove:"))
        elif option == '3':
            search_dvd(input("Enter the dvd tile you wanna search for:"))
        elif option == '4':
            update_dvd(input("Enter the dvd title you wanna update:"))
        elif option == '5':
            show_all_dvd()
        elif option == '6':
            add_customer()
        elif option == '7':
            lookup_customer(input("Enter Customer account number:"))
        elif option == '8':
            update_customer_details(input("Enter customer account number:"))
        elif option == '9':
            show_customers()
        elif option == '10':
            main()

def customer_panel():
    while True:
        print("\n\Welcome to Customer Panel\n"
              "=========================\n"
              "(1) Look for a DVD\n"
              "(2) Check a DVD out\n"
              "(3) Check a DVD in\n"
              "(4) All DVD details\n"
              "(5) All DVD titles\n"
              "(6) Quit\n")

        option = input("Select your mode: ")

        if option == '1':
            check_dvd_availability(input("Enter the title of DVD you wanna search for:"))
        elif option == '2':
            check_out_dvd(input("Enter the title of DVD you wanna check out:"))
        elif option == '3':
            check_in_dvd(input("Enter the title of DVD you wanna check in:"))
        elif option == '4':
            show_all_dvd()
        elif option == '5':
            show_all_titles()
        elif option == '6':
            main()





def main():
    while True:
        print("\nDVD store Management System\n"
              "=============================\n"
              "(1) ADMIN User mode\n"
              "(2) CUSTOMER User mode\n"
              "(3) Quit\n")

        option = input("Select your mode: ")

        if option == '1':
            admin_panel()
        elif option == '2':
            customer_panel()
        elif option == '3':
            quit()


if __name__ == '__main__':
    dvd_list = Linked_list()
    load_data()
    with open("customer.csv", 'r') as customer_data_file:
        customer_data = csv.reader(customer_data_file)
        next(customer_data)
        for index, row in enumerate(customer_data):
            first_name = row[0]
            last_name = row[1]
            account_number = row[2]
            rented_dvds = row[3]
            customer_object = Customer(first_name, last_name, account_number, rented_dvds)

            if index == 0:
                root = BSTnode(customer_object)
            else:
                root.insert(customer_object)
    main()

