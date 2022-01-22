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
    async def guess(self, ctx):
        """Guess the number. Work in progress, does not work properly now"""
        await ctx.send(f"I will now choose a number from 1 to 10 and you have to guess it. You have 3 lives.")
        number = random.randint(1, 10)
        loop = True
        lives = 3
        def check(m):
            if ctx.guild != None:
                if m.guild != None:
                    return m.author.id == ctx.author.id and ctx.channel.id == m.channel.id
            else:
                return m.author.id == ctx.author.id
        while loop == True and lives > 0:
            try:
                response = await self.bot.wait_for("message", timeout = 120, check = check)
            except asyncio.TimeoutError: # Once 120 seconds passes without a response
                  await ctx.send("TImed out because of no response")  
            else:
                try:
                    response = response.content
                    response = int(response)

                    if int(response) == number:
                        await ctx.send("Correct")
                        loop = False
                    elif int(response) > number:
                        await ctx.send("Too high!")
                        lives -= 1
                        await ctx.send(f"You have {lives} lives left")
                    elif int(response) < number:
                        await ctx.send("Too low!")
                        lives -= 1
                        await ctx.send(f"You have {lives} lives left")
                    elif int(response) < 1 or int(response) > 10:
                        await ctx.send("Out of range")
                        await ctx.send(f"You have {lives} lives left")
                except TypeError:
                    await ctx.send("Not a valid integer")
                    await ctx.send(f"You have {lives} lives left")
                except ValueError:
                    await ctx.send("Inappropriate argument value")
                    await ctx.send(f"You have {lives} lives left")
            

def setup(bot):
    bot.add_cog(Games(bot))