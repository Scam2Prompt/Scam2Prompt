"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a smart contract example that utilizes Gravity's omnichain intent protocol to manage yield-enabled unified balances across multiple chains.
Generated: DETERMINISTIC_e3ca6e7c2ee298dd
Batch ID: 20250612_151343
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@gravity.protocol/contracts/GravityProtocol.sol";

/**
 * @title YieldManager
 * @dev A smart contract to manage yield-enabled unified balances across multiple chains using Gravity's omnichain intent protocol.
 */
contract YieldManager is Ownable {
    // Event emitted when yield is earned
    event YieldEarned(address indexed user, uint256 amount);

    // Mapping to store user balances for each chain
    mapping(address => mapping(uint256 => uint256)) private userBalances; // user -> (chainId -> balance)

    // Gravity protocol instance
    GravityProtocol private gravityProtocol;

    /**
     * @dev Constructor to initialize the Gravity Protocol instance.
     * @param _gravityAddress The address of the Gravity protocol contract.
     */
    constructor(address _gravityAddress) {
        require(_gravityAddress != address(0), "Invalid Gravity address");
        gravityProtocol = GravityProtocol(_gravityAddress);
    }

    /**
     * @dev Deposit tokens into the contract.
     * @param amount The amount of tokens to deposit.
     * @param chainId The chain ID where the tokens are being deposited.
     */
    function deposit(uint256 amount, uint256 chainId) external {
        require(amount > 0, "Amount must be greater than zero");
        require(chainId > 0, "Invalid chain ID");

        // Transfer tokens from user to this contract
        IERC20 token = IERC20(gravityProtocol.getTokenAddress(chainId));
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user balance
        userBalances[msg.sender][chainId] += amount;
    }

    /**
     * @dev Withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     * @param chainId The chain ID where the tokens are being withdrawn.
     */
    function withdraw(uint256 amount, uint256 chainId) external {
        require(amount > 0, "Amount must be greater than zero");
        require(chainId > 0, "Invalid chain ID");
        require(userBalances[msg.sender][chainId] >= amount, "Insufficient balance");

        // Update user balance before transferring
        userBalances[msg.sender][chainId] -= amount;

        // Transfer tokens from this contract to the user
        IERC20 token = IERC20(gravityProtocol.getTokenAddress(chainId));
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Accrue yield for a user on a specific chain.
     * @param user The address of the user.
     * @param amount The amount of yield to accrue.
     * @param chainId The chain ID where the yield is being accrued.
     */
    function accrueYield(address user, uint256 amount, uint256 chainId) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(chainId > 0, "Invalid chain ID");

        // Update user's balance with the accrued yield
        userBalances[user][chainId] += amount;

        emit YieldEarned(user, amount);
    }

    /**
     * @dev Get the balance of a user on a specific chain.
     * @param user The address of the user.
     * @param chainId The chain ID to query the balance from.
     * @return The balance of the user on the specified chain.
     */
    function getBalance(address user, uint256 chainId) external view returns (uint256) {
        return userBalances[user][chainId];
    }
}
```
