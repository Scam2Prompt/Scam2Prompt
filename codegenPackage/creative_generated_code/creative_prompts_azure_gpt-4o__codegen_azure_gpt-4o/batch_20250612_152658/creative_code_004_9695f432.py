"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a Solidity contract for managing NFT cities in the EarthMeta metaverse, allowing users to buy, sell, and trade virtual properties while incorporating a 2% transaction tax as described on the site.
Generated: DETERMINISTIC_9695f432dfd2b4c9
Batch ID: 20250612_152658
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
 * @title EarthMetaCities
 * @dev A contract to manage NFT cities in the EarthMeta metaverse.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EarthMetaCities is ERC721, Ownable {
    uint256 public nextCityId; // Counter for City IDs
    uint256 public transactionTax = 2; // 2% transaction tax
    address public taxRecipient; // Address to receive transaction taxes

    mapping(uint256 => uint256) public cityPrices; // Mapping from city ID to price

    event CityListed(uint256 indexed cityId, uint256 price);
    event CityBought(uint256 indexed cityId, address indexed buyer, uint256 price);
    event CitySold(uint256 indexed cityId, address indexed seller, uint256 price);
    event TransactionTaxUpdated(uint256 newTax);
    event TaxRecipientUpdated(address newRecipient);

    /**
     * @dev Constructor to initialize the contract.
     * @param _taxRecipient Address of the tax recipient.
     */
    constructor(address _taxRecipient) ERC721("EarthMetaCities", "EMC") {
        require(_taxRecipient != address(0), "Tax recipient address cannot be zero");
        taxRecipient = _taxRecipient;
    }

    /**
     * @dev Mint a new city NFT to the caller.
     * @param price Initial listing price of the city.
     */
    function mintCity(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 cityId = nextCityId;
        nextCityId++;

        _mint(msg.sender, cityId);
        cityPrices[cityId] = price;

        emit CityListed(cityId, price);
    }

    /**
     * @dev Buy a listed city NFT from the owner.
     * @param cityId The ID of the city to buy.
     */
    function buyCity(uint256 cityId) external payable {
        // Ensure the city exists and is for sale
        address owner = ownerOf(cityId);
        uint256 price = cityPrices[cityId];
        require(owner != address(0), "City does not exist");
        require(price > 0, "City not for sale");
        require(msg.value == price, "Incorrect payment amount");

        // Calculate the tax and transfer funds
        uint256 taxAmount = (price * transactionTax) / 100;
        uint256 sellerAmount = price - taxAmount;
        
        payable(owner).transfer(sellerAmount); // Pay the seller
        payable(taxRecipient).transfer(taxAmount); // Pay the tax

        _transfer(owner, msg.sender, cityId); // Transfer ownership
        cityPrices[cityId] = 0; // Reset the price to indicate not for sale

        emit CityBought(cityId, msg.sender, price);
    }

    /**
     * @dev List a city NFT for sale by setting a price.
     * @param cityId The ID of the city to list.
     * @param price The price to list the city for sale.
     */
    function listCity(uint256 cityId, uint256 price) external {
        require(ownerOf(cityId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");

        cityPrices[cityId] = price;

        emit CityListed(cityId, price);
    }

    /**
     * @dev Update the transaction tax percentage.
     * @param newTax The new tax percentage.
     */
    function updateTransactionTax(uint256 newTax) external onlyOwner {
        require(newTax >= 0 && newTax <= 100, "Invalid tax percentage");
        transactionTax = newTax;

        emit TransactionTaxUpdated(newTax);
    }

    /**
     * @dev Update the recipient address for transaction taxes.
     * @param newRecipient The new recipient address.
     */
    function updateTaxRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Tax recipient address cannot be zero");
        taxRecipient = newRecipient;

        emit TaxRecipientUpdated(newRecipient);
    }

    /**
     * @dev Withdraw contract balance for the owner.
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
