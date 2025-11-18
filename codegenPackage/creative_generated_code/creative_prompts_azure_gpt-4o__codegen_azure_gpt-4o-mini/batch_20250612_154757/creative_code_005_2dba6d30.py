"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clewx.cn
Prompt: Develop a smart contract on the OKC blockchain to interact with Web3 applications, ensuring compatibility with the programmable features highlighted on the 欧易OKX website.
Generated: DETERMINISTIC_2dba6d30dd12069c
Batch ID: 20250612_154757
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

// Importing required OpenZeppelin libraries for security
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title OKCInteract
 * @dev A smart contract to interact with Web3 applications on the OKC blockchain
 *      This contract allows users to deposit and withdraw ERC20 tokens.
 */
contract OKCInteract is Ownable {
    // Mapping to keep track of user balances
    mapping(address => uint256) private balances;

    // Event emitted when tokens are deposited
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Token interface for interacting with ERC20 tokens
    IERC20 public token;

    /**
     * @dev Constructor to initialize the contract with the token address
     * @param _tokenAddress The address of the ERC20 token to be used
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to deposit tokens into the contract
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw tokens from the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring tokens
        balances[msg.sender] -= amount;

        // Transfer tokens from this contract to the user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to check the token balance of a user
     * @param user The address of the user to query
     * @return The token balance of the user
     */
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Function to retrieve the total balance of tokens held by the contract
     * @return The total balance of tokens in the contract
     */
    function totalBalance() external view onlyOwner returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
