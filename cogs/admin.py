import discord
from discord.ext import commands, tasks

import asyncio

class Admin(commands.Cog):
    """admin commands here"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Admin is working.')

    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        """logs off the bot"""
        global Off
        Off = discord.Embed(
            title = "Log out" ,
            description = "I am getting logged out. It's been a great time I spent with you." ,
            color = 0xd8b9c3
        )
        await ctx.send(embed=Off)
        await self.bot.close()

    @commands.command()
    @commands.is_owner()
    async def direct_message_test(ctx, user: discord.User):
        await user.send('hello')


def setup(bot):
    bot.add_cog(Admin(bot))