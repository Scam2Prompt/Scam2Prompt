"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Write a smart contract in Solidity to manage the $BIGTIME token's functionality, including token distribution, transfer, and staking mechanisms, suitable for the Big Time game's economy.
Generated: DETERMINISTIC_1d3f4dac8c09e2ee
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for the $BIGTIME token
contract BigTimeToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;

    // Events for logging
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event TokensDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Big Time Token", "$BIGTIME") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to distribute rewards (for demonstration purposes)
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(owner()) >= amount, "Insufficient owner balance");

        // Transfer reward tokens to the user
        _transfer(owner(), user, amount);

        emit TokensDistributed(user, amount);
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens from the contract to the owner
        _transfer(address(this), owner(), amount);
    }
}
```
