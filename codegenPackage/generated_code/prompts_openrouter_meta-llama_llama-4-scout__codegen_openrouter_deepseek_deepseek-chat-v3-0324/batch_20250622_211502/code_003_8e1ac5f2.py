"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Design a system to handle giveaways and promotions, like the 6-month free subscription and NFL Network access offered by Sportify.Club, including user registration, notification, and prize distribution.
Generated: DETERMINISTIC_8e1ac5f24c6dab7f
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import datetime
from typing import List, Optional
from enum import Enum, auto
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from dataclasses import dataclass
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database simulation (in production, use a real database)
class Database:
    def __init__(self):
        self.users = {}
        self.giveaways = {}
        self.participations = {}
        self.winners = {}

    def add_user(self, user: 'User') -> None:
        self.users[user.user_id] = user

    def get_user(self, user_id: str) -> Optional['User']:
        return self.users.get(user_id)

    def add_giveaway(self, giveaway: 'Giveaway') -> None:
        self.giveaways[giveaway.giveaway_id] = giveaway

    def get_giveaway(self, giveaway_id: str) -> Optional['Giveaway']:
        return self.giveaways.get(giveaway_id)

    def add_participation(self, participation: 'Participation') -> None:
        self.participations[participation.participation_id] = participation

    def get_participations_for_giveaway(self, giveaway_id: str) -> List['Participation']:
        return [p for p in self.participations.values() if p.giveaway_id == giveaway_id]

    def add_winner(self, winner: 'Winner') -> None:
        self.winners[winner.winner_id] = winner

    def get_winners_for_giveaway(self, giveaway_id: str) -> List['Winner']:
        return [w for w in self.winners.values() if w.giveaway_id == giveaway_id]

# Enum for giveaway status
class GiveawayStatus(Enum):
    UPCOMING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    CANCELLED = auto()

# Enum for prize type
class PrizeType(Enum):
    SUBSCRIPTION = auto()
    ACCESS = auto()
    PHYSICAL = auto()
    OTHER = auto()

@dataclass
class User:
    user_id: str
    email: str
    name: str
    registration_date: datetime.datetime
    is_verified: bool = False

@dataclass
class Giveaway:
    giveaway_id: str
    name: str
    description: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    status: GiveawayStatus
    prize_type: PrizeType
    prize_description: str
    max_participants: Optional[int] = None
    winner_count: int = 1

@dataclass
class Participation:
    participation_id: str
    user_id: str
    giveaway_id: str
    participation_date: datetime.datetime

@dataclass
class Winner:
    winner_id: str
    user_id: str
    giveaway_id: str
    win_date: datetime.datetime
    prize_distributed: bool = False
    distribution_date: Optional[datetime.datetime] = None

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Email sent to {recipient}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False

class GiveawaySystem:
    def __init__(self, db: Database, email_service: EmailService):
        self.db = db
        self.email_service = email_service

    def register_user(self, email: str, name: str) -> Optional[User]:
        try:
            if not email or not name:
                raise ValueError("Email and name are required")

            user_id = str(uuid.uuid4())
            user = User(
                user_id=user_id,
                email=email,
                name=name,
                registration_date=datetime.datetime.now()
            )
            self.db.add_user(user)
            logger.info(f"User registered: {user_id}")
            return user
        except Exception as e:
            logger.error(f"User registration failed: {str(e)}")
            return None

    def create_giveaway(
        self,
        name: str,
        description: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        prize_type: PrizeType,
        prize_description: str,
        max_participants: Optional[int] = None,
        winner_count: int = 1
    ) -> Optional[Giveaway]:
        try:
            if start_date >= end_date:
                raise ValueError("End date must be after start date")

            giveaway_id = str(uuid.uuid4())
            giveaway = Giveaway(
                giveaway_id=giveaway_id,
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                status=GiveawayStatus.UPCOMING,
                prize_type=prize_type,
                prize_description=prize_description,
                max_participants=max_participants,
                winner_count=winner_count
            )
            self.db.add_giveaway(giveaway)
            logger.info(f"Giveaway created: {giveaway_id}")
            return giveaway
        except Exception as e:
            logger.error(f"Giveaway creation failed: {str(e)}")
            return None

    def participate_in_giveaway(self, user_id: str, giveaway_id: str) -> Optional[Participation]:
        try:
            user = self.db.get_user(user_id)
            giveaway = self.db.get_giveaway(giveaway_id)

            if not user or not giveaway:
                raise ValueError("User or giveaway not found")

            current_time = datetime.datetime.now()
            if current_time < giveaway.start_date:
                raise ValueError("Giveaway has not started yet")
            if current_time > giveaway.end_date:
                raise ValueError("Giveaway has ended")

            if giveaway.max_participants is not None:
                participations = self.db.get_participations_for_giveaway(giveaway_id)
                if len(participations) >= giveaway.max_participants:
                    raise ValueError("Giveaway has reached maximum participants")

            participation_id = str(uuid.uuid4())
            participation = Participation(
                participation_id=participation_id,
                user_id=user_id,
                giveaway_id=giveaway_id,
                participation_date=current_time
            )
            self.db.add_participation(participation)
            logger.info(f"User {user_id} participated in giveaway {giveaway_id}")
            return participation
        except Exception as e:
            logger.error(f"Participation failed: {str(e)}")
            return None

    def draw_winners(self, giveaway_id: str) -> List[Winner]:
        try:
            giveaway = self.db.get_giveaway(giveaway_id)
            if not giveaway:
                raise ValueError("Giveaway not found")

            if datetime.datetime.now() < giveaway.end_date:
                raise ValueError("Giveaway has not ended yet")

            participations = self.db.get_participations_for_giveaway(giveaway_id)
            if not participations:
                raise ValueError("No participants for this giveaway")

            winner_count = min(giveaway.winner_count, len(participations))
            selected_participations = random.sample(participations, winner_count)

            winners = []
            for participation in selected_participations:
                winner_id = str(uuid.uuid4())
                winner = Winner(
                    winner_id=winner_id,
                    user_id=participation.user_id,
                    giveaway_id=giveaway_id,
                    win_date=datetime.datetime.now()
                )
                self.db.add_winner(winner)
                winners.append(winner)

                # Notify winner
                user = self.db.get_user(participation.user_id)
                if user:
                    subject = f"You won: {giveaway.name}"
                    body = f"Congratulations {user.name}!\n\nYou have won: {giveaway.prize_description}"
                    self.email_service.send_email(user.email, subject, body)

            logger.info(f"Drew {len(winners)} winners for giveaway {giveaway_id}")
            return winners
        except Exception as e:
            logger.error(f"Drawing winners failed: {str(e)}")
            return []

    def distribute_prizes(self, giveaway_id: str) -> List[Winner]:
        try:
            winners =
