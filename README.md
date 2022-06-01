# alita-counter
A simple bot to counter Alita Discord's bot in a word chain game

# Motivation
In the past few days, I spent quite a lot of time playing a word chain game with friends using Alita bot on Discord. However, I often lose either to my friends or to the bot itself, due to a lack of vocabulary and a bad check mate strategy. Therefore, I created this bot called AlitaCounter. 

# How it works
- AlitaCounter uses 35,970 data from the Indonesian dictionary (KBBI) to enrich vocabulary
- AlitaCounter equipped with a continuously improved checkmate strategy (i.e. choosing words with endings that rarely become word prefixes). Hence, every time AlitaCounter loses because of checkmate, it will learn and apply the checkmate data into the next game.

# Tech
- Python 3
- Libraries: `discord.py` and `pandas`
- KBBI data from (kbbi-data-source)[https://github.com/misterabdul/kbbi-data-source]
