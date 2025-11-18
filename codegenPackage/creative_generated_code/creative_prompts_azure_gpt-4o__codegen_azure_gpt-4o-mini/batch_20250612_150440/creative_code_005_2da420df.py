"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a Solidity contract that includes functionality for minting, staking, and withdrawing "FREE SHAVACADOO" tokens, ensuring proper security measures are implemented.
Generated: DETERMINISTIC_2da420dfed1a4869
Batch ID: 20250612_150440
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// The FreeShavacadoo token contract
contract FreeShavacadoo is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked amounts
    mapping(address => uint256) private _stakedAmounts;
    // Mapping to track whether an address is currently staking
    mapping(address => bool) private _isStaking;

    // Events for monitoring actions
    event Minted(address indexed to, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);
    
    // Constructor to set the token name and symbol
    constructor() ERC20("FREE SHAVACADOO", "FSA") {
        // Initially mint a supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to receive minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _mint(to, amount);
        emit Minted(to, amount);
    }

    /**
     * @dev Function to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from the caller to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakedAmounts[msg.sender] += amount;
        _isStaking[msg.sender] = true;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     */
    function withdraw() external nonReentrant {
        require(_isStaking[msg.sender], "You are not staking any tokens");
        uint256 amount = _stakedAmounts[msg.sender];

        require(amount > 0, "No tokens to withdraw");

        // Reset the staking status and amount
        _stakedAmounts[msg.sender] = 0;
        _isStaking[msg.sender] = false;

        // Transfer staked tokens back to the caller
        _transfer(address(this), msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to check the staked amount of a user.
     * @param staker The address of the staker.
     * @return The amount staked by the user.
     */
    function stakedAmount(address staker) external view returns (uint256) {
        return _stakedAmounts[staker];
    }
}
```
