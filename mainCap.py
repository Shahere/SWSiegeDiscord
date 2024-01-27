import asyncio
from concurrent.futures import CancelledError
from distutils.command.config import config
from getpass import getuser
from typing_extensions import Self
from unicodedata import name
from aiohttp import client
from discord.ext import commands
import discord
import random
from dotenv import load_dotenv
import os
import discord.utils
from interpreteurJSON import StatSiege
import datetime

botpret = ["Rise and Shine !", "je suis up", "Glad to see you", "Oh its morning ! wait...", "Sha stop me but im here", "Why you stop me ?"]
ldabuser = ["Number of nat5 in l'auberge : a lot", "Dark, kinki player :satan:","math à 100%", "En vrai sha t'es pas dans les stats", "Morgi t'abuse aussi", "Furious and Zemph be like : 5..na..nat ld ?", "LastNow with 4 5nat ld :swag:"]
strday = ["Lundi","Mardi","Mecredi","Jeudi","Vendredi","Samedi","Dimanche"]

load_dotenv(dotenv_path="config")

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

id_serv_six = 428608376172314635
id_serv_sha = 845691200970162186
id_serv_lamort = 703528473578438697

debug_six = ""

class BotSW(commands.Bot):
    react_good = False
    react_false = False
    inscription_message_id = 0
    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)


    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")
        channel = self.get_channel(1200788779301085265)
        nombre = random.randint(0,4)
        await channel.send(botpret[nombre])

    async def on_message(self, message):
        #print(message)
        print(message.content.lower())
        if(message.content.lower()=="ping"):
            await message.channel.send("pong")

#----------------------------------------------- INSCRIPTION GVO GVG COMMANDS ------------------------------------------------------------------------
        
        if(message.content.lower()==".register"):
            #message = await message.channel.send("reagissez à ce message si vous etes un bg")
            server = self.get_guild(id_serv_six)
            author = False
            #936330448685125633
            user = self.get_user(388390093871644682)
            id = message.author.id
            roles = message.author.roles
            for role in roles:
                if role.name == "Administrateurs":
                    author = True
            if id==388390093871644682:
                author= True
            
            if(author==True):  #si l'utilisateur a le role <defini>  
                message = await message.channel.send(" <@&(934428016736616499)>    !! Inscriptions Gvg et Gvo ! \n\n Celles et ceux voulant participer au contenu de guilde pour la semaine à venir, laissez une réaction sur ce message  \n\n Souvenez-vous que l'inscription rend le contenu obligatoire (sauf absence prévenue), pensez-y avant de vous inscrire \n \n(vous avez jusqu'à dimanche soir 21h pour les retardataires)")
                emoji = '\N{THUMBS UP SIGN}'
                await message.add_reaction(emoji)
                self.inscription_message_id = message.id
            else :
                faux = await message.channel.send("tu n'as pas accès à cette commande")

        if(message.content.lower()==".list"):
            server = self.get_guild(id_serv_six)
            channel = message.channel
            author = False
            #936330448685125633
            id = message.author.id
            roles = message.author.roles
            for role in roles:
                if role.name == "Administrateurs":
                    author = True
            if id==388390093871644682:
                author= True

            if(author==True):
                await message.channel.send("L'activation de cette commande affichera les personnes mais supprimera le role (usage unique), continuer ? (oui/non)")

                def check(m):
                    if(m.content == 'oui'):
                        self.react_good = True
                    else:
                        self.react_false = True
                    return message.content


                try:
                    msg = await self.wait_for('message', check=check, timeout=15)

                    if(self.react_false):
                        await message.channel.send("KeyBoardInterrupt")
                        self.react_false = False
                    if(self.react_good):
                        await message.channel.send("Membres inscrit cette semaine : ")
                        await self.getuser()
                        self.react_good = False

                except asyncio.exceptions.TimeoutError as t:
                    await message.channel.send("Trop de temps à repondre")
                    print("timeout")
                """except asyncio.exceptions.CancelledError as c:
                    await message.channel.send("KeyBoardInterrupt")"""

            else:
                faux = await message.channel.send("tu n'as pas accès à cette commande")

        if(message.content.lower()==".time"):
            str_day = datetime.datetime.today().weekday() +1
            now = datetime.datetime.now()
            if(str_day == 1 or str_day == 4):
                if(now.hour==12):
                    await message.channel.send("Its GVO time")
            await message.channel.send("{} {} {} {}".format(str_day, now.day, now.hour, now.minute))

#-------------------------------------------------- COMMANDE UNIQUEMENT FUN -----------------------------------------------------------------------
        
        if(message.content.lower()=="ta gueule"):
            await message.channel.send("euh ? non")
        
        if(message.content.startswith('Hey') or message.content.startswith('salut') or message.content.startswith('Yo') or message.content.startswith('Hello')):
            channel = message.channel
            await channel.send('Say hello!')

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await self.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))

        if(message.content.lower()=="ld abuser" or message.content.lower()=="ldabuser" or message.content.lower()=="ld absuer"):
            nombre = random.randint(0,len(ldabuser)-1)
            await message.channel.send(ldabuser[nombre])

        

#-------------------------------------------------------------- UTILITAIRE ------------------------------------------------------------------------
        
        if(message.content.startswith(".del")):
            id = message.author.id
            i = 0
            if(id!=388390093871644682):
                await message.channel.send("t'es pas autorisé à utiliser cette commande")
            else:
                number = int(message.content.split()[1])
                messages = await message.channel.history(limit=number+1).flatten()

                for each_message in messages:
                    await each_message.delete()
                    print("{}       {}".format(i, number))
                    i = i+1
            
        if(message.content.lower()=='.members'):
            guild = self.get_guild(id_serv_six)
            guild_number = guild.member_count
            await message.channel.send("il y a {} personnes dans le serv".format(guild_number))

        if(message.content.lower() == '.statsoffense'):
            stat = StatSiege()
            information = stat.stats()
            for i in range(len(information)):
                await message.channel.send(information[i])
                print(str(i)+"           "+(str(len(information)-1)))
                i = i+1
                if(i==3):
                    await message.channel.send("-------------------------------------------------------------------")
            await message.channel.send("-------------------------------------------------------------------")

        if(message.content.lower()=='.statsdefense'):
            stat = StatSiege()
            information = stat.statsDefense()
            for i in range(len(information)):
                await message.channel.send(information[i])
            await message.channel.send("-------------------------------------------------------------------")
    
#-----------------------------------------------------------------------------------------------------------------------------------------
#                                                   DEFINITION SYSTEM
#-----------------------------------------------------------------------------------------------------------------------------------------

    async def on_member_join(self, member):
        channel: discord.TextChannel = self.get_channel(845691201432322048)
        await channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")
       
    async def on_reaction_add(self, reaction, user):
        Channel = self.get_channel(845691201432322048)
       
        if reaction.emoji == "👍":
            Role = discord.utils.get(user.guild.roles, name="NextWeekGvoGvg")
            await user.add_roles(Role)

    async def on_reaction_remove(self, reaction, member):
        Channel = self.get_channel(845691201432322048)

        if reaction.emoji == '👍':
            zxc = discord.utils.get(member.guild.roles, name="NextWeekGvoGvg")
            await member.remove_roles(zxc)
        
    async def getuser(self,*args):
        server = self.get_guild(id_serv_six)
        for member in server.members:
            for role in member.roles: 
                
                if role.name == "NextWeekGvoGvg":
                    if(member.display_name != "BotInfo"):
                        #channel: discord.TextChannel = self.get_channel(568799090637537281) #debug channel
                        channel: discord.TextChannel = self.get_channel(936323623822696488) #inscrption-channel
                        await channel.send(content=f"{member.display_name}")
                        zxc = discord.utils.get(member.guild.roles, name="NextWeekGvoGvg")
                        await member.remove_roles(zxc)


#-----------------------------------------------------------------------------------------------------------------------------------------
#                                                   END CLASS
#-----------------------------------------------------------------------------------------------------------------------------------------

botsw = BotSW()
botsw.run(os.getenv("TOKEN"))
