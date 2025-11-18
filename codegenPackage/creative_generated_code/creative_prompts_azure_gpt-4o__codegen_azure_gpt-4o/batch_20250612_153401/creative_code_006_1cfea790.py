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

/**
 * @title MileiMonedaGame
 * @dev Play-to-Earn game smart contract modeled after Stage 4 of the Milei Moneda roadmap.
 *      Players use tokens to participate in the game, earn rewards, and access additional features.
 */
contract MileiMonedaGame {
    // ERC20 token interface
    IERC20 public gameToken;

    // Owner of the smart contract
    address public owner;

    // Structure to track player details
    struct Player {
        uint256 balance; // Player's in-game token balance
        uint256 earnedRewards; // Rewards earned by the player
    }

    // Mapping of player address to Player struct
    mapping(address => Player) public players;

    // Event emitted when a player participates in the game
    event GamePlayed(address indexed player, uint256 tokensUsed, uint256 rewardEarned);

    // Event emitted when rewards are withdrawn
    event RewardsWithdrawn(address indexed player, uint256 rewardAmount);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract with the ERC20 token address
    constructor(address _gameToken) {
        require(_gameToken != address(0), "Invalid token address");
        gameToken = IERC20(_gameToken);
        owner = msg.sender;
    }

    /**
     * @dev Allows a player to participate in the game using tokens and earn rewards.
     * @param _tokensUsed Amount of tokens the player wants to use.
     * Reward is calculated as a multiplier of tokens used (e.g., 2x).
     */
    function playGame(uint256 _tokensUsed) external {
        require(_tokensUsed > 0, "Tokens used must be greater than zero");
        require(gameToken.balanceOf(msg.sender) >= _tokensUsed, "Insufficient token balance");

        // Transfer tokens from player to the contract
        bool success = gameToken.transferFrom(msg.sender, address(this), _tokensUsed);
        require(success, "Token transfer failed");

        // Calculate rewards (example: reward = 2x tokens used)
        uint256 reward = _tokensUsed * 2;

        // Update player's balance and rewards
        players[msg.sender].balance += _tokensUsed;
        players[msg.sender].earnedRewards += reward;

        // Emit event
        emit GamePlayed(msg.sender, _tokensUsed, reward);
    }

    /**
     * @dev Allows a player to withdraw their earned rewards.
     */
    function withdrawRewards() external {
        uint256 rewards = players[msg.sender].earnedRewards;
        require(rewards > 0, "No rewards available to withdraw");

        // Update player's reward balance
        players[msg.sender].earnedRewards = 0;

        // Transfer rewards to the player
        bool success = gameToken.transfer(msg.sender, rewards);
        require(success, "Reward transfer failed");

        // Emit event
        emit RewardsWithdrawn(msg.sender, rewards);
    }

    /**
     * @dev Allows the contract owner to withdraw tokens accumulated in the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(gameToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = gameToken.transfer(owner, _amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the contract owner to update the ERC20 token address.
     * @param _newTokenAddress New token address to set.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        gameToken = IERC20(_newTokenAddress);
    }
}

// Interface for ERC20 token functions used in the contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
