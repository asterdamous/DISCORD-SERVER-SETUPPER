import os
import asyncio
import discord
from discord.ext import commands
from colorama import init, Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
========================================
   DISCORD SERVER SETUPPER BY ASTERDAMOUS
========================================
""" + Style.RESET_ALL)

bot_token   = input(Fore.YELLOW + "What is the bot token? " + Style.RESET_ALL)
owner_id    = int(input(Fore.YELLOW + "What is the owner's ID? " + Style.RESET_ALL))
server_name = input(Fore.YELLOW + "What should be the new server name? " + Style.RESET_ALL)
add_welcome = input(Fore.YELLOW + "Generate Welcome category? (y/n) " + Style.RESET_ALL).strip().lower() == "y"

print(Fore.MAGENTA + "\nPlease wait… starting bot…\n" + Style.RESET_ALL)

intents = discord.Intents.default()
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def setup_guild(guild):
    print(Fore.CYAN + f"Setting up guild: {guild.name} (ID: {guild.id})" + Style.RESET_ALL)
    await guild.edit(name=server_name)

    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(Fore.GREEN + f"Deleted channel: {channel.name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to delete channel {channel.name}: {e}" + Style.RESET_ALL)

    C = discord.Colour
    role_data = [
        ("Owner",          C.red()),
        ("Administrator",  C.blue()),
        ("Moderator",      C.green()),
        ("Top Hangouters", C.purple()),
        ("Members",        C.from_rgb(135, 206, 235)),
    ]
    for name, colour in role_data:
        await guild.create_role(name=name, colour=colour)
        print(Fore.GREEN + f"Created role: {name}" + Style.RESET_ALL)

    main_cat = await guild.create_category("Main")
    await guild.create_text_channel("announcement", category=main_cat)
    await guild.create_text_channel("rules", category=main_cat)
    await guild.create_text_channel("desk", category=main_cat)

    world_cat = await guild.create_category("World")
    await guild.create_text_channel("chat", category=world_cat)
    await guild.create_text_channel("bot-cmds", category=world_cat)
    await guild.create_text_channel("socials", category=world_cat)

    mem_cat = await guild.create_category("Memories")
    await guild.create_text_channel("gallery", category=mem_cat)
    await guild.create_text_channel("selfies", category=mem_cat)
    await guild.create_text_channel("arts", category=mem_cat)

    hang_cat = await guild.create_category("Voice-Hangouts")
    for i in range(1, 4):
        await guild.create_voice_channel(f"VC {i}", category=hang_cat)

    if add_welcome:
        welcome_cat = await guild.create_category("Welcome")
        await guild.create_text_channel("verify", category=welcome_cat)
        print(Fore.GREEN + "Created Welcome category with verify channel" + Style.RESET_ALL)

    with open("result.txt", "w") as f:
        f.write(f"Bot Token: {bot_token}\n")
        f.write(f"Owner ID: {owner_id}\n")
        f.write(f"Server Name: {server_name}\n")
        f.write(f"Welcome Category Added: {'Yes' if add_welcome else 'No'}\n")
        f.write(f"Guild ID: {guild.id}\n")
        f.write(f"Guild Name: {guild.name}\n")

    print(Fore.CYAN + "Setup complete, writing results to result.txt" + Style.RESET_ALL)

    await guild.leave()
    print(Fore.MAGENTA + f"Bot has left guild: {guild.name}" + Style.RESET_ALL)
    print(Fore.YELLOW + "\nSetup Done! Exiting terminal..." + Style.RESET_ALL)
    os._exit(0)

@bot.event
async def on_ready():
    print(Fore.GREEN + f"Logged in as {bot.user}\n" + Style.RESET_ALL)

    if bot.guilds:
        print(Fore.RED + "Warning: Bot is already in some servers. Setup will only run on new server joins." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Waiting for the bot to be added to your server..." + Style.RESET_ALL)


@bot.event
async def on_guild_join(guild):
    print(Fore.CYAN + f"Bot added to new guild: {guild.name} (ID: {guild.id})" + Style.RESET_ALL)
    await setup_guild(guild)

bot.run(bot_token)
