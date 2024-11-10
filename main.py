from pyrogram import Client, filters
import os, sys
import art
def init(app):
    with open("colorize.py", "w") as f:
        f.write('''def colorize(text, na):
    if na == "gray":
    	d = 30
    if na == "red":
    	d = 31
    if na == "green":
    	d = 32
    if na == "help":
    	d = 7
    if na == "yellow":
    	d = 33
    if na == "blue":
    	d = 34
    if na == "pink":
    	d = 35
    if na == "aqua":
    	d = 36
    if na == "red_f":
    	d = 41
    if na == "yellow_f":
    	d = 43
    if na == "green_f":
    	d = 42
    if na == "blue_f":
    	d = 44
    if na == "white_f":
    	d = 47
    return f"\033[39;10;0;{d};1m{text}\033[0m"''')
    @app.on_message(filters.command('custom', prefixes = '.') & filters.me)
    def execj(client, message):
    	from art import text2art
    	text = message.text.split(' ', maxsplit  = 2)[1]
    	color = message.text.split(' ', maxsplit = 2)[2]
    	art = text2art(text)
    	with open("utils/terminal_effects.py", "w") as f:
    		f.write(f'''import os, time

from colorize import colorize

def on_start():

    os.system("clear")

    print(colorize(r'\''{art}''\', "{color}"))


    time.sleep(1)



    print(colorize('> {text} userbot was launched. {text} by Ladvix\\n\\n', "{color}"))''')
    	message.edit_text(f"Текст запуска успешно изменён!")
    @app.on_message(filters.command('k', prefixes = '.') & filters.me)
    def negri():
    	print('''1.gray
2.red
3.green
4.help
5.yellow
6.blue
7.pink
8.aqua
9.yellow_f
10.red_f
11.green_f
12.blue_f
13.white_f''')
