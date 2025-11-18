"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangepepe.pages.dev
Prompt: Develop a smart contract in Solidity for a play-to-win game where players earn $ORPE tokens based on their weekly high scores.
Generated: DETERMINISTIC_ce9ee281acea4183
Batch ID: 20250612_150018
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

// Importing the ERC20 interface for the ORPE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PlayToWin {
    // State variables
    IERC20 public orpeToken; // ORPE token contract
    address public owner; // Contract owner
    uint256 public rewardAmount; // Amount of tokens rewarded for a high score

    // Struct to hold player information
    struct Player {
        uint256 highScore; // Player's high score
        uint256 lastClaimed; // Timestamp of last claim
    }

    // Mapping from player address to Player struct
    mapping(address => Player) public players;

    // Event to emit when a new high score is set
    event NewHighScore(address indexed player, uint256 score);

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _orpeToken, uint256 _rewardAmount) {
        require(_orpeToken != address(0), "Invalid token address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        
        orpeToken = IERC20(_orpeToken);
        rewardAmount = _rewardAmount;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to submit a new high score
    function submitScore(uint256 score) external {
        require(score > 0, "Score must be greater than zero");

        Player storage player = players[msg.sender];
        bool newHighScore = false;

        // Check if the new score is higher than the previous high score
        if (score > player.highScore) {
            player.highScore = score; // Update high score
            newHighScore = true;
            emit NewHighScore(msg.sender, score); // Emit event for new high score
        }

        // Reward the player if they set a new high score
        if (newHighScore) {
            require(orpeToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
            orpeToken.transfer(msg.sender, rewardAmount); // Transfer ORPE tokens to player
            player.lastClaimed = block.timestamp; // Update last claimed timestamp
        }
    }

    // Function to withdraw tokens from the contract (only for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(orpeToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        orpeToken.transfer(owner, amount); // Transfer tokens to the owner
    }

    // Function to set the reward amount (only for the owner)
    function setRewardAmount(uint256 _rewardAmount) external onlyOwner {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _rewardAmount; // Update the reward amount
    }

    // Function to get player info
    function getPlayerInfo(address playerAddress) external view returns (uint256 highScore, uint256 lastClaimed) {
        Player storage player = players[playerAddress];
        return (player.highScore, player.lastClaimed);
    }
}
```
