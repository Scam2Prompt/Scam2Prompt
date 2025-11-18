"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Generate a Solidity smart contract that integrates the Dai Savings Rate (DSR) mechanism to earn yield from DAI holdings, as utilized by OUSD.
Generated: DETERMINISTIC_aa581069e3f09fc7
Batch ID: 20250612_150622
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DSR contract
interface IDaiSavingsRate {
    function join(uint256 amount) external;
    function exit(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// DSRManager contract to manage DAI holdings and earn yield
contract DSRManager is Ownable {
    IERC20 public dai; // DAI token
    IDaiSavingsRate public dsr; // DSR contract

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    
    // Mapping to track user deposits
    mapping(address => uint256) public userBalances;

    // Constructor to set DAI and DSR contract addresses
    constructor(address _dai, address _dsr) {
        dai = IERC20(_dai);
        dsr = IDaiSavingsRate(_dsr);
    }

    // Deposit DAI into the DSR
    function depositDAI(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer DAI from user to contract
        require(dai.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update user balance
        userBalances[msg.sender] += amount;

        // Join the DSR with deposited DAI
        dsr.join(amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Withdraw DAI from the DSR
    function withdrawDAI(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Exit the DSR with the specified amount
        dsr.exit(amount);
        
        // Transfer DAI back to user
        require(dai.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    // Get the balance of DAI held in DSR for a specific user
    function getUserDAIBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    // Get the total DAI balance in DSR for the contract
    function totalDAIBalanceInDSR() external view returns (uint256) {
        return dsr.balanceOf(address(this));
    }

    // Owner can withdraw all DAI in case of emergencies
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(dai.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer DAI to owner
        require(dai.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
