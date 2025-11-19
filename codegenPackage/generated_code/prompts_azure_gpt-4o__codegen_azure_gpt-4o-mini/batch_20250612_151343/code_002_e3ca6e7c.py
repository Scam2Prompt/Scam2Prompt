"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a smart contract example that utilizes Gravity's omnichain intent protocol to manage yield-enabled unified balances across multiple chains.
Generated: DETERMINISTIC_e3ca6e7c2ee298dd
Batch ID: 20250612_151343
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
import "@gravityprotocol/gravity-bridge/contracts/Gravity.sol";

// Smart contract to manage yield-enabled unified balances across multiple chains
contract YieldManager is Ownable {
    // Mapping to store user balances across chains
    mapping(address => mapping(string => uint256)) private userBalances;

    // Event emitted when a user deposits funds
    event Deposited(address indexed user, string indexed chain, uint256 amount);

    // Event emitted when a user withdraws funds
    event Withdrawn(address indexed user, string indexed chain, uint256 amount);

    // Gravity contract instance for cross-chain communication
    Gravity private gravity;

    // Constructor to initialize the Gravity contract address
    constructor(address _gravityAddress) {
        gravity = Gravity(_gravityAddress);
    }

    // Function to deposit tokens into the contract
    function deposit(string memory chain, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to this contract
        IERC20 token = IERC20(gravity.getTokenAddress(chain));
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user balance
        userBalances[msg.sender][chain] += amount;

        // Emit deposit event
        emit Deposited(msg.sender, chain, amount);
    }

    // Function to withdraw tokens from the contract
    function withdraw(string memory chain, uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender][chain] >= amount, "Insufficient balance");

        // Update user balance before transferring to prevent reentrancy
        userBalances[msg.sender][chain] -= amount;

        // Transfer tokens from this contract to the user
        IERC20 token = IERC20(gravity.getTokenAddress(chain));
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, chain, amount);
    }

    // Function to get the balance of a user on a specific chain
    function getBalance(address user, string memory chain) external view returns (uint256) {
        return userBalances[user][chain];
    }

    // Function to set the Gravity contract address (only owner)
    function setGravityAddress(address _gravityAddress) external onlyOwner {
        gravity = Gravity(_gravityAddress);
    }
}
```
