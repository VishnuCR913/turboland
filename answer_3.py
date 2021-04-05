data_list=input('enter the data_list: ')

def deletion_order(data_list, priority):
    if priority=="frequency":
        sorted(data_list, key=lambda i: i['frequency'])
        data_list.remove(0)
    else:
        sorted(data_list, key=lambda i: i['last_updated'])
        data_list.pop()

            

