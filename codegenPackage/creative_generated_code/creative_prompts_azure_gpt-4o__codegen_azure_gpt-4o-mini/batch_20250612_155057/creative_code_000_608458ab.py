"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethevista.app
Prompt: Write a smart contract in Solidity that implements a custom fee structure for token swaps, where fees are charged in ETH instead of tokens, as described on Ethervista.
Generated: DETERMINISTIC_608458ab3577c241
Batch ID: 20250612_155057
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

// Importing the interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Main smart contract for the custom fee structure
contract TokenSwap {
    address public owner;
    uint256 public feePercentage; // Fee percentage in basis points (100 basis points = 1%)
    uint256 private constant MAX_FEE = 1000; // 10% maximum fee

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed user, uint256 tokenAmount, uint256 ethFee);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _feePercentage) {
        require(_feePercentage <= MAX_FEE, "Invalid fee percentage");
        owner = msg.sender;
        feePercentage = _feePercentage;
    }

    // Function to set a new fee percentage
    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= MAX_FEE, "Invalid fee percentage");
        feePercentage = _feePercentage;
    }

    // Function to swap tokens for ETH, charging a fee in ETH
    function swapTokensForETH(address tokenAddress, uint256 tokenAmount) external {
        // Calculate the fee
        uint256 ethFee = (tokenAmount * feePercentage) / 10000; // Convert basis points to percentage
        require(ethFee > 0, "Fee must be greater than zero");

        // Transfer tokens from the user to the contract
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        // Transfer the ETH fee to the owner
        (bool success, ) = owner.call{value: ethFee}("");
        require(success, "Fee transfer failed");

        // Emit an event for the swap
        emit SwapExecuted(msg.sender, tokenAmount, ethFee);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ETH directly
    receive() external payable {}
}
```
