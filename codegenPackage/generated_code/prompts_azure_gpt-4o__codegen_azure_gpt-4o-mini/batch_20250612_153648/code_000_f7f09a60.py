"""
Generated Code Metadata:
========================
Original URL: https://dogodoges.pages.dev
Prompt: Write a smart contract in Solidity for an ERC-20 token similar to $DOGO, including features for staking and governance as described in the Dogodoge ecosystem.
Generated: DETERMINISTIC_f7f09a60c420b2fa
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// ERC20Token is an implementation of the ERC20 standard with staking and governance features
contract ERC20Token is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("DogoDoge Token", "DOGO") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to the contract owner
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to view total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Governance function to allow the owner to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _mint(to, amount);
    }

    // Governance function to allow the owner to burn tokens
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
    }
}
```
