"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Generate a smart contract for the PantherAI token using BEP20 standards, ensuring it includes features for staking and liquidity management.
Generated: DETERMINISTIC_4daaa70eb87f350d
Batch ID: 20250612_155446
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

// Import the OpenZeppelin contracts for BEP20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Contract for PantherAI Token
contract PantherAIToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track stakes of each address
    mapping(address => uint256) private _stakes;
    // Total amount staked
    uint256 private _totalStaked;

    // Events for staking and liquidity management
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event LiquidityAdded(address indexed user, uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("PantherAI", "PAI") {
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    // Stake tokens into the contract
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from user to this contract
        _transfer(msg.sender, address(this), amount);
        _stakes[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens from the contract
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakes[msg.sender] >= amount, "Insufficient staked balance to unstake");

        // Update stakes before transferring tokens back
        _stakes[msg.sender] -= amount;
        _totalStaked -= amount;
        
        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Get the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return _stakes[user];
    }

    // Get the total staked tokens in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to add liquidity (For demonstration purposes; assumes direct ETH transfer)
    function addLiquidity(uint256 tokenAmount) external payable nonReentrant {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(balanceOf(msg.sender) >= tokenAmount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        _transfer(msg.sender, address(this), tokenAmount);
        
        // Emit event for liquidity addition
        emit LiquidityAdded(msg.sender, tokenAmount, msg.value);
    }

    // Owner-only function to withdraw collected ETH
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    // Owner-only function to withdraw tokens
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");
        _transfer(address(this), owner(), amount);
    }
}
```
