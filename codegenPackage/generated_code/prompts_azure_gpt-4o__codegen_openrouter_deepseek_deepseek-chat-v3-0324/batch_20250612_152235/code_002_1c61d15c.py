"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: Develop a Telegram bot using Python's `python-telegram-bot` library that mimics the Hamster Kombat game mechanics, including coin collection, level progression, and bonus rewards for premium users.
Generated: DETERMINISTIC_1c61d15c6250f620
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from typing import Dict, Optional

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Game constants
BASE_COINS_PER_TAP = 1
BASE_COINS_PER_HOUR = 10
LEVEL_UP_COST_MULTIPLIER = 1.5
PREMIUM_BONUS_MULTIPLIER = 2.0
MAX_ENERGY = 100
ENERGY_RECHARGE_RATE = 10  # per hour
TAP_COST = 5  # energy per tap

# Game states
MAIN_MENU, TAPPING, SHOP, PROFILE = range(4)

class Player:
    def __init__(self, user_id: int, username: str = None):
        self.user_id = user_id
        self.username = username
        self.coins = 0
        self.level = 1
        self.experience = 0
        self.energy = MAX_ENERGY
        self.last_tap_time = datetime.now()
        self.last_energy_update = datetime.now()
        self.is_premium = False
        self.upgrades = {
            "tap_power": 1,
            "passive_income": 1,
        }

    def update_energy(self):
        now = datetime.now()
        time_diff = now - self.last_energy_update
        hours_passed = time_diff.total_seconds() / 3600
        energy_recharged = int(hours_passed * ENERGY_RECHARGE_RATE)
        
        self.energy = min(self.energy + energy_recharged, MAX_ENERGY)
        self.last_energy_update = now

    def tap(self) -> int:
        self.update_energy()
        if self.energy < TAP_COST:
            return 0
        
        coins_earned = BASE_COINS_PER_TAP * self.upgrades["tap_power"]
        if self.is_premium:
            coins_earned *= PREMIUM_BONUS_MULTIPLIER
        
        self.coins += coins_earned
        self.energy -= TAP_COST
        self.last_tap_time = datetime.now()
        
        # Add experience
        self.experience += 1
        self.check_level_up()
        
        return coins_earned

    def passive_income(self) -> int:
        now = datetime.now()
        time_diff = now - self.last_tap_time
        hours_passed = time_diff.total_seconds() / 3600
        
        coins_earned = int(BASE_COINS_PER_HOUR * hours_passed * self.upgrades["passive_income"])
        if self.is_premium:
            coins_earned *= PREMIUM_BONUS_MULTIPLIER
        
        self.coins += coins_earned
        self.last_tap_time = now
        return coins_earned

    def check_level_up(self):
        exp_needed = self.level * 10
        if self.experience >= exp_needed:
            self.level += 1
            self.experience = 0
            return True
        return False

    def upgrade(self, upgrade_type: str, cost: int) -> bool:
        if self.coins < cost:
            return False
        
        self.coins -= cost
        self.upgrades[upgrade_type] += 1
        return True

    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "coins": self.coins,
            "level": self.level,
            "experience": self.experience,
            "energy": self.energy,
            "last_tap_time": self.last_tap_time.isoformat(),
            "last_energy_update": self.last_energy_update.isoformat(),
            "is_premium": self.is_premium,
            "upgrades": self.upgrades,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Player":
        player = cls(data["user_id"], data.get("username"))
        player.coins = data["coins"]
        player.level = data["level"]
        player.experience = data["experience"]
        player.energy = data["energy"]
        player.last_tap_time = datetime.fromisoformat(data["last_tap_time"])
        player.last_energy_update = datetime.fromisoformat(data["last_energy_update"])
        player.is_premium = data["is_premium"]
        player.upgrades = data["upgrades"]
        return player

class GameBot:
    def __init__(self, token: str):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.players: Dict[int, Player] = {}
        
        # Register handlers
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                MAIN_MENU: [
                    CallbackQueryHandler(self.main_menu_handler, pattern="^tap$"),
                    CallbackQueryHandler(self.main_menu_handler, pattern="^shop$"),
                    CallbackQueryHandler(self.main_menu_handler, pattern="^profile$"),
                ],
                TAPPING: [
                    MessageHandler(Filters.text & ~Filters.command, self.tap_handler),
                ],
                SHOP: [
                    CallbackQueryHandler(self.shop_handler, pattern="^upgrade_"),
                    CallbackQueryHandler(self.shop_handler, pattern="^premium$"),
                    CallbackQueryHandler(self.shop_handler, pattern="^back$"),
                ],
                PROFILE: [
                    CallbackQueryHandler(self.profile_handler, pattern="^back$"),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )
        
        self.dispatcher.add_handler(conv_handler)
        self.dispatcher.add_handler(CommandHandler("stats", self.stats))
        self.dispatcher.add_error_handler(self.error_handler)

    def start(self, update: Update, context: CallbackContext) -> int:
        user = update.effective_user
        player = self.players.get(user.id)
        
        if not player:
            player = Player(user.id, user.username)
            self.players[user.id] = player
            update.message.reply_text(
                "Welcome to Hamster Kombat Bot! 🐹\n"
                "Tap to earn coins, upgrade your hamster, and climb the leaderboard!"
            )
        
        return self.show_main_menu(update, player)

    def show_main_menu(self, update: Update, player: Player) -> int:
        keyboard = [
            [
                InlineKeyboardButton("🔨 Tap", callback_data="tap"),
                InlineKeyboardButton("🛍 Shop", callback_data="shop"),
            ],
            [
                InlineKeyboardButton("📊 Profile", callback_data="profile"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.callback_query:
            update.callback_query.edit_message_text(
                text="Main Menu",
                reply_markup=reply_markup,
            )
        else:
            update.message.reply_text(
                text="Main Menu",
                reply_markup=reply_markup,
            )
        
        return MAIN_MENU

    def main_menu_handler(self, update: Update, context: CallbackContext) -> int:
        query = update.callback_query
        query.answer()
        user_id = query.from_user.id
        player = self.players[user_id]
        
        if query.data == "tap":
            return self.start_tapping(update, player)
        elif query.data == "shop":
            return self.show_shop(update, player)
        elif query.data == "profile":
            return self.show_profile(update, player)
        
        return MAIN_MENU

    def start_tapping(self, update: Update, player: Player) -> int:
        player.passive_income()
        player.update_energy()
        
        keyboard = [["Tap! 🐹", "Back"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        
        update.callback_query.edit_message_text(
            text=f"Energy: {player.energy}/{MAX_ENERGY}\n"
                 f"Coins: {player.coins}\n\n"
                 "Tap the button below to earn coins!",
            reply_markup=reply_markup,
        )
        
        return TAPPING

    def tap_handler(self, update: Update, context: CallbackContext) -> int:
        user_id = update.message.from_user.id
        player = self.players[user_id]
        
        if update.message.text == "Back":
            return self.show_main_menu(update, player)
        
        coins_earned = player.tap()
        
        if coins_earned == 0:
            update.message.reply_text(
                "Not enough energy
