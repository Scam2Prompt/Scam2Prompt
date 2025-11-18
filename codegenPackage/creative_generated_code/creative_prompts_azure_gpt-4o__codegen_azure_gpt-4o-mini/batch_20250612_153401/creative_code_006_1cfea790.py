"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda.pages.dev
Prompt: Develop a Solidity smart contract for a Play-to-Earn game that integrates token usage options, modeled after the features planned in Stage 4 of the Milei Moneda roadmap.
Generated: DETERMINISTIC_1cfea790b0cccfaa
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin contracts for safe token handling and ownership
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The PlayToEarnGame contract allows players to earn tokens through gameplay
contract PlayToEarnGame is Ownable {
    // Token used in the game
    IERC20 public gameToken;

    // Struct to represent a player in the game
    struct Player {
        uint256 score;
        uint256 rewards;
        bool exists;
    }

    // Mapping of player addresses to Player structs
    mapping(address => Player) private players;

    // Event emitted when a player earns rewards
    event RewardsEarned(address indexed player, uint256 amount);

    // Constructor to initialize the game token address
    constructor(address _gameToken) {
        require(_gameToken != address(0), "Invalid token address");
        gameToken = IERC20(_gameToken);
    }

    // Function to register a player
    function registerPlayer() external {
        require(!players[msg.sender].exists, "Player already registered");
        
        // Initialize player's score and rewards
        players[msg.sender] = Player(0, 0, true);
    }

    // Function to simulate playing the game and earning rewards
    function playGame(uint256 _score) external {
        require(players[msg.sender].exists, "Player not registered");
        require(_score > 0, "Score must be greater than zero");

        // Update player's score
        players[msg.sender].score += _score;

        // Calculate rewards based on score
        uint256 rewards = _score * 10; // Example: 10 tokens per score point
        players[msg.sender].rewards += rewards;

        // Emit an event for rewards earned
        emit RewardsEarned(msg.sender, rewards);
    }

    // Function for players to claim their rewards
    function claimRewards() external {
        require(players[msg.sender].exists, "Player not registered");
        
        uint256 rewards = players[msg.sender].rewards;
        require(rewards > 0, "No rewards to claim");

        // Reset player's rewards to zero
        players[msg.sender].rewards = 0;

        // Transfer rewards to the player
        require(gameToken.transfer(msg.sender, rewards), "Token transfer failed");
    }

    // Function to check player's score and rewards
    function getPlayerInfo(address _player) external view returns (uint256 score, uint256 rewards) {
        require(players[_player].exists, "Player not registered");
        score = players[_player].score;
        rewards = players[_player].rewards;
    }

    // Function to withdraw tokens from the contract in case of emergency
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(gameToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer tokens to the specified address
        require(gameToken.transfer(_to, _amount), "Token transfer failed");
    }
}
```
