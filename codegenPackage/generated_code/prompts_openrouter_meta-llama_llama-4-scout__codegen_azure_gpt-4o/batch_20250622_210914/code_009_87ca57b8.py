"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Outline a decentralized application (dApp) concept that leverages OUSD for stablecoin lending or borrowing, including how the dApp would interact with OUSD's smart contracts.
Generated: DETERMINISTIC_87ca57b8991926a3
Batch ID: 20250622_210914
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

/**
 * @title StableLend
 * @dev A decentralized application (dApp) for lending and borrowing OUSD stablecoins.
 * This contract interacts with OUSD's smart contracts to enable lending and borrowing functionality.
 * Users can deposit OUSD to earn interest or borrow OUSD against collateral.
 */

interface IOUSD {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StableLend {
    // Address of the OUSD token contract
    address public immutable ousdToken;

    // Interest rate for lending (annualized, in basis points)
    uint256 public constant LENDING_RATE = 500; // 5% annual interest

    // Mapping to track user deposits
    mapping(address => uint256) public deposits;

    // Mapping to track user borrowings
    mapping(address => uint256) public borrowings;

    // Event emitted when a user deposits OUSD
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws OUSD
    event Withdraw(address indexed user, uint256 amount);

    // Event emitted when a user borrows OUSD
    event Borrow(address indexed user, uint256 amount);

    // Event emitted when a user repays borrowed OUSD
    event Repay(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the OUSD token address.
     * @param _ousdToken Address of the OUSD token contract.
     */
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = _ousdToken;
    }

    /**
     * @dev Deposit OUSD into the dApp to earn interest.
     * @param amount Amount of OUSD to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer OUSD from the user to the contract
        IOUSD(ousdToken).transferFrom(msg.sender, address(this), amount);

        // Update the user's deposit balance
        deposits[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw OUSD from the dApp.
     * @param amount Amount of OUSD to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "Insufficient deposit balance");

        // Update the user's deposit balance
        deposits[msg.sender] -= amount;

        // Transfer OUSD from the contract to the user
        IOUSD(ousdToken).transfer(msg.sender, amount);

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Borrow OUSD against collateral.
     * @param amount Amount of OUSD to borrow.
     */
    function borrow(uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");

        // In a production-ready dApp, collateral management would be implemented here.
        // For simplicity, this example assumes sufficient collateral is provided.

        // Update the user's borrowing balance
        borrowings[msg.sender] += amount;

        // Transfer OUSD from the contract to the user
        IOUSD(ousdToken).transfer(msg.sender, amount);

        emit Borrow(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed OUSD.
     * @param amount Amount of OUSD to repay.
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(borrowings[msg.sender] >= amount, "Repay amount exceeds borrowing balance");

        // Transfer OUSD from the user to the contract
        IOUSD(ousdToken).transferFrom(msg.sender, address(this), amount);

        // Update the user's borrowing balance
        borrowings[msg.sender] -= amount;

        emit Repay(msg.sender, amount);
    }

    /**
     * @dev Calculate the interest earned by a user on their deposit.
     * @param user Address of the user.
     * @return Interest earned in OUSD.
     */
    function calculateInterest(address user) external view returns (uint256) {
        // In a production-ready dApp, time-based interest calculation would be implemented here.
        // For simplicity, this example assumes a fixed interest rate.
        return (deposits[user] * LENDING_RATE) / 10000;
    }
}
```
