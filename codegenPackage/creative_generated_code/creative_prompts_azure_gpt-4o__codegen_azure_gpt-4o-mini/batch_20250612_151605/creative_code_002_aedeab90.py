"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Provide a Solidity smart contract example for integrating Amnis Finance's liquid staking tokens (amAPT and stAPT) into a DeFi lending platform.
Generated: DETERMINISTIC_aedeab90e2654d6e
Batch ID: 20250612_151605
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

// Importing necessary interfaces for ERC20 token and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Amnis Finance liquid staking token
interface IAmnisToken {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// DeFi Lending Platform contract
contract DeFiLendingPlatform is Ownable {
    // State variables for the contract
    IAmnisToken public amAPT;      // Address of amAPT token
    IAmnisToken public stAPT;      // Address of stAPT token
    mapping(address => uint256) public balances; // User balances for lending

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set token addresses
    constructor(address _amAPT, address _stAPT) {
        require(_amAPT != address(0), "Invalid amAPT address");
        require(_stAPT != address(0), "Invalid stAPT address");

        amAPT = IAmnisToken(_amAPT);
        stAPT = IAmnisToken(_stAPT);
    }

    // Function to deposit amAPT tokens into the lending platform
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");
        
        // Transfer amAPT tokens from user to contract
        require(amAPT.balanceOf(msg.sender) >= amount, "Insufficient amAPT balance");
        require(amAPT.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw amAPT tokens from the lending platform
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer amAPT tokens back to user
        require(amAPT.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to stake user deposits in Amnis Finance
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance to stake");

        // Update user balance
        balances[msg.sender] -= amount;

        // Call the stake function of amAPT
        amAPT.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw stAPT tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        
        // Call the withdraw function of stAPT
        stAPT.withdraw(amount);

        // Transfer stAPT tokens back to user
        require(stAPT.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to check user's balance of amAPT
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to get total balance held by the contract
    function totalBalance() external view onlyOwner returns (uint256) {
        return amAPT.balanceOf(address(this));
    }
}
```
