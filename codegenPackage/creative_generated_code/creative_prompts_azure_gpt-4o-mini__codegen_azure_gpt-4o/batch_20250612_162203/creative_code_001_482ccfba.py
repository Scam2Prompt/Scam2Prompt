"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-staking-iota.vercel.app
Prompt: How can I implement a buyback mechanism for NFTs similar to Lifinity Flares using Solidity?
Generated: DETERMINISTIC_482ccfba45d7a0c4
Batch ID: 20250612_162203
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
 * @title NFT Buyback Mechanism
 * @dev Implements an NFT buyback system where users can sell their NFTs back to the contract
 */
contract NFTBuyback {
    // Event emitted when an NFT is bought back
    event NFTBoughtBack(address indexed seller, uint256 indexed tokenId, uint256 buybackPrice);

    // ERC721 token contract address
    address public nftContract;

    // Address where funds for buybacks are held
    address public buybackFund;

    // Mapping of token IDs to their respective buyback prices
    mapping(uint256 => uint256) public buybackPrices;

    // Modifier to restrict access to only the buyback fund owner
    modifier onlyBuybackFundOwner() {
        require(msg.sender == buybackFund, "Caller is not the buyback fund owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _nftContract Address of the NFT contract
     * @param _buybackFund Address where funds are held for buybacks
     */
    constructor(address _nftContract, address _buybackFund) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_buybackFund != address(0), "Invalid buyback fund address");

        nftContract = _nftContract;
        buybackFund = _buybackFund;
    }

    /**
     * @dev Sets the buyback price for a specific token ID
     * @param tokenId The ID of the token to set the buyback price for
     * @param price The buyback price (in wei)
     */
    function setBuybackPrice(uint256 tokenId, uint256 price) external onlyBuybackFundOwner {
        require(price > 0, "Buyback price must be greater than zero");
        buybackPrices[tokenId] = price;
    }

    /**
     * @dev Executes the buyback of an NFT
     * @param tokenId The ID of the token to buy back
     */
    function buybackNFT(uint256 tokenId) external {
        uint256 price = buybackPrices[tokenId];
        require(price > 0, "Token is not eligible for buyback");

        // Ensure the caller owns the NFT
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Transfer the NFT from the seller to the buyback fund
        IERC721(nftContract).transferFrom(msg.sender, buybackFund, tokenId);

        // Send the buyback price to the seller
        (bool sent, ) = msg.sender.call{value: price}("");
        require(sent, "Failed to transfer buyback price");

        // Clear the buyback price for the token
        buybackPrices[tokenId] = 0;

        // Emit an event for the buyback
        emit NFTBoughtBack(msg.sender, tokenId, price);
    }

    /**
     * @dev Allows the buyback fund owner to withdraw contract funds
     */
    function withdrawFunds(uint256 amount) external onlyBuybackFundOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool sent, ) = buybackFund.call{value: amount}("");
        require(sent, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Interface for ERC721 NFT contract interaction
     */
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
        function transferFrom(address from, address to, uint256 tokenId) external;
    }
}
```
