from bot import Bot
from decouple import config


bot = Bot("https://www.anitube.site/57110/",'Dungeon_ni_deai_Sword_Oratoria')
bot.Open()
bot.driver.close()
