from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def saishi(ctx):
    await ctx.send('ごみ')


@client.event
async def on_message(message): 
    if message.content == "おはよう":
        await client.send_message(message.channel, "Hello world!!")
client.run('NzY0NDAwNjE4ODE0ODMyNzAx.X4FtjQ.ViiKUux6rAl0XB3dm0v4muxyzsg')
    
    
    
    
    
bot.run(token)
