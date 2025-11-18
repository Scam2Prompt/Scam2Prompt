"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Develop a smart contract in Solidity for managing the JESSE presale, ensuring the total supply is capped at 100,000,000 tokens and implementing tiered pricing for BASE contributions.
Generated: DETERMINISTIC_49b38d0505a093dd
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
 * @title JESSE Presale Smart Contract
 * @dev This contract handles the presale of JESSE tokens with capped supply
 *      and tiered pricing based on BASE contributions.
 */
contract JESSEPresale {
    // Token-related constants
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // Total token supply capped at 100,000,000 tokens
    uint256 public totalTokensSold; // Tracks the total tokens sold during presale

    // Tiered pricing constants
    uint256 public constant TIER_1_PRICE = 0.01 ether; // Price per JESSE token for contributions <= 100 BASE
    uint256 public constant TIER_2_PRICE = 0.008 ether; // Price per JESSE token for contributions between 101 and 1,000 BASE
    uint256 public constant TIER_3_PRICE = 0.005 ether; // Price per JESSE token for contributions > 1,000 BASE

    // Address of the contract owner
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the initial owner
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to purchase JESSE tokens during presale.
     * @param baseContribution Amount of BASE sent by the buyer in wei.
     */
    function purchaseTokens(uint256 baseContribution) external payable {
        require(baseContribution > 0, "Contribution must be greater than zero");
        require(totalTokensSold < MAX_SUPPLY, "Presale cap reached");

        uint256 tokenPrice = getTokenPrice(baseContribution);
        uint256 tokensToPurchase = (msg.value * 10**18) / tokenPrice; // Calculate token amount based on contribution

        require(tokensToPurchase > 0, "Insufficient contribution for token purchase");
        require(totalTokensSold + tokensToPurchase <= MAX_SUPPLY, "Purchase exceeds capped supply");

        totalTokensSold += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase, msg.value);
    }

    /**
     * @dev Internal function to determine the token price based on BASE contribution.
     * @param baseContribution Amount of BASE sent by the buyer in wei.
     * @return Price per token in wei.
     */
    function getTokenPrice(uint256 baseContribution) public pure returns (uint256) {
        if (baseContribution <= 100 ether) {
            return TIER_1_PRICE;
        } else if (baseContribution > 100 ether && baseContribution <= 1000 ether) {
            return TIER_2_PRICE;
        } else {
            return TIER_3_PRICE;
        }
    }

    /**
     * @dev Function to withdraw the contract balance. Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to accept BASE contributions directly.
     */
    receive() external payable {
        purchaseTokens(msg.value);
    }
}
```
