# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enum import Enum
import time
import random
import logging
import urllib.request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Spamming bot")


def logging(message):
    logger.info(message)
    # print(message)


class Bot:
    def __init__(self, link: str, name: str):
        """
        :param link: First ep link
        :param name: Anime name. Used to save files
        """
        # WebDriver options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")

        # Actions
        self.link = link
        self.name = name
        self.eps = 1
        profile = webdriver.Chrome(
            options=options, executable_path="./drivers/chromedriver_v103.exe"
        )
        """Instancia do selenium """
        self.driver = profile
        logging("Iniciando browser")

    def run(self):
        print(self.actions)
        for action in self.actions:
            print(action, self.actions[action])
            self.get(action, self.actions[action])
            time.sleep(5)
        self.driver.close()

    def Open(self):
        driver = self.driver
        driver.get(self.link)
        time.sleep(20)
        # <input class="inputDefault-3FGxgL input-2g-os5 inputField-2RZxdl" name="email" type="text" placeholder="" aria-label="E-mail ou número de telefone" autocomplete="off" maxlength="999" spellcheck="false" aria-labelledby="uid_17" value="">
        video_element = driver.find_element(By.XPATH, "//video")
        self.Download(video_element.get_attribute("src"))
        has_next = self.getNext()
        if has_next:
            self.link = has_next
            self.eps = self.eps + 1
            self.Open()

    def Download(self, link):
        name = f"{self.name}_{str(self.eps)}"
        logger.info(f"Downloading {name} from {link}")
        urllib.request.urlretrieve(link, f"./eps/{name}.mp4")
        logger.info(f"Download finished")
    
    def getNext(self) -> str:
        driver = self.driver
        next_button = driver.find_element(By.XPATH, "//a[@id='proximoEPLink']")
        if next_button.get_attribute('href'):
            return next_button.get_attribute('href')
        else:
            return False



    # <a id="proximoEPLink" href="https://www.anitube.site/57124/" title="Dungeon Ni Deai Wo Motomeru No Wa Machigatteiru No Darou Ka? – Episódio 02 – Monsterphila – Festival De Monstro"><span>Próximo</span> <i class="icon-proximo"></i></a>
    # <a title="Sem Próximo Episódio" class="linkdisabled" id="proximoEPLink"><span>Próximo</span> <i class="icon-proximo"></i></a>
