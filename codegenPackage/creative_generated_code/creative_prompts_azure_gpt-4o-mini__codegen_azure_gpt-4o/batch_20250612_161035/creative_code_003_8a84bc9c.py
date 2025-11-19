"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Develop a smart contract for secure property transactions using Global Miracle Coin, ensuring transparency and immutability.
Generated: DETERMINISTIC_8a84bc9ca25c81d2
Batch ID: 20250612_161035
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
 * @title PropertyTransaction
 * @dev A smart contract for secure property transactions using Global Miracle Coin (GMC).
 */
contract PropertyTransaction {
    // Address of the contract owner
    address public owner;

    // Define the Global Miracle Coin (GMC) token interface
    IERC20 public gmcToken;

    // Events for logging transactions
    event PropertyListed(uint256 propertyId, address seller, uint256 price);
    event PropertyPurchased(uint256 propertyId, address buyer, address seller, uint256 price);

    // Struct to represent a property
    struct Property {
        uint256 id;
        address seller;
        uint256 price;
        bool isAvailable;
    }

    // Mapping of property IDs to property details
    mapping(uint256 => Property) public properties;

    // Counter for generating unique property IDs
    uint256 private propertyCounter;

    /**
     * @dev Contract constructor
     * @param _gmcTokenAddress Address of the Global Miracle Coin token contract
     */
    constructor(address _gmcTokenAddress) {
        owner = msg.sender; // Initialize contract owner
        gmcToken = IERC20(_gmcTokenAddress); // Set GMC token interface
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev List a property for sale
     * @param _price Price of the property in GMC tokens
     */
    function listProperty(uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Increment property counter to generate a unique ID
        propertyCounter++;

        // Create a new property
        properties[propertyCounter] = Property({
            id: propertyCounter,
            seller: msg.sender,
            price: _price,
            isAvailable: true
        });

        // Emit an event for property listing
        emit PropertyListed(propertyCounter, msg.sender, _price);
    }

    /**
     * @dev Purchase a property
     * @param _propertyId The ID of the property to purchase
     */
    function purchaseProperty(uint256 _propertyId) external {
        Property storage property = properties[_propertyId];

        // Validate property availability
        require(property.isAvailable, "Property is not available for purchase");

        // Validate buyer's balance
        require(
            gmcToken.balanceOf(msg.sender) >= property.price,
            "Insufficient GMC balance"
        );

        // Transfer GMC tokens from buyer to seller
        bool success = gmcToken.transferFrom(msg.sender, property.seller, property.price);
        require(success, "Token transfer failed");

        // Mark the property as sold
        property.isAvailable = false;

        // Emit an event for property purchase
        emit PropertyPurchased(_propertyId, msg.sender, property.seller, property.price);
    }

    /**
     * @dev Withdraw GMC tokens from the contract (only owner)
     * @param _amount Amount of GMC tokens to withdraw
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(gmcToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        bool success = gmcToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Change the GMC token contract address (only owner)
     * @param _newAddress New GMC token contract address
     */
    function updateGmcTokenAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        gmcToken = IERC20(_newAddress);
    }
}

// Minimal interface for ERC20 token functionality
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
