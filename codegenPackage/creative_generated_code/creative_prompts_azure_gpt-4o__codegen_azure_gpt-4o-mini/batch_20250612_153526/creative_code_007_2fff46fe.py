"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gainstrade.pages.dev
Prompt: Provide code examples for lending $DAI, $USDC, or $WETH in a decentralized vault to earn yield, as outlined in the Gains Network ecosystem.
Generated: DETERMINISTIC_2fff46fef1d8c526
Batch ID: 20250612_153526
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the Gains Network vault
interface IVault {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
}

contract YieldLender {
    // State variables
    address public owner;
    IVault public vault;
    
    // Events for logging
    event Deposited(address indexed token, uint256 amount);
    event Withdrawn(address indexed token, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _vault) {
        owner = msg.sender;
        vault = IVault(_vault);
    }

    // Function to lend tokens to the vault
    function lend(address token, uint256 amount) external {
        // Check for zero amount
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from caller to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Approve the vault to spend the tokens
        IERC20(token).approve(address(vault), amount);
        
        // Deposit the tokens into the vault
        vault.deposit(token, amount);
        
        emit Deposited(token, amount);
    }

    // Function to withdraw tokens from the vault
    function withdraw(address token, uint256 amount) external onlyOwner {
        // Check for sufficient balance before withdrawal
        require(IERC20(token).balanceOf(address(vault)) >= amount, "Insufficient balance in vault");
        
        // Withdraw the tokens from the vault
        vault.withdraw(token, amount);
        
        // Transfer the tokens back to the owner
        IERC20(token).transfer(owner, amount);
        
        emit Withdrawn(token, amount);
    }

    // Function to recover any ERC20 tokens sent to this contract by mistake
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner, amount);
    }
}
```
