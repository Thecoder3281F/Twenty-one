import discord
from discord.ext import commands, tasks
import asyncio

class Moderation(commands.Cog):
    """Obviously in progress"""
    def __init__(self, bot):
        self.bot = bot

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ['s', 'm']:
                return (int(amount), unit)
                
            raise commands.BadArgument(message='Not a valid duration.')


       
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Moderation is working.')
    
    @commands.command()
    @commands.is_owner()
    async def kick(self, ctx, member : commands.MemberConverter):
        """self explanatory. Mention member"""
        await ctx.guild.kick(member)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.is_owner()
    async def ban(self, ctx, member : commands.MemberConverter):
        """self explanatory. Mention member"""
        await ctx.guild.ban(member)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.is_owner()
    async def temp_ban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(f'Banned {member} for {amount}{unit}')
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @commands.command()
    @commands.is_owner()
    async def unban(self, ctx, *, member):
        """self explanatory. Type member's user and discriminator"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


def setup(bot):
    bot.add_cog(Moderation(bot))