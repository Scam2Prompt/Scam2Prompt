"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicgame.pages.dev
Prompt: Provide an example of using Sonic's composable gaming primitives and sandbox utilities to build business logic for an on-chain game.
Generated: DETERMINISTIC_aa9056c00c01d3c8
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules from Sonic's composable gaming primitives
import { Game, Entity, Action, Sandbox } from 'sonic-gaming-sdk';

// Define the Game class that will manage the game logic
class OnChainGame extends Game {
    constructor() {
        super();
        
        // Initialize game entities
        this.player = new Entity('player', { x: 0, y: 0 });
        this.enemy = new Entity('enemy', { x: 5, y: 5 });
        
        // Use sandbox for managing the game state and interactions
        this.sandbox = new Sandbox();
    }

    // Function to initialize the game
    init() {
        this.sandbox.registerEntity(this.player);
        this.sandbox.registerEntity(this.enemy);
        console.log('Game initialized with player and enemy entities.');
    }

    // Function to handle player actions
    handleAction(action) {
        try {
            switch (action.type) {
                case 'move':
                    this.moveEntity(this.player, action.payload);
                    break;
                case 'attack':
                    this.attackEntity(this.player, this.enemy);
                    break;
                default:
                    throw new Error('Invalid action type');
            }
        } catch (error) {
            console.error('Error handling action:', error.message);
        }
    }

    // Function to move an entity
    moveEntity(entity, direction) {
        if (!['up', 'down', 'left', 'right'].includes(direction)) {
            throw new Error('Invalid move direction');
        }

        // Update the entity's position based on direction
        switch (direction) {
            case 'up':
                entity.position.y += 1;
                break;
            case 'down':
                entity.position.y -= 1;
                break;
            case 'left':
                entity.position.x -= 1;
                break;
            case 'right':
                entity.position.x += 1;
                break;
        }

        console.log(`${entity.name} moved ${direction} to position:`, entity.position);
    }

    // Function for attacking an entity
    attackEntity(attacker, target) {
        // Simple damage logic for demonstration
        const damage = 1;
        target.health = (target.health || 10) - damage;

        console.log(`${attacker.name} attacked ${target.name}. ${target.name} health: ${target.health}`);
        
        if (target.health <= 0) {
            console.log(`${target.name} has been defeated!`);
        }
    }
}

// Example of using the OnChainGame class
const game = new OnChainGame();
game.init();

// Simulate player actions
game.handleAction({ type: 'move', payload: 'up' });
game.handleAction({ type: 'attack' });
game.handleAction({ type: 'move', payload: 'right' });
game.handleAction({ type: 'attack' });

// Handle invalid action to demonstrate error handling
game.handleAction({ type: 'invalidAction' });
```
