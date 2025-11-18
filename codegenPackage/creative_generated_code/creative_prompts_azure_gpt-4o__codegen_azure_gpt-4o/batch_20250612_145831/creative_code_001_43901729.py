"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soonverse.pages.dev
Prompt: Generate code using Solidity to create a smart contract that integrates $SOON token functionality for a play-to-earn Web3 game.
Generated: DETERMINISTIC_439017294514874c
Batch ID: 20250612_145831
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
 * @dev This contract integrates $SOON token functionality for a play-to-earn game.
 *      Players earn $SOON tokens for completing actions in the game.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PlayToEarnGame {
    // Address of the $SOON token contract
    IERC20 public soonToken;

    // Owner of the contract
    address public owner;

    // Mapping to track player earnings
    mapping(address => uint256) public playerEarned;

    // Events
    event TokensEarned(address indexed player, uint256 amount);
    event TokensWithdrawn(address indexed player, uint256 amount);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the $SOON token contract address and set the contract owner.
     * @param tokenAddress Address of the $SOON token contract
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        soonToken = IERC20(tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to reward players with $SOON tokens.
     * @param player Address of the player to reward
     * @param amount Amount of $SOON tokens to reward
     */
    function rewardPlayer(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Player address cannot be zero");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update player earnings
        playerEarned[player] += amount;

        emit TokensEarned(player, amount);
    }

    /**
     * @dev Function for players to withdraw their earned $SOON tokens.
     */
    function withdrawEarnings() external {
        uint256 amount = playerEarned[msg.sender];
        require(amount > 0, "No earnings to withdraw");
        require(soonToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Reset player earnings
        playerEarned[msg.sender] = 0;

        // Transfer $SOON tokens to the player
        require(soonToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw remaining tokens from the contract.
     * @param amount Amount of $SOON tokens to withdraw
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(soonToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer $SOON tokens to the owner
        require(soonToken.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept incoming $SOON token transfers.
     */
    receive() external payable {
        revert("Contract does not accept native currency");
    }
}
```
