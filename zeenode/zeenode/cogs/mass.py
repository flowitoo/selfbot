import discord, pyfiglet
from discord.ext import commands as zeenode 

class mass(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

        
    @zeenode.command()
    async def massreact(self, ctx, emote):
        await ctx.message.delete()
        messages = await ctx.message.channel.history(limit=20).flatten()
        for message in messages:
            await message.add_reaction(emote)

def setup(bot):
    bot.add_cog(mass(bot))
