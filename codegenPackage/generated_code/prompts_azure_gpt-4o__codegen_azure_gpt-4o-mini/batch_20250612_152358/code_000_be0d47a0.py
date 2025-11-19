"""
Generated Code Metadata:
========================
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that integrates Moonwell's lending protocol for supplying assets and earning interest, ensuring compatibility with Moonbeam and Moonriver networks.
Generated: DETERMINISTIC_be0d47a0070c875d
Batch ID: 20250612_152358
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

// Importing the necessary interfaces from Moonwell's lending protocol
import "@moonwell/contract-interfaces/IWETH.sol";
import "@moonwell/contract-interfaces/IMoonwell.sol";

contract MoonwellLending {
    // State variables
    IMoonwell public moonwell; // Moonwell lending protocol interface
    IWETH public weth; // Wrapped Ether interface

    // Events
    event Supplied(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event InterestEarned(address indexed user, uint256 interest);

    // Constructor to initialize the contract with Moonwell and WETH addresses
    constructor(address _moonwell, address _weth) {
        require(_moonwell != address(0), "Invalid Moonwell address");
        require(_weth != address(0), "Invalid WETH address");
        
        moonwell = IMoonwell(_moonwell);
        weth = IWETH(_weth);
    }

    // Function to supply assets to Moonwell and earn interest
    function supply(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer WETH from user to this contract
        weth.transferFrom(msg.sender, address(this), amount);
        
        // Approve Moonwell to spend the WETH
        weth.approve(address(moonwell), amount);
        
        // Supply WETH to Moonwell
        moonwell.supply(address(weth), amount);
        
        emit Supplied(msg.sender, amount);
    }

    // Function to withdraw supplied assets from Moonwell
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw WETH from Moonwell
        moonwell.withdraw(address(weth), amount);
        
        // Transfer WETH back to the user
        weth.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim interest earned on supplied assets
    function claimInterest() external {
        // Logic to claim interest can be implemented here
        // This is a placeholder for future implementation
        uint256 interest = moonwell.claimInterest(msg.sender);
        
        require(interest > 0, "No interest to claim");
        
        // Transfer the claimed interest to the user
        weth.transfer(msg.sender, interest);
        
        emit InterestEarned(msg.sender, interest);
    }

    // Function to get the balance of WETH held by this contract
    function getWETHBalance() external view returns (uint256) {
        return weth.balanceOf(address(this));
    }
}
```
