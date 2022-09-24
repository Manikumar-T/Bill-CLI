stock_dict = {}
# function to add items stock
def add_items(item_str):
        item_list = item_str.split('|')
        for item in item_list:
            item = item.split(',')
            if len(item) == 3:
                if item[1].isdigit() and item[2].isdigit():
                    if (item[0] not in stock_dict.keys()):
                        if int(item[2]) > 0:
                            print("Adding ",item[0],end=' ')
                            stock_dict[item[0]] = {'Nos': int(item[1]), 'Rs': int(item[2])}
                            update_file()
                            print('completed!')
                        else:
                            print('cost of the items {} should be greater then zero'.format(item[0]))
                    else:
                        print('{} is already exists if you want to update use \" Update\"command'.format(item[0]))

                else:
                    print('Invalid command')
                    return
            else:
                print('Invalid command')
                return


#function to update items stock
def update_item(item_str):
    item_list = item_str.split('|')
    for item in item_list:
        item = item.split(',')
        if len(item) == 3:

            if item[1] =='-' and item[2].isdigit():
                if item[0] in stock_dict.keys():
                    if int(item[2]) > 0:
                        print("Updating ",item[0],end=' ')
                        stock_dict[item[0]]['Rs']=int(item[2])
                        update_file()
                        print('completed!')
                    else:
                        print('cost of the items {} should be greater then zero'.format(item[0]))

                else:
                    print('{} is not found if you want to Add use \"Add\"command'.format(item[0]))

            elif int(item[1])<0 or item[2] == '-' or item[1].isdigit() :

                    if item[0] in stock_dict.keys():
                        print("Updating",item[0],end=' ')
                        stock_dict[item[0]]['Nos']= stock_dict[item[0]]['Nos'] + int(item[1])
                        update_file()
                        print('completed!')

                    else:
                        print('{} is not found if you want to Add use \"Add\"command'.format(item[0]))


            elif  item[2].isdigit() and (int(item[1])<0 or item[1].isdigit()):

                    if item[0] in stock_dict.keys():
                        if int(item[2]) > 0:
                            print("Updating ",item[0],end=' ')
                            stock_dict[item[0]] = {'Nos': stock_dict[item[0]]['Nos'] + int(item[1]), 'Rs':int(item[2])}
                            update_file()
                            print('completed!')
                        else:
                            print('cost of the items {} should be greater then zero'.format(item[0]))

                    else:
                        print('{} is not found if you want to Add use \"Add\"command'.format(item[0]))

            else:
                print('Invalid command')
                return
        else:
            print('Invalid command')
            return
#function to remove item in stock
def remove_item(name):
    name_list = name.split('|')
    for name in name_list:
                if (name in stock_dict.keys()):
                    print("removing ",name,end=' ')
                    del stock_dict[name]
                    update_file()
                    print('completed!')
                else:
                    print('{} is not found '.format(name))

#function to update item in stock
def update_file():
    if len(stock_dict) > 0:
        with open('stock.txt', 'w') as f:
            for i in stock_dict.keys():
                stock = i + ',' + str(stock_dict[i]['Nos']) + ',' + str(stock_dict[i]['Rs']) + '\n'
                f.write(stock)
