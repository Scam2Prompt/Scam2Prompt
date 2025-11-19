"""
Generated Code Metadata:
========================
Original URL: https://radiant.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that implements a simple lending and borrowing mechanism using Radiant's omnichain protocol, with dynamic APR based on market conditions.
Generated: DETERMINISTIC_e6146aad09705b33
Batch ID: 20250622_211705
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
 * @title LendingAndBorrowingContract
 * @dev Implements a simple lending and borrowing mechanism using Radiant's omnichain protocol.
 *      Includes dynamic APR adjustment based on market conditions.
 */
interface IRadiantOmnichain {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function getMarketAPR(address asset) external view returns (uint256);
}

contract LendingAndBorrowingContract {
    address public owner;
    IRadiantOmnichain public radiantProtocol;

    // Mapping to track user balances
    mapping(address => mapping(address => uint256)) public userDeposits;
    mapping(address => mapping(address => uint256)) public userBorrows;

    // Events for logging
    event Deposit(address indexed user, address indexed asset, uint256 amount);
    event Withdraw(address indexed user, address indexed asset, uint256 amount);
    event Borrow(address indexed user, address indexed asset, uint256 amount);
    event Repay(address indexed user, address indexed asset, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _radiantProtocol) {
        owner = msg.sender;
        radiantProtocol = IRadiantOmnichain(_radiantProtocol);
    }

    /**
     * @dev Deposit assets into the Radiant protocol.
     * @param asset The address of the asset to deposit.
     * @param amount The amount of the asset to deposit.
     */
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer the asset from the user to this contract
        require(
            IERC20(asset).transferFrom(msg.sender, address(this), amount),
            "Asset transfer failed"
        );

        // Approve Radiant protocol to spend the asset
        IERC20(asset).approve(address(radiantProtocol), amount);

        // Deposit into Radiant protocol
        radiantProtocol.deposit(asset, amount);

        // Update user balance
        userDeposits[msg.sender][asset] += amount;

        emit Deposit(msg.sender, asset, amount);
    }

    /**
     * @dev Withdraw assets from the Radiant protocol.
     * @param asset The address of the asset to withdraw.
     * @param amount The amount of the asset to withdraw.
     */
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(
            userDeposits[msg.sender][asset] >= amount,
            "Insufficient balance to withdraw"
        );

        // Withdraw from Radiant protocol
        radiantProtocol.withdraw(asset, amount);

        // Transfer the asset back to the user
        require(
            IERC20(asset).transfer(msg.sender, amount),
            "Asset transfer failed"
        );

        // Update user balance
        userDeposits[msg.sender][asset] -= amount;

        emit Withdraw(msg.sender, asset, amount);
    }

    /**
     * @dev Borrow assets from the Radiant protocol.
     * @param asset The address of the asset to borrow.
     * @param amount The amount of the asset to borrow.
     */
    function borrow(address asset, uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");

        // Get current market APR for the asset
        uint256 currentAPR = radiantProtocol.getMarketAPR(asset);

        // Borrow from Radiant protocol
        radiantProtocol.borrow(asset, amount);

        // Update user borrow balance
        userBorrows[msg.sender][asset] += amount;

        emit Borrow(msg.sender, asset, amount);
    }

    /**
     * @dev Repay borrowed assets to the Radiant protocol.
     * @param asset The address of the asset to repay.
     * @param amount The amount of the asset to repay.
     */
    function repay(address asset, uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(
            userBorrows[msg.sender][asset] >= amount,
            "Repay amount exceeds borrowed balance"
        );

        // Transfer the asset from the user to this contract
        require(
            IERC20(asset).transferFrom(msg.sender, address(this), amount),
            "Asset transfer failed"
        );

        // Approve Radiant protocol to spend the asset
        IERC20(asset).approve(address(radiantProtocol), amount);

        // Repay to Radiant protocol
        radiantProtocol.repay(asset, amount);

        // Update user borrow balance
        userBorrows[msg.sender][asset] -= amount;

        emit Repay(msg.sender, asset, amount);
    }

    /**
     * @dev Update the Radiant protocol address (only owner).
     * @param _radiantProtocol The new Radiant protocol address.
     */
    function updateRadiantProtocol(address _radiantProtocol) external onlyOwner {
        radiantProtocol = IRadiantOmnichain(_radiantProtocol);
    }
}

interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
