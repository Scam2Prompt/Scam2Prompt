"""
Generated Code Metadata:
========================
Original URL: https://diamond-7n0.pages.dev
Prompt: Generate a Solidity code snippet for a simple decentralized finance (DeFi) application that utilizes Diamond Coin as a utility token for transactions.
Generated: DETERMINISTIC_340f074ca864055b
Batch ID: 20250622_210216
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
 * @title DeFi Application using Diamond Coin
 * @dev This contract allows users to deposit, withdraw, and transfer Diamond Coin (ERC20 token).
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DeFiApp {
    // Address of the Diamond Coin ERC20 token contract
    IERC20 public diamondCoin;

    // Mapping to track user balances within the DeFi app
    mapping(address => uint256) public userBalances;

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdraw(address indexed user, uint256 amount);

    // Event emitted when a user transfers tokens within the app
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Constructor to initialize the Diamond Coin contract address.
     * @param _diamondCoin Address of the Diamond Coin ERC20 token contract.
     */
    constructor(address _diamondCoin) {
        require(_diamondCoin != address(0), "Invalid token address");
        diamondCoin = IERC20(_diamondCoin);
    }

    /**
     * @dev Deposit Diamond Coin into the DeFi app.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = diamondCoin.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user balance
        userBalances[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw Diamond Coin from the DeFi app.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer tokens from the contract to the user
        bool success = diamondCoin.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Transfer Diamond Coin within the DeFi app.
     * @param to Recipient address.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        userBalances[msg.sender] -= amount;
        userBalances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Get the balance of a user within the DeFi app.
     * @param user Address of the user.
     * @return Balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }
}
```
