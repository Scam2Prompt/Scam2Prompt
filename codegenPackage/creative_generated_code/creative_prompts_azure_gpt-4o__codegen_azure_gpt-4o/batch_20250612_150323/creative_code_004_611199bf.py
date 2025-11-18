"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Write a script to automate proxy sales for NFTs using a contract structure similar to the Proxy Sales Contract mentioned on the CryptoTitties site.
Generated: DETERMINISTIC_611199bfcdaf87e1
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Smart Contract written in Solidity for automating proxy sales for NFTs. It includes error handling, follows best practices, and is well-documented with comments in the code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ProxyNFTSale
 * @dev A contract to facilitate proxy sales of NFTs
 */
contract ProxyNFTSale {
    // Struct to store sale details
    struct Sale {
        address seller;
        address buyer;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool completed;
    }

    // Event to log the creation of a new sale
    event SaleCreated(
        uint256 indexed saleId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );

    // Event to log the completion of a sale
    event SaleCompleted(
        uint256 indexed saleId,
        address indexed buyer,
        address indexed seller,
        uint256 tokenId
    );

    // Mapping to store sales by ID
    mapping(uint256 => Sale) public sales;

    // Counter for sales IDs
    uint256 public saleCounter;

    // Address of the contract owner
    address public owner;

    /**
     * @dev Modifier to restrict certain actions to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to ensure the sale exists
     * @param saleId The ID of the sale
     */
    modifier saleExists(uint256 saleId) {
        require(sales[saleId].seller != address(0), "Sale does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new sale
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the token being sold
     * @param price Price of the token in wei
     */
    function createSale(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero");

        // Increment the sale counter
        saleCounter++;

        // Create a new sale
        sales[saleCounter] = Sale({
            seller: msg.sender,
            buyer: address(0),
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            completed: false
        });

        emit SaleCreated(saleCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Function to complete a sale
     * @param saleId ID of the sale to complete
     */
    function completeSale(uint256 saleId) external payable saleExists(saleId) {
        Sale storage sale = sales[saleId];

        require(!sale.completed, "Sale has already been completed");
        require(msg.value == sale.price, "Incorrect payment amount");

        // Transfer the NFT from seller to buyer
        IERC721(sale.nftContract).transferFrom(sale.seller, msg.sender, sale.tokenId);

        // Transfer payment to the seller
        payable(sale.seller).transfer(msg.value);

        // Mark the sale as completed
        sale.completed = true;
        sale.buyer = msg.sender;

        emit SaleCompleted(saleId, msg.sender, sale.seller, sale.tokenId);
    }

    /**
     * @dev Function to withdraw any accidental ETH sent to the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }
}

/**
 * @dev Interface for interacting with ERC721 NFTs
 */
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```

### Notes: 
- Ensure the NFT contract supports `IERC721.transferFrom`. 
- Before deploying this contract, test thoroughly in a controlled environment.
