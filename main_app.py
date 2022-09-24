#import bill module
from bill import  *
#main function to start app
def app_start():

    while(True):
        command_str=input("$")
        command_list=command_str.split(' ')
        if command_list[0].lower() == 'add':
            if len(command_list) != 1:
                add_items(command_list[1])
            else:
                pass
        elif command_list[0].lower() == 'update':
            if len(command_list) != 1:
                update_item(command_list[1])
            else:
                pass
        elif  command_list[0].lower() == 'list':
            if len(command_list) != 1:
                list_items(command_list[1])
            else:
                list_all()
        elif command_list[0].lower() == 'remove':
            if len(command_list) != 1:
                remove_item(command_list[1])
            else:
                pass
        elif command_list[0].lower() == 'bill':
            if len(command_list) != 1:
                if command_list[1].lower() == 'add':
                    bill_add_items(command_list[2])
                elif command_list[1].lower() == 'update':
                    bill_update_item(command_list[2])
                elif command_list[1].lower() =='remove':
                    bill_remove_item(command_list[2])
                elif command_list[1].lower() == 'list':
                    if len(command_list) != 2:
                        bill_list_items(command_list[2])
                    else:
                        bill_list_all()

                else:
                    print("Invalid command..")


            else:
               bill(shop)

        elif command_list[0].lower() == 'help':
            help1()
            
        elif command_list[0].lower() == 'exit':
            if len(stock_dict)>0:
                with open('stock.txt','w') as f:
                    for i in stock_dict.keys():
                        stock=i+','+str(stock_dict[i]['Nos'])+','+str(stock_dict[i]['Rs'])+'\n'
                        f.write(stock)
            exit('bye')
        elif command_list[0].lower() == '':
            pass

        else:
            print('command {} is not found'.format(command_list[0]))
#function to get Shop details from the file
def shop_details():


                    shop_name = input('Enter the shop name: ')
                    shop_address = input('Enter the shop address: ')
                    shop_contacts=input('Enter the shop contact number: ')
                    f=open("shop_details.txt","w")
                    f.write(shop_name+'|'+shop_address+'|'+shop_contacts)
                    f.close()
                    with open("shop_details.txt") as f:
                     for i in f:
                        global shop
                        shop=i.split('|')
                        shop_title(shop)

#function to get stock from the file
def read_data():
    try:
        f=open('stock.txt')
        if len(f.read())==0:
            print('stock is empty')

        else:
            f = open("stock.txt")
            for i in f:
                    list1 = i.split(',')
                    stock_dict[list1[0]] = {'Nos': int(list1[1]), 'Rs':int(list1[2])}

    except:
           try:
                 with open('stock.txt','x') as f:
                     pass
           except:
                pass
    finally:
        app_start()

#Get the shop title from the file
def shop_title(shop):
#welcome banner
    print(''' 
█     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ 
▒░▒░▒░ ░  ▒░▒░▒░ BILLING SOFTWARE░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
you have any doubts to use this software type "help" comment
    ''')

try:
    f=open('shop_details.txt')
    if len(f.read())==0:
        shop_details()
    else:
        f = open("shop_details.txt")
        for i in f:
            shop=i.split('|')
            shop_title(shop)
except:
     shop_details()
finally:
    read_data()


