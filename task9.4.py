
contacts={"omar":"6789","yazid":"13579","ahmed":"2468"}

def add_c(name,num):
    contacts[name]=num
    print(f"{name}:{num} is added")
add_c("jannat",'12345')

def delete_c(name):
    print(f"{name} is removed")
    return name in contacts and contacts.pop(name)
delete_c("omar")

def srch_c(name,num):
    if name in contacts:
        print(f"name:{name} , phone:{num}")
    else:
        print("contact not found")
srch_c("rico","1550")

def view_c():
    print(contacts)
view_c()

newnum=4567
def update_c(name,newnum):
    contacts[name]=newnum
    if name in contacts:
        if newnum:
            contacts[name]
num=newnum
update_c("ahmed","4567")
print(contacts)