"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Write a smart contract in Solidity for a lending protocol that isolates risk to a single asset, similar to Silo Finance's Silo design."
Generated: DETERMINISTIC_0f00b32345560af7
Batch ID: 20250622_205111
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SiloLending
 * @dev A lending protocol that isolates risk to a single asset.
 */
contract SiloLending is Ownable {
    using SafeMath for uint256;

    // Struct to hold user data
    struct User {
        uint256 depositedAmount;
        uint256 borrowedAmount;
    }

    // Mapping of user addresses to their data
    mapping(address => User) private users;

    // The ERC20 token used for lending
    IERC20 public immutable asset;

    // Interest rate per block (in basis points)
    uint256 public interestRate;

    // Total deposited amount in the contract
    uint256 public totalDeposited;

    // Total borrowed amount in the contract
    uint256 public totalBorrowed;

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the asset and interest rate.
     * @param _asset The address of the ERC20 token used for lending.
     * @param _interestRate The interest rate in basis points (1% = 100 basis points).
     */
    constructor(IERC20 _asset, uint256 _interestRate) {
        asset = _asset;
        interestRate = _interestRate;
    }

    /**
     * @dev Deposit assets into the lending protocol.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to contract
        asset.transferFrom(msg.sender, address(this), amount);

        // Update user and total deposits
        users[msg.sender].depositedAmount = users[msg.sender].depositedAmount.add(amount);
        totalDeposited = totalDeposited.add(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw assets from the lending protocol.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(users[msg.sender].depositedAmount >= amount, "Insufficient balance");

        // Update user and total deposits
        users[msg.sender].depositedAmount = users[msg.sender].depositedAmount.sub(amount);
        totalDeposited = totalDeposited.sub(amount);

        // Transfer tokens back to user
        asset.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Borrow assets from the lending protocol.
     * @param amount The amount of tokens to borrow.
     */
    function borrow(uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(totalDeposited > totalBorrowed, "Insufficient liquidity");

        // Update user and total borrowed amounts
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.add(amount);
        totalBorrowed = totalBorrowed.add(amount);

        // Transfer tokens to the user
        asset.transfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed assets to the lending protocol.
     * @param amount The amount of tokens to repay.
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(users[msg.sender].borrowedAmount >= amount, "Repay amount exceeds borrowed amount");

        // Update user and total borrowed amounts
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.sub(amount);
        totalBorrowed = totalBorrowed.sub(amount);

        // Transfer tokens from user to contract
        asset.transferFrom(msg.sender, address(this), amount);

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Get the user's current balance of deposited and borrowed amounts.
     * @param user The address of the user.
     * @return depositedAmount The amount deposited by the user.
     * @return borrowedAmount The amount borrowed by the user.
     */
    function getUserBalance(address user) external view returns (uint256 depositedAmount, uint256 borrowedAmount) {
        User storage userData = users[user];
        return (userData.depositedAmount, userData.borrowedAmount);
    }
}
```
