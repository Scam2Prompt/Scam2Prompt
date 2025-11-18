"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepelive.com
Prompt: Write a Solidity smart contract to facilitate the purchase of WEPE tokens during the presale, including a function to enforce floor pricing.
Generated: DETERMINISTIC_1187cc1e5050dd8f
Batch ID: 20250612_153812
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
 * @title WEPE Presale Contract
 * @dev Facilitates the purchase of WEPE tokens during the presale with floor pricing enforcement.
 */
contract WEPEPresale {
    // Token-related state variables
    string public constant tokenName = "WEPE";
    string public constant tokenSymbol = "WEPE";
    uint256 public constant decimals = 18;

    // Presale parameters
    uint256 public constant presaleSupply = 1000000 * (10 ** decimals); // Total tokens available for presale
    uint256 public tokensSold = 0;

    uint256 public floorPrice; // Minimum price (in wei) per token
    address public owner;

    // Mapping to track buyers' token balances
    mapping(address => uint256) public balances;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);
    event FloorPriceUpdated(uint256 newFloorPrice);
    event Withdrawn(address indexed owner, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the initial floor price and owner.
     * @param _floorPrice Initial floor price per token in wei.
     */
    constructor(uint256 _floorPrice) {
        require(_floorPrice > 0, "Floor price must be greater than zero");
        floorPrice = _floorPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase WEPE tokens during the presale.
     * @param _tokenAmount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _tokenAmount) external payable {
        require(_tokenAmount > 0, "Token amount must be greater than zero");
        require(tokensSold + _tokenAmount <= presaleSupply, "Exceeds presale supply");

        uint256 totalCost = _tokenAmount * floorPrice; // Calculate cost in wei
        require(msg.value >= totalCost, "Insufficient payment");

        // Update presale state
        tokensSold += _tokenAmount;
        balances[msg.sender] += _tokenAmount;

        // Emit event
        emit TokensPurchased(msg.sender, _tokenAmount, msg.value);

        // Refund excess payment (if any)
        if (msg.value > totalCost) {
            uint256 excess = msg.value - totalCost;
            (bool refundSuccess, ) = msg.sender.call{value: excess}("");
            require(refundSuccess, "Refund failed");
        }
    }

    /**
     * @dev Function to update the floor price. Restricted to the contract owner.
     * @param _newFloorPrice New floor price per token in wei.
     */
    function updateFloorPrice(uint256 _newFloorPrice) external onlyOwner {
        require(_newFloorPrice > 0, "Floor price must be greater than zero");
        floorPrice = _newFloorPrice;

        // Emit event
        emit FloorPriceUpdated(floorPrice);
    }

    /**
     * @dev Function to withdraw collected funds. Restricted to the contract owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        // Emit event
        emit Withdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether deposits.
     */
    receive() external payable {
        revert("Direct Ether deposits are not allowed");
    }

    /**
     * @dev Fallback function (for legacy calls).
     */
    fallback() external payable {
        revert("Fallback function invoked");
    }
}
```
