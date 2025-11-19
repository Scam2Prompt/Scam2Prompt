"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Generate a Cairo code example for a simple NFT game on StarkNet, inspired by the Starknet Vietnam Community.
Generated: DETERMINISTIC_28646b6b5b5860fa
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
# StarkNet NFT Game Contract
# Author: StarkNet Vietnam Community-inspired example
# Description: A simple NFT game contract where players can mint NFTs and battle.

%lang starknet

# Import necessary libraries
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address, get_block_number
from starkware.starknet.common.storage import Storage

# Constants
const MAX_HEALTH = 100
const MAX_ATTACK = 20

# Storage variables
@storage_var
func nft_owner(nft_id: felt) -> felt:
end

@storage_var
func nft_health(nft_id: felt) -> felt:
end

@storage_var
func nft_attack(nft_id: felt) -> felt:
end

@storage_var
func nft_count() -> felt:
end

# Events
@event
func NFTMinted(nft_id: felt, owner: felt):
end

@event
func BattleResult(attacker_id: felt, defender_id: felt, winner_id: felt):
end

# Mint a new NFT
@external
func mint_nft() {
    # Get the caller's address
    let caller = get_caller_address()

    # Increment the NFT count
    let current_count = nft_count.read()
    let new_nft_id = current_count + 1
    nft_count.write(new_nft_id)

    # Assign default stats to the new NFT
    nft_owner.write(new_nft_id, caller)
    nft_health.write(new_nft_id, MAX_HEALTH)
    nft_attack.write(new_nft_id, MAX_ATTACK)

    # Emit the NFTMinted event
    emit NFTMinted(nft_id=new_nft_id, owner=caller)
}

# Battle between two NFTs
@external
func battle(attacker_id: felt, defender_id: felt) {
    # Validate ownership of the attacker NFT
    let caller = get_caller_address()
    let attacker_owner = nft_owner.read(attacker_id)
    assert attacker_owner == caller, "Caller does not own the attacker NFT"

    # Validate existence of the defender NFT
    let defender_owner = nft_owner.read(defender_id)
    assert defender_owner != 0, "Defender NFT does not exist"

    # Get stats for both NFTs
    let attacker_health = nft_health.read(attacker_id)
    let attacker_attack = nft_attack.read(attacker_id)
    let defender_health = nft_health.read(defender_id)
    let defender_attack = nft_attack.read(defender_id)

    # Simulate battle
    let attacker_new_health = attacker_health - defender_attack
    let defender_new_health = defender_health - attacker_attack

    # Update health stats
    nft_health.write(attacker_id, max(0, attacker_new_health))
    nft_health.write(defender_id, max(0, defender_new_health))

    # Determine winner
    let winner_id = if attacker_new_health > defender_new_health {
        attacker_id
    } else {
        defender_id
    }

    # Emit the BattleResult event
    emit BattleResult(attacker_id=attacker_id, defender_id=defender_id, winner_id=winner_id)
}

# Helper function to get NFT stats
@view
func get_nft_stats(nft_id: felt) -> (owner: felt, health: felt, attack: felt) {
    let owner = nft_owner.read(nft_id)
    let health = nft_health.read(nft_id)
    let attack = nft_attack.read(nft_id)
    return (owner, health, attack)
}
```
