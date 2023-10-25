# Home Made Translator

#### Video Demo: <URL HERE>

#### Description: Translator with text to speech support for several lanugages

#### Background To Project

I pick my younger siblings from school. On the way back we usually meet a very pleasant Asian lady. However she only knows very little English. I wished i could somehow talk to her but i couldnt. I someday meet her and try to make small talk and manage to find out she is from Hong Kong and she speaks Cantonese. Few days later im inspired to make an English to Cantonese Translator.

#### The Project

This project could have been really easy and it is quite easy... but what i learnt to make it... though easy was quite voluminous.

A module in python called googletrans allows for easy translation of text for various languages. Now that i think about it i never checked if it supports cantonese but i went on Google Translate grinning just to translate some stuff to Cantonese for fun... alas my grin left, leaving dismay as i couldnt find Cantonese among the options. Both Chinese traditional and simplified are different from Cantonese.

Would i give up now... No, There has to be another way... I then turned Bing Translate.
Will they have Cantonese... and Cantonese they did have. Happy i now was.

Unfortunately i couldnt find any modules that allowed for easy connection to Microsoft translator... moreover their API was behind a paywall (rare Microsoft L)... but i was determined.

And then i had the brilliant idea... Scrape Bing Translate.

That was it... I quickly got to reviewing Selenium and formulating how to scrape Bing Translate (PS Microsoft dont sue me... Just hire me :))

I wont bore you further with my story of triumph... but i successfully was able to scrape bing translate and make this app in the process learning and working with the following:

- selenium - the real mvp - webscraping and browser automation

- pyautogui - for gui automation

- shelve - for storing binary data

- beautiful soup - also for webscraping

- pyperclip - working with the clipboard

- gtts - speaking translated text(NB: W module unfortunately didnt have a cantonese speaker so i had to scrape another website for cantonese speaking ))

- speechrecognition - recognizing speech

- playsound - playing sounds

- os - deleting created audio files

- inputimeout - waiting for input for a specified time (tried implementing this myself and reviewed multithreading with python but in the end i left it to the professionals ha)

and there we have it an arguably better translator than both bing translate and google translate

#### Usage

As of now this translator is incomplete. It runs on the command line and it is missing a few features.
It will be quite easy to add a GUI in the future, however i dont see the need as i dont plan on releasing this to the public.
To stop the application you need to press Ctrl-C... hear me out...
this app is supposed to mimic the flow of a real conversation, i speak, it translates then speaks translated , the other person speaks it translates and speaks translated text... hence i dont want to accept any conventional inputs as accepting inputs will halt the flow of the program so eg if i put some prompt for user to swap languages or to continue, until they answer the prompt nothing happens.

Over the course of the conversation this prompt will quickly become a nuisance... I then turned to multithreading so i then have a timed input. Idea is to have a slight window after each translation for a user to enter some command. If user doesnt enter the command then conversation continues else a menu can popup.
Will try to implement this in the future.

As for now im happy with what ive done. Im able to hold basic conversation with the pleasant lady and i dont need anymore than that, as we dont swap languages mid conversation.

Just enter the input language and output language and the conversation begins.
