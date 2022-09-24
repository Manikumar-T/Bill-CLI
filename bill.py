from display import *
#import date module for date
from datetime import date
bill_items = {}
customer_flag=True
Total=0
#add items in the bill
def bill_add_items(item_str):
        global customer_name, customer_mobile_num, place,customer_flag
        item_list=item_str.split('|')
        for item in item_list:
            item = item.split(',')
            if len(item) == 2 and item[1].isdigit():
                if item[0] in stock_dict.keys():

                    if (item[0]  not in bill_items.keys()):
                        if stock_dict[item[0]]['Nos']>=int(item[1]):
                                if (len(bill_items) == 0):
                                    if (customer_flag == True):
                                        customer_name = input('Enter customer name: ')
                                customer_flag = False
                                print("Adding ",item[0],'to bill',end=' ')
                                bill_items[item[0]] = {'Nos': int(item[1]), 'Rs':int(stock_dict[item[0]]['Rs'] * int(item[1]))}
                                stock_dict[item[0]]['Nos']-=int(item[1])
                                print('completed!')
                        else:
                            print('out of stock')
                    else:
                        print('{} is already exists if you want to update use \" Update\"command'.format(item[0]))
                else:
                    print('{} is not found if you want to Add use \"Add\"command'.format(item[0]))


            else:
                print('Invalid command...')
                return


#update items in the bill
def bill_update_item(item_str):
    item_list = item_str.split('|')
    for item in item_list:
        item = item.split(',')
        if len(item) == 2:


            if  int(item[1])<0 or item[1].isdigit():

                    if item[0] in bill_items.keys():
                        if (stock_dict[item[0]]['Nos'] + int(item[1])>=0):
                            if bill_items[item[0]]['Nos']+int(item[1])<=0:
                                del bill_items[item[0]]

                            else:
                                print("Updating",item[0],end=' ')
                                bill_items[item[0]] = {'Nos':bill_items[item[0]]['Nos']+int(item[1]), 'Rs':int(stock_dict[item[0]]['Rs'] * bill_items[item[0]]['Nos'])}
                                stock_dict[item[0]]['Nos'] -= int(item[1])
                                print('completed!')
                        else:
                            print('out of stack')

                    else:
                        print('{} is not found if you want to Add use \"Bill Add\"command'.format(item[0]))

            else:
                print('Invalid command')
                return
        else:
            print('Invalid command')
            return
#remove the items  in the bill
def bill_remove_item(name):
    name_list = name.split('|')
    for name in name_list:
                if (name in bill_items.keys()):
                    print("removing ",name,end=' ')
                    del bill_items[name]
                    print('completed!')
                else:
                    print('{} is not found '.format(name))

#Display the particular items in bill
def bill_list_items(name):
    name_list = name.split('|')
    temp=[]
    global Total
    flag=False
    Total,i = 0,0
    for name in name_list:
        if name in bill_items.keys():
            if(i==0):
                print('BILL LIST'.center(102))
                print('+', '-' * 99, '+', sep='-')
                print('|{}|{}|{}|{}|'.format('s.NO'.center(22), 'Item Name'.center(52), 'Quantity'.center(12),'Amount'.center(12)))
                print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
            i += 1
            print('|', str(i).center(20), '|', str(name).center(50), '|', str(bill_items[name]['Nos']).center(10), '|',str(bill_items[name]['Rs']).center(10), '|')
            print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
            flag=True
            Total += bill_items[name]['Rs']
        else:
            temp.append(name)
    if(flag==True):
        print(' ' * 75, '|', 'Total'.center(10), '|', str(Total).center(10), '|')
        print(' ' * 76, '-' * 25, '', sep='+')
    for i in temp:
        print('{} is not found '.format(name))
#Display the all items in bill
def bill_list_all():
    global Total
    Total,i=0,0
    if len(bill_items)!=0:
        print('BILL LIST'.center(102))
        print('+','-'*99,'+',sep='-')
        print('|{}|{}|{}|{}|'.format('s.NO'.center(22),'Item Name'.center(52),'Quantity'.center(12),'Amount'.center(12)))
        print('|','-'*20,'+','-'*50,'+','-'*10,'+','-'*10,"|",sep='-')
        for key in bill_items.keys():
            i+=1
            print('|',str(i).center(20),'|', str(key).center(50),'|', str(bill_items[key]['Nos']).center(10),'|', str(bill_items[key]['Rs']).center(10),'|')
            print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
            Total += bill_items[key]['Rs']
        print(' '*75,'|','Total'.center(10),'|',str(Total).center(10),'|')
        print(' ' * 76,'-'*25,'',sep='+')

    else:
         print("bill is empty")
#Display bill in formate
def bill(shop):
    i,Total= 0,0
    global customer_name,customer_mobile_num,place
    if len(bill_items) != 0:
        print('INVOICE'.center(102))
        print(' +', '-' * 99, '+', sep='-')
        print(' |{}|\n |{}|\n |{}|'.format(shop[0].upper().center(101),shop[1].center(101),shop[2].center(101)))
        print(' +', '-' * 99, '+', sep='-')
        print(' |','Buyer Name:', customer_name.center(35),' '*25, '|',' Date:',date.today(),'      |', sep=' ')
        print(' +', '-' * 99, '+', sep='-')
        print(' |{}|{}|{}|{}|'.format('s.NO'.center(22), 'Item Name'.center(52), 'Quantity'.center(12),
                                     'Amount'.center(12)))
        print(' |', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
        for key in bill_items.keys():
            i += 1
            print(' |', str(i).center(20), '|', str(key).center(50), '|', str(bill_items[key]['Nos']).center(10), '|',
                  str(bill_items[key]['Rs']).center(10), '|')
            print(' |', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
            Total+=bill_items[key]['Rs']
        print(' '*76,'|','Total'.center(10),'|',str(Total).center(10),'|')
        print(' ' * 77,'-'*25,'',sep='+')

    else:
         print("bill is empty")