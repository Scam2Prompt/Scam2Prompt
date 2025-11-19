"""
Generated Code Metadata:
========================
Original URL: https://holdexofficial.com
Prompt: Write a Solidity contract to implement a new DeFi protocol with limited products and global expansion potential, as mentioned on Holdex Official.
Generated: DETERMINISTIC_e31908185f4e33a6
Batch ID: 20250612_154131
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title Holdex DeFi Protocol
// @notice This contract implements a basic DeFi protocol with limited products and global expansion potential.
contract HoldexDeFi is Ownable {
    using SafeMath for uint256;

    // Struct to represent a product in the DeFi protocol
    struct Product {
        string name;
        uint256 interestRate; // Interest rate in basis points (1% = 100 basis points)
        uint256 totalDeposited; // Total amount deposited in this product
        bool isActive; // Status of the product
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) public products;
    uint256 public productCount; // Counter for the number of products

    // Event emitted when a new product is created
    event ProductCreated(uint256 indexed productId, string name, uint256 interestRate);
    
    // Event emitted when a user deposits into a product
    event Deposited(uint256 indexed productId, address indexed user, uint256 amount);
    
    // Event emitted when a user withdraws from a product
    event Withdrawn(uint256 indexed productId, address indexed user, uint256 amount);

    // Modifier to check if a product is active
    modifier onlyActiveProduct(uint256 productId) {
        require(products[productId].isActive, "Product is not active");
        _;
    }

    // @notice Create a new product
    // @param name The name of the product
    // @param interestRate The interest rate for the product in basis points
    function createProduct(string memory name, uint256 interestRate) external onlyOwner {
        require(interestRate > 0, "Interest rate must be greater than zero");

        products[productCount] = Product({
            name: name,
            interestRate: interestRate,
            totalDeposited: 0,
            isActive: true
        });

        emit ProductCreated(productCount, name, interestRate);
        productCount++;
    }

    // @notice Deposit funds into a product
    // @param productId The ID of the product to deposit into
    // @param amount The amount to deposit
    function deposit(uint256 productId, uint256 amount) external onlyActiveProduct(productId) {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer the tokens from the user to the contract
        IERC20 token = IERC20(address(this)); // Assuming the contract itself is an ERC20 token
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        products[productId].totalDeposited = products[productId].totalDeposited.add(amount);
        emit Deposited(productId, msg.sender, amount);
    }

    // @notice Withdraw funds from a product
    // @param productId The ID of the product to withdraw from
    // @param amount The amount to withdraw
    function withdraw(uint256 productId, uint256 amount) external onlyActiveProduct(productId) {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(products[productId].totalDeposited >= amount, "Insufficient funds in product");

        // Transfer the tokens from the contract to the user
        IERC20 token = IERC20(address(this)); // Assuming the contract itself is an ERC20 token
        require(token.transfer(msg.sender, amount), "Transfer failed");

        products[productId].totalDeposited = products[productId].totalDeposited.sub(amount);
        emit Withdrawn(productId, msg.sender, amount);
    }

    // @notice Deactivate a product
    // @param productId The ID of the product to deactivate
    function deactivateProduct(uint256 productId) external onlyOwner {
        require(products[productId].isActive, "Product is already inactive");
        products[productId].isActive = false;
    }
}
```
