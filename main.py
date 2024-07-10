import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)   

class Verify(View):
    def __init__(self, role_id):
        super().__init__()
        self.role_id = role_id

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.gray)
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(self.role_id)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(embed=self.create_embed("Verification Successful", "You have been verified and assigned the role!"), ephemeral=True)
        else:
            await interaction.response.send_message(embed=self.create_embed("Error", "Role not found! Please contact an admin."), ephemeral=True)

    def create_embed(self, title, description):
        embed = discord.Embed(
            title=title,
            description=description,
            color=0x00ff00
        )
        return embed

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def verify(ctx):
    role_id = #YOUR ROLE ID
    embed = discord.Embed(
        title="Verification",
        description="Click the button below to verify yourself.",
        color=0x00ff00
    )
    view = Verify(role_id)
    await ctx.send(embed=embed, view=view)

client.run('YOUR_TOKEN')
