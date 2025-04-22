import discord
from discord.ext import commands

# ====== กำหนดค่าตรงนี้ ======
TOKEN = "MTI5MDc0Nzc1MTAzMzg2ODQzNA.GovXG4.NDrCKM6uvrRL3tV5oQuvVlYFqd4ElsMocZ_daI"
SERVER_ID = 1348574255729741834  # <--- ใส่ Server (Guild) ID ตรงนี้
VOICE_CHANNEL_ID = 1364194830674038835  # <--- ใส่ Voice Channel ID ตรงนี้
# ===========================

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ บอทออนไลน์แล้ว: {bot.user}")

    guild = bot.get_guild(SERVER_ID)
    if guild is None:
        print("❌ ไม่พบเซิร์ฟเวอร์ ตรวจสอบ SERVER_ID ให้ถูกต้อง")
        return

    channel = guild.get_channel(VOICE_CHANNEL_ID)
    if channel is None:
        print("❌ ไม่พบห้องเสียง ตรวจสอบ VOICE_CHANNEL_ID ให้ถูกต้อง")
        return

    if isinstance(channel, discord.VoiceChannel):
        try:
            vc = await channel.connect()
            await vc.guild.change_voice_state(channel=vc.channel, self_deaf=True)
            print(f"🎧 เข้าห้องเสียง: {channel.name} แล้ว และปิดหูสำเร็จ")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดขณะเข้าห้องเสียง: {e}")
    else:
        print("❌ ID ที่ใส่ไม่ใช่ Voice Channel")

bot.run(TOKEN)
