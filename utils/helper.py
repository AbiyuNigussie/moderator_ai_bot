import discord


async def send_embed(ctx, title, description, color=0x3498DB):
    embed = discord.Embed(title=title, description=description, color=color)
    await ctx.send(embed=embed)
