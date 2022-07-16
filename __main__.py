from bot import Bot
from decouple import config


bot = Bot("https://www.anitube.site/57123/",'Dungeon_ni_deai')
bot.Open()
bot.driver.close()
bot = Bot("https://www.anitube.site/880485/",'Dungeon_ni_deai_2')
bot.Open()
bot.driver.close()
bot = Bot("https://www.anitube.site/897372/",'Dungeon_ni_deai_3')
bot.Open()
bot.driver.close()
bot = Bot("https://www.anitube.site/57110/",'Dungeon_ni_deai_Sword_Oratoria')
bot.Open()
bot.driver.close()
