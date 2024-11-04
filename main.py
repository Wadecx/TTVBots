import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time

def main():
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
    twitch_username = input("Nom d'utilisateur Twitch : ")
    print(f"Lien à ouvrir : www.twitch.tv/{twitch_username}")
    proxy_count = int(input("Viewers : "))
    os.system('cls')

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

    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    #ADBLOCK EXT
    extension_path = 'adblock.crx'
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    input(Colorate.Vertical(Colors.purple, "Done ! you may need to wait 30 sec to see the viewers, press [ENTRER] to remove them "))
    driver.quit()


if __name__ == '__main__':
    main()