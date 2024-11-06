import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time

# ==================================================================================================================================================================================


#   ____  _          _       _                     
#  |  _ \(_)___  ___| | __ _(_)_ __ ___   ___ _ __ 
#  | | | | / __|/ __| |/ _` | | '_ ` _ \ / _ \ '__|
#  | |_| | \__ \ (__| | (_| | | | | | | |  __/ |   
#  |____/|_|___/\___|_|\__,_|_|_| |_| |_|\___|_|   
   
   #Disclaimer, [FR]

# **Avis de propriété intellectuelle et restrictions d'utilisation**
# Ce programme, ainsi que son code source, sa conception et l'ensemble de ses composantes, sont la propriété exclusive de **WaXeD**.
#  Toute reproduction, copie, modification, ou toute tentative de vol de ce programme, sans l'autorisation expresse et écrite de WaXeD, 
# est strictement interdite et constitue une violation des droits d'auteur et de la propriété intellectuelle.
# Les droits exclusifs de WaXeD incluent, mais ne se limitent pas à :
# - Le droit de distribution et de commercialisation de ce programme,
# - L'autorisation exclusive de modifier, adapter ou mettre à jour le programme,
# - La protection contre toute reproduction non autorisée de tout ou partie du code source, des fichiers ou des composantes graphiques de l’application.
# Toute utilisation non autorisée, sous quelque forme que ce soit, sera susceptible d’entraîner des poursuites judiciaires conformément aux lois en vigueur. 
# WaXeD se réserve le droit de prendre toutes les mesures nécessaires pour faire valoir ses droits, notamment en cas d'usage frauduleux ou de contrefaçon de ce programme.

#Disclaimer, [EN]

# **Intellectual Property Notice and Usage Restrictions**
# This program, along with its source code, design, and all components, is the exclusive property of **WaXeD**.
#  Any reproduction, copying, modification, or any attempt to steal this program, without the express written authorization of WaXeD,
#  is strictly prohibited and constitutes a violation of copyright and intellectual property rights.
# The exclusive rights of WaXeD include, but are not limited to:
# - The right to distribute and market this program,
# - The exclusive authorization to modify, adapt, or update the program,
# - Protection against any unauthorized reproduction of any part of the source code, files, or graphic components of the application.
# Any unauthorized use, in any form, may result in legal action in accordance with applicable laws.
# WaXeD reserves the right to take all necessary measures to enforce its rights, including in cases of fraudulent use or counterfeiting of this program.


# ==================================================================================================================================================================================


proxy_url = ""
twitch_username = ""
proxy_count = 0
ttv_viwers_V = 1.0

def initialize():
    global proxy_url, twitch_username, proxy_count
    os.system('cls')
    os.system(f"title WaXeD - TTVBotZzz ")
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter("""
                                                         ➖🟪🟪🟪🟪🟪🟪🟪🟪
            ██╗    ██╗ █████╗ ██╗  ██╗███████╗██████╗     🟪🟪⬛⬛⬛⬛⬛⬛🟪
            ██║    ██║██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗    🟪🟪⬛⬛🟪⬛🟪⬛🟪 
            ██║ █╗ ██║███████║ ╚███╔╝ █████╗  ██║  ██║    🟪🟪⬛⬛🟪⬛🟪⬛🟪  
            ██║███╗██║██╔══██║ ██╔██╗ ██╔══╝  ██║  ██║    🟪🟪⬛⬛⬛⬛⬛⬛🟪  
            ╚███╔███╔╝██║  ██║██╔╝ ██╗███████╗██████╔╝    🟪🟪🟪🟪⬛⬛⬛🟪🟪 
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝     🟪🟪🟪🟪⬛🟪🟪    
                                                          🟪🟪🟪🟪🟪🟪
                                                          ➖➖🟪🟪
                                                               
            Github : https://github.com/Wadecx

                                    """)))

    proxyList = {
        1: "https://www.blockaway.net", 
    }

    print(Colorate.Vertical(Colors.red_to_blue, "Proxy Server :"))
    choix_proxy = int(input("> Sélectionnez un numéro de proxy (1, Recommandé) : "))
    proxy_url = proxyList.get(choix_proxy)
    twitch_username = input(Colorate.Vertical(Colors.red_to_blue,"Username : "))
    proxy_count = int(input(Colorate.Vertical(Colors.red_to_blue,"Viewers : ")))
    os.system('cls')

def main():
    """Fonction principale pour exécuter le bot sans redemander les inputs."""
    global proxy_url, twitch_username, proxy_count

    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter("""
                                                         ➖🟪🟪🟪🟪🟪🟪🟪🟪
            ██╗    ██╗ █████╗ ██╗  ██╗███████╗██████╗     🟪🟪⬛⬛⬛⬛⬛⬛🟪
            ██║    ██║██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗    🟪🟪⬛⬛🟪⬛🟪⬛🟪 
            ██║ █╗ ██║███████║ ╚███╔╝ █████╗  ██║  ██║    🟪🟪⬛⬛🟪⬛🟪⬛🟪  
            ██║███╗██║██╔══██║ ██╔██╗ ██╔══╝  ██║  ██║    🟪🟪⬛⬛⬛⬛⬛⬛🟪  
            ╚███╔███╔╝██║  ██║██╔╝ ██╗███████╗██████╔╝    🟪🟪🟪🟪⬛⬛⬛🟪🟪 
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝     🟪🟪🟪🟪⬛🟪🟪    
                                                          🟪🟪🟪🟪🟪🟪
                                                          ➖➖🟪🟪
                                                               
            Github : https://github.com/Wadecx
            Status : Viewers send !                                                     

                                    """)))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    # ADBLOCK EXT
    extension_path = 'adblock.crx'
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)

    # Ouvrir le proxy et naviguer vers l'URL de Twitch
    driver.get(proxy_url)
    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    wait_time = 120  
    print(f"Attendez {wait_time} ")
    time.sleep(wait_time)  

    driver.quit()  

initialize()


if __name__ == '__main__':
    while True:
        main()
        print("Redémarrage du programme...")
        time.sleep(3)  
