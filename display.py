from modifie_items import *
#function to Display the list the particular item
def list_items(name):
    name_list = name.split('|')
    i=0
    temp=[]
    for name in name_list:
        if name in stock_dict.keys():
            if(i==0):
                print('STOCK LIST'.center(102))
                print('+', '-' * 99, '+', sep='-')
                print('|{}|{}|{}|{}|'.format('s.NO'.center(22), 'Item Name'.center(52), 'Quantity'.center(12),'Amount'.center(12)))
                print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')

            i += 1
            print('|', str(i).center(20), '|', str(name).center(50), '|', str(stock_dict[name]['Nos']).center(10), '|', str(stock_dict[name]['Rs']).center(10), '|')
            print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')


        else:
            temp.append(name)
    for i in temp:
        print('{} is not found '.format(name))
#function to Display the all list item
def list_all():
    i=0
    if len(stock_dict)!=0:
        print('STOCK LIST'.center(102))
        print('+','-'*99,'+',sep='-')
        print('|{}|{}|{}|{}|'.format('s.NO'.center(22),'Item Name'.center(52),'Quantity'.center(12),'Amount'.center(12)))
        print('|','-'*20,'+','-'*50,'+','-'*10,'+','-'*10,"|",sep='-')
        for key in stock_dict.keys():
            i+=1
            print('|', str(i).center(20),'|', str(key).center(50),'|', str(stock_dict[key]['Nos']).center(10), '|', str(stock_dict[key]['Rs']).center(10), '|')
            print('|', '-' * 20, '+', '-' * 50, '+', '-' * 10, '+', '-' * 10, "|", sep='-')
    else:
        print("list is empty")






def help1():
    print('''
                                         __, _, ____,  __,    ____, 
                                        (-|__| (-|_,  (-|    (-|__) 
                                         _|  |, _|__,  _|__,  _|    
                                        (      (      (      (    

stock related comments:

	add <item_name>,<Quantity>,<cost> - add a single items into stock
	
	add <item_name1>,<Quantity>,<cost>|<item_name2>,<Quantity>,<cost>..... - add a multiple item into stock
	
	list - List all items in the stock
	
	list <item_name> - list particular single item in stock
	
	list <item_name1>|<item_name2>...... - list particular items in stock
	
	update <item_name>,<Quantity>,<cost> -update a single items in stock

	update <item_name1>,<Quantity>,<cost>|<item_name2>,<Quantity>,<cost>..... - update a multiple item in stock
	
	remove <item_name> -remove a single items in stock	
	
	remove <item_name1>|<item_name2>..... - remove a multiple item in stock

Bill related comments:

	bill add <item_name>,<Quantity>,<cost> - add a single items into stock
	
	bill add <item_name1>,<Quantity>,<cost>|<item_name2>,<Quantity>,<cost>..... - add a multiple item into bill
	
	bill -show the bill

	bill list - List all items in the bill
	
	bill list <item_name> - list particular single item in bill
	
	bill list <item_name1>|<item_name2>...... - list particular items in bill
	
	bill update <item_name>,<Quantity>,<cost> -update a single items in bill

	bill update <item_name1>,<Quantity>,<cost>|<item_name2>,<Quantity>,<cost>..... - update a multiple item in bill
	
	bill remove <item_name> -remove a single items in  bill	
	
	bill remove <item_name1>|<item_name2>..... - remove a multiple item in bill''')
