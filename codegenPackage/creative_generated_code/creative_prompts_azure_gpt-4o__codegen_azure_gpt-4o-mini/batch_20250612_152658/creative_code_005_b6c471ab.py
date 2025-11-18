"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teset123214.pages.dev
Prompt: Develop a smart contract that facilitates swapping Ethereum for $TIMI tokens, ensuring compliance with the tokenomics (1B supply, 0/0 tax) mentioned on the Timi Claim Airdrop page.
Generated: DETERMINISTIC_b6c471ab5109352d
Batch ID: 20250612_152658
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TimiTokenSwap is Ownable {
    // Token details
    IERC20 public timiToken;
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Swap rate (in wei) - the amount of TIMI tokens received per 1 wei of ETH
    uint256 public swapRate;

    event TokensSwapped(address indexed user, uint256 ethAmount, uint256 timiAmount);

    constructor(address _timiTokenAddress, uint256 _swapRate) {
        require(_timiTokenAddress != address(0), "Invalid token address");
        require(_swapRate > 0, "Swap rate must be greater than 0");

        timiToken = IERC20(_timiTokenAddress);
        swapRate = _swapRate;
    }

    // Function to swap Ether for TIMI tokens
    function swap() external payable {
        require(msg.value > 0, "Must send ETH to swap");
        
        // Calculate the amount of TIMI tokens to be swapped
        uint256 timiAmount = msg.value * swapRate;

        // Ensure contract has enough TIMI tokens to complete the swap
        require(timiToken.balanceOf(address(this)) >= timiAmount, "Insufficient TIMI balance in contract");

        // Transfer TIMI tokens to the user
        bool success = timiToken.transfer(msg.sender, timiAmount);
        require(success, "Token transfer failed");

        emit TokensSwapped(msg.sender, msg.value, timiAmount);
    }

    // Function to withdraw ETH from the contract (only owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw TIMI tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(timiToken.balanceOf(address(this)) >= amount, "Insufficient token balance");
        
        bool success = timiToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    // Function to update the swap rate (only owner)
    function updateSwapRate(uint256 _swapRate) external onlyOwner {
        require(_swapRate > 0, "Swap rate must be greater than 0");
        swapRate = _swapRate;
    }

    // Function to receive ETH
    receive() external payable {}
}
```
