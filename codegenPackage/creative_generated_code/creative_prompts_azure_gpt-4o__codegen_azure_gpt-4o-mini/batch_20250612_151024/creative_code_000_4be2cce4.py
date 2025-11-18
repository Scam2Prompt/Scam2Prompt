"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gen-da6.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token similar to "$ENTS," including functionality for tokenomics and rewards distribution.
Generated: DETERMINISTIC_4be2cce457ff2382
Batch ID: 20250612_151024
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

// Import ERC20 and Ownable contracts from OpenZeppelin for standard functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ENTS Token Contract
 * @dev Implementation of a basic ERC20 token with tokenomics and rewards distribution.
 */
contract ENTS is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals
    
    // Reward distribution variables
    uint256 public rewardPool;
    uint256 public rewardPercentage = 5; // 5% distributed as rewards
    
    // Events for logging
    event RewardsDistributed(address indexed to, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     */
    constructor() ERC20("ENTS Token", "ENTS") {
        _mint(msg.sender, MAX_SUPPLY); // Mint the total supply to the owner
    }

    /**
     * @dev Override the _transfer function to include reward distribution logic.
     * @param from The address sending the tokens.
     * @param to The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Calculate the reward to distribute
        uint256 reward = (amount * rewardPercentage) / 100;
        rewardPool += reward; // Add reward to the pool
        super._transfer(from, to, amount - reward); // Transfer the net amount
    }

    /**
     * @dev Allows the owner to distribute rewards from the reward pool.
     * @param recipient The address to receive the rewards.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(amount <= rewardPool, "Insufficient reward pool");

        rewardPool -= amount; // Deduct the amount from the pool
        _mint(recipient, amount); // Mint new tokens as rewards
        
        emit RewardsDistributed(recipient, amount); // Emit event for logging
    }

    /**
     * @dev Function to change the reward percentage.
     * @param newPercentage The new reward percentage to set.
     */
    function setRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Percentage cannot exceed 100");
        rewardPercentage = newPercentage; // Update the reward percentage
    }

    /**
     * @dev Function to withdraw tokens mistakenly sent to the contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount); // Transfer tokens to owner
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Cannot send Ether to this contract");
    }
}
```
