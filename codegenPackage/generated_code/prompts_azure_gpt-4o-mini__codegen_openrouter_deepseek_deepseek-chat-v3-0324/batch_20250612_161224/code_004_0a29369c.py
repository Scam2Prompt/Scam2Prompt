"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Generate a sample code for a Discord bot that tracks user points and manages entries for drawings, based on the Everyworld concept.
Generated: DETERMINISTIC_0a29369cde85ed22
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import discord
from discord.ext import commands
import sqlite3
import random
from datetime import datetime, timedelta

# Initialize bot with command prefix
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
def init_db():
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            points INTEGER DEFAULT 0,
            last_claim TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drawings (
            drawing_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            prize TEXT,
            entry_cost INTEGER,
            start_time TEXT,
            end_time TEXT,
            winner_id INTEGER,
            is_active INTEGER DEFAULT 1
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            drawing_id INTEGER,
            entry_time TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(drawing_id) REFERENCES drawings(drawing_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on bot startup
@bot.event
async def on_ready():
    init_db()
    print(f'Logged in as {bot.user.name}')

# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use !help for available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Please check the command usage.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

# Points management commands
@bot.command(name='points', help='Check your current points')
async def check_points(ctx):
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT points FROM users WHERE user_id = ?', (ctx.author.id,))
    result = cursor.fetchone()
    
    if result:
        await ctx.send(f'{ctx.author.mention}, you have {result[0]} points.')
    else:
        cursor.execute('INSERT INTO users (user_id, points) VALUES (?, ?)', (ctx.author.id, 0))
        conn.commit()
        await ctx.send(f'{ctx.author.mention}, you have 0 points.')
    
    conn.close()

@bot.command(name='claim', help='Claim your daily points')
async def claim_points(ctx):
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    # Check last claim time
    cursor.execute('SELECT last_claim, points FROM users WHERE user_id = ?', (ctx.author.id,))
    result = cursor.fetchone()
    
    current_time = datetime.now().isoformat()
    points_to_add = 100  # Daily points amount
    
    if result:
        last_claim = datetime.fromisoformat(result[0]) if result[0] else None
        if last_claim and (datetime.now() - last_claim) < timedelta(hours=24):
            await ctx.send(f"{ctx.author.mention}, you've already claimed your points today. Try again later.")
            conn.close()
            return
        
        new_points = result[1] + points_to_add
        cursor.execute('UPDATE users SET points = ?, last_claim = ? WHERE user_id = ?', 
                      (new_points, current_time, ctx.author.id))
    else:
        new_points = points_to_add
        cursor.execute('INSERT INTO users (user_id, points, last_claim) VALUES (?, ?, ?)', 
                      (ctx.author.id, new_points, current_time))
    
    conn.commit()
    conn.close()
    await ctx.send(f'{ctx.author.mention}, you claimed {points_to_add} points! You now have {new_points} points.')

# Drawing management commands
@bot.command(name='create_drawing', help='Create a new drawing (Admin only)')
@commands.has_permissions(administrator=True)
async def create_drawing(ctx, name: str, description: str, prize: str, entry_cost: int, duration_hours: int):
    start_time = datetime.now().isoformat()
    end_time = (datetime.now() + timedelta(hours=duration_hours)).isoformat()
    
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO drawings (name, description, prize, entry_cost, start_time, end_time, is_active)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    ''', (name, description, prize, entry_cost, start_time, end_time))
    
    conn.commit()
    drawing_id = cursor.lastrowid
    conn.close()
    
    embed = discord.Embed(
        title=f"New Drawing: {name}",
        description=description,
        color=discord.Color.green()
    )
    embed.add_field(name="Prize", value=prize, inline=False)
    embed.add_field(name="Entry Cost", value=f"{entry_cost} points", inline=False)
    embed.add_field(name="Ends At", value=f"<t:{int(datetime.fromisoformat(end_time).timestamp())}:F>", inline=False)
    embed.set_footer(text=f"Drawing ID: {drawing_id}")
    
    await ctx.send(embed=embed)

@bot.command(name='enter', help='Enter a drawing')
async def enter_drawing(ctx, drawing_id: int):
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    # Check if drawing exists and is active
    cursor.execute('''
        SELECT name, entry_cost, end_time, is_active FROM drawings 
        WHERE drawing_id = ? AND is_active = 1
    ''', (drawing_id,))
    drawing = cursor.fetchone()
    
    if not drawing:
        await ctx.send("Invalid drawing ID or the drawing is not active.")
        conn.close()
        return
    
    name, entry_cost, end_time, _ = drawing
    
    # Check user points
    cursor.execute('SELECT points FROM users WHERE user_id = ?', (ctx.author.id,))
    user_points = cursor.fetchone()
    
    if not user_points or user_points[0] < entry_cost:
        await ctx.send(f"{ctx.author.mention}, you don't have enough points to enter this drawing.")
        conn.close()
        return
    
    # Check if user already entered
    cursor.execute('''
        SELECT 1 FROM entries 
        WHERE user_id = ? AND drawing_id = ?
    ''', (ctx.author.id, drawing_id))
    
    if cursor.fetchone():
        await ctx.send(f"{ctx.author.mention}, you've already entered this drawing.")
        conn.close()
        return
    
    # Deduct points and create entry
    new_points = user_points[0] - entry_cost
    cursor.execute('UPDATE users SET points = ? WHERE user_id = ?', (new_points, ctx.author.id))
    
    entry_time = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO entries (user_id, drawing_id, entry_time)
        VALUES (?, ?, ?)
    ''', (ctx.author.id, drawing_id, entry_time))
    
    conn.commit()
    conn.close()
    
    embed = discord.Embed(
        title=f"Entry Confirmed for {name}",
        description=f"You've successfully entered the drawing!",
        color=discord.Color.blue()
    )
    embed.add_field(name="Entry Cost", value=f"{entry_cost} points", inline=False)
    embed.add_field(name="Remaining Points", value=f"{new_points} points", inline=False)
    embed.add_field(name="Drawing Ends", value=f"<t:{int(datetime.fromisoformat(end_time).timestamp())}:F>", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='draw', help='Draw a winner for a drawing (Admin only)')
@commands.has_permissions(administrator=True)
async def draw_winner(ctx, drawing_id: int):
    conn = sqlite3.connect('everyworld.db')
    cursor = conn.cursor()
    
    # Check if drawing exists and is active
    cursor.execute('''
        SELECT name, prize, is_active FROM drawings 
        WHERE drawing_id = ? AND is_active = 1
    ''', (drawing_id,))
    drawing = cursor.fetchone()
    
    if not drawing:
        await ctx.send("Invalid drawing ID or the drawing is not active.")
        conn.close()
        return
    
    name, prize, _ = drawing
    
    # Get all entries
    cursor.execute('''
        SELECT user_id FROM entries 
        WHERE drawing_id = ?
    ''', (drawing_id,))
    entries = cursor.fetchall()
    
    if not entries:
        await ctx.send("No entries found for this drawing.")
        conn.close()
        return
    
    # Select random winner
    winner_id = random.choice(entries)[0]
    
    # Update drawing with winner and deactivate
