import discord
from discord.ext import commands, tasks
import random

class Fun(commands.Cog):
    """weird commands for fun"""
    
    def __init__(self, bot):
        self.bot = bot

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Fun is working.')

    
    # Commands
    @commands.command()
    async def ping(self, ctx):
        """latency"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """the 8 ball command. """
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases = ['randomfact'])
    async def random_fact(self, ctx):
        """random fact. self explanatory"""
        responses2 = [
            "9+10=21.",
            "I like 21",
            "hello",
            "um...",
            "Algodoo should have an update.",
            "hi",
            "good job!"
        ]
        await ctx.send(f'{random.choice(responses2)}')
    
    @commands.command(aliases = ['dice'])
    async def roll_dice(self, ctx):
        """roll a dice from 1 to 6"""
        await ctx.send(f':game_die: {random.randint(1, 6)}')
    


    @commands.command(aliases = ['repeat'])
    async def copy(self, ctx, *, statement):
        """repeats what you say"""
        await ctx.send(statement)
    
    @commands.command(aliases = ['swap'])
    @commands.check_any(commands.is_owner())
    async def replace(self, ctx, *, statement):
        """replaces what you say"""
        await ctx.channel.purge(limit = 1)
        await ctx.send(statement)


    
def setup(bot):
    bot.add_cog(Fun(bot))
