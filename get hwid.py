import subprocess, time, os
from colorama import Fore

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

os.system("cls")
print(Fore.RED)
banner = """                
|__| |  | | |  \    \_/ | |\ | 
|  | |/\| | |__/    / \ | | \| 
"""
print(banner)
print(f'HWID: {hwid}') 
print(Fore.RESET)
exit()
