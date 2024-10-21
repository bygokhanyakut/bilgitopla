import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init
from termcolor import colored

# Sabit güvenlik tokeni
security_token = "token123"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    init()
    print(colored("""
████████╗███████╗██╗░░░░░███████╗███████╗░█████╗░███╗░░██╗  ██████╗░██╗██╗░░░░░░██████╗░██╗░██████╗██╗
╚══██╔══╝██╔════╝██║░░░░░██╔════╝██╔════╝██╔══██╗████╗░██║  ██╔══██╗██║██║░░░░░██╔════╝░██║██╔════╝██║
░░░██║░░░█████╗░░██║░░░░░█████╗░░█████╗░░██║░░██║██╔██╗██║  ██████╦╝██║██║░░░░░██║░░██╗░██║╚█████╗░██║
░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██╔══╝░░██║░░██║██║╚████║  ██╔══██╗██║██║░░░░░██║░░╚██╗██║░╚═══██╗██║
░░░██║░░░███████╗███████╗███████╗██║░░░░░╚█████╔╝██║░╚███║  ██████╦╝██║███████╗╚██████╔╝██║██████╔╝██║
░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░╚═╝

████████╗░█████╗░██████╗░██╗░░░░░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗
░░░██║░░░██║░░██║██████╔╝██║░░░░░███████║
░░░██║░░░██║░░██║██╔═══╝░██║░░░░░██╔══██║
░░░██║░░░╚█████╔╝██║░░░░░███████╗██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝

    """, "magenta"))

    print(colored("""
    ---------------------------------------------
        Geliştirici : Gokhan Yakut
        GitHub      : https://github.com/bygokhanyakut
        YouTube     : https://www.youtube.com/@G%C3%B6khan-Yakut
        Twitter     : https://x.com/bygokhanYakut
        İnstagram   : https://www.instagram.com/gokhan_yakut_04/
    ---------------------------------------------
    """, "cyan"))

def verify_token(user_token):
    # Kullanıcının gönderdiği token ile sabit tokeni karşılaştırır
    return user_token == security_token

def phone_info():
    while True:
        init()
        print(colored("*********** Menü ***********", "yellow"))
        print(colored("1] Çıkış / Exit", "magenta"))
        print(colored("2] Telefon Numarası Bilgisi Topla / Phone Number Information", "green"))
        print(colored("*****************************", "yellow"))

        choice = input(colored("Seçiminizi yapın / Make your choice: ", "cyan"))

        def operation():
            if choice == "1": 
                exit()
            elif choice == "2":
                banner()
                user_token = input(colored("Güvenlik tokeninizi girin (Security token): ", "green"))
                
                if verify_token(user_token):
                    number = input(colored("Lütfen telefon numarasını ülke kodu ile birlikte girin (+90..........): ", "green"))
                    
                    try:
                        phone_number = phonenumbers.parse(number, None)  
                        print(colored("Ülke/Şehir - Country/City: ", "cyan"), geocoder.description_for_number(phone_number, 'tr'))
                        print(colored("Saat Dilimi - Time zone: ", "cyan"), timezone.time_zones_for_number(phone_number))
                        print(colored("Operatör - Operator: ", "cyan"), carrier.name_for_number(phone_number, 'tr'))
                    except phonenumbers.NumberParseException:
                        print(colored("Geçersiz numara girdiniz. Lütfen tekrar deneyin.", "red"))
                else:
                    print(colored("Geçersiz token! Yetkisiz işlem.", "red"))
            else:
                print(colored("Hatalı işlem - Incorrect operation", "red"))
        
        operation()

banner()
phone_info()
