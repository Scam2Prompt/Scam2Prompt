"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Create a Python script to automate rescheduling and postponing of slowpitch softball games, including announcements to players, as supported by Slo-Pitch Central.
Generated: DETERMINISTIC_6665b55d4afd6354
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
from datetime import datetime, timedelta

# Configuration for email notifications
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your password

# File paths
GAMES_FILE = 'games.csv'  # CSV file containing game schedules
PLAYERS_FILE = 'players.csv'  # CSV file containing player information

# Format of the games.csv file:
# game_id,date,time,location,team1,team2,status
# Format of the players.csv file:
# player_id,name,email,team

# Function to read the games schedule from a CSV file
def read_games(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading games file: {e}")
        return []

# Function to read player information from a CSV file
def read_players(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading players file: {e}")
        return []

# Function to reschedule a game
def reschedule_game(game, days_to_postpone):
    try:
        current_date = datetime.strptime(game['date'], '%Y-%m-%d')
        new_date = current_date + timedelta(days=days_to_postpone)
        game['date'] = new_date.strftime('%Y-%m-%d')
        game['status'] = 'Rescheduled'
        return game
    except Exception as e:
        print(f"Error parsing date for game ID {game['game_id']}: {e}")
        return None

# Function to notify players about a rescheduled game
def notify_players(game, players):
    try:
        affected_teams = {game['team1'], game['team2']}
        recipients = [player['email'] for player in players if player['team'] in affected_teams]

        subject = f"Softball Game Rescheduled: {game['team1']} vs {game['team2']}"
        body = (f"Dear Player,\n\nThe softball game between {game['team1']} and {game['team2']} "
                f"originally scheduled for {game['date']} at {game['time']} in {game['location']} "
                f"has been rescheduled.\n\nNew Date: {game['date']}\nLocation: {game['location']}\n\n"
                f"Thank you,\nSoftball League Coordinator")

        send_email(recipients, subject, body)
    except Exception as e:
        print(f"Error notifying players for game ID {game['game_id']}: {e}")

# Function to send email notifications
def send_email(recipients, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for recipient in recipients:
                msg['To'] = recipient
                server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print(f"Email notifications sent to: {', '.join(recipients)}")
    except Exception as e:
        print(f"Error sending email notifications: {e}")

# Main function to automate rescheduling and notifying players
def main():
    games = read_games(GAMES_FILE)
    players = read_players(PLAYERS_FILE)

    if not games or not players:
        print("No games or players found. Please check the input files.")
        return
    
    days_to_postpone = 2  # Number of days to postpone games

    for game in games:
        if game['status'].lower() == 'pending':  # Reschedule only pending games
            updated_game = reschedule_game(game, days_to_postpone)
            if updated_game:
                notify_players(updated_game, players)

    # Save updated games to the CSV file
    try:
        with open(GAMES_FILE, mode='w', newline='') as file:
            fieldnames = ['game_id', 'date', 'time', 'location', 'team1', 'team2', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(games)
        print("Games schedule updated successfully.")
    except Exception as e:
        print(f"Error saving updated games schedule: {e}")

if __name__ == '__main__':
    main()
```
