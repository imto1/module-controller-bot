#!/usr/bin/python3
import time
import logging
import datetime
import subprocess
import os
import urllib
import json
import requests


#initializing log
now = datetime.datetime.now()
logging.basicConfig(filename=("log/" + str(now.year) + str(now.month) + str(now.day) + ".log"),
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


#global variables
TOKEN = "970592554:AAFMNLvMAShUMgjcw_XbKsN3ozI9psrEVAQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
AUTHORIZED = {
    "test" : "12345678"
    }
ROOT = ()
NA = ()
username = ""
password = ""
loged_in = False

#API handlers
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset) 
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates -1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)


def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            Chat = update["message"]["chat"]
            if text == "/start":
                start_bot(Chat)
            elif text.startswith("$"):
                command = text.substing(1)
                internal_command(command, chat)
            else:
                pass
        except KeyError:
            pass


#events
def terminal(command):
    if command in NA:
        return "'{}' is not supported!".format(command)
    elif command in ROOT and login-check() == False:
        return "Unauthorized access! Please login first!"
    else:
        return excecute(command)


def excecute(command):
    try:
        if command == "password":
            args = command.split("=")
            if args[1] in ACCOUNTS:
                return "Insert your password:\nHint: $passwd=password"
            else:
                return "Login failed!"
        else:
            output = subprocess.run(command, stdout=subprocess.PIPE)
            return output.stdout.decode("utf-8")
    except Exception as e:
        print(e)
        return str(e)


def start_bot(chat):
	user = chat["username"]
	name = chat["first_name"]
	send_message("Welcome {}!\nIOT module controller for {}.".format(name, user), chat)
    #login(chat)

    
def internal_command(command, chat):
    out = "`"
    out += terminal(text)
    out += "`"
    send_message(out, chat)


def login():
    send_message("**Login:**\n`Hint: $user=username`", chat)


#main
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
