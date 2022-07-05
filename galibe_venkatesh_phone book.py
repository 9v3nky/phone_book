def get_key(val):
    for key, value in phone_book.items():
         if val == value:
             return key
 
    return "name doesn't exist"
phone_book = {} 

#loop
option = 1
while option > 0:
    print("---phone book---\n")
    print("0: Exit  \t 1: Add   \t 2: list ")
    print("3: Modify\t 4: Search\t 5:Delete ")
    option = int(input("Select option "))
    if(option == 1):
        cell_no = int(input("Enter cell no "))
        name = input("Enter name ") 
        phone_book[cell_no] = name
        print("successfully Added ")
    

    elif(option == 2):
        print("the list cell no in phone book ")
        print(phone_book)
    
    elif(option == 3):
        print("1: modify cell no\t\t 2: modify name ")
        modify = int(input("Select 1 or 2 "))
        if(modify == 1):
            del_name = input("enter name no ")
            key = get_key(del_name)
            if(key == "name doesn't exist"):
                print(key)
            else:
                del phone_book[key]
                cell_no = int(input("Enter cell no "))
                phone_book[cell_no] = name
                print("Successfully modified\n\n")
        elif(modify == 2):
            cell_no = int(input("Enter cell no "))
            name = input("Enter name ") 
            del phone_book[cell_no]
            phone_book[cell_no] = name
            print("Successfully modified\n\n")
        else:
            print("wrong selection\n")



    elif(option == 4):
        
        search_name = input("Enter name ")
        print(get_key(search_name))

    elif(option == 5):
        del_name = input("Enter name to delete ")
        key = get_key(del_name)
        if(key == "name doesn't exist"):
            print(key)
        else:
            del phone_book[key]
            print("Successfully deleted ", del_name)
    else:
        print("wrong option selected. select again ")  


