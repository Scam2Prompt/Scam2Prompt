"""
Generated Code Metadata:
========================
Original URL: https://usdfi-git-kyberswap-widget-tbot.vercel.app
Prompt: Generate code to create a decentralized lending portfolio using MoneyLegos, as highlighted on the webpage.
Generated: DETERMINISTIC_ecfb1bd6a48ee4fb
Batch ID: 20250612_154637
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for a lending protocol (e.g., Aave, Compound)
interface ILendingProtocol {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function getBalance(address asset, address user) external view returns (uint256);
}

// Decentralized Lending Portfolio Contract
contract LendingPortfolio is Ownable {
    using SafeMath for uint256;

    // Mapping to track user deposits
    mapping(address => mapping(address => uint256)) private userDeposits;

    // Instance of the lending protocol
    ILendingProtocol public lendingProtocol;

    // Event emitted when a user deposits funds
    event Deposited(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user withdraws funds
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    // Constructor to set the lending protocol address
    constructor(address _lendingProtocol) {
        require(_lendingProtocol != address(0), "Invalid lending protocol address");
        lendingProtocol = ILendingProtocol(_lendingProtocol);
    }

    // Function to deposit assets into the lending protocol
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user deposits
        userDeposits[msg.sender][asset] = userDeposits[msg.sender][asset].add(amount);

        // Deposit into the lending protocol
        IERC20(asset).approve(address(lendingProtocol), amount);
        lendingProtocol.deposit(asset, amount);

        emit Deposited(msg.sender, asset, amount);
    }

    // Function to withdraw assets from the lending protocol
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userDeposits[msg.sender][asset] >= amount, "Insufficient balance");

        // Withdraw from the lending protocol
        lendingProtocol.withdraw(asset, amount);

        // Update user deposits
        userDeposits[msg.sender][asset] = userDeposits[msg.sender][asset].sub(amount);

        // Transfer the withdrawn amount back to the user
        require(IERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to get the balance of a user for a specific asset
    function getUserBalance(address user, address asset) external view returns (uint256) {
        return userDeposits[user][asset];
    }

    // Function to set a new lending protocol (only owner)
    function setLendingProtocol(address _lendingProtocol) external onlyOwner {
        require(_lendingProtocol != address(0), "Invalid lending protocol address");
        lendingProtocol = ILendingProtocol(_lendingProtocol);
    }
}
```
