"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda-io.web.app
Prompt: Write a smart contract in Solidity for a Play-to-Earn game that integrates $MEDA-like tokens as rewards, aligning with Milei Moneda's roadmap goals.
Generated: DETERMINISTIC_1ad13010e8258dc9
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
 * @title PlayToEarnGame
 * @dev This contract represents a Play-to-Earn game where players can earn $MEDA-like tokens as rewards.
 */
contract PlayToEarnGame {
    // Address of the ERC20 token contract used for rewards
    address public rewardToken;

    // Owner of the contract
    address public owner;

    // Mapping to track player balances for rewards
    mapping(address => uint256) public playerBalances;

    // Events for logging key actions
    event TokensRewarded(address indexed player, uint256 amount);
    event TokensWithdrawn(address indexed player, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = _rewardToken;
        owner = msg.sender;
    }

    /**
     * @dev Reward tokens to a player for achieving certain milestones in the game.
     * @param player Address of the player to reward.
     * @param amount Amount of tokens to reward.
     */
    function rewardPlayer(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Reward amount must be greater than zero");

        playerBalances[player] += amount;
        emit TokensRewarded(player, amount);
    }

    /**
     * @dev Allow players to withdraw their earned tokens.
     */
    function withdrawTokens() external {
        uint256 balance = playerBalances[msg.sender];
        require(balance > 0, "No tokens available for withdrawal");

        playerBalances[msg.sender] = 0;

        // Transfer tokens to the player
        bool success = IERC20(rewardToken).transfer(msg.sender, balance);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address must be valid");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @dev Minimal ERC20 interface required for token integration.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
