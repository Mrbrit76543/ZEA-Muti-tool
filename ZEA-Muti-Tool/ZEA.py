import os
import time
import shutil

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def blinking():
    text = """
.%%%%%%..%%%%%%...%%%%...........%%%%%....%%%%....%%%%...%%%%%%..%%%%%%..%%..%%...%%%%...........%%..%%..%%%%%..
....%%...%%......%%..%%..........%%..%%..%%..%%..%%..%%....%%......%%....%%%.%%..%%..............%%..%%..%%..%%.
...%%....%%%%....%%%%%%..........%%%%%...%%..%%..%%..%%....%%......%%....%%.%%%..%%.%%%..........%%..%%..%%%%%..
..%%.....%%......%%..%%..........%%..%%..%%..%%..%%..%%....%%......%%....%%..%%..%%..%%..........%%..%%..%%.....
.%%%%%%..%%%%%%..%%..%%..........%%%%%....%%%%....%%%%.....%%....%%%%%%..%%..%%...%%%%............%%%%...%%.....
................................................................................................................                                                                                                                               
  (ZEA loading..)
    """
    terminal_size = get_terminal_size()
    centered_text = center_text(text, terminal_size.columns)
    
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[31m{centered_text}\033[0m")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    blinking()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    menu = """
___  ____ ____    _  _ _  _ ___ _    ___ ____ ____ _    
  /  |___ |__|    |\/| |  |  |  | __  |  |  | |  | |    
 /__ |___ |  |    |  | |__|  |  |     |  |__| |__| |___ 
                                                        
                                             ║
                                             ║
                                             ║
      ╔══════════════════════════════════════════════════════════════════════════════════╗
      ║ ZEA Tool | v1.0.4 | [0] > Support (discord) https://discord.gg/un4yj5xvV7                         
      ║══════════════════════════════════════════════════════════════════════════════════║
      ║                                                                                  ║
      ║ [1] > N/A                       [11] > Discord Token Info                        ║
      ║ [2] > IP Info                   [12] > Discord Token Nuker                       ║
      ║ [3] > Spoofer                   [13] > Discord Token Joiner                      ║
      ║ [4] > Mass Report (NEW)         [14] > Discord Token BruteForce                  ║
      ║ [5] > Phone Number Lookup       [15] > N/A                                       ║
      ║ [6] > Mail Info                 [16] > Discord Token Generator                   ║
      ║ [7] > Username Tracker          [17] > Discord Nitro Generator                   ║
      ║ [8] > SQL Vulnerability         [18] > Discord Server Info                       ║
      ║ [9] > Discord Raid              [19] > Web Cloner (#soon)                        ║
      ║ [10] > Dmall                    [20] > Next Page (1/2) (#soon)                   ║
      ║                                                                                  ║
      ╚══════════════════════════════════════════════════════════════════════════════════╝
   """
    
    while True:
        print(f"\033[31m{menu}")

        try:
            choice = int(input('Choice >> '))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 1:
                    os.system('python ./tools/cyb3rtech.py')
                elif choice == 2:
                    os.system('python ./tools/geoip.py')
                elif choice == 3:
                    os.system('python ./tools/ZEA_Spoofer.py')
                elif choice == 4:
                    os.system('python ./tools/Mass_report_new.py')
                elif choice == 5:
                    os.system('python ./tools/phone_number.py')
                elif choice == 6:
                    os.system('python ./tools/mail_info.py')
                elif choice == 7:
                    os.system('python ./tools/username_tracker.py')
                elif choice == 8:
                    os.system('python ./tools/sql_vulnerability.py')
                elif choice == 9:
                    os.system('python ./tools/discord_raid.py')
                elif choice == 10:
                    os.system('python ./tools/dmall.py')
                elif choice == 11:
                    os.system('python ./tools/discord_token_info.py')
                elif choice == 12:
                    os.system('python ./tools/discord_token_nuker.py')
                elif choice == 13:
                    os.system('python ./tools/discord_token_joiner.py')
                elif choice == 14:
                    os.system('python ./tools/discord_token_bruteforce.py')
                elif choice == 15:
                    os.system('python ./cyb3rtech.py')
                elif choice == 16:
                    os.system('python ./cyb3rtech.py')
                elif choice == 17:
                    os.system('python ./tools/discord_nitro_generator.py')
                elif choice == 18:
                    os.system('python ./cyb3rtech.py')
                elif choice == 19:
                    os.system('python ./tools/web_cloner.py')
                elif choice == 20:
                    os.system('python ./nextpage.py')
                else:
                    raise ValueError
            choice_script(choice)
            break
        except ValueError:
            print("\033[31m[!] >\033[0m Invalid choice \033[31m< [!]\033[0m")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
