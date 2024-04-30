from random import random
import discord #import du module
from discord.ext import commands
#Intents 
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents) 
intents.message_content = True
# guilds = serveurs discords
intents.guilds = True
intents.members = True

jokes = [
    "Quelle est la différence entre un footballeur, un handballeur et un pédophile ?  Le footballeur marque du pied, le handballeur marque de la main, et le pédophile Marc Dutroux.",
    "Quelle partie du légume ne passe pas dans le mixer ?   La chaise roulante.",
    "Pourquoi les orphelins ne jouent-ils jamais au cache-cache ? Parce qu'ils ne trouvent jamais personne pour les chercher.",
    "Quelle est la différence entre Paul Walker et un ordinateur ?   Quand mon ordinateur se plante, ça me soûle."
]

ban ="nul"


# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
 print (f"{bot.user.name} s'est bien connecté !")

# Commande !ping
@bot.command()
async def ping(ctx):
    await ctx.send('pong 🏓')

# Commande !touché
@bot.command()
async def touché(ctx):
    await ctx.send('coulé ! ⛴️')

@bot.command()
async def membres(ctx):
  members_list = "\n".join([f"{member.display_name} - {', '.join([role.name for role in member.roles])}" for member in ctx.guild.members])
  await ctx.send(f"Liste des membres sur ce serveur :\n{members_list}")


@bot.event
async def on_message(message):
    # Vérifie si le message contient "bonjour" en tant que sous-chaîne
    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")



    #blague aléatoire
    if "joke" in message.content.lower():
     await message.channel.send(f"Je vais te raconter une blague")
     joke = random.choice(jokes)
     await message.channel.send(joke)



    await bot.process_commands(message)

# Commande !welcome pour envoyer le message de bienvenue
@bot.command()
async def welcome(ctx):
    await ctx.send(f"Bonjour à toi")

# Événement pour envoyer le message de bienvenue lorsque qu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    # Envoie du message de bienvenue dans le salon de bienvenue (vous pouvez changer l'ID du salon)
    welcome_channel = bot.get_channel(1234840617868197920)
    await welcome_channel.send(f"{member.mention}, Salut toi")



#connexion du bot au serveur avec au token
bot.run("TOKEN")