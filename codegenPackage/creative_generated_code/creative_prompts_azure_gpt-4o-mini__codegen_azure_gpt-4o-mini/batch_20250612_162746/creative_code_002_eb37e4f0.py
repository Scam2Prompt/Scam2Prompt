"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a-brk.pages.dev
Prompt: Provide an example of how to implement a smart contract for burning Notcoin tokens.
Generated: DETERMINISTIC_eb37e4f052684239
Batch ID: 20250612_162746
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for burning Notcoin tokens
contract NotcoinBurner is Ownable {
    // Reference to the Notcoin token contract
    IERC20 public notcoinToken;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to set the Notcoin token address
    constructor(address _notcoinTokenAddress) {
        require(_notcoinTokenAddress != address(0), "Invalid token address");
        notcoinToken = IERC20(_notcoinTokenAddress);
    }

    // Function to burn tokens from the caller's account
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(notcoinToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to this contract and burn them
        notcoinToken.transferFrom(msg.sender, address(this), amount);
        // Approving the token transfer for burning
        notcoinToken.approve(address(this), amount);
        // Burn the tokens by transferring them to the zero address
        notcoinToken.transfer(address(0), amount);

        emit TokensBurned(msg.sender, amount);
    }
}
```
