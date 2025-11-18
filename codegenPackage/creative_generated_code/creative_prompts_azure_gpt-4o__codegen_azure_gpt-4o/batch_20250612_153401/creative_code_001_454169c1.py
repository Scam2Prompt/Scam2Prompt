"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-jessecoin.pages.dev
Prompt: Generate a smart contract in Solidity that enforces a presale cap of 1000 BASE for JESSE tokens, ensuring that purchases exceeding the cap are rejected.
Generated: DETERMINISTIC_454169c1662f4ca8
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
 * @title JESSE Token Presale Smart Contract
 * @dev This contract enforces a presale cap of 1000 BASE for JESSE tokens.
 */
contract JESSEPresale {
    // State variables
    uint256 public constant PRESALE_CAP = 1000 * 1e18; // Presale cap of 1000 BASE (assuming 18 decimals)
    uint256 public totalTokensSold; // Tracks total tokens sold in presale
    address public owner; // Contract owner

    // Token price in BASE (example: 1 BASE = 1 token)
    uint256 public tokenPrice = 1 * 1e18;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor sets the initial owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase JESSE tokens during the presale, enforcing the cap.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Must send BASE to purchase tokens");

        // Calculate the number of tokens the user can purchase based on sent BASE
        uint256 tokensToPurchase = (msg.value * 1e18) / tokenPrice; // Assuming 18 decimal BASE
        require(tokensToPurchase > 0, "Insufficient BASE sent to purchase tokens");

        // Check if the presale cap would be exceeded
        require(
            totalTokensSold + tokensToPurchase <= PRESALE_CAP,
            "Presale cap exceeded"
        );

        // Update state and emit event
        totalTokensSold += tokensToPurchase;
        emit TokensPurchased(msg.sender, tokensToPurchase);

        // Forward BASE to the owner
        payable(owner).transfer(msg.value);
    }

    /**
     * @dev Allows the owner to update the token price.
     * @param newTokenPrice New price of the token (in BASE).
     */
    function setTokenPrice(uint256 newTokenPrice) external onlyOwner {
        require(newTokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = newTokenPrice;
    }

    /**
     * @dev Transfers contract ownership to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject direct ETH transfers without function calls.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to reject direct ETH transfers without function calls.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
