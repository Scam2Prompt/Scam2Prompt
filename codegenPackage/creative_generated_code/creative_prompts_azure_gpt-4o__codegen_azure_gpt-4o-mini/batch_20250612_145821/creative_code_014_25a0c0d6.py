"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepeunchained.pages.dev
Prompt: Write a guide for creating a decentralized application (dApp) for buying and staking $PEPU tokens on Pepe Unchained Layer 2 blockchain.
Generated: DETERMINISTIC_25a0c0d62d6784c3
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 contract for $PEPU token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Contract for the $PEPU token
contract PepeToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("Pepe Token", "$PEPU") {
        _mint(msg.sender, initialSupply);
    }

    // Function to mint new tokens, only owner can call this
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}

// Contract for staking $PEPU tokens
contract PepeStaking is ReentrancyGuard, Ownable {
    // Mapping to track each user's staked balance
    mapping(address => uint256) public stakedBalances;
    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reference to the PepeToken contract
    PepeToken public pepuToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the $PEPU token contract address
    constructor(address _pepuTokenAddress) {
        pepuToken = PepeToken(_pepuTokenAddress);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient $PEPU balance");

        // Transfer $PEPU tokens to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's staked balance and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer $PEPU tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```

This code provides a simple dApp structure for buying and staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain. It includes an ERC20 token contract and a staking contract with basic functionalities, ensuring error handling and following best practices.
