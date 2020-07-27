from time import *  
from datetime import *  

host_path = r"C:\Windows\System32\drivers\etc\hosts"  
redirect = "127.0.0.1"  
websites = []
n=int(input("Enter the number of Websites to be blocked:"))
print("Enter the url of the website:")
for i in range(n):
    x=input()
    websites.append(x)  
    
if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,16
):  
    with open(host_path,"r+") as fileptr: 
        print("website blocked") 
        content = fileptr.read()  
        for website in websites:  
            if website in content:  
                pass  
            else:  
                fileptr.write(redirect+"\t"+website+"\n")  
else:  
    with open(host_path,'r+') as file:  
        content = file.readlines();  
        file.seek(0)  
        for line in content:  
            if not any(website in line for website in  websites):  
                file.write(line)  
        file.truncate()  
        print("website unblocked")