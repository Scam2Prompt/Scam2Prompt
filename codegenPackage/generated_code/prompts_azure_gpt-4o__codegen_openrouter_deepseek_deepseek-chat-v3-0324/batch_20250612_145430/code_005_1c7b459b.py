"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Develop a smart contract for a GameFi application on StarkNet L2, using resources from the StarkNet ecosystem.
Generated: DETERMINISTIC_1c7b459b81a82d8e
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.math import assert_nn_le, assert_nn
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address

# Storage variables
@storage_var
func player_scores(address: felt) -> (score: felt):
end

@storage_var
func game_state() -> (state: felt):
end

@storage_var
func owner() -> (owner_address: felt):
end

# Constants
const GAME_ACTIVE = 1
const GAME_PAUSED = 0
const MIN_SCORE = 0
const MAX_SCORE = 1000
const SCORE_INCREMENT = 10

# Events
@event
func score_updated(player: felt, new_score: felt):
end

@event
func game_state_changed(new_state: felt):
end

# Contract constructor
@constructor
func constructor{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    # Set contract deployer as owner
    let (deployer) = get_caller_address()
    owner.write(deployer)
    # Initialize game as active
    game_state.write(GAME_ACTIVE)
    return ()
end

# Modifier to check if caller is owner
func only_owner{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    let (caller) = get_caller_address()
    let (current_owner) = owner.read()
    assert caller = current_owner
    return ()
end

# Modifier to check if game is active
func game_active{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    let (state) = game_state.read()
    assert state = GAME_ACTIVE
    return ()
end

# Update player score
@external
func update_score{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(amount: felt):
    # Check game is active
    game_active()

    # Validate score increment
    assert_nn(amount)
    assert_nn_le(amount, SCORE_INCREMENT)

    # Get player address and current score
    let (player) = get_caller_address()
    let (current_score) = player_scores.read(player)

    # Calculate new score with bounds checking
    let new_score = current_score + amount
    assert_nn_le(new_score, MAX_SCORE)

    # Update storage and emit event
    player_scores.write(player, new_score)
    score_updated.emit(player, new_score)
    return ()
end

# Get player score
@view
func get_score{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(player: felt) -> (score: felt):
    let (score) = player_scores.read(player)
    return (score)
end

# Pause game (owner only)
@external
func pause_game{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    only_owner()
    game_state.write(GAME_PAUSED)
    game_state_changed.emit(GAME_PAUSED)
    return ()
end

# Resume game (owner only)
@external
func resume_game{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    only_owner()
    game_state.write(GAME_ACTIVE)
    game_state_changed.emit(GAME_ACTIVE)
    return ()
end

# Transfer ownership (owner only)
@external
func transfer_ownership{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(new_owner: felt):
    only_owner()
    owner.write(new_owner)
    return ()
end
```
