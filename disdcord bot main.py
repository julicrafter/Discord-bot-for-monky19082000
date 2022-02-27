
from collections import UserString
import random # for the joke (random.choice) Function
import discord #for discord
import time # for the sleep and wait fuctions
import json #to storage for lvl bot the user data
import os # to say where the .json files are stored 


from discord.ext import commands #for command
from discord.ext import tasks #for chanching presence in background automactical
from itertools import cycle # for cycle fuction is tasks.loop


intents = discord.Intents.all()
discord.member = True                                                                
client = commands.Bot(command_prefix = "!",intents = intents) # client for the whole shit
status = cycle(["!help für alle commands" , "hilft dir" , "wird gefangen gehalten" , "!Twitch" , "!määh"]) # status cycle 
os.chdir(r'C:\Users\justus\Documents\Dokumente\vsc\dc bot für monky') # os show where the bot folder is

#infos
@client.command(aliases = [ "infos" , "Info", "info"] )
async def Infos(context):    

    myembed = discord.Embed(title="Current Version" , description="The bot is in V1.2", color=0x1B84CA)
    myembed.add_field(name="Version Code:" , value="V1.2.0" , inline=False)
    myembed.add_field(name = "Date Released:", value="05.02.2022", inline=False)
    myembed.add_field(name="Last Update Released" , value="12.02.2022" , inline=False)
    myembed.set_footer(text="Bot Codet by juli_crafter#8905")
    myembed.set_author(name="juli_crafter#8905")
    
    await context.message.channel.send(embed=myembed)
    
#Help
@client.command(aliases = ["Help" , "Hilfe" ,"hilfe"])
async def _help(ctx):
    
    myembed = discord.Embed(title = "Hier ist eine liste aller Commands" , description = "", color = 0xFFFFFF)
    myembed.add_field(name = "Twitch:" , value = "!Twitch" , inline = False)
    myembed.add_field(name = "Määäh" , value = "!Määäh" , inline = False)
    myembed.add_field(name = "Schlechte Witze" , value = "!schlechte_witze" , inline = False)
    myembed.add_field(name = "witze" , value = "!witze" , inline = False)
    myembed.set_footer(text = "Dieser Bot Wurde von juli_crafter#8905 gecodet")
    myembed.set_author(name = "juli_crafter#8905")
    
    await ctx.message.channel.send(embed=myembed)
    
#Mod Help
@client.command(aliases = ["mhelp" , "MHelp" , "Mhelp" , "mHelp" , "MODHelp" , "ModHelp" , "Modhelp"])
@commands.has_permissions(administrator = True )
async def modhelp(ctx):
    
    myembed = discord.Embed(title = "Mod Commands" , description = "Hier ist eine Liste aller Mod Commands und wie man sie nutzt" , color = 0xFF0000)
    myembed.add_field(name = "clear" , value = '"!clear" + "anzahl der narichten die Gelöschte werden soll" !clear ist auch ne naricht also Mindestens 2' , inline = False )
    myembed.add_field(name = "kick" , value = '"!kick" + "@name" + "grund' , inline = False )
    myembed.add_field(name = "ban" , value = '"!ban" +  "@name" + "grund"' , inline = False)
    myembed.add_field(name = "unban" , value = '"!unban" + "@name"')
    myembed.set_footer(text = "Dieser Bot wurde von juli_crafter#8905 gecodet")
    myembed.set_author(name = "juli_crafter#8905")
    
    await ctx.message.channel.send(embed = myembed)    
 
    
#Twitch
@client.command(aliases = ["Twitch"])
async def twitch(ctx):
    
    await ctx.send("https://www.twitch.tv/monky19082000")

#Määäh    
@client.command(aliases = ["Määh" , "määäh" , "Määäh"])
async def määh(ctx):
    responses = ["Määäh",
                 "MÄÄÄÄÄÄÄÄÄH",
                 "Määäähhh",
                 "määääääääääh",
                 "määäääääh",
                 "Määäääääääääähhhhh",
                 "määäääääääääääääääh",
                 "määääh",
                 "Määh",
                 "Määäääh", ]
    await ctx.send(f"{random.choice(responses)}")

#aubex
@client.command(aliases = ["Aubex"])
async def aubex(ctx):
    
    await ctx.send("MÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
#LS22 server id

@client.command(aliases = ["ID","IP","ip"])
@commands.has_role(922607031989452890)
async def id():
    ls22_dedi = client.get_channel(922607541861630033)
    
    myembed = discord.Embed(title = "LS22 Dediserver Informationen", description = "Hier findes dui die Ip und das Passwort zum LS22 Dedi Server")
    myembed.add_field(name = "Server Name:" , value = "Acker Wuehler 3.0")
    myembed.add_field(name = "Passwort:" , value = "1234")
    myembed.set_footer(text = "Dieser Bot wurde von juli_crafter#8905")
    
    await ls22_dedi.send(embed = myembed)

#schlechte witze  
@client.command(aliases = ["Schlechte_Witze" , "schlechte_Witze", "Schlechte_witze"])
async def schlechte_witze(ctx):
    response = ["ich bin atheist Gott sei dank",
                "Was geht hier vor? deine Uhr",
                "Füße hoch der witz kommt Flach",
                "Geht ein Cowboy zum frisaur. Kommt er raus Pony weg.",
                "Steht ein Baum alleine im Wald",
                'Sag mal Postbote ohne "O". Briefträger ',
                'Was sagt der Große stift zu Kleinen Stift. Wachsmal Stift',
                "Was ist Grün und klopft andd die Tür? Ein Klopfsalat",
                "Wenn du beim Metzger Klingest Brauchste dich nicht wundern wenn Kein schwein aufmacht",
                "Sitzt einer im Stehcafe",
                "Warum kann ein Bagger nicht schwimmen? Weil er nur ein arm hat",
                "Was macht eine Bombe im Bordell? Puff",
                "Was ist der Schlimmste Tag für ein U-boot? Tag der Offenen Tür",
                "Treffen sich 2 Kerzen Sagt die eine zur anderen gehen. wir Heute aus?",
                "Mein Zahnartz sagt ich brauch ne Krone. Endlich sieht es jemand wie ich.",
                "Was Trinken Führungskräfte? Leitungswasser",
                "Meine Freundin ist Eingebildet. Dann such dir eine reale!",
                "wie heißt ein spainier ohne auto? Carlos",
                "Scheiße ist wenn ein Furz was wiegt",
                "haben sie angst vor Asiaten? Ja, panisch"             
                
                ]
    await ctx.send(f"{random.choice(response)}")
    
    
#witze
@client.command(aliases = ["Witze" , "Joke" , "joke"])
async def witze(ctx):
    response = ["ich bin atheist Gott sei dank",
                "Was geht hier vor? deine Uhr",
                "Füße hoch der witz kommt Flach",
                "Geht ein Cowboy zum frisaur. Kommt er raus Pony weg.",
                "Steht ein Baum alleine im Wald",
                'Sag mal Postbote ohne "O". Briefträger ',
                'Was sagt der Große stift zu Kleinen Stift. Wachsmal Stift',
                "Was ist Grün und klopft and die Tür? Ein Klopfsalat",
                "Wenn du beim Metzger Klingest Brauchste dich nicht wundern wenn Kein schwein aufmacht",
                "Sitzt einer im Stehcafe",
                "Warum kann ein Bagger nicht schwimmen? Weil er nur ein arm hat",
                "Was macht eine Bombe im Bordell? Puff",
                "Was ist der Schlimmste Tag für ein U-boot? Tag der Offenen Tür",
                "Treffen sich 2 Kerzen Sagt die eine zur anderen. gehen wir Heute aus?",
                "Mein Zahnartz sagt ich brauch ne Krone. Endlich sieht es jemand wie ich.",
                "Was Trinken Führungskräfte? Leitungswasser",
                "Meine Freundin ist Eingebildet. Dann such dir eine reale!",
                "wie heißt ein spainier ohne auto? Carlos",
                "Egal wie neu du bist, Manuel ist Neuer",
                "Wat sät der Kölner, wenn der Rasenmäher kapoot ist? Mäht nix",
                "Scheiße ist wenn ein Furz was wiegt",
                "Zahnarzt zum Patienten: Das kann jetzt ein  Bisschen weh tun"
                "Patient: kein Problem"
                "Zahnartz: Ich habe seit 3 Jahren ein Verhältnis mit ihrer Frau.",  
                "haben sie angst vor Asiaten? Ja, panisch",
                "wie nennt man ne gruppe von Wölfen? Wolfgang",
                "War heute ohne Handy auf Klo. Wir habe 232 Fliesen"           
                
                ]
    await ctx.send(f"{random.choice(response)}")


#Mod Commands
   
#ping
@client.command(aliases = ["Ping"])
@commands.has_permissions(administrator = True)
async def ping(ctx):
    await ctx.send(f"Der ping des Bot ist {round(client.latency * 1000)}ms")
    
#clear  to deleate a bunch of massange at once 
#do not forget to count the !clear message too
@client.command(aliases = ["Clear"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount = 2):
    
    
    await ctx.channel.purge(limit = amount)

#kick   
@client.command(aliases = ["Kick"])
@commands.has_permissions(kick_members = True) # permission check
async def kick(ctx, member : discord.Member,*, reason = None,amount = 1): #the amount ist for the deliting of the message
    await member.kick(reason = reason)
    time.sleep(10) # waiting 10 secs
    await ctx.channel.purge(limit = amount) # delleting the command message

#ban   
@client.command(alisases = ["Ban"])
@commands.has_permissions(ban_members = True) #permission check
async def ban(ctx, member : discord.Member,*, reason = None,amount = 1): #the amount ist for the deliting of the message
    await member.ban(reason = reason)
    time.sleep(10)# waiting 10 secs
    await ctx.channel.purge(limit = amount) # delleting the command message

#unban with massage in the chat
@client.command(aliases = ["Unban"])
@commands.has_permissions(ban_members = True , administrator = True ) #permission
async def unban(ctx, *, member,amount = 1):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for ban_entry in banned_user:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user) 
            await ctx.send(f'unbanned {user.name}#{user.discriminator}')
            return   


#status change 
@tasks.loop(seconds = 60)
async def status_change():
     await client.change_presence(status = discord.Status.dnd , activity = discord.Game(next(status)))

#Error Codes

#command not existing

@client.event
async def on_command_error(ctx , error, amount):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("command not found error 10")
        time.sleep(30)
        await ctx.channel.purge(limmit = amount)

#clear error
@client.event
async def clear_error(ctx, error, amount = 1):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("please specify an amount to delete")
        time.sleep(30)
        await ctx.channel.purge(limit = amount)

#permission error
@client.event
async def on_command_error(ctx , error, amount = 1):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send("You dont have enough permissions")
        time.sleep(30)
        await ctx.channel.purge(limit = amount)

#lvl system
@client.event
async def on_member_join(member):
    with open('user.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('user.json', 'w') as f:
        json.dump(users, f)

#is that when you write a message the bot you will get exp and be checked ich you lvled up
@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('user.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('user.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)

#update the whole user Database in the json file
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1

#add the experience to thje client id
async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

#for the lvl up in the level system and it send a message if you lvl up
async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None ):
    if not member:
        id = ctx.message.author.id
        with open('user.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('user.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')      
      

#Sonstiges
 
#on ready
@client.event
async def on_ready():
    
    status_change.start()
    
    haupt = client.get_channel(939615617030438943)
    await haupt.send("ich bin online")

#member updates

#on member join
@client.event
async def on_member_join(member):
    
    haupt = client.get_channel(892097003989893123)
   
    await haupt.send(f"Hallo schön das du Da bist @{member}",)
    
#on member remove
@client.event
async def on_member_remove(member):
    
    haupt = client.get_channel(892097003989893123)
    
    await haupt.send(f"Schade das @{member} gegangen ist")
    
#Mod Log

#member role update
@client.event
async def on_member_update(member , after ):
    
    mod_log = client.get_channel(939887977931366400)
    
    await mod_log.send(f"Das Mitglied {member} hat was verändert")


#monky special command
def monky_def(ctx):
    
    return ctx.author.id == 833140188624453682


@client.command()
@commands.check(monky_def)
async def monky(ctx):
    
    await ctx.send(f"Gib Die Bannanen her sonst töte ich dich xD")


#justus Befehl
def is_it_me(ctx):
    
    return ctx.author.id == 293433578145185793


@client.command()
@commands.check(is_it_me)
async def author(ctx):
    
    await ctx.send(f"hi am the Bot author {ctx.author}")
   
    
#Client run
client.run('token')