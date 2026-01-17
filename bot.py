import discord
from discord.ext import commands
import asyncio
from config import DISCORD_TOKEN, EMBED_COLOR

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{'='*50}")
    print(f"Bot conectado como {bot.user}")
    print(f"ID: {bot.user.id}")
    print(f"Servidores: {len(bot.guilds)}")
    print(f"{'='*50}")
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="LHUB | /ajuda"
        )
    )
    
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos slash")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

@bot.event
async def on_guild_join(guild):
    print(f"Bot adicionado ao servidor: {guild.name} ({guild.id})")

@bot.event
async def on_guild_remove(guild):
    print(f"Bot removido do servidor: {guild.name} ({guild.id})")

async def load_cogs():
    cogs = ["cogs.commands", "cogs.admin"]
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"Cog carregado: {cog}")
        except Exception as e:
            print(f"Erro ao carregar {cog}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
