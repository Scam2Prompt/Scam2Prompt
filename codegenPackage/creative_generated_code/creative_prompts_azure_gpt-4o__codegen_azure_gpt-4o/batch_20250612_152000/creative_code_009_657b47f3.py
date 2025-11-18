"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Provide example code for building a GameFi application on Metis Layer 2 that leverages its scalability and low gas fees.
Generated: DETERMINISTIC_657b47f3466e8b78
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * GameFi Application on Metis Layer 2
 * This example demonstrates a simple ERC-20 token contract and a GameFi reward system
 * leveraging Metis Layer 2 scalability and low gas fees.
 */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import OpenZeppelin contracts for security and standardization
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GameToken Contract - ERC-20 Token for GameFi rewards
contract GameToken is ERC20, Ownable {
    /**
     * @dev Constructor to initialize the token with name and symbol.
     * - Initial supply is minted to the deployer address.
     */
    constructor(uint256 initialSupply) ERC20("GameToken", "GT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mint new tokens. Only the owner can mint tokens.
     * @param to Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}

// GameFi Contract - Handles game logic and rewards using GameToken
contract GameFi {
    GameToken public gameToken;

    // Mapping to track player scores
    mapping(address => uint256) public playerScores;

    // Event emitted when a player receives a reward
    event RewardClaimed(address indexed player, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the GameFi contract.
     * @param tokenAddress Address of the deployed GameToken contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        gameToken = GameToken(tokenAddress);
    }

    /**
     * @dev Function to update the player's score (simulate a game action).
     * @param player Address of the player.
     * @param score Incremental score to add to the player.
     */
    function updateScore(address player, uint256 score) external {
        require(player != address(0), "Invalid player address");
        require(score > 0, "Score must be positive");

        playerScores[player] += score;
    }

    /**
     * @dev Function to claim rewards based on the player's score.
     * Rewards are proportional to the player's score (example: 1 token per score point).
     */
    function claimRewards() external {
        uint256 score = playerScores[msg.sender];
        require(score > 0, "No rewards available");

        // Calculate rewards based on the score
        uint256 rewardAmount = score;

        // Reset player's score after claiming rewards
        playerScores[msg.sender] = 0;

        // Transfer the reward tokens to the player
        require(
            gameToken.balanceOf(address(this)) >= rewardAmount,
            "Insufficient reward tokens"
        );

        gameToken.transfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function for the owner to deposit reward tokens into the contract.
     * @param amount Number of tokens to deposit.
     */
    function depositRewards(uint256 amount) external {
        require(amount > 0, "Amount must be positive");

        // Transfer tokens from the sender to this contract
        require(
            gameToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
    }
}
```
