import os

def load_config(filename):
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()
    return config

config = load_config('config.txt')

os.system('cls' if os.name == 'nt' else 'clear')
menu = """
         ▄▄▄█████▓ ▒█████   ▒█████   ██▓        ██▓ ███▄    █   █████▒▒█████
         ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
         ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
         ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
           ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
           ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░
             ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░
            ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒
                     ░ ░      ░ ░      ░  ░    ░           ░            ░ ░

"""
menu2 = f"""
> Tool Name     : ('ZEA Muti-Tool')
> Version       : ('v3')}
> Creator       : ('MR Brit')
> Coding        : ('VSC')
> Discord [W]   : ('https://discord.gg/un4yj5xvV7')
""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")
    input("\n\033[31mPress Enter to return to the main menu...\033[0m")
    os.system('python cyb3rtech.py')

if __name__ == "__main__":
    show_menu()
