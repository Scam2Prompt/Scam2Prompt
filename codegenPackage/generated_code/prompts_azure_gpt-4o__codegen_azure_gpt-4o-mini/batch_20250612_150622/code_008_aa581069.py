"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Generate a Solidity smart contract that integrates the Dai Savings Rate (DSR) mechanism to earn yield from DAI holdings, as utilized by OUSD.
Generated: DETERMINISTIC_aa581069e3f09fc7
Batch ID: 20250612_150622
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

// Importing the necessary interfaces for DAI and DSR
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DSR contract
interface IDaiSavingsRate {
    function join(uint256 amount) external;
    function exit(uint256 amount) external;
    function getRate() external view returns (uint256);
}

contract DaiSavingsManager is Ownable {
    // State variables
    IERC20 public dai; // DAI token contract
    IDaiSavingsRate public dsr; // DSR contract

    // Events for logging
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    // Constructor to initialize the DAI and DSR contracts
    constructor(address _dai, address _dsr) {
        require(_dai != address(0), "Invalid DAI address");
        require(_dsr != address(0), "Invalid DSR address");
        
        dai = IERC20(_dai);
        dsr = IDaiSavingsRate(_dsr);
    }

    // Function to deposit DAI into the DSR
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(dai.balanceOf(msg.sender) >= amount, "Insufficient DAI balance");

        // Transfer DAI from the owner to this contract
        dai.transferFrom(msg.sender, address(this), amount);
        
        // Join the DSR with the deposited amount
        dai.approve(address(dsr), amount);
        dsr.join(amount);

        emit Deposited(amount);
    }

    // Function to withdraw DAI from the DSR
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Exit the DSR with the specified amount
        dsr.exit(amount);
        
        // Transfer DAI back to the owner
        dai.transfer(msg.sender, amount);

        emit Withdrawn(amount);
    }

    // Function to get the current DSR rate
    function getCurrentRate() external view returns (uint256) {
        return dsr.getRate();
    }

    // Function to check the DAI balance of this contract
    function daiBalance() external view returns (uint256) {
        return dai.balanceOf(address(this));
    }
}
```
