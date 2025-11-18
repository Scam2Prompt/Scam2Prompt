"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverser.pages.dev
Prompt: Develop a Web3Payments-powered smart contract for securely storing presale purchase information on-chain for $DOGEVERSE buyers.
Generated: DETERMINISTIC_58e71056de9ba09c
Batch ID: 20250612_151100
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

// Importing OpenZeppelin's Ownable contract to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating a contract for managing presale purchases
contract DogeversePresale is Ownable {
    
    // Struct to hold buyer information
    struct BuyerInfo {
        address buyerAddress;  // Address of the buyer
        uint256 amountPaid;    // Amount paid in wei
        uint256 timestamp;     // Timestamp of purchase
    }

    // Mapping to store buyer information against their address
    mapping(address => BuyerInfo) public presaleBuyers;

    // Event to log successful purchases
    event PurchaseRecorded(address indexed buyer, uint256 amount, uint256 timestamp);

    // Function to record a presale purchase
    function recordPurchase() external payable {
        require(msg.value > 0, "Payment must be greater than zero");
        require(presaleBuyers[msg.sender].amountPaid == 0, "You have already purchased");

        // Create a new BuyerInfo instance and store it
        presaleBuyers[msg.sender] = BuyerInfo({
            buyerAddress: msg.sender,
            amountPaid: msg.value,
            timestamp: block.timestamp
        });

        // Emit the purchase event
        emit PurchaseRecorded(msg.sender, msg.value, block.timestamp);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the contract's balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to retrieve buyer information
    function getBuyerInfo(address buyer) external view returns (BuyerInfo memory) {
        require(presaleBuyers[buyer].amountPaid > 0, "No purchase found for this address");
        return presaleBuyers[buyer];
    }
}
```
