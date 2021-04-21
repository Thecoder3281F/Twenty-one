import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from pretty_help import PrettyHelp, Navigation

bot = commands.Bot(command_prefix = '21/', case_insensitive = True)
status = cycle(['Waiting for 21/help', 'Hi', '9+10=21', '''hi
hi''', "21"])


nav = Navigation(":arrow_up:")
color = discord.Color.dark_green()

bot.help_command = PrettyHelp(navigation=nav, color=color, active_time=10)


@bot.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(bot))


# Background Tasks

@tasks.loop(seconds = 10)
async def change_status():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(next(status)))


# Events

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')


# Extension related stuff
@bot.command()
@commands.check_any(commands.is_owner())
async def load(ctx, extension):
    """loads cogs"""
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.check_any(commands.is_owner())
async def unload(ctx, extension):
    """unloads cogs"""
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.check_any(commands.is_owner())
async def reload(ctx, extension):
    """reloads cogs"""
    bot.reload_extension(f'cogs.{extension}')


@bot.command()
@commands.is_owner()
async def logout(ctx):
    """logs off the bot"""
    global Off
    Off = discord.Embed(
        title = "Log out" ,
        description = "I am getting logged out. It's been a great time I spent with you. Sayonara!" ,
        color = 0xd8b9c3
    )
    await ctx.send(embed=Off)
    await bot.logout()


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify a cog to load.')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify a cog to unload.')

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify a cog to reload.')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# Run
bot.run(os.getenv('TOKEN')