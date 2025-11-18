"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Create a Solidity smart contract for a GMNTCoin-based NFT marketplace that supports transactions on the Binance Smart Chain with reduced fees compared to Ethereum.
Generated: DETERMINISTIC_e6f202f43aee2b08
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title GMNTCoin NFT Marketplace
 * @notice A marketplace for NFTs that uses GMNTCoin for transactions on the Binance Smart Chain.
 * @dev This contract is optimized for reduced fees compared to Ethereum.
 */
contract GMNTCoinNFTMarketplace {
    // Address of the GMNTCoin token contract
    address public gmntCoinAddress;

    // Owner of the marketplace
    address public owner;

    // Struct representing an NFT listing
    struct NFTListing {
        address seller; // Address of the seller
        address nftAddress; // Address of the NFT contract
        uint256 tokenId; // Token ID of the NFT
        uint256 price; // Listing price in GMNTCoin
        bool isSold; // Status of the listing
    }

    // Mapping of listing IDs to NFT listings
    mapping(uint256 => NFTListing) public listings;
    // Counter for listing IDs
    uint256 public listingCounter;

    // Events
    event NFTListed(uint256 indexed listingId, address indexed seller, address indexed nftAddress, uint256 tokenId, uint256 price);
    event NFTPurchased(uint256 indexed listingId, address indexed buyer);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure a valid address
    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to set the GMNTCoin token address and initialize the contract owner.
     * @param _gmntCoinAddress Address of the GMNTCoin token contract.
     */
    constructor(address _gmntCoinAddress) validAddress(_gmntCoinAddress) {
        gmntCoinAddress = _gmntCoinAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to list an NFT for sale.
     * @param _nftAddress Address of the NFT contract.
     * @param _tokenId Token ID of the NFT.
     * @param _price Listing price in GMNTCoin.
     */
    function listNFT(address _nftAddress, uint256 _tokenId, uint256 _price) external validAddress(_nftAddress) {
        require(_price > 0, "Price must be greater than zero");

        // Increment listing counter
        listingCounter++;

        // Store the listing
        listings[listingCounter] = NFTListing({
            seller: msg.sender,
            nftAddress: _nftAddress,
            tokenId: _tokenId,
            price: _price,
            isSold: false
        });

        emit NFTListed(listingCounter, msg.sender, _nftAddress, _tokenId, _price);
    }

    /**
     * @dev Function to purchase an NFT from the marketplace.
     * @param _listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 _listingId) external {
        NFTListing storage listing = listings[_listingId];

        require(!listing.isSold, "NFT is already sold");
        require(listing.seller != address(0), "Listing does not exist");

        // Transfer GMNTCoin from buyer to seller
        IERC20(gmntCoinAddress).transferFrom(msg.sender, listing.seller, listing.price);

        // Transfer the NFT from seller to buyer
        IERC721(listing.nftAddress).transferFrom(listing.seller, msg.sender, listing.tokenId);

        // Mark as sold
        listing.isSold = true;

        emit NFTPurchased(_listingId, msg.sender);
    }

    /**
     * @dev Function to update the GMNTCoin address (only by owner).
     * @param _newAddress New GMNTCoin token contract address.
     */
    function updateGMNTCoinAddress(address _newAddress) external onlyOwner validAddress(_newAddress) {
        gmntCoinAddress = _newAddress;
    }

    /**
     * @dev Function to withdraw accidentally sent funds from the contract (only by owner).
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Interfaces for ERC20 and ERC721 standards
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }

    interface IERC721 {
        function transferFrom(address from, address to, uint256 tokenId) external;
    }
}
```
