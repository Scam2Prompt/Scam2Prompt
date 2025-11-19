"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-24m.pages.dev
Prompt: Create a smart contract in Solidity to manage the Dogeverse tokenomics, including token allocation, presale, and staking mechanisms.
Generated: DETERMINISTIC_bb8eb372b8a1cc0c
Batch ID: 20250622_204646
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

// DogeverseToken contract inherits from ERC20, Ownable, and ReentrancyGuard
contract DogeverseToken is ERC20, Ownable, ReentrancyGuard {
    // State variables for presale and staking
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public presalePrice;
    uint256 public totalSupplyCap;
    uint256 public totalStaked;
    
    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Events for logging important actions
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event PresalePurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token with name, symbol, and total supply cap
    constructor(string memory name, string memory symbol, uint256 _totalSupplyCap) 
        ERC20(name, symbol) 
    {
        totalSupplyCap = _totalSupplyCap * (10 ** decimals());
        _mint(msg.sender, totalSupplyCap); // Mint total supply to the owner
    }

    // Function to start the presale
    function startPresale(uint256 duration, uint256 price) external onlyOwner {
        presaleStart = block.timestamp;
        presaleEnd = presaleStart + duration;
        presalePrice = price;
    }

    // Function to purchase tokens during the presale
    function buyPresaleTokens(uint256 amount) external payable nonReentrant {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");
        require(totalSupply() + amount <= totalSupplyCap, "Exceeds total supply cap");

        _transfer(owner(), msg.sender, amount);
        emit PresalePurchased(msg.sender, amount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from user to contract for staking
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);
        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
