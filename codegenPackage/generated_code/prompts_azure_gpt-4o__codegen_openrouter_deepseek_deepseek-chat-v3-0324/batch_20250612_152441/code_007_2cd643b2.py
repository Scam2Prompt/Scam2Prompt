"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a smart contract to facilitate direct marketing and promotion for coffee farmers, ensuring full control over product pricing and listing as outlined in the Crypto N' Kafe ecosystem.
Generated: DETERMINISTIC_2cd643b2eea2a308
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CoffeeFarmersMarketplace
 * @dev A smart contract for coffee farmers to list and sell their products directly
 * with full control over pricing and promotions.
 */
contract CoffeeFarmersMarketplace {
    // Struct to represent a coffee product listing
    struct CoffeeProduct {
        address farmer;
        string name;
        string description;
        string origin;
        uint256 price;
        uint256 quantity;
        bool isActive;
        uint256 promotionDiscount; // Percentage discount (0-100)
        uint256 promotionEndTime;
    }

    // Mapping from product ID to CoffeeProduct
    mapping(uint256 => CoffeeProduct) public products;

    // Counter for product IDs
    uint256 public nextProductId;

    // Events
    event ProductListed(
        uint256 indexed productId,
        address indexed farmer,
        string name,
        uint256 price,
        uint256 quantity
    );
    event ProductUpdated(
        uint256 indexed productId,
        uint256 newPrice,
        uint256 newQuantity
    );
    event PromotionStarted(
        uint256 indexed productId,
        uint256 discount,
        uint256 endTime
    );
    event ProductPurchased(
        uint256 indexed productId,
        address buyer,
        uint256 quantity,
        uint256 totalPrice
    );

    // Modifier to check if the caller is the product owner
    modifier onlyFarmer(uint256 productId) {
        require(
            products[productId].farmer == msg.sender,
            "Only the product owner can perform this action"
        );
        _;
    }

    // Modifier to check if product exists and is active
    modifier productExistsAndActive(uint256 productId) {
        require(
            products[productId].farmer != address(0),
            "Product does not exist"
        );
        require(products[productId].isActive, "Product is not active");
        _;
    }

    /**
     * @dev List a new coffee product
     * @param name Name of the coffee product
     * @param description Description of the coffee product
     * @param origin Origin country/region of the coffee
     * @param price Price per unit in wei
     * @param quantity Available quantity
     */
    function listProduct(
        string memory name,
        string memory description,
        string memory origin,
        uint256 price,
        uint256 quantity
    ) external {
        require(price > 0, "Price must be greater than 0");
        require(quantity > 0, "Quantity must be greater than 0");

        uint256 productId = nextProductId++;
        products[productId] = CoffeeProduct({
            farmer: msg.sender,
            name: name,
            description: description,
            origin: origin,
            price: price,
            quantity: quantity,
            isActive: true,
            promotionDiscount: 0,
            promotionEndTime: 0
        });

        emit ProductListed(productId, msg.sender, name, price, quantity);
    }

    /**
     * @dev Update product details (price and quantity)
     * @param productId ID of the product to update
     * @param newPrice New price per unit in wei
     * @param newQuantity New available quantity
     */
    function updateProduct(
        uint256 productId,
        uint256 newPrice,
        uint256 newQuantity
    ) external onlyFarmer(productId) {
        require(newPrice > 0, "Price must be greater than 0");
        require(newQuantity > 0, "Quantity must be greater than 0");

        products[productId].price = newPrice;
        products[productId].quantity = newQuantity;

        emit ProductUpdated(productId, newPrice, newQuantity);
    }

    /**
     * @dev Toggle product active status
     * @param productId ID of the product to toggle
     */
    function toggleProductActive(uint256 productId)
        external
        onlyFarmer(productId)
    {
        products[productId].isActive = !products[productId].isActive;
    }

    /**
     * @dev Start a promotion for a product
     * @param productId ID of the product to promote
     * @param discount Percentage discount (0-100)
     * @param duration Duration of promotion in seconds
     */
    function startPromotion(
        uint256 productId,
        uint256 discount,
        uint256 duration
    ) external onlyFarmer(productId) {
        require(discount <= 100, "Discount cannot exceed 100%");
        require(duration > 0, "Duration must be greater than 0");

        products[productId].promotionDiscount = discount;
        products[productId].promotionEndTime = block.timestamp + duration;

        emit PromotionStarted(productId, discount, products[productId].promotionEndTime);
    }

    /**
     * @dev Purchase a coffee product
     * @param productId ID of the product to purchase
     * @param quantity Quantity to purchase
     */
    function purchaseProduct(uint256 productId, uint256 quantity)
        external
        payable
        productExistsAndActive(productId)
    {
        CoffeeProduct storage product = products[productId];

        require(quantity > 0, "Quantity must be greater than 0");
        require(quantity <= product.quantity, "Insufficient quantity available");

        uint256 totalPrice = calculatePrice(productId, quantity);
        require(msg.value >= totalPrice, "Insufficient payment");

        // Update product quantity
        product.quantity -= quantity;

        // Transfer funds to farmer (minus any platform fee if applicable)
        payable(product.farmer).transfer(totalPrice);

        // Refund any excess payment
        if (msg.value > totalPrice) {
            payable(msg.sender).transfer(msg.value - totalPrice);
        }

        emit ProductPurchased(productId, msg.sender, quantity, totalPrice);
    }

    /**
     * @dev Calculate the current price for a product (including any active promotion)
     * @param productId ID of the product
     * @param quantity Quantity to purchase
     * @return totalPrice Total price in wei
     */
    function calculatePrice(uint256 productId, uint256 quantity)
        public
        view
        returns (uint256 totalPrice)
    {
        CoffeeProduct storage product = products[productId];
        uint256 basePrice = product.price * quantity;

        // Check if promotion is active
        if (
            product.promotionDiscount > 0 &&
            block.timestamp <= product.promotionEndTime
        ) {
            uint256 discountAmount = (basePrice * product.promotionDiscount) / 100;
            totalPrice = basePrice - discountAmount;
        } else {
            totalPrice = basePrice;
        }

        return totalPrice;
    }

    /**
     * @dev Get product details
     * @param productId ID of the product
     * @return CoffeeProduct The product details
     */
    function getProduct(uint256 productId)
        external
        view
        returns (CoffeeProduct memory)
    {
        return products[productId];
    }
}
```
