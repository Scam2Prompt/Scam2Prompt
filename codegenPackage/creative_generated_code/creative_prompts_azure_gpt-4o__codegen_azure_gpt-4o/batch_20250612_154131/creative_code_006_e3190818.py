"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdexofficial.com
Prompt: Write a Solidity contract to implement a new DeFi protocol with limited products and global expansion potential, as mentioned on Holdex Official.
Generated: DETERMINISTIC_e31908185f4e33a6
Batch ID: 20250612_154131
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
 * @title HoldexDeFiProtocol
 * @dev A decentralized finance protocol with limited products and global expansion potential.
 */
contract HoldexDeFiProtocol {
    // Struct to represent a product in the protocol
    struct Product {
        string name;
        uint256 totalDeposits;
        uint256 interestRate; // Annual interest rate in basis points (e.g., 500 = 5%)
        bool isActive;
    }

    // Owner of the contract
    address public owner;

    // List of products offered by the protocol
    Product[] public products;

    // Mapping of user balances per product
    mapping(uint256 => mapping(address => uint256)) public userBalances;

    // Events
    event ProductAdded(uint256 productId, string name, uint256 interestRate);
    event DepositMade(address indexed user, uint256 productId, uint256 amount);
    event WithdrawalMade(address indexed user, uint256 productId, uint256 amount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if the product is active
    modifier productIsActive(uint256 productId) {
        require(productId < products.length, "Invalid product ID");
        require(products[productId].isActive, "Product is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new product to the protocol
     * @param name The name of the product
     * @param interestRate Annual interest rate in basis points
     */
    function addProduct(string memory name, uint256 interestRate) external onlyOwner {
        products.push(Product({
            name: name,
            totalDeposits: 0,
            interestRate: interestRate,
            isActive: true
        }));
        emit ProductAdded(products.length - 1, name, interestRate);
    }

    /**
     * @dev Deactivate a product
     * @param productId The ID of the product to deactivate
     */
    function deactivateProduct(uint256 productId) external onlyOwner {
        require(productId < products.length, "Invalid product ID");
        products[productId].isActive = false;
    }

    /**
     * @dev Deposit funds into a product
     * @param productId The ID of the product to deposit into
     */
    function deposit(uint256 productId) external payable productIsActive(productId) {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user balance and total deposits for the product
        userBalances[productId][msg.sender] += msg.value;
        products[productId].totalDeposits += msg.value;

        emit DepositMade(msg.sender, productId, msg.value);
    }

    /**
     * @dev Withdraw funds from a product
     * @param productId The ID of the product to withdraw from
     * @param amount The amount of funds to withdraw
     */
    function withdraw(uint256 productId, uint256 amount) external productIsActive(productId) {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[productId][msg.sender] >= amount, "Insufficient balance");

        // Update user balance and total deposits for the product
        userBalances[productId][msg.sender] -= amount;
        products[productId].totalDeposits -= amount;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit WithdrawalMade(msg.sender, productId, amount);
    }

    /**
     * @dev Get details of a product
     * @param productId The ID of the product
     * @return name The name of the product
     * @return totalDeposits The total deposits in the product
     * @return interestRate The annual interest rate of the product
     * @return isActive Whether the product is active
     */
    function getProduct(uint256 productId)
        external
        view
        returns (string memory name, uint256 totalDeposits, uint256 interestRate, bool isActive)
    {
        require(productId < products.length, "Invalid product ID");
        Product memory product = products[productId];
        return (product.name, product.totalDeposits, product.interestRate, product.isActive);
    }

    /**
     * @dev Get the balance of a user in a specific product
     * @param productId The ID of the product
     * @param user The address of the user
     * @return balance The balance of the user in the product
     */
    function getUserBalance(uint256 productId, address user) external view returns (uint256 balance) {
        require(productId < products.length, "Invalid product ID");
        return userBalances[productId][user];
    }
}
```
