"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Develop a Solidity contract for a decentralized NFT marketplace similar to the one in the Catgirl ecosystem, including features for buying and selling CATGIRL¢-based NFTs.
Generated: DETERMINISTIC_2fe5474c3898dfe8
Batch ID: 20250612_153606
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title CATGIRL NFT Marketplace Contract
 * @author [Your Name]
 * @notice A decentralized NFT marketplace for buying and selling CATGIRL¢-based NFTs.
 */
contract CatgirlMarketplace is Ownable {
    // Mapping of NFT owners to their respective balances
    mapping (address => uint256) public balances;

    // Mapping of NFT listings to their respective owners and prices
    mapping (uint256 => Listing) public listings;

    // Mapping of CATGIRL¢ token allowances
    mapping (address => mapping (address => uint256)) public allowances;

    // Event emitted when an NFT is listed for sale
    event ListingCreated(uint256 indexed tokenId, address indexed owner, uint256 price);

    // Event emitted when an NFT is removed from listing
    event ListingRemoved(uint256 indexed tokenId);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Event emitted when CATGIRL¢ tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Struct representing an NFT listing
    struct Listing {
        address owner;
        uint256 price;
    }

    // Address of the CATGIRL¢ token contract
    address public catgirlToken;

    /**
     * @notice Initializes the CATGIRL NFT marketplace contract.
     * @param _catgirlToken Address of the CATGIRL¢ token contract.
     */
    constructor(address _catgirlToken) public {
        catgirlToken = _catgirlToken;
    }

    /**
     * @notice Lists an NFT for sale.
     * @param _tokenId ID of the NFT to list.
     * @param _price Price of the NFT in CATGIRL¢.
     */
    function listNFT(uint256 _tokenId, uint256 _price) public {
        // Check if the NFT is owned by the sender
        require(SafeERC721(catgirlToken).ownerOf(_tokenId) == msg.sender, "You do not own this NFT.");

        // Create a new listing
        listings[_tokenId] = Listing(msg.sender, _price);

        // Emit a ListingCreated event
        emit ListingCreated(_tokenId, msg.sender, _price);
    }

    /**
     * @notice Removes an NFT from listing.
     * @param _tokenId ID of the NFT to remove.
     */
    function removeListing(uint256 _tokenId) public {
        // Check if the NFT is listed
        require(listings[_tokenId].owner != address(0), "This NFT is not listed.");

        // Check if the sender is the owner of the NFT
        require(listings[_tokenId].owner == msg.sender, "You do not own this NFT.");

        // Remove the listing
        delete listings[_tokenId];

        // Emit a ListingRemoved event
        emit ListingRemoved(_tokenId);
    }

    /**
     * @notice Purchases an NFT.
     * @param _tokenId ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 _tokenId) public {
        // Check if the NFT is listed
        require(listings[_tokenId].owner != address(0), "This NFT is not listed.");

        // Check if the sender has sufficient CATGIRL¢ balance
        require(balances[msg.sender] >= listings[_tokenId].price, "You do not have sufficient CATGIRL¢ balance.");

        // Transfer CATGIRL¢ tokens from the buyer to the seller
        balances[msg.sender] -= listings[_tokenId].price;
        balances[listings[_tokenId].owner] += listings[_tokenId].price;

        // Transfer ownership of the NFT
        SafeERC721(catgirlToken).transferFrom(listings[_tokenId].owner, msg.sender, _tokenId);

        // Remove the listing
        delete listings[_tokenId];

        // Emit an NFTPurchased event
        emit NFTPurchased(_tokenId, msg.sender, listings[_tokenId].price);
    }

    /**
     * @notice Transfers CATGIRL¢ tokens.
     * @param _to Address of the recipient.
     * @param _amount Amount of CATGIRL¢ tokens to transfer.
     */
    function transferCatgirlTokens(address _to, uint256 _amount) public {
        // Check if the sender has sufficient CATGIRL¢ balance
        require(balances[msg.sender] >= _amount, "You do not have sufficient CATGIRL¢ balance.");

        // Transfer CATGIRL¢ tokens
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        // Emit a Transfer event
        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @notice Approves an address to spend CATGIRL¢ tokens on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _amount Amount of CATGIRL¢ tokens to approve.
     */
    function approveCatgirlTokens(address _spender, uint256 _amount) public {
        allowances[msg.sender][_spender] = _amount;
    }

    /**
     * @notice Transfers CATGIRL¢ tokens on behalf of the owner.
     * @param _from Address of the owner.
     * @param _to Address of the recipient.
     * @param _amount Amount of CATGIRL¢ tokens to transfer.
     */
    function transferCatgirlTokensOnBehalf(address _from, address _to, uint256 _amount) public {
        // Check if the spender is approved
        require(allowances[_from][msg.sender] >= _amount, "You are not approved to spend these tokens.");

        // Transfer CATGIRL¢ tokens
        balances[_from] -= _amount;
        balances[_to] += _amount;

        // Emit a Transfer event
        emit Transfer(_from, _to, _amount);
    }

    /**
     * @notice Updates the CATGIRL¢ balance of an address.
     * @param _address Address of the account.
     * @param _amount New balance of the account.
     */
    function updateBalance(address _address, uint256 _amount) public onlyOwner {
        balances[_address] = _amount;
    }
}
```
