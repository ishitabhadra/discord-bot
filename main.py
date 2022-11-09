import discord
import random
import asyncio
import requests
import json
import os
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!ishita', intents=intents)
@bot.event
async def on_connect():
  print("Your bot is online")


@bot.command()
#name
async def Name(ctx,name):
  await ctx.reply("hello " + name)

@bot.command()
#add
async def Add(ctx, number1, number2):
   sum = int(number1) + int(number2)
   await ctx.reply(str(number1) + " + " + str(number2) + " = " + str(sum))
   #await ctx.reply(sum)

@bot.command()
#random dog from list
async def Dog(ctx):
  doglist = ["https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/chow-chow-portrait-royalty-free-image-1652926953.jpg?crop=0.44455xw:1xh;center,top&resize=980:*","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/shih-tzu-little-dog-royalty-free-image-1652927214.jpg?crop=0.447xw:1.00xh;0.248xw,0&resize=980:*","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/happy-dog-outdoors-royalty-free-image-1652927740.jpg?crop=0.447xw:1.00xh;0.187xw,0&resize=980:*","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/lonely-pug-royalty-free-image-1652974264.jpg?crop=0.447xw:1.00xh;0.355xw,0&resize=980:*","https://media.giphy.com/media/cjbxJXhNXDMjhlr1S8/giphy.gif","https://media4.giphy.com/media/3ndAvMC5LFPNMCzq7m/giphy-downsized-large.gif","https://thumbs.gfycat.com/NaughtyPoliteGrosbeak-max-1mb.gif","https://media1.giphy.com/media/l4FGI8GoTL7N4DsyI/giphy.gif"]
  
  await ctx.reply(random.choice(doglist))

@bot.command(aliases = ["8ball","8Ball","eightball"])
#8ball
async def EightBall(ctx,*, phrase:str):
  responselist = ["As I see it, yes.", "Ask again later.", "Better not tell you now.","Concentrate and ask again.","Don’t count on it.","It is certain.", "It is decidedly so.","Most likely.", "My reply is no.", "My sources say no.","Outlook not so good.", "Outlook good.","Yes – definitely.", "You may rely on it."]
  
  await ctx.reply(("**"+phrase+"**") + "?: " + (random.choice(responselist)))



@bot.command(aliases = ["rps"])
#rockpaperscissors
async def Rps(ctx, rps):
  rpslist = ["rock","paper","scissors"]
  
  x = random.choice(rpslist)

  if x=="rock":
    if rps=="rock":
      await ctx.reply("Tie 👔 ! You chose " + rps + " and bot chose " + x)
    elif rps=="paper":
      await ctx.reply("You win 😊 ! You chose " + rps + " and bot chose " + x)
    elif rps=="scissors":
      await ctx.reply("You lose 😥 ! You chose " + rps + " and bot chose " + x)

  if x=="paper":
    if rps=="paper":
      await ctx.reply("Tie 👔 ! You chose " + rps + " and bot chose " + x)
    elif rps=="scissors":
      await ctx.reply("You win 😊 ! You chose " + rps + " and bot chose " + x)
    elif rps=="rock":
      await ctx.reply("You lose 😥 ! You chose " + rps + " and bot chose " + x)
      
  if x=="scissors":
    if rps=="scissors":
      await ctx.reply("Tie 👔 ! You chose " + rps + " and bot chose " + x)
    elif rps=="rock":
      await ctx.reply("You win 😊 ! You chose " + rps + " and bot chose " + x)
    elif rps=="paper":
      await ctx.reply("You lose 😥 ! You chose " + rps + " and bot chose " + x)
      
@bot.command(aliases = ["time"])
#does not work with 10-12s yet
async def Time(ctx, *, time):
  #await ctx.reply(time)
  t = time[2:4]
  x = time[0:2]
  x = int(x)
  #await ctx.reply(t)
  if len(time)==4:
    if t=="pm":
      if 0<x<6 or x==12:
        await ctx.reply("good afternoon 🌆")
      elif 5<x<12:
        await ctx.reply("good evening ⋆⁺₊⋆ ☾ ⋆⁺₊⋆ ☁︎ ")
    if t=="am":
      await ctx.reply("good morning 𖤓")
  else:
    t = time[3:5]
    x = time[0:3]
    x = int(x)
    if t=="pm":
      if x==12:
        await ctx.reply("good afternoon 🌆")
      else:
        await ctx.reply("good night ⋆⁺₊⋆ ☾⋆⁺₊⋆")
    else:
      if x==12:
        await ctx.reply("good night ⋆⁺₊⋆ ☾⋆⁺₊⋆")
      else:
        await ctx.reply("good morning ☀️")

@bot.command()
async def Help(ctx):
  embed = discord.Embed(title="Commands list", color = 0xFF5733)
  embed.set_thumbnail(url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=640:*")

  embed.add_field(name="!ishitaName", value="Replies with hello and your name", inline=False)

  embed.add_field(name="!ishitaAdd", value="Adds two numbers", inline=False)

  embed.add_field(name="!ishitaDog", value="Sends a random image of a dog", inline=False)

  embed.add_field(name="!ishita8ball", value="Ask the Magic 8 Ball a question", inline=False)

  embed.add_field(name="!ishitaRps", value="Play rock, paper, scissors with the bot", inline=False)

  embed.add_field(name="!ishitaTime", value="Replies with good morning, afternoon, evening, or night", inline=False)

  embed.add_field(name="!ishitaJoke", value="Replies with a joke", inline=False)

  embed.add_field(name="!ishitaWeather", value="Using a zipcode, the bot replies with the weather info", inline=False)

  embed.add_field(name="!ishitaGeoIP", value="Enter a valid IP address and bot replies with location and currency name", inline=False)

  embed.add_field(name="!ishitaDictionary", value="Replies with the definition of the word using the Merriam-Webster API", inline=False)

  

  await ctx.send(embed=embed)
  

#use a joke API to get a joke setup, wait a few seconds
#and deliver the punchline
@bot.command()
async def Joke(ctx):
  url = "https://official-joke-api.appspot.com/random_joke"
  req = requests.get(url)
  #data variable that holds the json data that the api holds
  data = req.json()
  #pull the joke setup from json data
  setup = data["setup"]
  punchline = data["punchline"]
  
  #await ctx.send(setup +"\n" + punchline)
  await ctx.send(setup)
  #import asyncio
  await asyncio.sleep(1)
  await ctx.send(punchline)

@bot.command()
async def Weather(ctx, zip):
  my_secret_weather = os.environ['WeatherAPIKey']
  
  url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip+",us&appid="+ my_secret_weather
  my_secret_weather = os.environ['WeatherAPIKey']
  req = requests.get(url)
  #data variable that holds the json data that the api holds
  data = req.json()

  d = data["weather"][0]["description"]
  a = data["name"]
  w = data["main"]["temp"]
  w = int(w)


  f = (1.8*(w-273.15))+32
  f = str(f)
  f = f[0:4]

  d = str(d)
  x = len(d)
  g = d[1:x]
  
  z = d[0:1]
  
  await ctx.send(z.upper() + g + " outside in " + a + " and " + f + " °F")
  
@bot.command()
async def GeoIP(ctx, ip):
  my_secret = os.environ['my_secret_ip']
  url = "https://api.ipbase.com/v2/info?apikey="+ my_secret + "&ip=" + ip
  req = requests.get(url)
  data = req.json()
  #https://api.ipbase.com/v2/info?apikey=Vk1zEUhrLULUT8r5qlTkLfkzwzrTF3OL3UdNGQJ3&ip=53.81.187.48

  city = data["data"]["location"]["city"]["name"]
  continent = data["data"]["location"]["continent"]["name"]
  country = data["data"]["location"]["country"]["name"]
  currency = data["data"]["location"]["country"]["currencies"][0]["name"]
  symbol = data["data"]["location"]["country"]["currencies"][0]["symbol"]

  await ctx.send("This is at " + city + ", " + country+ ", " + continent)
  await ctx.send("Currency: " + currency + " " + symbol)
  # await ctx.send(city)
  # await ctx.send(continent)
  # await ctx.send(country)

  #https://ipbase.com/
  
  
@bot.command()
async def Dictionary(ctx, word):
  dictionary_api = os.environ['dictionary_api']
  #dictionary api key - 0e58677e-ba64-4ef6-be7c-583d1c26e764
  url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + dictionary_api
  
  req = requests.get(url)
  data = req.json()

  w = data[0]["shortdef"][0]

  await ctx.send(w)


  
  #https://plainenglish.io/blog/send-an-embed-with-a-discord-bot-in-python - for embed 

my_secret = os.environ['TOKEN']
bot.run(my_secret)
#MTAzNDIyMTcyMjA1ODEwNDg0Mw.G0QJmA.MW8BtZpt65cw40zJGjhyhoMuxumC3LGsWUQ1Hs - token

