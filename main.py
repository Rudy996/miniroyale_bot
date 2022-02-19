from selenium import webdriver
import time
import pyautogui
import getpass

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_extension("MetaMask.crx")
options.add_extension("Phantom.crx")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
pyautogui.FAILSAFE = True

try:
    time.sleep(5)
    email = input("Email: ")
    password = getpass.getpass(prompt='Enter password:')
    ctff1 = int(input("Number of matches CTF 2-1: "))
    tdmm1 = int(input("Number of matches TDM 2-2: "))
    bgg1 = int(input("Number of matches BattleRoyale 2-3: "))
    ctff2 = int(input("Number of matches CTF 2-4: "))
    bgg2 = int(input("Number of matches BattleRoyale 2-5: "))
    tdmm2 = int(input("Number of matches TDM 2-6: "))

    time.sleep(2)
    driver.get("https://miniroyale.io/?ref=leave")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.close()
    time.sleep(0.5)
    time.sleep(25)
    pyautogui.click(385, 164)
    time.sleep(0.1)
    pyautogui.click(1258,432)
    time.sleep(0.1)
    pyautogui.click(745, 540)
    time.sleep(0.1)
    pyautogui.write(email, interval=0.1)
    pyautogui.click(1090, 540)
    time.sleep(0.1)
    pyautogui.write(password, interval=0.1)
    pyautogui.click(938, 685)
    time.sleep(2)
    pyautogui.click(117, 17)
    time.sleep(10)
    print("Выбираю режим CTF 2-1")
    pyautogui.click()
    pyautogui.click(1702, 865)  # выбор режима
    time.sleep(0.5)
    pyautogui.click(390, 467) # battleroyale
    time.sleep(0.5)
    pyautogui.click(709, 503)  # tdm
    time.sleep(0.5)
    pyautogui.click(933, 926)  # set modes
    time.sleep(0.5)
    ctf = 0
    while ctf < ctff1:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1419, 840)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(10)
            pyautogui.click(1718, 971)
            time.sleep(20)
            ctf = ctf + 1
            print(f"Сыгран {ctf} ctf 2-")
    print("Выбираю режим TDM 2-2")
    pyautogui.click()
    pyautogui.click(1702, 865) #выбор режима
    time.sleep(0.5)
    pyautogui.click(709, 503) # tdm
    time.sleep(0.5)
    pyautogui.click(1046, 481)  # ctf
    time.sleep(0.5)
    pyautogui.click(933, 926) # set modes
    time.sleep(0.5)
    tdm = 0
    while tdm < tdmm1:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1419, 840)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(10)
            pyautogui.click(1718, 971)
            time.sleep(20)
            tdm = tdm + 1
            print(f"Сыгран {tdm} tdm 2-2")
    print("Выбираю режим BattleRoyale 2-3")
    pyautogui.click(1702, 865) #выбор режима
    time.sleep(0.5)
    pyautogui.click(390, 467)  # battleroyale
    time.sleep(0.5)
    pyautogui.click(709, 503)  # tdm
    time.sleep(0.5)
    pyautogui.click(933, 926)  # set modes
    bg = 0
    while bg < bgg1:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1080, 855)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(15)
            bg = bg + 1
            print(f"Сыгран {bg} BattleRoyale 2-3")

    print("Выбираю режим CTF 2-4")
    pyautogui.click()
    pyautogui.click(1702, 865)  # выбор режима
    time.sleep(0.5)
    pyautogui.click(1046, 481)  # ctf
    time.sleep(0.5)
    pyautogui.click(390, 467)  # battleroyale
    time.sleep(0.5)
    pyautogui.click(933, 926)  # set modes
    time.sleep(0.5)
    ctf1 = 0
    while ctf1 < ctff2:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1419, 840)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(10)
            pyautogui.click(1718, 971)
            time.sleep(20)
            ctf1 = ctf1 + 1
            print(f"Сыгран {ctf1} ctf 2-4")
    print("Выбираю режим BattleRoyale 2-5")
    pyautogui.click(1702, 865) #выбор режима
    time.sleep(0.5)
    pyautogui.click(390, 467)  # battleroyale
    time.sleep(0.5)
    pyautogui.click(1046, 481)  # ctf
    time.sleep(0.5)
    pyautogui.click(933, 926)  # set modes
    bg1 = 0
    while bg1 < bgg2:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1080, 855)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(15)
            bg1 = bg1 + 1
            print(f"Сыгран {bg1} BattleRoyale 2-5")
    print("Выбираю режим TDM 2-6")
    pyautogui.click()
    pyautogui.click(1702, 865)  # выбор режима
    time.sleep(0.5)
    pyautogui.click(709, 503)  # tdm
    time.sleep(0.5)
    pyautogui.click(390, 467)  # battleroyale
    time.sleep(0.5)
    pyautogui.click(933, 926)  # set modes
    time.sleep(0.5)
    tdm1 = 0
    while tdm1 < tdmm2:
        time.sleep(0.5)
        pyautogui.click(1672, 741)
        x = 0
        while x < 250:
            pyautogui.click()
            time.sleep(1)
            x = x + 1
            print(f"Прошло секунд: {x}")
        else:
            pyautogui.click(1419, 840)
            time.sleep(10)
            pyautogui.click(1750, 975)
            time.sleep(10)
            pyautogui.click(1718, 971)
            time.sleep(20)
            tdm1 = tdm1 + 1
            print(f"Сыгран {tdm1} tdm 2-6")

    print("Было сыграно:")
    print(f"CTF 2-1: {ctf}")
    print(f"TDM 2-2: {tdm}")
    print(f"BattleRoyale 2-3: {bg}")
    print(f"CTF 2-4: {ctf1}")
    print(f"BattleRoyale 2-4: {bg1}")
    print(f"TDM 2-6: {tdm1}")
    print("Были сыграны все режима. \n Конец работы через: 20 секунд")
    time.sleep(20)




except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
