import os,sys,requests,json

banner = """ 


 ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      ██▒   █▓ ▄▄▄       ██▓     ██▓▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
 ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▓██░   █▒▒████▄    ▓██▒    ▓██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒    ▓██  █▒░▒██  ▀█▄  ▒██░    ▒██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄       ▒██ █░░░██▄▄▄▄██ ▒██░    ░██░░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒      ▒▀█░   ▓█   ▓██▒░██████▒░██░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░      ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░░▓   ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░      ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░         ░░    ░   ▒     ░ ░    ▒ ░ ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
         ░    ░            ░    ░         ░  ░   ░              ░        ░  ░    ░  ░ ░     ░          ░  ░            ░ ░     ░     
                                     ░                         ░                          ░                                          
                                           ░                         ░                          ░                                          

Tool Information :
- Tool Name : USA Phone Number Validator
- Creator : Soul Kings
- Version : 1.0 [FREE]

Join our telegram channel : @raid_store

"""
api = "https://soulapizy.000webhostapp.com/phonevalidator/"

#Main
print(banner)

#Open Number List
filename = input("Input Phone Number List (Exemple: list.txt) : ")
try:
    file = open(filename,"r")
except:
    sys.exit("[!] Error. No File Exist")
combo = file.readlines()
file.close()

for line in combo:
    line = line.strip()
    data = {"phone": line}
    try:
        response = requests.post(api, data=data).text
    except:
        print("[!] Stopped.")
        combo.append(line)
        break
    if "Success" in response:
        print('\r[\033[92m ' + response + ' \033[0m] ')
        open('hits.txt','a').write(str(line)+'\n')
        open('full-hits.txt','a').write(str('[ ' + response + ' ]')+'\n')
    elif "Unknown" in response:
        print('\r[\033[91mUnknown\033[0m] ' + line)
    elif "Fail" in response:
        print('\r[\033[91mFail\033[0m] ' + line)
    else:
        print('\r[\033[91mBad\033[0m] ' + line)

print("Done....")
