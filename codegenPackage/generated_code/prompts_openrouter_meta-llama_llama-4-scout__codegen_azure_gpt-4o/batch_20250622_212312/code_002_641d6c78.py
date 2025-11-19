"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Generate code for minting, trading, and collateralizing NFTs on Linea's zkEVM using Ethereum battle-tested components.
Generated: DETERMINISTIC_641d6c78d06e9bf7
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFTMintTradeCollateral
 * @dev Contract for minting, trading, and collateralizing NFTs on Linea's zkEVM.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTMintTradeCollateral is ERC721, Ownable, ReentrancyGuard {
    uint256 public nextTokenId; // Tracks the next token ID to be minted
    uint256 public mintPrice; // Price for minting an NFT
    mapping(uint256 => uint256) public collateral; // Maps token ID to collateral amount
    mapping(uint256 => address) public tokenOwner; // Tracks the owner of each token

    event NFTMinted(address indexed owner, uint256 indexed tokenId);
    event NFTTraded(address indexed seller, address indexed buyer, uint256 indexed tokenId, uint256 price);
    event CollateralDeposited(uint256 indexed tokenId, uint256 amount);
    event CollateralWithdrawn(uint256 indexed tokenId, uint256 amount);

    constructor(string memory name, string memory symbol, uint256 _mintPrice) ERC721(name, symbol) {
        mintPrice = _mintPrice;
    }

    /**
     * @dev Mint a new NFT.
     */
    function mintNFT() external payable nonReentrant {
        require(msg.value == mintPrice, "Incorrect mint price");

        uint256 tokenId = nextTokenId;
        nextTokenId++;

        _safeMint(msg.sender, tokenId);
        tokenOwner[tokenId] = msg.sender;

        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Trade an NFT to a new owner.
     * @param tokenId The ID of the token to trade.
     * @param buyer The address of the buyer.
     * @param price The price of the trade.
     */
    function tradeNFT(uint256 tokenId, address buyer, uint256 price) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(buyer != address(0), "Invalid buyer address");
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the buyer
        _transfer(msg.sender, buyer, tokenId);

        // Transfer the payment to the seller
        (bool success, ) = msg.sender.call{value: price}("");
        require(success, "Payment transfer failed");

        tokenOwner[tokenId] = buyer;

        emit NFTTraded(msg.sender, buyer, tokenId, price);
    }

    /**
     * @dev Deposit collateral for an NFT.
     * @param tokenId The ID of the token to deposit collateral for.
     */
    function depositCollateral(uint256 tokenId) external payable nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(msg.value > 0, "Collateral must be greater than zero");

        collateral[tokenId] += msg.value;

        emit CollateralDeposited(tokenId, msg.value);
    }

    /**
     * @dev Withdraw collateral for an NFT.
     * @param tokenId The ID of the token to withdraw collateral from.
     * @param amount The amount of collateral to withdraw.
     */
    function withdrawCollateral(uint256 tokenId, uint256 amount) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(collateral[tokenId] >= amount, "Insufficient collateral");

        collateral[tokenId] -= amount;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Collateral withdrawal failed");

        emit CollateralWithdrawn(tokenId, amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
