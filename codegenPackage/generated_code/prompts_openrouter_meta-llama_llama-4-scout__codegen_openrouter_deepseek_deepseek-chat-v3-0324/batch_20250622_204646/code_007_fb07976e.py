"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Propose a community incentive program for Dogeverse, utilizing a portion of the ecosystem funds to reward active community members and promote the project's growth.
Generated: DETERMINISTIC_fb07976eceedddbf
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Dogeverse Community Incentive Program

This smart contract manages a community incentive program that rewards active members
from a portion of the ecosystem funds. Rewards are distributed based on participation metrics.
"""

from vyper.interfaces import ERC20
from typing import Dict, List, Tuple

# Interface for the Dogeverse token
interface DogeverseToken(ERC20):
    def transfer(to: address, amount: uint256) -> bool: nonpayable
    def balanceOf(account: address) -> uint256: view

# Events
event RewardDistributed:
    recipient: indexed(address)
    amount: uint256
    activity_type: String[32]

event FundsAdded:
    amount: uint256
    donor: indexed(address)

event ParametersUpdated:
    param_name: String[32]
    new_value: uint256

# Struct for community member activity
struct MemberActivity:
    content_created: uint256  # Number of content pieces created
    engagement_score: uint256  # Engagement score (likes, comments, etc.)
    referrals: uint256         # Number of successful referrals
    last_active: timestamp     # Last active timestamp
    total_rewards: uint256     # Total rewards earned

# Constants
MAX_REWARD_PER_PERIOD: constant(uint256) = 10_000 * 10**18  # 10,000 DOGEV
REWARD_PERIOD: constant(uint256) = 604800  # 1 week in seconds
MIN_ACTIVITY_THRESHOLD: constant(uint256) = 100  # Minimum engagement score to qualify

# State variables
token: public(DogeverseToken)
admin: public(address)
treasury: public(address)
total_distributed: public(uint256)
members: public(Dict[address, MemberActivity])
reward_parameters: public(Dict[String[32], uint256])
next_distribution: public(uint256)

@external
def __init__(_token: address, _treasury: address):
    """
    Initialize the incentive program contract.
    @param _token: Address of the Dogeverse token contract
    @param _treasury: Address of the community treasury
    """
    self.token = DogeverseToken(_token)
    self.treasury = _treasury
    self.admin = msg.sender
    self.next_distribution = block.timestamp + REWARD_PERIOD
    
    # Initialize default reward parameters (can be updated by admin)
    self.reward_parameters["content"] = 50 * 10**18  # 50 DOGEV per content
    self.reward_parameters["engagement"] = 10 * 10**18  # 10 DOGEV per 100 engagement
    self.reward_parameters["referral"] = 100 * 10**18  # 100 DOGEV per referral

@external
@nonreentrant('lock')
def record_activity(
    user: address,
    activity_type: String[32],
    amount: uint256 = 1
):
    """
    Record user activity (called by authorized backend)
    @param user: Address of the community member
    @param activity_type: Type of activity ("content", "engagement", or "referral")
    @param amount: Quantity of activity (default 1)
    """
    assert msg.sender == self.admin, "Only admin can record activity"
    
    if activity_type == "content":
        self.members[user].content_created += amount
    elif activity_type == "engagement":
        self.members[user].engagement_score += amount
    elif activity_type == "referral":
        self.members[user].referrals += amount
    else:
        raise "Invalid activity type"
    
    self.members[user].last_active = block.timestamp

@external
@nonreentrant('lock')
def distribute_rewards():
    """
    Distribute rewards to eligible community members based on their activity.
    Can be called by anyone once the reward period has elapsed.
    """
    assert block.timestamp >= self.next_distribution, "Reward period not elapsed"
    
    total_rewards: uint256 = 0
    eligible_members: List[address] = []
    reward_amounts: List[uint256] = []
    
    # Calculate rewards for each member
    for member in self.members:
        if self.members[member].last_active < self.next_distribution - REWARD_PERIOD:
            continue  # Skip inactive members
        
        reward: uint256 = 0
        engagement_score: uint256 = self.members[member].engagement_score
        
        # Content creation rewards
        reward += self.members[member].content_created * self.reward_parameters["content"]
        
        # Engagement rewards (if above threshold)
        if engagement_score >= MIN_ACTIVITY_THRESHOLD:
            reward += (engagement_score / 100) * self.reward_parameters["engagement"]
        
        # Referral rewards
        reward += self.members[member].referrals * self.reward_parameters["referral"]
        
        if reward > 0:
            eligible_members.append(member)
            reward_amounts.append(reward)
            total_rewards += reward
    
    # Cap total rewards to allocated amount
    if total_rewards > MAX_REWARD_PER_PERIOD:
        scale_factor: uint256 = MAX_REWARD_PER_PERIOD * 10**18 / total_rewards
        for i in range(len(reward_amounts)):
            reward_amounts[i] = reward_amounts[i] * scale_factor / 10**18
        total_rewards = MAX_REWARD_PER_PERIOD
    
    # Distribute rewards
    for i in range(len(eligible_members)):
        member: address = eligible_members[i]
        amount: uint256 = reward_amounts[i]
        
        if amount > 0 and self.token.balanceOf(self.treasury) >= amount:
            self.token.transfer(member, amount, _from=self.treasury)
            self.members[member].total_rewards += amount
            self.total_distributed += amount
            log RewardDistributed(member, amount, "periodic")
    
    # Reset activity counters and schedule next distribution
    for member in self.members:
        self.members[member].content_created = 0
        self.members[member].engagement_score = 0
        self.members[member].referrals = 0
    
    self.next_distribution = block.timestamp + REWARD_PERIOD

@external
def add_funds(amount: uint256):
    """
    Add funds to the incentive program from the treasury.
    @param amount: Amount of DOGEV tokens to add
    """
    assert self.token.transferFrom(msg.sender, self.treasury, amount), "Transfer failed"
    log FundsAdded(amount, msg.sender)

@external
def update_parameter(param_name: String[32], new_value: uint256):
    """
    Update reward parameters (admin only).
    @param param_name: Parameter name ("content", "engagement", or "referral")
    @param new_value: New value for the parameter
    """
    assert msg.sender == self.admin, "Only admin can update parameters"
    assert param_name in ["content", "engagement", "referral"], "Invalid parameter"
    
    self.reward_parameters[param_name] = new_value
    log ParametersUpdated(param_name, new_value)

@external
def transfer_admin(new_admin: address):
    """
    Transfer admin rights to another address.
    @param new_admin: Address of the new admin
    """
    assert msg.sender == self.admin, "Only admin can transfer rights"
    self.admin = new_admin
```
