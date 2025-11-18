"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue-interface.netlify.app
Prompt: Create a function in Solidity to interact with the Morpho protocol for managing deposits and borrowing transactions.
Generated: DETERMINISTIC_f63d004a6e2f4c81
Batch ID: 20250612_155032
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

// Interface for Morpho Protocol
interface IMorpho {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
}

contract MorphoManager {
    IMorpho public morpho; // Instance of the Morpho Protocol

    // Event emitted when funds are supplied
    event Supplied(address indexed user, address indexed asset, uint256 amount);
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);
    // Event emitted when a borrow occurs
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    // Event emitted when a repayment occurs
    event Repaid(address indexed user, address indexed asset, uint256 amount);

    // Constructor to set the Morpho Protocol address
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Morpho address cannot be zero");
        morpho = IMorpho(_morphoAddress);
    }

    // Function to supply assets to the Morpho Protocol
    function supply(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer asset to this contract
        require(ERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Approve the Morpho protocol to spend the assets
        ERC20(asset).approve(address(morpho), amount);

        // Supply the assets to the Morpho protocol
        morpho.supply(asset, amount);

        emit Supplied(msg.sender, asset, amount);
    }

    // Function to withdraw assets from the Morpho Protocol
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw assets from Morpho
        morpho.withdraw(asset, amount);
        
        // Transfer assets back to user
        require(ERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to borrow assets from the Morpho Protocol
    function borrow(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Borrow assets from Morpho
        morpho.borrow(asset, amount);
        
        // Transfer borrowed assets to user
        require(ERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Borrowed(msg.sender, asset, amount);
    }

    // Function to repay borrowed assets to the Morpho Protocol
    function repay(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer assets from user to this contract
        require(ERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the Morpho protocol to spend the repayment amount
        ERC20(asset).approve(address(morpho), amount);

        // Repay the borrowed assets
        morpho.repay(asset, amount);

        emit Repaid(msg.sender, asset, amount);
    }
}

// ERC20 Interface
interface ERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
