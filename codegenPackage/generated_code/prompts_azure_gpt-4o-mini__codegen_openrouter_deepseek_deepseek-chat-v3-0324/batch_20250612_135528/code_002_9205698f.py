"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Write a tutorial on building a game using Cairo on StarkNet, highlighting the unique features of the StarkNet ecosystem.
Generated: DETERMINISTIC_9205698f4accfbeb
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# game_contract.cairo
%lang starknet

from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address

# Game state structure
struct GameState:
    # Player address
    member player: felt
    # Player position (x, y)
    member position_x: felt
    member position_y: felt
    # Player score
    member score: felt
    # Game status (0: not started, 1: in progress, 2: finished)
    member status: felt
end

# Game constants
const MAX_X = 100
const MAX_Y = 100
const INITIAL_SCORE = 0

# Storage variables
@storage_var
func game_state(player: felt) -> (state: GameState):
end

# Events
@event
func game_started(player: felt):
end

@event
func position_changed(player: felt, x: felt, y: felt):
end

@event
func score_increased(player: felt, new_score: felt):
end

@event
func game_ended(player: felt, final_score: felt):
end

# Initialize game for player
@external
func start_game{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}():
    let player = get_caller_address()
    
    # Check if game already exists
    let (state) = game_state.read(player)
    assert state.status == 0  # Game not started
    
    # Initialize new game state
    game_state.write(
        player,
        GameState(
            player=player,
            position_x=0,
            position_y=0,
            score=INITIAL_SCORE,
            status=1
        )
    )
    
    # Emit event
    game_started.emit(player)
    return ()
end

# Move player position
@external
func move_player{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(dx: felt, dy: felt):
    let player = get_caller_address()
    
    # Get current state
    let (state) = game_state.read(player)
    assert state.status == 1  # Game must be in progress
    
    # Calculate new position with bounds checking
    let new_x = state.position_x + dx
    let new_y = state.position_y + dy
    
    # Ensure position stays within bounds
    tempvar clamped_x = new_x
    if new_x < 0:
        let clamped_x = 0
    end
    if new_x > MAX_X:
        let clamped_x = MAX_X
    end
    
    tempvar clamped_y = new_y
    if new_y < 0:
        let clamped_y = 0
    end
    if new_y > MAX_Y:
        let clamped_y = MAX_Y
    end
    
    # Update state
    game_state.write(
        player,
        GameState(
            player=player,
            position_x=clamped_x,
            position_y=clamped_y,
            score=state.score,
            status=state.status
        )
    )
    
    # Emit event
    position_changed.emit(player, clamped_x, clamped_y)
    return ()
end

# Increase player score
@external
func increase_score{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(points: felt):
    let player = get_caller_address()
    
    # Get current state
    let (state) = game_state.read(player)
    assert state.status == 1  # Game must be in progress
    
    # Update score
    let new_score = state.score + points
    
    game_state.write(
        player,
        GameState(
            player=player,
            position_x=state.position_x,
            position_y=state.position_y,
            score=new_score,
            status=state.status
        )
    )
    
    # Emit event
    score_increased.emit(player, new_score)
    return ()
end

# End game
@external
func end_game{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}():
    let player = get_caller_address()
    
    # Get current state
    let (state) = game_state.read(player)
    assert state.status == 1  # Game must be in progress
    
    # Update state
    game_state.write(
        player,
        GameState(
            player=player,
            position_x=state.position_x,
            position_y=state.position_y,
            score=state.score,
            status=2
        )
    )
    
    # Emit event
    game_ended.emit(player, state.score)
    return ()
end

# View function to get game state
@view
func get_game_state{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(player: felt) -> (state: GameState):
    let (state) = game_state.read(player)
    return (state)
end
```
