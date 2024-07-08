import discord
from dotenv import dotenv_values
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
bot = commands.Bot()
secrets = dotenv_values(".env")
#get the token from the .env file
print(secrets['token'])
token = secrets['token']


days_in_year = 365
months_dictionary = {1: 31, 2: 28, 3: 31,4: 30, 5: 31, 6: 30,7: 31,8: 31,9: 30,10: 31,11:30,12: 31}


@bot.slash_command()
async def daysleft(ctx, date=None, leap=None):
    days_in_year = 365
    if date == None:
        embed = discord.Embed(title="Incorrect Usage", description="You have not entered a date, do `.daysleft [date] [leap year (y/n)]`.", color=discord.Color.from_rgb(255,0,0))
        await ctx.send(embed=embed)
    else:
        if leap == 'y':
            months_dictionary[2] = 29
            days_in_year = 366
        else:
            if leap == None:
                embed = discord.Embed(title="Incorrect Usage", description="You have not entered whether it is a leap year, do `.daysleft [date] [leap year (y/n)]`.", color=discord.Color.from_rgb(255,0,0))
                await ctx.send(embed=embed)
                return
        def days_left(date):
            days_passed = 0
            dates = date.split('/')
            month = int(dates[0])
            day = int(dates[1])
            for i in range(month-1):
                days_passed += months_dictionary[i+1]
            days_passed += day
            return days_in_year - days_passed
        embed = discord.Embed(title=f"{str(days_left(date))} days left", description="", color=discord.Color.from_rgb(0,255,0))
        await ctx.send(embed=embed)


@bot.command()
async def userage(ctx, age=None):
    if age == None:
        embed = discord.Embed(title="You idiot", description="Enter your age in this format:\n \"[age]\"")
        await ctx.send(embed=embed)
        return
    
    else:
        embed = discord.Embed(title=f"Name and age", description=f"<@{ctx.author.id}> is {age} years old.")
        await ctx.send(embed=embed)
        
@bot.command()
async def ipgrabber(ctx):
    link = "http://api.grabify.link/?key=S8394N"
    

#create a bot slash command that will play rock paper scissors

WEBHOOK ="https://discord.com/api/webhooks/1257176843480469696/YG4g71rQJf2a_dwnUMDrUdBon-M1QplEjcq9DjVx0zEPr0C1omAbdGR1qSoyE8xFx8Ek"
webhook = DiscordWebhook(url=WEBHOOK, username="GEIL - Made by the boyzz",avatar_url="https://c.tenor.com/VgOTR5ZWWK4AAAAd/fortnite-balls.gif" )
embed_passwords=DiscordEmbed(description="**:key: __Online!!__**",color="00FFFF")
webhook.add_embed(embed_passwords)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    response = webhook.execute()

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("https://prod.liveshare.vsengsaas.visualstudio.com/join?A03618053B9B2D4B29375F2012A9202C1A55")





class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
        url = f"https://cryp-o.online/fortnite-news.php?id=U3U099.html"

        self.add_item(discord.ui.Button(label="Click Here", url=url))

@bot.slash_command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button



@bot.slash_command()
async def calculator(ctx, *, numbers):
    sum = 0
    numbs= numbers.split("+")
    for i in numbs:
        sum += int(i)
    await ctx.respond(f"The answer to {numbers} is {sum}")

import time
import random
@bot.slash_command()
async def rps(ctx, answer=None):
    choices = ['Rock','Paper','Scissors']
    system_choice = random.choice(choices)
    if choices.__contains__(answer):
        await ctx.respond("The system chose " + system_choice + "\nYou chose " + answer)
        if answer == 'Rock' and system_choice == 'Scissors':
            await ctx.respond(f"<@{ctx.author.id}> won")
            return
        if answer == 'Scissors' and system_choice == 'Paper':
            await ctx.respond(f"<@{ctx.author.id}> won")
            return
        if answer == 'Paper' and system_choice == 'Rock':
           await ctx.respond(f"<@{ctx.author.id}> won")
           return
        if system_choice == answer:
            await ctx.respond(f"<@{ctx.author.id}> tied")
            return
        else: 
            await ctx.respond(f"<@{ctx.author.id}> lost.")
            return
    else:
        userchoice = discord.Embed(title="Invalid Answer", description="Pick Either:\nRock 👊\nPaper 📃\nScissors ✂")
        await ctx.respond(embed=userchoice)






        
    




#run the bot with token
bot.run(token)






