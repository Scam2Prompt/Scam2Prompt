"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code to integrate Ethereum-based token payments into a decentralized marketplace, referencing Pushd's use of native tokens for transaction fees and voting rights.
Generated: DETERMINISTIC_32cf22cade448a62
Batch ID: 20250612_145923
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

// Import necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for integrating Ethereum-based token payments
contract DecentralizedMarketplace is Ownable {
    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed itemId, address indexed seller, uint256 price, address tokenAddress);
    
    // Event emitted when a purchase is made
    event ItemPurchased(uint256 indexed itemId, address indexed buyer, address indexed seller, uint256 price);

    // Struct to represent an item in the marketplace
    struct Item {
        uint256 id;
        address seller;
        uint256 price;
        address tokenAddress; // Token used for payment
        bool isListed;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;

    // Counter for item IDs
    uint256 public itemCount;

    /**
     * @notice Lists a new item for sale in the marketplace
     * @param _price The price of the item
     * @param _tokenAddress The address of the ERC20 token used for payment
     */
    function listItem(uint256 _price, address _tokenAddress) external {
        require(_price > 0, "Price must be greater than zero");
        require(_tokenAddress != address(0), "Invalid token address");

        itemCount++;
        items[itemCount] = Item(itemCount, msg.sender, _price, _tokenAddress, true);

        emit ItemListed(itemCount, msg.sender, _price, _tokenAddress);
    }

    /**
     * @notice Buys an item listed in the marketplace
     * @param _itemId The ID of the item to purchase
     */
    function purchaseItem(uint256 _itemId) external {
        Item storage item = items[_itemId];

        require(item.isListed, "Item is not listed");
        require(item.price > 0, "Item price must be greater than zero");

        // Transfer the payment from the buyer to the seller
        IERC20(item.tokenAddress).transferFrom(msg.sender, item.seller, item.price);

        // Mark the item as sold
        item.isListed = false;

        emit ItemPurchased(_itemId, msg.sender, item.seller, item.price);
    }

    /**
     * @notice Retrieves the details of an item by its ID
     * @param _itemId The ID of the item
     * @return id The ID of the item
     * @return seller The address of the seller
     * @return price The price of the item
     * @return tokenAddress The address of the token used for payment
     * @return isListed Whether the item is currently listed for sale
     */
    function getItem(uint256 _itemId) external view returns (uint256 id, address seller, uint256 price, address tokenAddress, bool isListed) {
        Item storage item = items[_itemId];
        return (item.id, item.seller, item.price, item.tokenAddress, item.isListed);
    }

    /**
     * @notice Allows the owner to withdraw tokens from the contract
     * @param _tokenAddress The address of the ERC20 token to withdraw
     * @param _amount The amount of tokens to withdraw
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(IERC20(_tokenAddress).balanceOf(address(this)) >= _amount, "Insufficient balance");
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
