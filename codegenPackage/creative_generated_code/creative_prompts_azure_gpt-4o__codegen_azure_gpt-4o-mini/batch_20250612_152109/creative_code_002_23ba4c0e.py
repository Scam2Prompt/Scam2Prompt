"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papeairdropclaim.pages.dev
Prompt: Create a function in Solidity that facilitates swapping ETH for $PAPE tokens, ensuring the transaction is confirmed and the tokens are added to the user's balance.
Generated: DETERMINISTIC_23ba4c0efe8a7f9b
Batch ID: 20250612_152109
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Contract for swapping ETH for $PAPE tokens
contract EthToPapeSwap {
    IERC20 public papeToken; // ERC20 token contract instance
    address public owner;     // Owner of the contract

    // Event to emit when a swap occurs
    event Swap(address indexed user, uint256 ethAmount, uint256 papeAmount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the token address and owner
    constructor(address _papeToken) {
        require(_papeToken != address(0), "Invalid token address");
        papeToken = IERC20(_papeToken);
        owner = msg.sender;
    }

    // Function to swap ETH for $PAPE tokens
    function swap() external payable {
        require(msg.value > 0, "Must send ETH to swap");
        
        // Define the rate: 1 ETH = 1000 $PAPE tokens (example rate)
        uint256 papeAmount = msg.value * 1000;

        // Ensure contract has enough $PAPE tokens for the swap
        require(papeToken.balanceOf(address(this)) >= papeAmount, "Insufficient $PAPE balance in contract");

        // Transfer $PAPE tokens to the user
        bool success = papeToken.transfer(msg.sender, papeAmount);
        require(success, "Token transfer failed");

        // Emit event for the swap
        emit Swap(msg.sender, msg.value, papeAmount);
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEth() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Function to withdraw $PAPE tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(papeToken.transfer(owner, amount), "Token transfer failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
