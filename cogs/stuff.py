import discord
from discord.ext import commands, tasks 

class Stuff(commands.Cog):
    """random things"""
    def __init__(self, bot):
        self.bot = bot


       
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Stuff is working.')
    
    
    @commands.command()
    async def test(self, ctx):
        """a redundant command"""
        await ctx.send('test')

    @commands.command()
    async def clear(self, ctx, amount = 2):
        """clears messages(should be in moderation but who cares)"""
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    async def credits(self, ctx):
        """look yourself"""
        await ctx.send('`Created by Thecoder3281f#6650 under the guidance of Lucas#6947\'s videos`')

    @commands.command(aliases = ['invite'])
    async def invite_me(self, ctx):
        """this the invite link"""
        await ctx.send('Use this link to invite me to your server: https://discord.com/api/oauth2/authorize?bot_id=707412967708426251&permissions=8&scope=bot')

    @commands.command()
    async def suggestion(self, ctx,*, text):
        """Work in progress"""
        await ctx.send('Suggestion is pending.')
        suggestions = open(r"Suggestions.txt", "a")
        suggestions.write('\n')
        suggestions.write(text)
        suggestions.close()

    @commands.command(aliases = ['github'])
    async def my_github(self, ctx):
        """self explanatory"""
        await ctx.send('Here is the github for this bot. `https://github.com/Thecoder3281F/testing`')

    @commands.command(aliases = ['featured'])
    async def featured_people(self, ctx):
        """look"""
        await ctx.send('This is a very good bot: `https://github.com/The-Codin-Hole/HotWired-Bot`')

    @commands.command()
    async def faqs(self, ctx):
        """Frequently asked questions"""
        await ctx.send('''
        I am made in Python. 
        I am made by Thecoder3281f#6650.
        Hello!
        9+10=21
        ''')



def setup(bot):
    bot.add_cog(Stuff(bot))