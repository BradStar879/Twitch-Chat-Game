import os
import random
from twitchio.ext import commands
import paint
import time

approved_users = [os.environ['CHANNEL']]
waiting_users = {}

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NAME'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NAME']} is online!")
    with open('approvedusers', 'r') as f:
        content = f.readlines()
    names = [x.strip() for x in content]
    for name in names:
        approved_users.append(name)
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me is online!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NAME'].lower():
        return

    await bot.handle_commands(ctx)
    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower() or 'i love you' in ctx.content.lower():
        await ctx.send(f"Hi, @{ctx.author.name}!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


@bot.command(name='poop')
async def poop(ctx):
    if approved_user(ctx.author):
        await ctx.send('poopies')


@bot.command(name='dice')
async def dice(ctx):
    await ctx.send(random.randint(1, 3))


@bot.command(name='addapproveduser')
async def add_approved_user(ctx):
    if approved_user(ctx.author):
        user = ctx.content[17:]
        if ' ' not in user:
            approved_users.append(user)
            approved_users_file = open('approvedusers', 'a')
            approved_users_file.write(user + '\n')
            await ctx.send(user + ' approved!')
        else:
            await ctx.send(user + ' not a valid user!')


@bot.command(name='checkapprovedusers')
async def check_approved_users(ctx):
    if approved_user(ctx.author):
        await ctx.send(approved_users)


@bot.command(name='color')
async def color(ctx):
    if ctx.author.name not in waiting_users or int(round(time.time())) - waiting_users[ctx.author.name] >= 30:
        if paint.write_pixel(ctx.content):
            waiting_users[ctx.author.name] = int(round(time.time()))
            await ctx.send(ctx.author.name + ' pixel successful')


@bot.command(name='resetimage')
async def reset_image(ctx):
    if approved_user(ctx.author):
        paint.reset_image()


def approved_user(author):
    return author in approved_users


if __name__ == "__main__":
    bot.run()
