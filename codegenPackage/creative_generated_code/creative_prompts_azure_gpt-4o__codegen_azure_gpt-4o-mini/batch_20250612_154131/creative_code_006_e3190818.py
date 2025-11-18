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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Ownable contract to restrict access to certain functions
contract Ownable {
    address public owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor() {
        owner = msg.sender; // Set the contract deployer as the initial owner
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Transfer ownership to a new address
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

// DeFi Protocol contract
contract HoldexDeFi is Ownable {
    // Struct to store product information
    struct Product {
        string name;
        uint256 interestRate; // Interest rate in basis points (e.g., 500 = 5%)
        bool isActive;
    }

    // Mapping of product ID to Product details
    mapping(uint256 => Product) public products;
    uint256 public totalProducts;

    // Mapping to store user's deposits
    mapping(address => mapping(uint256 => uint256)) public userDeposits;

    event ProductCreated(uint256 productId, string name, uint256 interestRate);
    event ProductUpdated(uint256 productId, string name, uint256 interestRate);
    event ProductStatusUpdated(uint256 productId, bool isActive);
    event Deposited(address indexed user, uint256 productId, uint256 amount);

    // Create a new product
    function createProduct(string memory name, uint256 interestRate) public onlyOwner {
        require(interestRate > 0, "Interest rate must be greater than 0");
        products[totalProducts] = Product(name, interestRate, true);
        emit ProductCreated(totalProducts, name, interestRate);
        totalProducts++;
    }

    // Update an existing product
    function updateProduct(uint256 productId, string memory name, uint256 interestRate) public onlyOwner {
        require(productId < totalProducts, "Product does not exist");
        require(interestRate > 0, "Interest rate must be greater than 0");

        products[productId].name = name;
        products[productId].interestRate = interestRate;

        emit ProductUpdated(productId, name, interestRate);
    }

    // Update product status (active/inactive)
    function updateProductStatus(uint256 productId, bool isActive) public onlyOwner {
        require(productId < totalProducts, "Product does not exist");
        products[productId].isActive = isActive;

        emit ProductStatusUpdated(productId, isActive);
    }

    // Deposit funds into a specific product
    function deposit(uint256 productId, uint256 amount) public {
        require(productId < totalProducts, "Product does not exist");
        require(products[productId].isActive, "Product is inactive");
        require(amount > 0, "Deposit amount must be greater than 0");

        userDeposits[msg.sender][productId] += amount;

        emit Deposited(msg.sender, productId, amount);
    }

    // Retrieve total deposit of a user for a specific product
    function getUserDeposit(address user, uint256 productId) public view returns (uint256) {
        return userDeposits[user][productId];
    }
}
```
