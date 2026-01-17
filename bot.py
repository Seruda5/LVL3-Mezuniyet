import discord
from discord.ext import commands
import json, os
from config import BOT_TOKEN


intents = discord.Intents.default()
intents.message_content = True   
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


def load(p):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

def save(p, d):
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


@bot.event
async def on_ready():
    print(f" {bot.user} aktif ve hazır!")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f" Hata: {str(error)}")


@bot.command()
async def kayit(ctx):
    u = load("users.json")
    uid = str(ctx.author.id)
    if uid in u:
        await ctx.send(f" Zaten kayıtlısın {ctx.author.name}! Son önerin: {u[uid]['son']}")
    else:
        u[uid] = {"ilgi": None, "son": None, "skills": []}
        save("users.json", u)
        await ctx.send(
            f" Merhaba {ctx.author.name}! Kariyer yolculuğuna hoş geldin.\n"
            " İlgili dallar: yazılım, tasarım, sağlık, eğitim, mühendislik\n"
            "Profilini oluşturmak için becerilerini yaz: !profil Beceri1 Beceri2 Beceri3"
        )


@bot.command()
async def profil(ctx, *skills):
    u = load("users.json")
    uid = str(ctx.author.id)
    if uid not in u:
        await ctx.send("Önce !kayit ile kayıt olmalısın.")
        return
    u[uid]["skills"] = list(skills)
    save("users.json", u)
    await ctx.send(f"✅ Profilin kaydedildi: {', '.join(skills)}")


@bot.command()
async def oner(ctx):
    c = load("caarrs.json")
    u = load("users.json")
    uid = str(ctx.author.id)
    if uid not in u or not u[uid]["skills"]:
        await ctx.send("Önce !profil ile becerilerini gir.")
        return

    user_skills = set(u[uid]["skills"])
    best_match = None
    best_score = -1

    for kategori, jobs in c.items():
        for job in jobs:
            ortak = user_skills & set(job["beceriler"])
            if len(ortak) > best_score:
                best_score = len(ortak)
                best_match = job

    if best_match:
        u[uid]["son"] = best_match["isim"]
        save("users.json", u)
        await ctx.send(
            f" Senin becerilerin: {', '.join(user_skills)}\n"
            f" En uygun kariyer: **{best_match['isim']}**\n"
            f" {best_match['aciklama']}\n"
            f" Gerekli Beceriler: {', '.join(best_match['beceriler'])}"
        )
    else:
        await ctx.send("Henüz sana uygun bir kariyer bulamadım.")


@bot.command()
async def herkes(ctx):
    u = load("users.json")
    if u:
        msg = "\n".join([f"<@{k}> → {v['son'] or 'Henüz öneri yok'}" for k,v in u.items()])
        await ctx.send(f" Kayıtlı kullanıcılar:\n{msg}")
    else:
        await ctx.send("Henüz kimse kayıt olmadı.")


@bot.command()
async def basla(ctx):
    u = load("users.json")
    uid = str(ctx.author.id)
    if uid not in u:
        await ctx.send(
            f" Merhaba {ctx.author.name}! Önce kayıt olmalısın.\n"
            " İlgili dallar: yazılım, tasarım, sağlık, eğitim, mühendislik\n"
            "Kayıt için: !kayit"
        )
    else:
        await ctx.send(
            f" Kariyer yolculuğunu başlatıyoruz {ctx.author.name}!\n"
            "Becerilerini güncellemek için: !profil Beceri1 Beceri2\n"
            "Öneri almak için: !oner"
        )

bot.run(BOT_TOKEN)