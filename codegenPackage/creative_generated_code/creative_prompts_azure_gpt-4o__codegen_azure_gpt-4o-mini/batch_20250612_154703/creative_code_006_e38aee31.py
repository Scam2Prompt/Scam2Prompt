"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.network
Prompt: Develop a tutorial for swapping ERC-20 tokens on Aave, including borrowed and supplied assets, using the Aave Protocol's composability features.
Generated: DETERMINISTIC_e38aee3103050dcd
Batch ID: 20250612_154703
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

import "@aave/protocol-v2/interfaces/ILendingPool.sol";
import "@aave/protocol-v2/interfaces/ILendingPoolAddressesProvider.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenSwapper {
    using SafeMath for uint256;

    ILendingPoolAddressesProvider public addressesProvider;
    ILendingPool public lendingPool;

    // Events for logging
    event TokensSupplied(address indexed user, address indexed asset, uint256 amount);
    event TokensBorrowed(address indexed user, address indexed asset, uint256 amount);
    event TokensSwapped(address indexed user, address indexed fromAsset, address indexed toAsset, uint256 amount);

    // Constructor to initialize the Aave lending pool addresses provider
    constructor(address _provider) {
        addressesProvider = ILendingPoolAddressesProvider(_provider);
        lendingPool = ILendingPool(addressesProvider.getLendingPool());
    }

    // Function to supply tokens to Aave
    function supplyTokens(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(asset).transferFrom(msg.sender, address(this), amount); // Transfer tokens to this contract
        IERC20(asset).approve(address(lendingPool), amount); // Approve the lending pool to spend the tokens

        lendingPool.deposit(asset, amount, msg.sender, 0); // Supply tokens to Aave
        emit TokensSupplied(msg.sender, asset, amount);
    }

    // Function to borrow tokens from Aave
    function borrowTokens(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Ensure the user has enough collateral
        uint256 healthFactor = lendingPool.getUserAccountData(msg.sender).healthFactor;
        require(healthFactor > 1, "Health factor must be greater than 1 to borrow");

        lendingPool.borrow(asset, amount, 2, 0, msg.sender); // Borrow tokens with variable interest rate
        emit TokensBorrowed(msg.sender, asset, amount);
    }

    // Function to swap tokens
    function swapTokens(address fromAsset, address toAsset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to contract
        IERC20(fromAsset).transferFrom(msg.sender, address(this), amount);
        IERC20(fromAsset).approve(address(lendingPool), amount);

        // Withdraw the asset to swap
        lendingPool.withdraw(fromAsset, amount, address(this));

        // Here you would normally perform the swap operation (for example, via a DEX)

        // For demonstration purposes, we’ll just assume the swap is executed correctly.
        uint256 swappedAmount = amount; // This should be the amount received after the swap
        IERC20(toAsset).transfer(msg.sender, swappedAmount); // Transfer swapped tokens to user

        emit TokensSwapped(msg.sender, fromAsset, toAsset, swappedAmount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        lendingPool.withdraw(asset, amount, msg.sender); // Withdraw tokens from Aave
    }
}
```

This smart contract allows users to supply, borrow, and swap ERC-20 tokens using the Aave protocol. Please ensure proper testing on a testnet before deploying on the mainnet.
