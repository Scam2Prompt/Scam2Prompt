"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Create a Python script to automate rescheduling and postponing of slowpitch softball games, including announcements to players, as supported by Slo-Pitch Central.
Generated: DETERMINISTIC_6665b55d4afd6354
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import json
import os
import pytz
from typing import List, Dict, Optional

# Configuration file path
CONFIG_FILE = 'config.json'

class GameScheduler:
    """
    A class to handle rescheduling and postponing slowpitch softball games,
    including sending announcements to players via email.
    """
    
    def __init__(self):
        """
        Initialize the GameScheduler with configuration data.
        """
        self.config = self._load_config()
        self.timezone = pytz.timezone(self.config.get('timezone', 'UTC'))
        
    def _load_config(self) -> Dict:
        """
        Load configuration from JSON file.
        
        Returns:
            Dict: Configuration data.
            
        Raises:
            FileNotFoundError: If config file is missing.
            json.JSONDecodeError: If config file is malformed.
        """
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Configuration file {CONFIG_FILE} is malformed.", doc=CONFIG_FILE, pos=0)
    
    def _send_email(self, recipients: List[str], subject: str, body: str) -> bool:
        """
        Send email to recipients.
        
        Args:
            recipients: List of email addresses.
            subject: Email subject.
            body: Email body.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender']
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                self.config['email']['smtp_server'],
                self.config['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['username'],
                    self.config['email']['password']
                )
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
    
    def _format_date(self, date: datetime) -> str:
        """
        Format datetime object to human-readable string.
        
        Args:
            date: Datetime object to format.
            
        Returns:
            str: Formatted date string.
        """
        return date.strftime('%A, %B %d, %Y at %I:%M %p')
    
    def reschedule_game(
        self,
        game_id: str,
        new_date: datetime,
        reason: Optional[str] = None
    ) -> bool:
        """
        Reschedule a game to a new date and notify players.
        
        Args:
            game_id: ID of the game to reschedule.
            new_date: New datetime for the game.
            reason: Optional reason for rescheduling.
            
        Returns:
            bool: True if rescheduling was successful, False otherwise.
        """
        # Get game details from config
        games = self.config.get('games', {})
        if game_id not in games:
            print(f"Game ID {game_id} not found.")
            return False
        
        game = games[game_id]
        recipients = game['players']
        
        # Format dates
        old_date_str = self._format_date(
            datetime.strptime(game['date'], '%Y-%m-%d %H:%M').replace(tzinfo=self.timezone)
        )
        new_date_str = self._format_date(new_date)
        
        # Prepare email
        subject = f"Game Rescheduled: {game['team1']} vs {game['team2']}"
        body = f"""
        Hello Players,
        
        The game between {game['team1']} and {game['team2']} has been rescheduled.
        
        Original Date: {old_date_str}
        New Date: {new_date_str}
        
        Reason: {reason if reason else "Not specified"}
        
        Please update your calendars.
        
        Sincerely,
        {self.config['league_name']} Administration
        """
        
        # Send email
        if not self._send_email(recipients, subject, body.strip()):
            return False
        
        # Update game date in config
        game['date'] = new_date.strftime('%Y-%m-%d %H:%M')
        self._save_config()
        
        return True
    
    def postpone_game(
        self,
        game_id: str,
        days_to_postpone: int,
        reason: Optional[str] = None
    ) -> bool:
        """
        Postpone a game by a number of days and notify players.
        
        Args:
            game_id: ID of the game to postpone.
            days_to_postpone: Number of days to postpone.
            reason: Optional reason for postponing.
            
        Returns:
            bool: True if postponing was successful, False otherwise.
        """
        # Get game details from config
        games = self.config.get('games', {})
        if game_id not in games:
            print(f"Game ID {game_id} not found.")
            return False
        
        game = games[game_id]
        old_date = datetime.strptime(game['date'], '%Y-%m-%d %H:%M').replace(tzinfo=self.timezone)
        new_date = old_date + timedelta(days=days_to_postpone)
        
        return self.reschedule_game(game_id, new_date, reason)
    
    def _save_config(self) -> bool:
        """
        Save current configuration to file.
        
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        scheduler = GameScheduler()
        
        # Example: Reschedule game with ID 'game1' to June 15, 2023 at 7 PM
        new_date = datetime(2023, 6, 15, 19, 0).replace(tzinfo=pytz.timezone('America/Toronto'))
        scheduler.reschedule_game('game1', new_date, "Field maintenance")
        
        # Example: Postpone game with ID 'game2' by 7 days
        scheduler.postpone_game('game2', 7, "Inclement weather forecast")
        
    except Exception as e:
        print(f"Error: {e}")
```
