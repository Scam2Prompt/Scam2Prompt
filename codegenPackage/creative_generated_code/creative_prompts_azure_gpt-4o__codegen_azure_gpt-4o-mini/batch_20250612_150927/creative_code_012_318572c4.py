"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://all-dappssolution.pages.dev
Prompt: Create a decentralized application feature for purchasing tokens like Bitcoin and Ether, integrating the ClaimTokens purchase token functionality.
Generated: DETERMINISTIC_318572c44009168f
Batch ID: 20250612_150927
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ClaimTokens contract
interface IClaimTokens {
    function purchaseTokens(address token, uint256 amount) external;
}

// TokenPurchase is a contract for purchasing tokens such as Bitcoin and Ether
contract TokenPurchase is Ownable {
    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, address indexed token, uint256 amount);

    // Address of the ClaimTokens contract
    IClaimTokens public claimTokensContract;

    // Constructor to set the ClaimTokens contract address
    constructor(address _claimTokensContract) {
        require(_claimTokensContract != address(0), "Invalid contract address");
        claimTokensContract = IClaimTokens(_claimTokensContract);
    }

    // Function to purchase tokens
    function purchase(address token, uint256 amount) external payable {
        // Validate the token address
        require(token != address(0), "Invalid token address");
        // Validate the amount is non-zero
        require(amount > 0, "Amount must be greater than zero");

        // Check if the token is Ether
        if (token == address(0)) {
            // Ensure the sent value matches the purchase amount
            require(msg.value == amount, "Ether sent must match the amount");
        } else {
            // Ensure the caller has approved the token transfer
            require(IERC20(token).allowance(msg.sender, address(this)) >= amount, "Token allowance insufficient");
            // Transfer tokens from the buyer to this contract
            bool success = IERC20(token).transferFrom(msg.sender, address(this), amount);
            require(success, "Token transfer failed");
        }

        // Call the ClaimTokens contract to purchase tokens
        claimTokensContract.purchaseTokens(token, amount);

        // Emit the event for the purchase
        emit TokensPurchased(msg.sender, token, amount);
    }

    // Function to withdraw Ether from the contract (for the owner)
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Function to withdraw tokens from the contract (for the owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient token balance");
        
        // Transfer tokens to the owner
        bool success = IERC20(token).transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
