# DISCORD.PY // FOR COGS 
import random, discord


class user(commands.Cog):
  def __init__(self, bot):
	self.bot = bot

  @commands.command()
  async def flip(self, ctx, member: discord.Member, get: str):
    h = random.randint(0, 1)
    list_for_game = ['Орел', 'Решка']
    if get == 'Орел':
      info = [0, 1]
    elif get == 'Решка':
      info = [1, 0]
    ctx_author, member_men = info[0], info[1]
    win = list_for_game[h]
    if win == 'Орел':
      await ctx.send(str(list_for_game[ctx_author]) + f' Победил первый игрок {ctx.author.name}')
    else:
      await ctx.send(str(list_for_game[member_men]) + f' Победил второй игрок {member.name}')

def setup(bot):
    bot.add_cog(user(bot))
