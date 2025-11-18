"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-merlinstarter.pages.dev
Prompt: Write a Solidity contract to implement a token swap mechanism for $MP tokens on the Merlin Chain, referencing the pricing structure provided for the BTC pool.
Generated: DETERMINISTIC_bd55c013353d9545
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

// Importing OpenZeppelin Contracts for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token Swap Contract
contract TokenSwap is Ownable {
    // ERC20 token interfaces
    IERC20 public mpToken;
    IERC20 public btcToken;

    // BTC price reference in terms of MP tokens
    uint256 public btcToMpPrice; // price of 1 BTC in MP tokens

    // Event emitted on successful swap
    event Swap(address indexed user, uint256 btcAmount, uint256 mpAmount);

    // Constructor to initialize tokens and pricing
    constructor(address _mpToken, address _btcToken, uint256 _btcToMpPrice) {
        mpToken = IERC20(_mpToken);
        btcToken = IERC20(_btcToken);
        btcToMpPrice = _btcToMpPrice;
    }

    // Function to set the BTC to MP price
    function setBtcToMpPrice(uint256 newPrice) external onlyOwner {
        btcToMpPrice = newPrice;
    }

    // Function to swap BTC for MP tokens
    function swapBtcForMp(uint256 btcAmount) external {
        // Validate the input amount
        require(btcAmount > 0, "Amount must be greater than zero.");

        // Calculate the MP tokens to be received
        uint256 mpAmount = btcAmount * btcToMpPrice;

        // Ensure the contract has enough MP tokens to swap
        require(mpToken.balanceOf(address(this)) >= mpAmount, "Insufficient MP token balance in contract.");

        // Transfer BTC from user to contract
        require(btcToken.transferFrom(msg.sender, address(this), btcAmount), "Failed to transfer BTC.");

        // Transfer MP tokens to user
        require(mpToken.transfer(msg.sender, mpAmount), "Failed to transfer MP tokens.");

        // Emit the swap event
        emit Swap(msg.sender, btcAmount, mpAmount);
    }

    // Function to withdraw tokens from contract (for owner only)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract.");
        require(token.transfer(msg.sender, amount), "Token transfer failed.");
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}
}
```
