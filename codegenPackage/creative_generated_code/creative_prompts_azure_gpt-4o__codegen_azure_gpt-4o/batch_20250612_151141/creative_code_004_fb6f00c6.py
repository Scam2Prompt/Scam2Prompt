"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoinvip.pages.dev
Prompt: Write Solidity smart contract code for a token swap mechanism that supports $PEIPEI and ensures zero tax transactions as described in the tokenomics.
Generated: DETERMINISTIC_fb6f00c6084aff0b
Batch ID: 20250612_151141
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
 * @dev Smart contract to facilitate token swaps for $PEIPEI with zero tax transactions.
 * This contract assumes both tokens are ERC20 compliant.
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract TokenSwap {
    // Address of the $PEIPEI token contract
    address public immutable peipeiToken;

    // Address of the other token for swapping
    address public immutable otherToken;

    // Owner of the contract
    address public owner;

    // Events
    event SwapExecuted(address indexed user, uint256 peipeiAmount, uint256 otherTokenAmount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses and set the owner.
     * @param _peipeiToken Address of the $PEIPEI token contract.
     * @param _otherToken Address of the other token contract.
     */
    constructor(address _peipeiToken, address _otherToken) {
        require(_peipeiToken != address(0), "Invalid $PEIPEI token address");
        require(_otherToken != address(0), "Invalid other token address");

        peipeiToken = _peipeiToken;
        otherToken = _otherToken;
        owner = msg.sender;
    }

    /**
     * @dev Swap $PEIPEI tokens for the other token at a 1:1 ratio.
     * Assumes zero tax transactions as described in the tokenomics.
     * @param peipeiAmount Amount of $PEIPEI tokens to swap.
     */
    function swap(uint256 peipeiAmount) external {
        require(peipeiAmount > 0, "Swap amount must be greater than zero");

        IERC20 peipei = IERC20(peipeiToken);
        IERC20 other = IERC20(otherToken);

        // Ensure sender has approved the $PEIPEI tokens to the contract
        uint256 allowance = peipei.allowance(msg.sender, address(this));
        require(allowance >= peipeiAmount, "Insufficient allowance for $PEIPEI tokens");

        // Transfer $PEIPEI tokens from the sender to the contract
        bool peipeiTransfer = peipei.transferFrom(msg.sender, address(this), peipeiAmount);
        require(peipeiTransfer, "Failed to transfer $PEIPEI tokens");

        // Calculate 1:1 swap amount for the other token
        uint256 otherTokenAmount = peipeiAmount;

        // Ensure the contract has enough balance of the other token
        uint256 contractBalance = other.balanceOf(address(this));
        require(contractBalance >= otherTokenAmount, "Insufficient other token balance in contract");

        // Transfer the other token to the sender
        bool otherTransfer = other.transfer(msg.sender, otherTokenAmount);
        require(otherTransfer, "Failed to transfer other token");

        // Emit event for the swap
        emit SwapExecuted(msg.sender, peipeiAmount, otherTokenAmount);
    }

    /**
     * @dev Withdraw tokens from the contract (only owner).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");

        IERC20 tokenContract = IERC20(token);
        uint256 contractBalance = tokenContract.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient token balance in contract");

        // Transfer tokens to the owner
        bool transferSuccess = tokenContract.transfer(owner, amount);
        require(transferSuccess, "Token transfer failed");
    }

    /**
     * @dev Transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
