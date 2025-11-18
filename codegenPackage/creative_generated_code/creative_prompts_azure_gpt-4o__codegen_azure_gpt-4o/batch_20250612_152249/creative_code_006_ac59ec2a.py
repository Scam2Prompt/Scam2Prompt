"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Develop a smart contract in Solidity to facilitate decentralized commodity trading (e.g., Gold, Silver, Coffee) on the CVEX platform using USDC as collateral.
Generated: DETERMINISTIC_ac59ec2adfb81bc0
Batch ID: 20250612_152249
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
 * @title CommodityTrading
 * @dev A smart contract for decentralized commodity trading on the CVEX platform using USDC as collateral.
 *      Allows users to list, trade, and settle commodity orders in a secure and transparent manner.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract CommodityTrading {
    // ERC20 Token (USDC) used as collateral
    IERC20 public usdcToken;

    // Commodity struct to store details of a listed commodity
    struct Commodity {
        uint256 id;
        string name;
        uint256 pricePerUnit; // Price in USDC (scaled by 1e6 to match USDC decimals)
        uint256 quantityAvailable;
        address seller;
    }

    // Order struct to store details of a traded commodity
    struct Order {
        uint256 commodityId;
        uint256 quantity;
        uint256 totalPrice; // Price in USDC
        address buyer;
    }

    // Commodity ID generator
    uint256 private nextCommodityId;

    // Mapping to store listed commodities
    mapping(uint256 => Commodity) public commodities;

    // Mapping to store active orders
    mapping(uint256 => Order) public orders;

    // Event emitted when a new commodity is listed
    event CommodityListed(uint256 id, string name, uint256 pricePerUnit, uint256 quantityAvailable, address seller);

    // Event emitted when a commodity is ordered
    event CommodityOrdered(uint256 orderId, uint256 commodityId, uint256 quantity, uint256 totalPrice, address buyer);

    // Event emitted when an order is settled and the buyer receives the commodity
    event OrderSettled(uint256 orderId, uint256 commodityId, uint256 quantity, uint256 totalPrice, address buyer, address seller);

    /**
     * @dev Constructor to initialize the USDC token contract.
     * @param _usdcToken Address of the USDC ERC20 token contract.
     */
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "USDC token address cannot be zero");
        usdcToken = IERC20(_usdcToken);
    }

    /**
     * @dev Function to list a new commodity for sale.
     * @param _name Name of the commodity (e.g., Gold, Silver, Coffee).
     * @param _pricePerUnit Price per unit of the commodity (in USDC, scaled by 1e6).
     * @param _quantityAvailable Quantity of the commodity available for sale.
     */
    function listCommodity(string memory _name, uint256 _pricePerUnit, uint256 _quantityAvailable) external {
        require(bytes(_name).length > 0, "Commodity name cannot be empty");
        require(_pricePerUnit > 0, "Price per unit must be greater than zero");
        require(_quantityAvailable > 0, "Quantity available must be greater than zero");

        uint256 commodityId = nextCommodityId++;
        commodities[commodityId] = Commodity(commodityId, _name, _pricePerUnit, _quantityAvailable, msg.sender);

        emit CommodityListed(commodityId, _name, _pricePerUnit, _quantityAvailable, msg.sender);
    }

    /**
     * @dev Function to order a commodity.
     * @param _commodityId ID of the commodity to order.
     * @param _quantity Quantity of the commodity to order.
     */
    function orderCommodity(uint256 _commodityId, uint256 _quantity) external {
        Commodity storage commodity = commodities[_commodityId];
        require(commodity.quantityAvailable >= _quantity, "Not enough quantity available");
        require(_quantity > 0, "Order quantity must be greater than zero");

        uint256 totalPrice = _quantity * commodity.pricePerUnit;
        require(usdcToken.transferFrom(msg.sender, address(this), totalPrice), "USDC transfer failed");

        commodity.quantityAvailable -= _quantity;

        uint256 orderId = _commodityId; // Order ID is same as commodity ID for simplicity (can be improved)
        orders[orderId] = Order(_commodityId, _quantity, totalPrice, msg.sender);

        emit CommodityOrdered(orderId, _commodityId, _quantity, totalPrice, msg.sender);
    }

    /**
     * @dev Function to settle an order and transfer payment to the seller.
     * @param _orderId ID of the order to settle.
     */
    function settleOrder(uint256 _orderId) external {
        Order storage order = orders[_orderId];
        require(order.buyer == msg.sender, "Only the buyer can settle the order");

        Commodity storage commodity = commodities[order.commodityId];
        require(commodity.seller != address(0), "Invalid commodity seller");

        // Transfer payment to the seller
        require(usdcToken.transfer(commodity.seller, order.totalPrice), "USDC transfer to seller failed");

        emit OrderSettled(_orderId, order.commodityId, order.quantity, order.totalPrice, order.buyer, commodity.seller);

        // Delete the order
        delete orders[_orderId];
    }
}
```
