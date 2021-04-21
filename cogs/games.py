import discord
from discord.ext import commands, tasks
import random
import asyncio
class Games(commands.Cog):
    """games here"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Games is working.')

    @commands.command()
    async def guess(self, ctx, a, b):
        """Guess the number. Work in progress, does not work now"""
        tries = 3
        await ctx.send(f"I will now choose a number from {a} to {b} and you have to guess it. You have 3 tries")
        number = random.randint(a, b)
        loop = True
        def check(m):
            if ctx.guild != None:
                if m.guild != None:
                    return m.author.id == ctx.author.id and ctx.channel.id == m.channel.id
            else:
                return m.author.id == ctx.author.id
        while loop == True:
            try:
                response = await self.bot.wait_for("message", timeout = 120, check = check)
            except asyncio.TimeoutError: # Once 120 seconds passes without a response
                    ...
            else:
                while tries > 0:
                    try:
                        response = response.content
                        response = int(response)
                        if int(response) > b:
                            await ctx.send(f"Higher than {b}")
                        elif int(response) == number:
                            await ctx.send("Correct")
                            loop = False
                        elif int(response) > number:
                            await ctx.send("Too high!")
                            tries -= 1
                            await ctx.send(f"You have {tries} left.")
                        elif int(response) < number:
                            await ctx.send("Too low!")
                            tries -= 1
                            await ctx.send(f"You have {tries} left.")
                    except ValueError:
                        await ctx.send("invalid number")
                await ctx.send(f"You ran out of guesses. The correct number is {number}.")

                

                
    

def setup(bot):
    bot.add_cog(Games(bot))