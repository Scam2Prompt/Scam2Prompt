"""
Generated Code Metadata:
========================
Original URL: https://bitbot-8m4.pages.dev
Prompt: Create a governance mechanism for $BITBOT token holders to vote on strategic decisions, integrating it into a Telegram-based trading platform.
Generated: DETERMINISTIC_83141dbe3e3febbb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum
import json
import hashlib
from web3 import Web3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
    MessageHandler,
    Filters
)

# Configuration
CONFIG = {
    "contract_address": os.getenv("CONTRACT_ADDRESS"),
    "infura_url": os.getenv("INFURA_URL"),
    "telegram_token": os.getenv("TELEGRAM_TOKEN"),
    "admin_ids": json.loads(os.getenv("ADMIN_IDS", "[]")),
    "min_voting_power": float(os.getenv("MIN_VOTING_POWER", "100.0")),
    "voting_duration_days": int(os.getenv("VOTING_DURATION_DAYS", "7"))
}

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(CONFIG["infura_url"]))

# Load contract ABI
with open("BitbotGovernanceABI.json") as f:
    CONTRACT_ABI = json.load(f)

contract = w3.eth.contract(address=CONFIG["contract_address"], abi=CONTRACT_ABI)

class ProposalStatus(Enum):
    PENDING = "Pending"
    ACTIVE = "Active"
    PASSED = "Passed"
    REJECTED = "Rejected"
    EXECUTED = "Executed"

class Proposal:
    def __init__(
        self,
        proposal_id: int,
        title: str,
        description: str,
        creator: str,
        created_at: datetime,
        end_time: datetime,
        status: ProposalStatus,
        options: List[str],
        votes: Dict[str, int] = None
    ):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.creator = creator
        self.created_at = created_at
        self.end_time = end_time
        self.status = status
        self.options = options
        self.votes = votes or {option: 0 for option in options}

    def to_dict(self) -> Dict:
        return {
            "proposal_id": self.proposal_id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "created_at": self.created_at.isoformat(),
            "end_time": self.end_time.isoformat(),
            "status": self.status.value,
            "options": self.options,
            "votes": self.votes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Proposal':
        return cls(
            proposal_id=data["proposal_id"],
            title=data["title"],
            description=data["description"],
            creator=data["creator"],
            created_at=datetime.fromisoformat(data["created_at"]),
            end_time=datetime.fromisoformat(data["end_time"]),
            status=ProposalStatus(data["status"]),
            options=data["options"],
            votes=data["votes"]
        )

class GovernanceBot:
    def __init__(self):
        self.updater = Updater(CONFIG["telegram_token"])
        self.dispatcher = self.updater.dispatcher
        self.proposals: Dict[int, Proposal] = {}
        self.user_votes: Dict[str, Dict[int, str]] = {}  # {user_id: {proposal_id: option}}

        # Register handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("create_proposal", self.create_proposal))
        self.dispatcher.add_handler(CommandHandler("vote", self.vote))
        self.dispatcher.add_handler(CommandHandler("proposals", self.list_proposals))
        self.dispatcher.add_handler(CallbackQueryHandler(self.button_handler))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_message))

        # Load existing proposals
        self._load_proposals()

    def _load_proposals(self):
        try:
            with open("proposals.json", "r") as f:
                data = json.load(f)
                for proposal_id, proposal_data in data.items():
                    self.proposals[int(proposal_id)] = Proposal.from_dict(proposal_data)
        except FileNotFoundError:
            pass

    def _save_proposals(self):
        data = {str(pid): prop.to_dict() for pid, prop in self.proposals.items()}
        with open("proposals.json", "w") as f:
            json.dump(data, f, indent=2)

    def _get_user_voting_power(self, user_address: str) -> float:
        try:
            balance = contract.functions.balanceOf(user_address).call()
            decimals = contract.functions.decimals().call()
            voting_power = balance / (10 ** decimals)
            return voting_power
        except Exception as e:
            print(f"Error getting voting power: {e}")
            return 0.0

    def _verify_user_address(self, user_id: str, address: str) -> bool:
        # In a real implementation, this would verify the user owns the address
        # For demo purposes, we'll just check if it's a valid Ethereum address
        return Web3.isAddress(address)

    def _generate_proposal_id(self) -> int:
        return len(self.proposals) + 1

    def _update_proposal_statuses(self):
        now = datetime.now()
        for proposal in self.proposals.values():
            if proposal.status == ProposalStatus.ACTIVE and now >= proposal.end_time:
                total_votes = sum(proposal.votes.values())
                if total_votes > 0:
                    winning_option = max(proposal.votes.items(), key=lambda x: x[1])[0]
                    proposal.status = ProposalStatus.PASSED if winning_option != "Abstain" else ProposalStatus.REJECTED
                else:
                    proposal.status = ProposalStatus.REJECTED
        self._save_proposals()

    def start(self, update: Update, context: CallbackContext):
        user = update.effective_user
        update.message.reply_text(
            f"Welcome {user.first_name} to $BITBOT Governance!\n\n"
            "Available commands:\n"
            "/create_proposal - Create a new proposal (Admins only)\n"
            "/vote - Vote on active proposals\n"
            "/proposals - List all proposals\n\n"
            "Please register your Ethereum address to participate in governance."
        )

    def create_proposal(self, update: Update, context: CallbackContext):
        user = update.effective_user
        if str(user.id) not in CONFIG["admin_ids"]:
            update.message.reply_text("Only admins can create proposals.")
            return

        context.user_data["creating_proposal"] = True
        context.user_data["proposal_stage"] = "title"
        update.message.reply_text("Please enter the proposal title:")

    def handle_message(self, update: Update, context: CallbackContext):
        user = update.effective_user
        text = update.message.text

        if context.user_data.get("creating_proposal"):
            stage = context.user_data.get("proposal_stage")
            
            if stage == "title":
                context.user_data["proposal_title"] = text
                context.user_data["proposal_stage"] = "description"
                update.message.reply_text("Please enter the proposal description:")
            
            elif stage == "description":
                context.user_data["proposal_description"] = text
                context.user_data["proposal_stage"] = "options"
                update.message.reply_text(
                    "Please enter the voting options separated by commas (e.g., Yes,No,Abstain):"
                )
            
            elif stage == "options":
                options = [opt.strip() for opt in text.split(",") if opt.strip()]
                if len(options) < 2:
                    update.message.reply_text("Please provide at least 2 options.")
                    return
                
                proposal_id = self._generate_proposal_id()
                end_time = datetime.now() + timedelta(days=CONFIG["voting_duration_days"])
                
                proposal = Proposal(
                    proposal_id=proposal_id,
                    title=context.user_data["proposal_title"],
                    description=context.user_data["proposal_description"],
                    creator=user.first_name,
                    created_at=datetime.now(),
                    end_time=end_time,
                    status=ProposalStatus.ACTIVE,
                    options=options
                )
                
                self.proposals[proposal_id] = proposal
                self._save_proposals()
                
                del context.user_data["creating_proposal"]
                del context.user_data["proposal_stage"]
                
                update.message.reply_text(
                    f"Proposal #{proposal_id} created successfully!\n"
                    f"Title: {proposal.title}\n"
                    f"Voting ends on: {proposal.end_time.strftime('%Y-%m-%d %H:%M')}\n\n"
                    "Use /vote to participate in governance."
                )

    def vote(self, update: Update, context: CallbackContext):
        user = update.e
