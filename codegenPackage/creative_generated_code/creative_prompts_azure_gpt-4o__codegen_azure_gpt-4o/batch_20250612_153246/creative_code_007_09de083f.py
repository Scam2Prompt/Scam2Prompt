"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-in.web.app
Prompt: Write a function in Solidity to burn tokens as part of the Phase 3 roadmap event, reducing the circulating supply of $RBLZ.
Generated: DETERMINISTIC_09de083f64c24699
Batch ID: 20250612_153246
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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
}

contract TokenBurner {
    address public owner; // Contract owner
    IERC20 public RBLZToken; // Reference to the RBLZ token contract

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the token contract address and the owner
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        RBLZToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    // Function to burn tokens from the owner's balance
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 ownerBalance = RBLZToken.balanceOf(owner);
        require(ownerBalance >= amount, "Insufficient balance to burn");

        // Approve the token contract to transfer the amount
        bool approvalSuccess = RBLZToken.approve(address(this), amount);
        require(approvalSuccess, "Token approval failed");

        // Transfer the tokens to the contract
        bool transferSuccess = RBLZToken.transferFrom(owner, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Burn the tokens
        RBLZToken.burn(amount);

        emit TokensBurned(owner, amount); // Emit the event
    }

    // Function to update the token contract address (only by owner)
    function setTokenAddress(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        RBLZToken = IERC20(_tokenAddress);
    }

    // Function to transfer contract ownership
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
