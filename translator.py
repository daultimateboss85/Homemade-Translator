from selenium import webdriver
import time
import pyperclip
from getTextFromSpeech import getTextFromSpeech
import pyttsx3
import shelve
from selenium.webdriver.edge.options import Options as EdgeOptions
import pyautogui as pag
from gtts import gTTS
from playsound import playsound
import os
from inputimeout import inputimeout, TimeoutOccurred

options = EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
languages = shelve.open("langs_data")["langs"]

def speakText(text):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def sub_main():
    # open browser
    browser = webdriver.Edge(options=options)
    window = pag.getWindowsWithTitle("data:, - Profile 1 - Microsoft\u200b Edge")[0]
    window.topleft = (-2000,-2000)

    browser.get(
        "https://www.bing.com/Translator?toWww=1&redig=215FFC5EB6154E628E9150DFE1C8EBCE"
    )
    # finding all elements i need once for efficiency

    # open other tab for speaking cantonese
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://www.eguidedog.net/ekho.php")
    time.sleep(2)
    # accept cookies :{
    cookies = browser.find_element("class name", "fc-button-label")
    cookies.click()

    # finding elements on cantonese speech page
    browser.execute_script("document.querySelector('#voice').selectedIndex = 1")

    speak_button = browser.find_element("id", "buttonSPR")
    cant_text = browser.find_element("id", "text")

    # slow down
    speed = browser.find_element("id", "speedDelta")
    speed.clear()
    speed.send_keys(-5)

    # switch back to translator
    browser.switch_to.window(browser.window_handles[0])

    # getting elements i need once for efficiency sake
    click_button = browser.find_element("id", "tta_copyIcon")
    in_text = browser.find_element("id", "tta_input_ta")
    reverse_button = browser.find_element("id", "tta_revIcon")
    time.sleep(2)

    # selecting languages to use in convo
    in_language = input("Input Language: ")
    out_language = input("Output Language: ")
    count = 0  # offestting index based on number of times used

    while True:
        # get speech
        text = getTextFromSpeech(in_language)

        # if count = 1 then add 1 to both sides else
        # need to strategize selection of options as they change depending on how many have been chosen previously
        if count == 0:
            # seleting language to translate from
            browser.execute_script(
                f"document.querySelector('#tta_srcsl').selectedIndex = {languages[in_language]['index'] + 1} "
            )

            # selecting language to translate to
            browser.execute_script(
                f"document.querySelector('#tta_tgtsl').selectedIndex = {languages[out_language]['index'] + 1} "
            )

        in_text.send_keys(text)
        time.sleep(1)

        # getting translated text
        try:
            click_button.click()
        except Exception as e:
            print(e)
            print("Error in program")
            time.sleep(10)

        time.sleep(1)
        translated_text = pyperclip.paste()

        # speak translated text
        print("Translated to", out_language, ":", translated_text)

        if out_language == "Cantonese (Traditional)":
            # swap to second tab
            browser.switch_to.window(browser.window_handles[1])

            if count in [2, 3]:
                browser.refresh()
                # finding elements on cantonese speech page
                browser.execute_script(
                    "document.querySelector('#voice').selectedIndex = 1"
                )

                speak_button = browser.find_element("id", "buttonSPR")
                cant_text = browser.find_element("id", "text")

                # slow down
                speed = browser.find_element("id", "speedDelta")
                speed.clear()
                speed.send_keys(-5)

            cant_text.clear()
            cant_text.send_keys(translated_text)
            time.sleep(1)

            try:
                speak_button.click()
                time.sleep(2)
            except:
                print("Error occured")

            browser.switch_to.window(browser.window_handles[0])

        else:
            tts = gTTS(translated_text, lang=languages[out_language]["value"])
            tts.save("output.mp3")
            time.sleep(1)
            playsound("output.mp3")
            os.unlink("output.mp3")
            # speakText(translated_text)

        # swap languages around so other user can speak
        in_language, out_language = out_language, in_language
        time.sleep(1)
        count += 1

        reverse_button.click()

        # once gotten translated text clear input
        in_text.clear()

def main():
    while True:
        returned = sub_main()
        if returned == "Swap":
            continue
        else:
            break

main()
