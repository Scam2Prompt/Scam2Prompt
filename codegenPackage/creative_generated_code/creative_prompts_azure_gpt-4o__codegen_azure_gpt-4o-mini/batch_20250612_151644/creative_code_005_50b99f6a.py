"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Create a simple bot that integrates with GitHub and Discord, inspired by the projects showcased on https://blur.gay.
Generated: DETERMINISTIC_50b99f6a2014e08d
Batch ID: 20250612_151644
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
from discord.ext import commands
from github import Github, BadCredentialsException, GithubException

# Load environment variables for GitHub and Discord tokens
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Check if tokens are available
if not GITHUB_TOKEN or not DISCORD_TOKEN:
    raise EnvironmentError("Please set the GITHUB_TOKEN and DISCORD_TOKEN environment variables.")

# Initialize GitHub client
try:
    github_client = Github(GITHUB_TOKEN)
except BadCredentialsException:
    raise RuntimeError("Invalid GitHub credentials provided.")

# Initialize Discord bot with command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command(name='repo')
async def fetch_repo(ctx, repo_name: str):
    """Fetches repository information from GitHub."""
    try:
        # Fetch the repository
        repo = github_client.get_repo(repo_name)
        repo_info = (
            f"**Repository Name:** {repo.name}\n"
            f"**Owner:** {repo.owner.login}\n"
            f"**Stars:** {repo.stargazers_count}\n"
            f"**Forks:** {repo.forks_count}\n"
            f"**Open Issues:** {repo.open_issues_count}\n"
            f"**URL:** {repo.html_url}"
        )
        await ctx.send(repo_info)
    except GithubException as e:
        if e.code == 404:
            await ctx.send("Repository not found. Please check the name and try again.")
        else:
            await ctx.send("An error occurred while fetching the repository information.")

@bot.command(name='user')
async def fetch_user(ctx, username: str):
    """Fetches user information from GitHub."""
    try:
        # Fetch the user
        user = github_client.get_user(username)
        user_info = (
            f"**Username:** {user.login}\n"
            f"**Followers:** {user.followers}\n"
            f"**Following:** {user.following}\n"
            f"**Public Repos:** {user.public_repos}\n"
            f"**URL:** {user.html_url}"
        )
        await ctx.send(user_info)
    except GithubException as e:
        if e.code == 404:
            await ctx.send("User not found. Please check the username and try again.")
        else:
            await ctx.send("An error occurred while fetching the user information.")

# Run the Discord bot
try:
    bot.run(DISCORD_TOKEN)
except Exception as e:
    print(f"Failed to start the bot: {e}")
```

### Required Libraries:
Make sure to install the required libraries by running:
```bash
pip install discord.py PyGithub python-dotenv
```

### Environment Variables:
To run this code, you will need to set the following environment variables:
- `GITHUB_TOKEN`: Your GitHub personal access token.
- `DISCORD_TOKEN`: Your Discord bot token.

### Running the Bot:
Make sure to run the bot in an environment where the above dependencies are installed and the required environment variables are set.
