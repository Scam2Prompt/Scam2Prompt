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

/**
 * @title DogeversePresale
 * @dev Smart contract for securely storing presale purchase information for $DOGEVERSE buyers.
 */
contract DogeversePresale {
    // Owner of the contract
    address public owner;

    // Struct to hold presale purchase data
    struct Purchase {
        address buyer;
        uint256 amountPaid; // In wei
        uint256 tokensPurchased; // $DOGEVERSE tokens
        uint256 timestamp; // Time of purchase
    }

    // Mapping to store purchases by buyer address
    mapping(address => Purchase[]) public purchases;

    // Event emitted when a purchase is recorded
    event PurchaseRecorded(
        address indexed buyer,
        uint256 amountPaid,
        uint256 tokensPurchased,
        uint256 timestamp
    );

    // Error for unauthorized actions
    error Unauthorized();

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Records a presale purchase on-chain.
     * @param _buyer Address of the buyer.
     * @param _amountPaid Amount paid by the buyer in wei.
     * @param _tokensPurchased Number of $DOGEVERSE tokens purchased.
     */
    function recordPurchase(
        address _buyer,
        uint256 _amountPaid,
        uint256 _tokensPurchased
    ) external onlyOwner {
        require(_buyer != address(0), "Invalid buyer address");
        require(_amountPaid > 0, "Amount paid must be greater than zero");
        require(_tokensPurchased > 0, "Tokens purchased must be greater than zero");

        // Create a new purchase entry
        Purchase memory newPurchase = Purchase({
            buyer: _buyer,
            amountPaid: _amountPaid,
            tokensPurchased: _tokensPurchased,
            timestamp: block.timestamp
        });

        // Store the purchase in the mapping
        purchases[_buyer].push(newPurchase);

        // Emit the PurchaseRecorded event
        emit PurchaseRecorded(_buyer, _amountPaid, _tokensPurchased, block.timestamp);
    }

    /**
     * @dev Retrieves all presale purchases made by a buyer.
     * @param _buyer Address of the buyer.
     * @return Array of Purchase structs.
     */
    function getPurchases(address _buyer) external view returns (Purchase[] memory) {
        return purchases[_buyer];
    }

    /**
     * @dev Updates the contract owner. Can only be called by the current owner.
     * @param _newOwner Address of the new owner.
     */
    function updateOwner(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
