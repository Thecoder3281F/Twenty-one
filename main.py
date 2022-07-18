import discord
import os
from discord.ext import commands, tasks
from itertools import cycle


class CustomHelpCommand(commands.HelpCommand):
    """A custom help command. More functionality will be added later"""

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send("```\n" + f"{cog.qualified_name}: {[command.name for command in mapping[cog]]}" + "```")
    
    async def send_cog_help(self, cog):
        await self.get_destination().send("```\n" + f"{cog.qualified_name}: {[command.name for command in cog.get_commands()]}" + "```")

    async def send_group_help(self, group):
        await self.get_destination().send("```\n" + f"{group.name}: {[command.name for index, command in enumerate(group.commands)]}" + "```")

    async def send_command_help(self, command):
        await self.get_destination().send("```\n" + command.name + "```")

    

bot = commands.Bot(command_prefix = '21/', case_insensitive = True, help_command=CustomHelpCommand())
status = cycle(['Waiting for 21/help', 'Hi', '9+10=21', '''hi
hi''', "21"])



# Ready function

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
@commands.is_owner()
async def load(ctx, extension):
    """loads cogs"""
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    """unloads cogs"""
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    """reloads cogs"""
    bot.reload_extension(f'cogs.{extension}')


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
bot.run('token')
