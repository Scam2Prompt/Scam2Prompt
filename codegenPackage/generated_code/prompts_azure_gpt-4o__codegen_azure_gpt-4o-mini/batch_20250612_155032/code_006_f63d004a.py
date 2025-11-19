"""
Generated Code Metadata:
========================
Original URL: https://blue-interface.netlify.app
Prompt: Create a function in Solidity to interact with the Morpho protocol for managing deposits and borrowing transactions.
Generated: DETERMINISTIC_f63d004a6e2f4c81
Batch ID: 20250612_155032
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

// Importing the Morpho protocol interface
import "@morpho.xyz/morpho-core/contracts/interfaces/IMorpho.sol";

contract MorphoManager {
    // Instance of the Morpho protocol interface
    IMorpho public morpho;

    // Event emitted when a deposit is made
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a borrow is made
    event Borrowed(address indexed user, uint256 amount);

    // Constructor to initialize the Morpho protocol address
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morphoAddress);
    }

    // Function to deposit assets into the Morpho protocol
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the asset from the user to this contract
        // Assuming the asset is an ERC20 token
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Approve the Morpho protocol to spend the deposited assets
        IERC20(asset).approve(address(morpho), amount);
        
        // Interact with the Morpho protocol to deposit the assets
        morpho.deposit(asset, amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Function to borrow assets from the Morpho protocol
    function borrow(address asset, uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");
        
        // Interact with the Morpho protocol to borrow the assets
        morpho.borrow(asset, amount);
        
        // Transfer the borrowed assets to the user
        IERC20(asset).transfer(msg.sender, amount);
        
        emit Borrowed(msg.sender, amount);
    }

    // Function to withdraw assets from the Morpho protocol
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        
        // Interact with the Morpho protocol to withdraw the assets
        morpho.withdraw(asset, amount);
        
        // Transfer the withdrawn assets to the user
        IERC20(asset).transfer(msg.sender, amount);
    }

    // Function to repay borrowed assets
    function repay(address asset, uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        
        // Transfer the asset from the user to this contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Approve the Morpho protocol to spend the repaid assets
        IERC20(asset).approve(address(morpho), amount);
        
        // Interact with the Morpho protocol to repay the borrowed assets
        morpho.repay(asset, amount);
    }
}
```
