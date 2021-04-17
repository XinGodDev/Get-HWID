import subprocess
import os as o; o.system('cls')if os.name == 'nt' else 'clear'
from colorama import Fore

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

os.system("cls")
banner = """
|__| |  | | |  \    \_/ | |\ | 
|  | |/\| | |__/    / \ | | \| """
print(f'{Fore.RED}{banner}\nHWID: {hwid}{Fore.RESET}') 
