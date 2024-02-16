#Q5
dic1={}
key_str=str(input("Enter keys separated by spaces:"))
value_str=str(input("Enter values separated by spaces:"))
key_list=key_str.split(" ")
value_list=value_str.split(" ")
if len(key_list)!=len(value_list):
    print("ERROR")
else:
    for i in range(len(key_list)):
        dic1.update({key_list[i]:value_list[i]})
    print(dic1)
