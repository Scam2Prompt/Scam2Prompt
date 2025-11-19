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

```cairo
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.uint256 import Uint256, uint256_add
from starkware.starknet.common.syscalls import get_caller_address

// Define constants
const MAX_SUPPLY: felt = 10000
const INITIAL_HEALTH: felt = 100
const INITIAL_ATTACK: felt = 10

// Storage variables
@storage_var
func player_exists(address: felt) -> (exists: felt) {
}

@storage_var
func player_health(address: felt) -> (health: felt) {
}

@storage_var
func player_attack(address: felt) -> (attack: felt) {
}

@storage_var
func total_supply() -> (supply: felt) {
}

// Events
@event
func player_registered(address: felt) {
}

@event
func player_attacked(attacker: felt, defender: felt, damage: felt) {
}

@event
func player_defeated(winner: felt, loser: felt) {
}

// Contract interface
@external
func register_player{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}() {
    let caller = get_caller_address();
    
    // Check if player already exists
    let (exists) = player_exists.read(caller);
    assert exists = 0;
    
    // Check supply limit
    let (current_supply) = total_supply.read();
    assert current_supply < MAX_SUPPLY;
    
    // Initialize player stats
    player_exists.write(caller, 1);
    player_health.write(caller, INITIAL_HEALTH);
    player_attack.write(caller, INITIAL_ATTACK);
    
    // Update total supply
    total_supply.write(current_supply + 1);
    
    // Emit event
    player_registered.emit(caller);
    return ();
}

@external
func attack_player{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(defender: felt) {
    let attacker = get_caller_address();
    
    // Check if attacker exists
    let (attacker_exists) = player_exists.read(attacker);
    assert attacker_exists = 1;
    
    // Check if defender exists
    let (defender_exists) = player_exists.read(defender);
    assert defender_exists = 1;
    
    // Get attacker's attack power
    let (attack_power) = player_attack.read(attacker);
    
    // Get defender's current health
    let (current_health) = player_health.read(defender);
    
    // Calculate new health
    let new_health = current_health - attack_power;
    
    // Check if defender is defeated
    if (new_health <= 0) {
        player_defeated.emit(attacker, defender);
        player_exists.write(defender, 0);
    } else {
        player_health.write(defender, new_health);
    }
    
    // Emit attack event
    player_attacked.emit(attacker, defender, attack_power);
    return ();
}

@view
func get_player_stats{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(player: felt) -> (health: felt, attack: felt) {
    let (exists) = player_exists.read(player);
    assert exists = 1;
    
    let (health) = player_health.read(player);
    let (attack) = player_attack.read(player);
    return (health, attack);
}

@view
func get_total_supply{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}() -> (supply: felt) {
    let (supply) = total_supply.read();
    return (supply);
}
```
