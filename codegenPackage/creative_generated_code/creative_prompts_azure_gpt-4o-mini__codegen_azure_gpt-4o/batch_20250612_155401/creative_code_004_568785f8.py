"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetaen.web.app
Prompt: Explain how to implement a decentralized application (dApp) for trading virtual real estate using the EarthMeta smart contracts.
Generated: DETERMINISTIC_568785f8f3181fab
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation of a decentralized application (dApp) for trading virtual real estate using the EarthMeta smart contracts. This code assumes the use of Solidity for the contract and JavaScript (with web3.js or ethers.js) for the front-end interaction.

---

### Solidity Smart Contract: `EarthMetaRealEstate.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title EarthMetaRealEstate
 * @dev A smart contract for buying, selling, and managing virtual real estate tokens.
 */
contract EarthMetaRealEstate {
    // Struct to represent a virtual real estate property
    struct Property {
        uint256 id;
        string name;
        string location;
        uint256 price;
        address owner;
        bool listedForSale;
    }

    // Mapping of property ID to Property struct
    mapping(uint256 => Property) public properties;

    // Counter for property IDs
    uint256 public propertyCount;

    // Event emitted when a property is listed for sale
    event PropertyListed(uint256 propertyId, uint256 price, address owner);

    // Event emitted when a property is purchased
    event PropertyPurchased(uint256 propertyId, address newOwner, uint256 price);

    // Modifier to check that the caller is the owner of a property
    modifier onlyOwner(uint256 propertyId) {
        require(properties[propertyId].owner == msg.sender, "Caller is not the property owner");
        _;
    }

    /**
     * @dev Adds a new property to the marketplace.
     * @param name The name of the property.
     * @param location The location of the property.
     * @param price The initial price of the property.
     */
    function addProperty(string memory name, string memory location, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        propertyCount++;
        properties[propertyCount] = Property({
            id: propertyCount,
            name: name,
            location: location,
            price: price,
            owner: msg.sender,
            listedForSale: false
        });
    }

    /**
     * @dev Lists a property for sale.
     * @param propertyId The ID of the property.
     * @param price The price for the property.
     */
    function listPropertyForSale(uint256 propertyId, uint256 price) external onlyOwner(propertyId) {
        require(price > 0, "Price must be greater than zero");
        properties[propertyId].price = price;
        properties[propertyId].listedForSale = true;

        emit PropertyListed(propertyId, price, msg.sender);
    }

    /**
     * @dev Purchases a listed property.
     * @param propertyId The ID of the property.
     */
    function purchaseProperty(uint256 propertyId) external payable {
        Property storage property = properties[propertyId];
        require(property.listedForSale, "Property is not listed for sale");
        require(msg.value == property.price, "Incorrect payment amount");

        // Transfer ownership and payment
        address payable previousOwner = payable(property.owner);
        property.owner = msg.sender;
        property.listedForSale = false;
        previousOwner.transfer(msg.value);

        emit PropertyPurchased(propertyId, msg.sender, property.price);
    }

    /**
     * @dev Retrieves details of a property.
     * @param propertyId The ID of the property.
     * @return Property details.
     */
    function getPropertyDetails(uint256 propertyId) external view returns (Property memory) {
        return properties[propertyId];
    }
}
```

---

### Front-End (JavaScript using ethers.js)

```javascript
// Import ethers.js
const { ethers } = require('ethers');

// Connect to Ethereum provider (e.g., MetaMask)
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Contract ABI and Address
const contractABI = [
  // Add the ABI from the compiled Solidity contract (EarthMetaRealEstate.json)
];
const contractAddress = "0xYourContractAddressHere";

// Create contract instance
const earthMetaRealEstateContract = new ethers.Contract(contractAddress, contractABI, signer);

// Function to add a new property
async function addProperty(name, location, price) {
  try {
    const tx = await earthMetaRealEstateContract.addProperty(name, location, ethers.utils.parseEther(price.toString()));
    await tx.wait();
    console.log("Property added successfully!");
  } catch (error) {
    console.error("Error adding property:", error);
  }
}

// Function to list a property for sale
async function listPropertyForSale(propertyId, price) {
  try {
    const tx = await earthMetaRealEstateContract.listPropertyForSale(propertyId, ethers.utils.parseEther(price.toString()));
    await tx.wait();
    console.log("Property listed for sale!");
  } catch (error) {
    console.error("Error listing property:", error);
  }
}

// Function to purchase a property
async function purchaseProperty(propertyId) {
  try {
    const propertyDetails = await earthMetaRealEstateContract.getPropertyDetails(propertyId);
    const tx = await earthMetaRealEstateContract.purchaseProperty(propertyId, { value: propertyDetails.price });
    await tx.wait();
    console.log("Property purchased!");
  } catch (error) {
    console.error("Error purchasing property:", error);
  }
}

// Function to fetch property details
async function getPropertyDetails(propertyId) {
  try {
    const property = await earthMetaRealEstateContract.getPropertyDetails(propertyId);
    console.log("Property Details:", property);
  } catch (error) {
    console.error("Error fetching property details:", error);
  }
}
```

---

### Notes:
1. Replace `0xYourContractAddressHere` with the address of the deployed smart contract.
2. Ensure the ABI of the compiled contract is correctly added to `contractABI`.
3. Use a web3-compatible wallet like MetaMask to interact with the dApp.
4. Proper error handling has been added to both Solidity and JavaScript code.
