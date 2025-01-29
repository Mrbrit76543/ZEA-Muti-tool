import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 ________  ________   ______         ______   ______         _______   ________  ________  ________  ________  _______  
|        \|        \ /      \       |      \ /      \       |       \ |        \|        \|        \|        \|       \ 
 \$$$$$$$$| $$$$$$$$|  $$$$$$\       \$$$$$$|  $$$$$$\      | $$$$$$$\| $$$$$$$$ \$$$$$$$$ \$$$$$$$$| $$$$$$$$| $$$$$$$\
    /  $$ | $$__    | $$__| $$        | $$  | $$___\$$      | $$__/ $$| $$__       | $$      | $$   | $$__    | $$__| $$
   /  $$  | $$  \   | $$    $$        | $$   \$$    \       | $$    $$| $$  \      | $$      | $$   | $$  \   | $$    $$
  /  $$   | $$$$$   | $$$$$$$$        | $$   _\$$$$$$\      | $$$$$$$\| $$$$$      | $$      | $$   | $$$$$   | $$$$$$$\
 /  $$___ | $$_____ | $$  | $$       _| $$_ |  \__| $$      | $$__/ $$| $$_____    | $$      | $$   | $$_____ | $$  | $$
|  $$    \| $$     \| $$  | $$      |   $$ \ \$$    $$      | $$    $$| $$     \   | $$      | $$   | $$     \| $$  | $$
 \$$$$$$$$ \$$$$$$$$ \$$   \$$       \$$$$$$  \$$$$$$        \$$$$$$$  \$$$$$$$$    \$$       \$$    \$$$$$$$$ \$$   \$$
                                                                                                                        
                                                                                                                        
                                                                                                                        
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: ZEA Offens Security
""")

def display_menu():
    print(Fore.GREEN + """
    1: ZEA-Tool (Hacking Tools)       | 2: ZEA-Paid-Tools
    3: Info (about-us)                
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python ZEA-Muti-Tool\tools\zero-tool.py"/zero-tool.py"' if os.name == 'nt' else 'python ZEA-Muti-Tool\tools/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')
       
        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
