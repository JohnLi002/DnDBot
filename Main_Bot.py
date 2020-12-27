#Bot
import discord as ds, random
from discord.ext import commands

#This program is where all the commands will activate in


bot = commands.Bot(command_prefix='!')

class MyClient(ds.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


@bot.command()
async def multiRoll(ctx, num, dice):
    rolls = []
    totalResult = 0
    count = 0
    while(count < dice):
        result = random.randint(1, num)
        totalResult += result
        rolls.append(result)
        count += 1
    
    formatRoll = 'You have rolled '
    if(len(rolls) == 1):
        formatRoll += '1 die. \nRoll = {'
    elif(len(rolls) == 0):
        formatRoll += 'NOTHING!'
    else:
        formatRoll += str(len(rolls)) + " dice. \nRolls = {"
    for r in rolls:
        formatRoll += str(r)
        if count != 1:
            formatRoll += ', '
        count -= 1
    formatRoll += "}"

    ctx.send(formatRoll)

client = MyClient()
client.run('token')
