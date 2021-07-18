import os
import time
from pathlib import Path

from fake_useragent import UserAgent

from settings import Settings
from storage import Storage
from user_account import User_accout

settings = Settings('settings.json')
dir_path = Path(os.curdir, 'data')
store = Storage('user.db')
login = settings['login']
password = settings['password']
user_agent = UserAgent().random

try:
    user_agent = store[login + '_user_agent']
except:
    store[login + '_user_agent'] = user_agent
    store.commit()

user_acc = User_accout(login, password, user_agent)
user_acc.auth_and_set_cookies()

if not os.path.exists(dir_path):
    os.mkdir(Path(os.curdir, 'data'))

time.sleep(3)
passport_data = user_acc.get_passport_data()
passport_file = open(Path(dir_path, 'passport.txt'), "w")

print(passport_data)
passport_file.write(passport_data)
