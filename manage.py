from ast import If
import os
from colorama import Fore

# print()
os.system('clear')
print ('\033[1m' + '''

    _____  _    _ _____           _   _                 
    |  __ \| |  | |  __ \         | | (_)                
    | |__) | |__| | |__) |_ _ _ __| |_ _ ___  __ _ _ __  
    |  ___/|  __  |  ___/ _` | '__| __| / __|/ _` | '_ \ 
    | |    | |  | | |  | (_| | |  | |_| \__ \ (_| | | | |
    |_|    |_|  |_|_|   \__,_|_|   \__|_|___/\__,_|_| |_|
                                        By: Sourav Bapari

 YouTube: https://m.youtube.com/techinsouravofficial
 Instagram: https://instagram.com/techinsourav
''')
print('\033[0m' + Fore.GREEN + '''
 1 -> make:channel         Create a new channel class
 2 -> make:command         Create a new Artisan command
 3 -> make:controller      Create a new controller class
 4 -> make:event           Create a new event class
 5 -> make:exception       Create a new custom exception class
 6 -> make:factory         Create a new model factory
 7 -> make:job             Create a new job class
 8 -> make:listener        Create a new event listener class
 9 -> make:mail            Create a new email class
 10-> make:middleware      Create a new middleware class
 11-> make:migration       Create a new migration file
 12-> make:model           Create a new Eloquent model class
 13-> make:notification    Create a new notification class
 14-> make:observer        Create a new observer class
 15-> make:policy          Create a new policy class
 16-> make:provider        Create a new service provider class
 17-> make:request         Create a new form request class
 18-> make:resource        Create a new resource
 19-> make:rule            Create a new validation rule
 20-> make:seeder          Create a new seeder class
 21-> make:test            Create a new test class
''')

def commend(com,fnm,typ):
    print(Fore.CYAN)
    run = com+typ+" "+fnm
    print("\n Your Commend => "+run)
    print(Fore.RED)
    print("\n\n Are you Sure To Run This Y/n")
    print(Fore.WHITE)
    yn = input("\n Enter Y/N: ")
    yn = yn.lower()
    if yn == 'y':
        os.system(run)
    
 


print(Fore.WHITE)
inp = input("\n Select Your Number: ")
print(Fore.YELLOW)
fnm = input("\n Name Your File:")
com = "php artisan "
inp = int(inp);
if inp == 1:
    commend(com,fnm,"make:channel")
if inp == 2:
    commend(com,fnm,"make:command")
if inp == 3:
    commend(com,fnm,"make:controller")
if inp == 4:
    commend(com,fnm,"make:event")
if inp == 5:
    commend(com,fnm,"make:exception")
if inp == 6:
    commend(com,fnm,"make:factory")
if inp == 7:
    commend(com,fnm,"make:job")
if inp == 8:
    commend(com,fnm,"make:listener")
if inp == 9:
    commend(com,fnm,"make:mail")
if inp == 10:
    commend(com,fnm,"make:middleware")
if inp == 11:
    commend(com,fnm,"make:migration")
if inp == 12:
    commend(com,fnm,"make:model")
if inp == 13:
    commend(com,fnm,"make:notification")
if inp == 14:
    commend(com,fnm,"make:observer")
if inp == 15:
    commend(com,fnm,"make:policy")
if inp == 16:
    commend(com,fnm,"make:provider")
if inp == 17:
    commend(com,fnm,"make:request")
if inp == 18:
    commend(com,fnm,"make:resource")
if inp == 19:
    commend(com,fnm,"make:rule")
if inp == 20:
    commend(com,fnm,"make:seeder")
if inp == 21:
    commend(com,fnm,"make:test")
        
    
    

