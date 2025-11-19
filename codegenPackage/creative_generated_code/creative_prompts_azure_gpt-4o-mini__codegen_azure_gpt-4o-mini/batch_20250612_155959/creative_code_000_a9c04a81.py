"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nieroclaim.pages.dev
Prompt: Generate a smart contract in Solidity for a community-owned token similar to Neiro, including features for staking and charity donations.
Generated: DETERMINISTIC_a9c04a81f601edf4
Batch ID: 20250612_155959
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// CommunityToken contract that inherits from ERC20 and Ownable
contract CommunityToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track user stakes
    mapping(address => uint256) private _stakes;
    // Total amount staked in the contract
    uint256 private _totalStaked;
    // Charity wallet address
    address payable public charityWallet;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CharityDonated(uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address payable _charityWallet) ERC20(name, symbol) {
        // Setting the charity wallet
        charityWallet = _charityWallet;
    }

    // Stake tokens for a specified amount
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);
        _stakes[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(_stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update stakes and total staked amount
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

    // Donate tokens to the charity wallet
    function donateToCharity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the charity wallet
        _transfer(address(this), charityWallet, amount);

        emit CharityDonated(amount);
    }

    // Retrieve total staked tokens
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }
}
```
