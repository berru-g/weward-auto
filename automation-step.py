from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Configuration des options de l'appareil Android cible
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Nom_de_votre_appareil',
    'appPackage': 'com.example.weward',
    'appActivity': 'com.example.weward.MainActivity'
}

# Initialisation du driver Appium
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Attendre que l'application se charge
time.sleep(5)

# Recherche du bouton "Valider mes pas" par son ID ou son xpath
button_id = 'com.example.weward:id/button_validate_steps'
button_xpath = '//android.widget.Button[@text="Valider mes pas"]'

try:
    # Recherche du bouton par ID
    button = driver.find_element_by_id(button_id)
except:
    # Si la recherche par ID échoue, recherche du bouton par xpath
    button = driver.find_element_by_xpath(button_xpath)

# Clic sur le bouton
TouchAction(driver).tap(button).perform()

# Fermeture du driver Appium
driver.quit()
