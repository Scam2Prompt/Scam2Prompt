"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Generate Solidity code for deploying a non-custodial smart contract that integrates Morpho's optimized vaults for earning yield.
Generated: DETERMINISTIC_9577d036ed89e408
Batch ID: 20250612_154057
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

// Import Morpho's optimized vault interface
import "@morpho.xyz/morpho-core/contracts/interfaces/IMorpho.sol";

contract NonCustodialVault {
    // State variables
    address public owner;
    IMorpho public morpho;

    // Mapping to track user deposits
    mapping(address => uint256) private userDeposits;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with Morpho's address
    constructor(address _morphoAddress) {
        owner = msg.sender;
        morpho = IMorpho(_morphoAddress);
    }

    // Deposit function for users to deposit funds into the vault
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer the tokens to the contract
        // Assume the token is ERC20 and follows the standard interface
        // The contract should have the correct token approval
        require(ERC20(morpho.token()).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user deposits
        userDeposits[msg.sender] += amount;

        // Call Morpho to optimize the vault and earn yield
        morpho.supply(amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw function for users to withdraw their funds from the vault
    function withdraw(uint256 amount) external {
        require(userDeposits[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update user deposits
        userDeposits[msg.sender] -= amount;

        // Call Morpho to withdraw funds from the optimized vault
        morpho.redeem(amount);

        // Transfer tokens back to the user
        require(ERC20(morpho.token()).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the user's deposit balance
    function balanceOf(address user) external view returns (uint256) {
        return userDeposits[user];
    }

    // Function to retrieve the contract owner
    function getOwner() external view returns (address) {
        return owner;
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(morpho.token()), "Cannot withdraw Morpho tokens");
        require(ERC20(tokenAddress).transfer(owner, amount), "Transfer failed");
    }
}

// Minimal ERC20 interface for token transfers
interface ERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
