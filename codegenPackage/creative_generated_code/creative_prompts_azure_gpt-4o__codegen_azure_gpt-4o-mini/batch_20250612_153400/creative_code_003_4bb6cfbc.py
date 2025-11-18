"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorchain1.vercel.app
Prompt: Create a smart contract that integrates THORChain's liquidity savers vaults to allow single asset liquidity deposits and earn swap fees.
Generated: DETERMINISTIC_4bb6cfbcac74aa4e
Batch ID: 20250612_153400
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

// Import necessary interfaces from THORChain
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for THORChain's liquidity saver vault
interface ITHORChainVault {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getSwapFees(address token) external view returns (uint256);
}

// Smart contract to manage single asset liquidity deposits to THORChain
contract LiquiditySaver is Ownable {
    ITHORChainVault public vault;

    // Event to log deposits
    event Deposited(address indexed user, address indexed token, uint256 amount);
    // Event to log withdrawals
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Constructor to set the vault address
    constructor(address _vaultAddress) {
        require(_vaultAddress != address(0), "Invalid vault address");
        vault = ITHORChainVault(_vaultAddress);
    }

    // Function to deposit a single asset into the liquidity saver vault
    function deposit(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the vault to spend the token
        IERC20(token).approve(address(vault), amount);
        
        // Deposit to the THORChain vault
        vault.deposit(token, amount);

        emit Deposited(msg.sender, token, amount);
    }

    // Function to withdraw a single asset from the liquidity saver vault
    function withdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        vault.withdraw(token, amount);

        // Transfer the withdrawn amount back to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, token, amount);
    }

    // Function to view the accumulated swap fees for a specific token
    function viewSwapFees(address token) external view returns (uint256) {
        return vault.getSwapFees(token);
    }

    // Fallback function to receive ETH (in case of any ETH transfer)
    receive() external payable {
        // Accept ETH, but do nothing with it
    }
}
```
