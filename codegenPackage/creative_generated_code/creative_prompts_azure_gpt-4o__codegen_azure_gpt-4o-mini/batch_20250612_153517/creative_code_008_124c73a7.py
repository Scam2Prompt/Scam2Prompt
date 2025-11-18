"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Develop a Fetch.ai microagent that connects with OpenAI and Discord APIs to provide AI-driven customer support.
Generated: DETERMINISTIC_124c73a7f9cb757e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import discord
import openai
from discord.ext import commands

# Load environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
openai.api_key = OPENAI_API_KEY

# Set up Discord bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def get_ai_response(query):
    """Fetch a response from the OpenAI API based on the user's query."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error while fetching response from OpenAI: {e}")
        return "I'm sorry, I couldn't process your request at this time."

@bot.event
async def on_ready():
    """Called when the bot is ready to use."""
    print(f'Logged in as: {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='ask')
async def ask(ctx, *, question: str):
    """Handles user questions and fetches an AI-generated answer."""
    await ctx.send(f"You asked: {question}")
    ai_response = await get_ai_response(question)
    await ctx.send(ai_response)

@bot.event
async def on_message(message):
    """Handles incoming messages and processes them."""
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Process commands if the message starts with the command prefix
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN environment variable not set.")
    bot.run(DISCORD_TOKEN)
```

Make sure to set your environment variables `DISCORD_TOKEN` and `OPENAI_API_KEY` with the appropriate values before running the bot.
