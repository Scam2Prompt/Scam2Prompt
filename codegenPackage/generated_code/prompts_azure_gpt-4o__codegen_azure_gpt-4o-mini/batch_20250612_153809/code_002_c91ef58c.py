"""
Generated Code Metadata:
========================
Original URL: https://izumi-finance.org
Prompt: Generate Solidity code for a decentralized finance protocol that supports multiple blockchain ecosystems, as described in iZUMi Finance's flexibility feature.
Generated: DETERMINISTIC_c91ef58cefc385be
Batch ID: 20250612_153809
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

// Interface for the decentralized finance protocol
interface IDeFiProtocol {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getBalance(address token, address user) external view returns (uint256);
}

// Main contract for the DeFi protocol
contract MultiChainDeFi is IDeFiProtocol, Ownable {
    using SafeMath for uint256;

    // Mapping to track user balances for each token
    mapping(address => mapping(address => uint256)) private balances;

    // Event emitted when a deposit is made
    event Deposited(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Deposit function to allow users to deposit tokens into the protocol
    function deposit(address token, uint256 amount) external override {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's balance
        balances[token][msg.sender] = balances[token][msg.sender].add(amount);

        emit Deposited(msg.sender, token, amount);
    }

    // Withdraw function to allow users to withdraw tokens from the protocol
    function withdraw(address token, uint256 amount) external override {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[token][msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring to prevent reentrancy
        balances[token][msg.sender] = balances[token][msg.sender].sub(amount);
        
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, token, amount);
    }

    // Function to get the balance of a user for a specific token
    function getBalance(address token, address user) external view override returns (uint256) {
        return balances[token][user];
    }

    // Function to allow the owner to withdraw tokens from the contract
    function ownerWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
