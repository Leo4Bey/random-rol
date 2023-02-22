import discord
from discord import app_commands
from discord.ext import commands
from config import *
import asyncio
import random
from discord.ui import Button, View
intents = discord.Intents.all()

intents.message_content = True
intents.members = True


class LeoRolAl(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Rol al', style=discord.ButtonStyle.green, custom_id='leo_rol_al')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        random_number = random.randint(0,99)
        role1 = interaction.guild.get_role(rol1)
        role2 = interaction.guild.get_role(rol2)
        role3 = interaction.guild.get_role(rol3)
        role4 = interaction.guild.get_role(rol4)
        role5 = interaction.guild.get_role(rol5)
        role6 = interaction.guild.get_role(rol6)
        role7 = interaction.guild.get_role(rol7)
        role8 = interaction.guild.get_role(rol9)
        role9 = interaction.guild.get_role(rol9)
        role10 = interaction.guild.get_role(rol10)
        rlist = ["role1","role2","role3","role4","role5","role6","role7","role8","role9","role5","role6","role5","role1","role6","role4","role4","role5","role7","role7","role5","role5","role5","role6","role8","role5","role5","role6","role5","role8","role4","role4","role4","role6","role7","role7","role6","role9","role6","role4","role4","role4","role4","role5","role4","role4","role4","role1","role2","role2","role2","role2","role2","role2","role3","role5","role3","role3","role3","role2","role2","role3","role3","role3","role3","role7","role7","role3","role2","role6","role6","role2","role2","role2","role2","role2","role1","role1","role1","role1","role3","role8","role3","role3","role3","role1","role1","role1","role1","role1","role1","role1","role1","role1","role1","role8","role1","role1","role1","role9","role10",]
        msg2 = f'{interaction.user.mention} zaten üzerinde daha önceden alınmış rastgele bir rol mevcut.'
        if role1 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role2 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role3 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role4 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role5 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role6 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role7 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role8 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role9 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        elif role10 in interaction.user.roles:
            msg = await interaction.response.send_message(msg2, ephemeral=True)
        else:
            leobey = rlist[random_number]
            if leobey == "role1":
                await interaction.user.add_roles(role1)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %20'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role2":
                await interaction.user.add_roles(role2)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %15'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role3":
                await interaction.user.add_roles(role3)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %14'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role4":
                await interaction.user.add_roles(role4)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %13'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role5":
                await interaction.user.add_roles(role5)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %12'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role6":
                await interaction.user.add_roles(role6)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %10'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role7":
                await interaction.user.add_roles(role7)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %7'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role8":
                await interaction.user.add_roles(role8)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %5'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role9":
                await interaction.user.add_roles(role9)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %3'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
            elif leobey == "role10":
                await interaction.user.add_roles(role10)
                msg2 = f'hey! {interaction.user.mention}, rastgele bir rol aldın ve bu rolün çıkma olasılı %1'
                msg = await interaction.response.send_message(msg2, ephemeral=True)
    
class LeoButtonListener(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents) # $ yerine prefixinizi yazabilirsiniz - you can prefix here currentprefix is $

    async def setup_hook(self) -> None:
        self.add_view(LeoRolAl())


bot = LeoButtonListener()
@bot.command(name="rr")
@commands.has_permissions(administrator = True)
async def rr(ctx):
    LeoRolEmbed = discord.Embed(
        title = f'{servernm} - Random Rol Alma',
        description =f'Hey hepinize merhaba random rol almak istersen aşağıdaki butona tıklayarak rol alabilirsin ama ondan önce rollerin nadirliğine bakmanı tavsiye ederiz.\n\n<@&{rol1}>: %20\n<@&{rol2}>: %15\n<@&{rol3}>: %14\n<@&{rol4}>: %13\n<@&{rol5}>: %12\n<@&{rol6}>: %10\n<@&{rol7}>: %7\n<@&{rol8}>: %5\n<@&{rol9}>: %3\n<@&{rol10}>: %1',
        colour = discord.Colour.random()
    )
    LeoRolEmbed.set_footer(text=footer)
    view = LeoRolAl()
    await ctx.send(embed=LeoRolEmbed, view=view)


@bot.event 
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name=footer))

bot.run(token)
