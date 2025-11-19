"""
Generated Code Metadata:
========================
Original URL: https://safe-app.morpho.dev
Prompt: Develop a smart contract that interacts with Morpho's V2 platform to automate lending and borrowing processes.
Generated: DETERMINISTIC_0fca0fed7941976b
Batch ID: 20250612_145444
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

// Importing necessary interfaces from Morpho's V2 platform
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

// Interface for Morpho's lending and borrowing functions
interface IMorpho {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
}

// Smart contract for automating lending and borrowing on Morpho's V2 platform
contract MorphoLending is Ownable, ReentrancyGuard {
    IMorpho public morpho; // Instance of Morpho's interface
    mapping(address => mapping(address => uint256)) public userBalances; // User balances for each asset

    // Event declarations for logging actions
    event Supplied(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);

    // Constructor to set the Morpho contract address
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morphoAddress);
    }

    // Function to supply assets to Morpho
    function supply(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance
        userBalances[msg.sender][asset] += amount;

        // Supply the asset to Morpho
        IERC20(asset).approve(address(morpho), amount);
        morpho.supply(asset, amount);

        emit Supplied(msg.sender, asset, amount);
    }

    // Function to withdraw assets from Morpho
    function withdraw(address asset, uint256 amount) external nonReentrant {
        require(userBalances[msg.sender][asset] >= amount, "Insufficient balance");

        // Withdraw the asset from Morpho
        morpho.withdraw(asset, amount);

        // Update user balance
        userBalances[msg.sender][asset] -= amount;

        // Transfer the asset back to the user
        require(IERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to borrow assets from Morpho
    function borrow(address asset, uint256 amount) external nonReentrant {
        // Borrow the asset from Morpho
        morpho.borrow(asset, amount);

        // Update user balance
        userBalances[msg.sender][asset] += amount;

        emit Borrowed(msg.sender, asset, amount);
    }

    // Function to repay borrowed assets to Morpho
    function repay(address asset, uint256 amount) external nonReentrant {
        require(userBalances[msg.sender][asset] >= amount, "Insufficient balance to repay");

        // Update user balance
        userBalances[msg.sender][asset] -= amount;

        // Transfer the asset from the user to the contract
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve and repay the borrowed amount to Morpho
        IERC20(asset).approve(address(morpho), amount);
        morpho.repay(asset, amount);

        emit Repaid(msg.sender, asset, amount);
    }

    // Function to set a new Morpho contract address (onlyOwner)
    function setMorphoAddress(address _morphoAddress) external onlyOwner {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morphoAddress);
    }
}
```
