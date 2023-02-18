#!/usr/bin/env python3.10
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define the list of options
options = {
    'Ask Robin': ['Part A', 'Part B', 'Contact us']
}

description = {
    'Part A' : """Daily Scheduled Study

Every 3 Days (twice week) : Question Posting Sessions Updated For Each Exam on our private telegram group 

Notes pdf on the drive and updated iSense One Page Comprehensive Notes

Lectures ( on website redaharbyCourses.com )

Quizes for chapters & 
High yield mocks 
on  ( on website redaharbyCourses.com )

No need to subscribe to any online Q bank or buy any books 
We provide you with all the materials needed to pass 

iFiles ( 9 Specialty Files Selected by me from various books to enhance your paper 2 level )

24/7 Support For Any Question or Even Personal Queries From 10 Team Members 

In History This is 
The First MRCS Course 
Founded In 2017 

The Only Course That Provides Timed Simulated Mocks Accrording To The Exam Mark Distribution on A Website 

In Reality The Real Highest Scores As We Post FACEBOOK & Phone Number For Who Got Above 90% To Call Them For Us To Be Authentic

The Only Course Provided By A UK Registrar 3 Year Experience In The NHS

That is Why Little Bit More Expensive From Any Other Course In The Market

What is the Course duration?
4 Months from day one of your subscription till your exam date
How to book?
Go to https://redaharbycourses.com/subscribe/book-your-course-now/
and select 270 GBP And pay online""",
    'Part B' : """Our MRCS OSCE  History

UK Northampton February 2023

https://www.facebook.com/photo?fbid=560232589460010&set=a.197108449105761

Egypt Cairo February 2023

https://www.facebook.com/photo/?fbid=557284049754864&set=a.197108449105761
 
Dubai UAE 

https://m.facebook.com/story.php?story_fbid=pfbid02HjBBw56VYDvVn9t1Kydx4AK5DZFDj4YDCJj3pENtrgWb41uQrUURnuftuaDxga3yl&id=100008429049588

https://fb.watch/hkOpepyRdA/

Lahore Pakistan 

https://www.facebook.com/100064198205777/posts/495081389308464/?d=n

https://www.facebook.com/100064198205777/posts/493843419432261/?d=n

Hull UK
https://fb.watch/gZp_JhgBAg/
https://fb.watch/gZq3EVAZ0U/

Malaysia 
https://fb.watch/gZq1GE0sOW/

India Chennai 
https://fb.watch/fQ17O2FWiZ/
https://www.facebook.com/reel/466058112227236?fs=e&s=TIeQ9V

In Malaysia Kuala Lumpur 🇲🇾 
https://m.facebook.com/story.php?story_fbid=428348395981764&id=100064198205777
Also
https://m.facebook.com/story.php?story_fbid=428155106001093&id=100064198205777

Egypt 🇪🇬 Cairo
https://m.facebook.com/story.php?story_fbid=423573889792548&id=100064198205777

India 🇮🇳 Calicut 
https://m.facebook.com/story.php?story_fbid=399450332204904&id=100064198205777

Pakistan Islamabad May 2022 🇵🇰
https://www.facebook.com/100064198205777/posts/368078202008784/

London May 2022 🇬🇧 
https://fb.watch/d9obhhj7z3/

London February 2022 🇬🇧 
https://m.facebook.com/story.php?story_fbid=306340324849239&id=100064198205777

https://www.facebook.com/100064198205777/posts/305145184968753/

https://www.facebook.com/100064198205777/posts/364528925697045/

https://m.facebook.com/story.php?story_fbid=305145184968753&id=100064198205777

https://m.facebook.com/story.php?story_fbid=2930535270570746&id=100008429049588

Cairo 2022  🇪🇬 
https://www.facebook.com/photo?fbid=329863979163540&set=a.197108449105761

London 2021 🇬🇧 
https://fb.watch/bs7lGdCin8/

Manchester 2020 🇬🇧 
https://www.facebook.com/192474441340019/posts/574104916510301/

Cairo 2019 🇪🇬 
https://www.facebook.com/192474441340019/posts/549511102303016/

MRCS OSCE Course Feedback 

Thawwab
https://m.facebook.com/story.php?story_fbid=394170792732858&id=100064198205777

Fayyaz 
https://fb.watch/dXljXSQRJx/

Nida 
https://fb.watch/dN-iDgVnMm/

Sayed Nabil
https://www.facebook.com/MRCSCoursesbyRedaHarby/videos/389303049928426

Saha
https://www.facebook.com/MRCSCoursesbyRedaHarby/videos/707449536981420

Gouse 
https://fb.watch/dN-pfF4bfL/

Farhan Ahmed 
https://fb.watch/dN-jE1MRle/

Harris Siddique :
https://fb.watch/bUmM-R3_GL/

Gaurav Sali:
https://fb.watch/bUmNvZWNvh/

Mario Shokry
https://youtu.be/MlkJBWbt2yc

Joshua Gaetosmd
https://youtu.be/6MB-pQYHVms

Aneela Razzaq:
https://fb.watch/bUmPGgvkl6/

Christopher Nwatuzor:
https://fb.watch/bUmQ8ivBM8/

Saiteja:
https://fb.watch/d9oIS101YE/

Priya Raj:
https://fb.watch/bUmQCyJBnq/

Sreedutt Murali :
https://www.youtube.com/watch?v=xHzpYqOsdCo

Sabereen Huq :
https://fb.watch/bUmR0n9LaB/

Eleni :
https://youtu.be/

Priyank
https://youtu.be/IYHSOnXVQiw

Just For History Records 

First MRCS Course 
First MRCS Hands' On Course 
First MRCS QBANK Interactive Website Course 

First Hands' On Travelled By Himself To Calicut  
First Hands' On Travelled By Himself To London 5 Times 
First Hands' On Travelled By Himself To Chennai 
First Hands' On Travelled By Himself To Pakistan 
Islamabad 
First Hands' On Travelled By Himself To Pakistan 
Lahore 
First Hands' On Travelled By Himself To Manchester 
First Hands' On Travelled By Himself To Kuala Lumpur
What is the Course duration?
4 Months from day one of your subscription till your exam date
How to book?
Go to https://redaharbycourses.com/subscribe/book-your-course-now/
and select 290 GBP And pay online""",
    'Part C' : """Part B description""",
    'Part D' : """Part B description""",
    'Contact us' : """Please message me my telegram then: https://t.me/MrRedaHarby"""
}

# Define the start function
def start(update, context):
    # Create a list of InlineKeyboardButtons for each option
    keyboard = []
    for option in options:
        button = InlineKeyboardButton(option, callback_data=option)
        keyboard.append([button])
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send a message to the user with the option buttons
    update.message.reply_text('Hello let us:', reply_markup=reply_markup)

# Define the option function
def option_f(update, context):
    query = update.callback_query
    option = query.data
    sub_options = options[option]
    # Create a list of InlineKeyboardButtons for each sub-option
    keyboard = []
    for sub_option in sub_options:
        button = InlineKeyboardButton(sub_option, callback_data=sub_option)
        keyboard.append([button])
    # If there are sub-options, send a message to the user with the sub-option buttons
    if keyboard:
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=f' {option}:', reply_markup=reply_markup)
    # If there are no sub-options, send a message to the user indicating that there are no sub-options
    else:
        query.edit_message_text(text=f'There are no sub-options for {option}.')

# Define the sub_option function
def sub_option_f(update, context):
    query = update.callback_query
    sub_option = query.data
    # Send a message to the user with the selected sub-option
    query.edit_message_text(text=f'{description[sub_option]}')

# Create an updater and dispatcher for the bot
updater = Updater(token='6218495450:AAEpqMjShCsbhHq9yJ7Q1g-eM-POtVtoHz8', use_context=True)
dispatcher = updater.dispatcher
# Add handlers for the /start command and InlineKeyboardButton callbacks
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Add a CallbackQueryHandler for each option and sub-option
for option in options:
    dispatcher.add_handler(CallbackQueryHandler(option_f, pattern=option))
    sub_options = options[option]
    for sub_option in sub_options:
        dispatcher.add_handler(CallbackQueryHandler(sub_option_f, pattern=sub_option))

# Start the bot
updater.start_polling()
