"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lermlinstrate.pages.dev
Prompt: Create a Solidity smart contract example that interacts with the Merlin Chain to facilitate token swaps for $MP in the $BTC pool.
Generated: DETERMINISTIC_feae56c5413bbfb5
Batch ID: 20250612_153401
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

/**
 * @title TokenSwap
 * @dev A smart contract for facilitating token swaps for $MP in the $BTC pool on the Merlin Chain.
 */
contract TokenSwap {
    // Address of the $MP token contract
    address public mpTokenAddress;
    
    // Address of the $BTC token contract
    address public btcTokenAddress;

    // Event to log successful swaps
    event SwapExecuted(address indexed user, uint256 mpAmount, uint256 btcReceived);

    // Error definitions for better clarity
    error InsufficientBalance();
    error TransferFailed();

    /**
     * @dev Constructor to initialize token addresses.
     * @param _mpTokenAddress The address of the $MP token contract.
     * @param _btcTokenAddress The address of the $BTC token contract.
     */
    constructor(address _mpTokenAddress, address _btcTokenAddress) {
        mpTokenAddress = _mpTokenAddress;
        btcTokenAddress = _btcTokenAddress;
    }

    /**
     * @dev Function to swap $MP tokens for $BTC tokens.
     * @param mpAmount The amount of $MP tokens to swap.
     * @return btcReceived The amount of $BTC tokens received from the swap.
     */
    function swapMPForBTC(uint256 mpAmount) external returns (uint256 btcReceived) {
        // Check user balance of $MP tokens
        uint256 userMPBalance = IERC20(mpTokenAddress).balanceOf(msg.sender);
        if (userMPBalance < mpAmount) {
            revert InsufficientBalance();
        }

        // Transfer $MP tokens from the user to this contract
        bool transferSuccess = IERC20(mpTokenAddress).transferFrom(msg.sender, address(this), mpAmount);
        if (!transferSuccess) {
            revert TransferFailed();
        }

        // Calculate the amount of $BTC tokens to send back (for simplicity, assuming a 1:1 swap ratio)
        btcReceived = mpAmount;

        // Transfer $BTC tokens to the user
        transferSuccess = IERC20(btcTokenAddress).transfer(msg.sender, btcReceived);
        if (!transferSuccess) {
            revert TransferFailed();
        }

        emit SwapExecuted(msg.sender, mpAmount, btcReceived);
    }
}

/**
 * @title IERC20
 * @dev Interface for the ERC20 standard as defined in the EIP.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
