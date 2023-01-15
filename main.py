import cv2 as cv
import numpy as np
from mss import mss
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    bounding_box = {'top': 300, 'left': 200, 'width': 120, 'height': 100}
    sct = mss()
    template = cv.imread(r'cactus.png')
    template2 = cv.imread(r'cactus2.png')

    driver = webdriver.Chrome()
    driver.get("https://chromedino.com/")
    dino = driver.find_element(By.XPATH, "html/body")
    dino.send_keys(Keys.ARROW_UP)

    while True:
        sct_img = sct.grab(bounding_box)

        cv.imshow('Dino', np.array(sct_img))

        status = find_cactus(sct_img, template, template2)
        if status == 1:
            print("Ok")
            dino.send_keys(Keys.ARROW_UP)

        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break


def find_cactus(sct_img, template, template2):
    target = np.array(sct_img)
    target = cv.cvtColor(target, cv.COLOR_BGRA2BGR)

    res = cv.matchTemplate(template, target, cv.TM_CCOEFF_NORMED)
    res2 = cv.matchTemplate(template2, target, cv.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res >= threshold)
    loc2 = np.where(res2 >= threshold)

    for pt in zip(*loc[::-1]):
        return 1
    for pt in zip(*loc2[::-1]):
        return 1


if __name__ == '__main__':
    main()
