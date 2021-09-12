#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:32:40 2021

@author: isaackliewer
"""
#Author: Isaac Kliewer 
#Assignment Number: 7
#Date: 4-15-21
#Description: This program allows the user to interact with the 
              # inventory of a garden store by viewing, editing, 
              #and updating the information of products. 





def read_file(file_name, dict_prices, dict_quantities):  #Define the function that reads the 
    openFile = open('initial_inventory.txt', 'r')        #inventory from file to dictionaries.
    read3info = openFile.readline().rstrip('\n')
    readSep = read3info.split(';')
    while read3info:                                   #Boolean loop to transfer info from the 
        dict_prices[readSep[0]] = readSep[1]           #file to the dictionaries while there is 
        dict_quantities[readSep[0]] = readSep[2]       #still data to be transferred.
        read3info = openFile.readline().rstrip('\n')
        readSep = read3info.split(';')
    openFile.close()
    
    
    

def print_menu():      #Define function that prints the menu list for the user to choose from.
    print('Please select an option from the menu list below.')
    optionlist = ['1. View list of available products. ', '2. View details for one product. ', 
                  '3. Add a new product. ', '4. Update information for a product. ', '5. Exit. ']
    for i in range(len(optionlist)): 
        print(optionlist[i])
    
    
    
def get_user_choice():   #This function queries the user on their choice of action, 
    callmenu = print_menu()   #and returns it in the variable called choicemenu, which 
    choicemenu = input('What would you like to do? ') #is actually stored in a variable called
    return choicemenu               #menuchoice when the function is called.
    
    
    
def display_all(dict_prices):   #This function displays all of the items in the inventory
    for key in dict_prices:     # by iterating through the keys of one of our dictionaries. 
        print(key)
    
    
    
    
def display_item(dict_prices, dict_quantities):   #This function accesses both dictionaries to 
    choiceitem = input('What is the name of the product? ') #display price/qty for one select 
    if choiceitem in dict_prices:                           #product, and searches via key. 
        print("Price: ", dict_prices[choiceitem])
        print("Quantity: ", dict_quantities[choiceitem])
    else: 
        print("Product is not in the inventory. ") #Notify user if the product they entered 
                                                     #exists within the inventory. 
    
    
    
    
    
def update_item(dict_prices, dict_quantities): #This function allows the user to update information
    choiceitem = input('What is the name of the product? ') #for a product that exists in the 
    if choiceitem  not in dict_prices:                      #inventory already. 
       print("Product is not in the inventory. ")
       print(" ")
    else: #Decision structure to filter through our three options and test for invalid options. 
        updatequery = input("What would you like to update? (Options: price, quantity, both) ")
        if updatequery == 'both':
            price = input("What is the updated price of "+choiceitem +"? ")
            dict_prices[choiceitem] = price
            quantity = input("What is the updated quantity of "+choiceitem +"? ")
            dict_quantities[choiceitem] = quantity
        elif updatequery == 'price':
            price = input("What is the updated price of "+choiceitem +"? ")
            dict_prices[choiceitem] = price
        elif updatequery == 'quantity': 
            quantity = input("What is the updated quantity of "+choiceitem +"? ")
            dict_quantities[choiceitem] = quantity
        else:                                       #If they didn't choose one of the three options,
            print(updatequery, " is not an option.") #then they are notified. 
        
    
    
    
    
def new_item(dict_prices, dict_quantities): #Precreated function that allows the user to add a new
    name = input("What is the name of the new item? ") #item to the inventory, as well as its info.
    price = input("What is the price of "+name +"? ")
    quantity = input("What is the available quantity of "+name +"? ")
    dict_prices[name] = price
    dict_quantities[name] = quantity
    
    
    
def main():
    dict_prices = {}      #Predefine the dictionaries as blank so that they exist to be worked on.
    dict_quantities = {}
    file_name = 'initial_inventory.txt'
    read_file(file_name, dict_prices, dict_quantities) #Read inventory from file to dictionaries. 
    menuchoice = get_user_choice() #Prime loop with a choice to be classified as invalid or valid.
    while menuchoice != '5':
        if menuchoice == '1': 
            display_all(dict_prices)
        elif menuchoice == '2':
            display_item(dict_prices, dict_quantities)
        elif menuchoice == '3': 
            new_item(dict_prices, dict_quantities)
        elif menuchoice == '4':
            update_item(dict_prices, dict_quantities)
        elif menuchoice == '5':
            break
        else: 
            print('Not an option. ')
        menuchoice = get_user_choice() #Reprocess input to conduct another transation until exit. 

main()
        