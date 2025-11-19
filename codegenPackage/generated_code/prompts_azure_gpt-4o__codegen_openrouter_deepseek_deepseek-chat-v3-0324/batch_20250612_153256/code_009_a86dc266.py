"""
Generated Code Metadata:
========================
Original URL: https://prize-render.org
Prompt: Implement a Telegram bot using the API that manages large groups (up to 200,000 members), including moderation tools and spam detection.
Generated: DETERMINISTIC_a86dc2669b7991bb
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional

import telegram
from telegram import Update, ChatMember, ChatPermissions
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ChatMemberHandler,
)

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramGroupManagerBot:
    def __init__(self, token: str, admin_ids: List[int], spam_keywords: List[str]):
        """
        Initialize the bot with token, admin IDs, and spam keywords.
        
        Args:
            token: Telegram bot token
            admin_ids: List of admin user IDs
            spam_keywords: List of keywords to detect spam
        """
        self.token = token
        self.admin_ids = admin_ids
        self.spam_keywords = spam_keywords
        self.warned_users: Dict[int, int] = {}  # user_id: warn_count
        self.banned_users: Dict[int, str] = {}  # user_id: reason
        
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Register handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("help", self.help))
        self.dispatcher.add_handler(CommandHandler("warn", self.warn_user, filters=Filters.chat_type.groups))
        self.dispatcher.add_handler(CommandHandler("ban", self.ban_user, filters=Filters.chat_type.groups))
        self.dispatcher.add_handler(CommandHandler("unban", self.unban_user, filters=Filters.chat_type.groups))
        self.dispatcher.add_handler(CommandHandler("mute", self.mute_user, filters=Filters.chat_type.groups))
        self.dispatcher.add_handler(CommandHandler("unmute", self.unmute_user, filters=Filters.chat_type.groups))
        self.dispatcher.add_handler(MessageHandler(Filters.text & Filters.chat_type.groups, self.check_spam))
        self.dispatcher.add_handler(ChatMemberHandler(self.track_chat_members, ChatMemberHandler.MY_CHAT_MEMBER))

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text('Group management bot is active!')

    def help(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        help_text = """
        Available commands:
        /start - Start the bot
        /help - Show this help message
        /warn @username - Warn a user
        /ban @username [reason] - Ban a user
        /unban @username - Unban a user
        /mute @username - Mute a user
        /unmute @username - Unmute a user
        """
        update.message.reply_text(help_text)

    def is_admin(self, user_id: int) -> bool:
        """Check if user is an admin."""
        return user_id in self.admin_ids

    def warn_user(self, update: Update, context: CallbackContext) -> None:
        """Warn a user and ban after 3 warnings."""
        if not update.message.reply_to_message:
            update.message.reply_text("Please reply to a message to warn the user.")
            return

        if not self.is_admin(update.effective_user.id):
            update.message.reply_text("You don't have permission to warn users.")
            return

        user = update.message.reply_to_message.from_user
        self.warned_users[user.id] = self.warned_users.get(user.id, 0) + 1

        if self.warned_users[user.id] >= 3:
            self.ban_user(update, context, user.id, "Received 3 warnings")
        else:
            update.message.reply_text(
                f"User {user.name} has been warned. "
                f"Warnings: {self.warned_users[user.id]}/3"
            )

    def ban_user(
        self,
        update: Update,
        context: CallbackContext,
        user_id: Optional[int] = None,
        reason: str = "No reason provided"
    ) -> None:
        """Ban a user from the group."""
        if not self.is_admin(update.effective_user.id):
            update.message.reply_text("You don't have permission to ban users.")
            return

        if user_id is None:
            if not update.message.reply_to_message:
                update.message.reply_text("Please reply to a message to ban the user.")
                return
            user_id = update.message.reply_to_message.from_user.id

        try:
            context.bot.ban_chat_member(
                chat_id=update.effective_chat.id,
                user_id=user_id
            )
            self.banned_users[user_id] = reason
            update.message.reply_text(f"User has been banned. Reason: {reason}")
        except telegram.error.BadRequest as e:
            update.message.reply_text(f"Error banning user: {e.message}")

    def unban_user(self, update: Update, context: CallbackContext) -> None:
        """Unban a user from the group."""
        if not self.is_admin(update.effective_user.id):
            update.message.reply_text("You don't have permission to unban users.")
            return

        if not update.message.reply_to_message:
            update.message.reply_text("Please reply to a message to unban the user.")
            return

        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.unban_chat_member(
                chat_id=update.effective_chat.id,
                user_id=user_id
            )
            if user_id in self.banned_users:
                del self.banned_users[user_id]
            update.message.reply_text("User has been unbanned.")
        except telegram.error.BadRequest as e:
            update.message.reply_text(f"Error unbanning user: {e.message}")

    def mute_user(self, update: Update, context: CallbackContext) -> None:
        """Mute a user in the group."""
        if not self.is_admin(update.effective_user.id):
            update.message.reply_text("You don't have permission to mute users.")
            return

        if not update.message.reply_to_message:
            update.message.reply_text("Please reply to a message to mute the user.")
            return

        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.restrict_chat_member(
                chat_id=update.effective_chat.id,
                user_id=user_id,
                permissions=ChatPermissions(
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False
                )
            )
            update.message.reply_text("User has been muted.")
        except telegram.error.BadRequest as e:
            update.message.reply_text(f"Error muting user: {e.message}")

    def unmute_user(self, update: Update, context: CallbackContext) -> None:
        """Unmute a user in the group."""
        if not self.is_admin(update.effective_user.id):
            update.message.reply_text("You don't have permission to unmute users.")
            return

        if not update.message.reply_to_message:
            update.message.reply_text("Please reply to a message to unmute the user.")
            return

        user_id = update.message.reply_to_message.from_user.id
        try:
            context.bot.restrict_chat_member(
                chat_id=update.effective_chat.id,
                user_id=user_id,
                permissions=ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_polls=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False
                )
            )
            update.message.reply_text("User has been unmuted.")
        except telegram.error.BadRequest as e:
            update.message.reply_text(f"Error unmuting user: {e.message}")

    def check_spam(self, update: Update, context: CallbackContext) -> None:
        """Check messages for spam content."""
        message = update.message
        if not message or not message.text:
            return

        user = message.from_user
        if user.id in self.banned_users:
            message.delete()
            return

        text = message.text.lower()
        if any(keyword.lower() in text for keyword in self.spam_keywords):
            message.delete()
            self.warn_user(update, context)

    def track_chat_members
