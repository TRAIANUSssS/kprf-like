import time
import traceback
import os

from Selenium.ConnectToURL import connect
from Selenium.findElementByXpathToSelenium import search
from Selenium.SeleniumClick import click
from Selenium.StartSelenium import create_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KPRF_Parser(object):
    def __init__(self, port, headless):
        self.count = 0
        self.errors = 0
        self.port = port
        self.headless = headless
        self.start_time = time.time()

        self.create_drivers()

    def create_drivers(self):
        print("Started!")
        while True:
            try:
                self.driver = create_driver(headless=headless, port=self.port)
                self.pars_page()
            except:
                self.errors += 1
                print(traceback.format_exc())
            finally:
                try:
                    self.driver.close()
                    self.driver.quit()
                except:
                    time.sleep(10)
                time.sleep(1)
                self.print_stat()

    def pars_page(self):
        connect("https://www.spb.kp.ru/media/933494/?participant=648f40cc627b2d0007bb0641", self.driver, delay=0,
                _print=False)

        like_button = self.get_like_button()

        if like_button is not None:
            click(self.driver, like_button)
            time.sleep(0.3)
            if self.get_like_button().get_attribute("data-is-voted") == "true":
                self.count += 1

    def get_like_button(self):
        try:
            like_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class = 'sc-17zudeo-1 ixAGFv']//div[@data-is-voted]")))
        except:
            self.errors += 1
            like_button = None
        finally:
            return like_button

    def print_stat(self):
        total_time = round(time.time() - self.start_time, 2)
        if self.count != 0:
            avg = round(total_time / self.count, 2)
        else:
            avg = 0

        print(f"\rLike count: {self.count}, total time: {total_time}, avg time: {avg}, errors: {self.errors}", end='')


if __name__ == "__main__":
    try:
        headless = input("Turn ON headless mode? y/n ")
        port = input("write port: ")
        _class = KPRF_Parser(port, headless == "y")
    except:
        print(traceback.format_exc())
    finally:
        a = input("end?")
