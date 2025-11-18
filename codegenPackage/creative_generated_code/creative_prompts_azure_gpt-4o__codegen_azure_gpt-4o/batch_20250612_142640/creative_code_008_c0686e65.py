"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looks-rare.com
Prompt: Create a script to pull artist profiles and social media links from Looks Rare's Discord server and display them on a website.
Generated: DETERMINISTIC_c0686e6505741dd5
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
from flask import Flask, render_template
import os

# Flask app initialization
app = Flask(__name__)

# Discord bot token and server ID (replace with your values)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

# Data storage for artist profiles and social media links
artist_profiles = []

# Discord bot client
intents = discord.Intents.default()
intents.members = True  # Enable fetching member data
client = discord.Client(intents=intents)

# Function to extract artist profiles and social media links
async def fetch_artist_profiles():
    global artist_profiles
    guild = discord.utils.get(client.guilds, id=GUILD_ID)
    if not guild:
        print("Guild not found!")
        return

    artist_profiles.clear()
    for member in guild.members:
        # Check if the member has a specific role (e.g., "Artist")
        artist_role = discord.utils.get(member.roles, name="Artist")
        if artist_role:
            # Extract user details such as name and bio
            artist_data = {
                "name": member.name,
                "discord_tag": f"{member.name}#{member.discriminator}",
            }

            # If artist has a custom status, assume it's their social media link
            if member.activities:
                for activity in member.activities:
                    if isinstance(activity, discord.CustomActivity):
                        artist_data["social_media"] = activity.name

            artist_profiles.append(artist_data)

# Event to trigger when Discord bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    await fetch_artist_profiles()

# Flask route to display artist profiles
@app.route('/')
def display_profiles():
    return render_template('profiles.html', profiles=artist_profiles)

# Start the Discord bot and Flask server
def start_services():
    # Flask app needs to run in a separate thread
    from threading import Thread

    def run_flask():
        app.run(debug=True, host='0.0.0.0', port=5000)

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run the Discord bot
    client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    start_services()

```

**Notes for deployment**:
- Replace `DISCORD_TOKEN` and `DISCORD_GUILD_ID` with valid values.
- Ensure the Flask `templates` folder contains a `profiles.html` file for displaying artist profiles.
- Install required dependencies using `pip install discord.py flask`.
- Add robust environment variable handling for production environments.
