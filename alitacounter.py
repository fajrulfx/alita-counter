import discord
import requests
import pandas as pd
import time

bot_token = 'XXX'
data = pd.read_csv('https://gist.githubusercontent.com/fajrulfx/f48e4ed8c0157f995154b4baca49242c/raw/6057177971b1396867deaad19824fac3690e265e/kbbi_clean.csv')
database = data['kata'].tolist()

skaklist = pd.read_csv('skak.csv')['kata'].tolist()

def add_skak_database(word):
    if word in skaklist:
        pass
    else:
        if word != 'undefined':
            skaklist.append(word)
            pd.DataFrame(skaklist, columns=['kata']).to_csv('skak.csv', index=False)

def database_check(kata, used=[''], addskak=True):
    try:
        database_select = []
        database_skak = []
        for word in database:
            word = str(word)
            if word.startswith(kata) == True:
                database_select.append(word)
        for word in used:
            if word in database_select:
                database_select.remove(word)

        for word in database_select:
            if word.endswith(skak) == True:
                database_skak.append(word)

        if len(database_skak) != 0:
            database_select = database_skak       

        if len(database_select) != 0:
            return max(database_select, key=len)
        else:
            if addskak == True:
                add_skak_database(kata)
            return 'roll'

    except:
        if addskak == True:
            add_skak_database(kata)
        return 'roll'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global skak
        global kata
        global jawab
        global used_word
        global name_now
        global name_old

        name_now = message.author.id

        if message.author == self.user:
            return

        if message.author.id == int(590047618479030272):
            try:
                embed = message.embeds[0].to_dict() 
                cek = embed['fields'][0]['value']
                indeks = cek.index("<@981332425831481354>") - 24
                if cek[indeks] == 'd':
                    teks = embed['footer']['text']
                    end = teks.index("|") - 2
                    kata = teks[30:end]
                    jawab = database_check(kata, used_word)
                    used_word.append(jawab)
                    time.sleep(3)
                    await message.channel.send(jawab)
            except:
                pass

        if message.content == '!counter':
            used_word = []
            skaklist = pd.read_csv('skak.csv')['kata'].tolist()
            skak = tuple(skaklist)
            await message.channel.send('join')

        if message.content == 'Kata sudah digunakan..': 
            used_word.append(jawab)
            jawab = database_check(kata, used_word, addskak=False)
            time.sleep(2)
            await message.channel.send(jawab)
        
        if message.content == 'Roll point sudah habis!' and name_old == int(981332425831481354):
            await message.channel.send('giveup')



        name_old = name_now

client = MyClient()
client.run(bot_token)
