"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity contract that allows users to lend $DAI, $USDC, or $WETH and earn yield, replicating the Vault functionality described in the Gains Network ecosystem.
Generated: DETERMINISTIC_1917720317c53e38
Batch ID: 20250612_152827
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

// Vault contract for lending DAI, USDC, and WETH
contract YieldVault is Ownable {
    // Mapping to track user deposits
    mapping(address => mapping(address => uint256)) public userDeposits;

    // Mapping to track total deposits for each token
    mapping(address => uint256) public totalDeposits;

    // Events for deposit and withdrawal actions
    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Supported tokens
    address public constant DAI = 0x6B175474E89094C44Da98b954EedeAC495271d0F; // DAI token address
    address public constant USDC = 0xA0b86991c6218b36c1d19d4a2e9EB0ce3606EB48; // USDC token address
    address public constant WETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2; // WETH token address

    // Modifier to check if the token is supported
    modifier onlySupportedToken(address token) {
        require(token == DAI || token == USDC || token == WETH, "Unsupported token");
        _;
    }

    // Function to deposit tokens into the vault
    function deposit(address token, uint256 amount) external onlySupportedToken(token) {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update user and total deposits
        userDeposits[msg.sender][token] += amount;
        totalDeposits[token] += amount;

        emit Deposited(msg.sender, token, amount);
    }

    // Function to withdraw tokens from the vault
    function withdraw(address token, uint256 amount) external onlySupportedToken(token) {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userDeposits[msg.sender][token] >= amount, "Insufficient balance");

        // Update user and total deposits
        userDeposits[msg.sender][token] -= amount;
        totalDeposits[token] -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, token, amount);
    }

    // Function to get the total deposits of a specific token
    function getTotalDeposits(address token) external view onlySupportedToken(token) returns (uint256) {
        return totalDeposits[token];
    }

    // Function to get the user's deposit balance for a specific token
    function getUserDeposit(address token) external view onlySupportedToken(token) returns (uint256) {
        return userDeposits[msg.sender][token];
    }
}
```
