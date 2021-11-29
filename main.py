import discord 
from discord.ext import commands
import random

client = commands.Bot('>')

@client.event 
async def on_ready():
  print("Bot Is Ready")
  
@client.command()
async def rps(ctx, message):
  answer = message.lower()
  choices = ["rock", "paper", "scissors"]
  computers_answer = random.choice(choices)
  if answer not in choices:
    await ctx.send("That Is Not An Option!  Here are the options : rock, paper, scissors")
  else: 
   if computers_answer == answer:
      await ctx.send(f"Its An Tie You Picked {answer} And I Picked {answer}")
   if computers_answer == "rock": 
    if answer == "paper": 
      await ctx.send(f"{computers_answer}!  You Win! 🎉")
      
   if computers_answer == "paper": 
    if answer == "scissors": 
      await ctx.send(f"{computers_answer}!  You Win! 🎉")
      
   if computers_answer == "scissors": 
    if answer == "rock": 
      await ctx.send(f"{computers_answer}!  You Win! 🎉")  
      
   if computers_answer == "paper": 
    if answer == "rock": 
      await ctx.send(f"{computers_answer}!  You Lost😞")
      
   if computers_answer == "rock": 
    if answer == "scissors": 
      await ctx.send(f"{computers_answer}!  You Lost😞")
      
   if computers_answer == "scissors": 
      if answer == "paper": 
        await ctx.send(f"{computers_answer}!  You Lost😞")
        
client.run('TOKEN')      
