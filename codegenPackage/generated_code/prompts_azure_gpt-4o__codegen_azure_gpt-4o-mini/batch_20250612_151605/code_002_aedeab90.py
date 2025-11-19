"""
Generated Code Metadata:
========================
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Provide a Solidity smart contract example for integrating Amnis Finance's liquid staking tokens (amAPT and stAPT) into a DeFi lending platform.
Generated: DETERMINISTIC_aedeab90e2654d6e
Batch ID: 20250612_151605
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the lending platform
interface ILendingPlatform {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
}

// AmnisFinanceStaking is a contract for integrating Amnis Finance's liquid staking tokens
contract AmnisFinanceStaking is Ownable {
    // State variables for the contract
    IERC20 public amAPT; // amAPT token contract
    IERC20 public stAPT; // stAPT token contract
    ILendingPlatform public lendingPlatform; // Reference to the lending platform

    // Events for logging actions
    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Constructor to initialize the contract with token addresses and lending platform
    constructor(address _amAPT, address _stAPT, address _lendingPlatform) {
        require(_amAPT != address(0), "Invalid amAPT address");
        require(_stAPT != address(0), "Invalid stAPT address");
        require(_lendingPlatform != address(0), "Invalid lending platform address");

        amAPT = IERC20(_amAPT);
        stAPT = IERC20(_stAPT);
        lendingPlatform = ILendingPlatform(_lendingPlatform);
    }

    // Function to deposit amAPT tokens into the lending platform
    function depositAmAPT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer amAPT tokens from the user to this contract
        require(amAPT.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the lending platform to spend the tokens
        amAPT.approve(address(lendingPlatform), amount);

        // Deposit the tokens into the lending platform
        lendingPlatform.deposit(address(amAPT), amount);

        emit Deposited(msg.sender, address(amAPT), amount);
    }

    // Function to deposit stAPT tokens into the lending platform
    function depositStAPT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer stAPT tokens from the user to this contract
        require(stAPT.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the lending platform to spend the tokens
        stAPT.approve(address(lendingPlatform), amount);

        // Deposit the tokens into the lending platform
        lendingPlatform.deposit(address(stAPT), amount);

        emit Deposited(msg.sender, address(stAPT), amount);
    }

    // Function to withdraw amAPT tokens from the lending platform
    function withdrawAmAPT(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw the tokens from the lending platform
        lendingPlatform.withdraw(address(amAPT), amount);

        // Transfer the tokens back to the owner
        require(amAPT.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, address(amAPT), amount);
    }

    // Function to withdraw stAPT tokens from the lending platform
    function withdrawStAPT(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw the tokens from the lending platform
        lendingPlatform.withdraw(address(stAPT), amount);

        // Transfer the tokens back to the owner
        require(stAPT.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, address(stAPT), amount);
    }
}
```
