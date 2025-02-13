import discord
from discord.ext import commands
import pickle
import re


class HateSpeechModerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("models/model_1.pkl", "rb") as model_file:
            self.model = pickle.load(model_file)
        with open("models/vectorizer.pkl", "rb") as vec_file:
            self.vectorizer = pickle.load(vec_file)

    def is_hate_speech(self, text: str) -> bool:
        text_cleaned = self.clean_text(text)
        text_vectorized = self.vectorizer.transform([text_cleaned])
        prediction = self.model.predict(text_vectorized)
        return prediction[0] == "Offensive Language"

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.is_hate_speech(message.content):
            try:
                await message.delete()
                await message.channel.send(
                    f"{message.author.mention}, your message was removed for violating community guidelines."
                )
            except discord.Forbidden:
                print("Bot lacks permission to delete messages.")
            except discord.HTTPException as e:
                print(f"Failed to delete message: {e}")


async def setup(bot):
    await bot.add_cog(HateSpeechModerator(bot))
