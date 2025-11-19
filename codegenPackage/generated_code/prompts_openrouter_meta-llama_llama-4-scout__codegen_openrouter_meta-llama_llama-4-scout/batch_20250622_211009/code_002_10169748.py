"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Generate a smart contract code in Solidity that enables users to create, buy, and sell meme-based tokens on a blockchain platform, similar to METAL's tokenomics.
Generated: DETERMINISTIC_10169748cca43ac8
Batch ID: 20250622_211009
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title MemeToken Contract
 * @author [Your Name]
 * @notice A smart contract for creating, buying, and selling meme-based tokens.
 */
contract MemeToken {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token IDs to their respective owners
    mapping (address => mapping (uint256 => Meme)) public tokenOwners;

    // Mapping of token IDs to their respective URIs
    mapping (uint256 => string) public tokenURIs;

    // Mapping of token IDs to their respective prices
    mapping (uint256 => uint256) public tokenPrices;

    // Total supply of tokens
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Event emitted when a new token is created
    event NewToken(address indexed owner, uint256 tokenId, string uri);

    // Event emitted when a token is bought
    event TokenBought(address indexed buyer, uint256 tokenId, uint256 price);

    // Event emitted when a token is sold
    event TokenSold(address indexed seller, uint256 tokenId, uint256 price);

    /**
     * @dev Constructor function
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     */
    constructor(string memory _name, string memory _symbol) public {
        owner = msg.sender;
        totalSupply = 0;
    }

    /**
     * @dev Creates a new meme token
     * @param _uri URI of the token
     * @param _price Price of the token
     * @return uint256 ID of the newly created token
     */
    function createToken(string memory _uri, uint256 _price) public returns (uint256) {
        require(msg.sender == owner, "Only the owner can create tokens");

        uint256 tokenId = totalSupply.add(1);
        tokenOwners[msg.sender][tokenId] = Meme(msg.sender, _uri);
        tokenURIs[tokenId] = _uri;
        tokenPrices[tokenId] = _price;
        totalSupply = tokenId;

        emit NewToken(msg.sender, tokenId, _uri);

        return tokenId;
    }

    /**
     * @dev Buys a meme token
     * @param _tokenId ID of the token to buy
     */
    function buyToken(uint256 _tokenId) public payable {
        require(tokenPrices[_tokenId] > 0, "Token does not exist or is not for sale");
        require(msg.value >= tokenPrices[_tokenId], "Insufficient payment");

        address seller = tokenOwners[tokenOwners[msg.sender][_tokenId].owner][_tokenId].owner;
        tokenOwners[msg.sender][_tokenId] = Meme(msg.sender, tokenURIs[_tokenId]);
        tokenOwners[seller][_tokenId].owner = seller;

        payable(seller).transfer(tokenPrices[_tokenId]);

        emit TokenBought(msg.sender, _tokenId, tokenPrices[_tokenId]);
    }

    /**
     * @dev Sells a meme token
     * @param _tokenId ID of the token to sell
     * @param _price Price of the token
     */
    function sellToken(uint256 _tokenId, uint256 _price) public {
        require(tokenOwners[msg.sender][_tokenId].owner == msg.sender, "You do not own this token");

        tokenPrices[_tokenId] = _price;

        emit TokenSold(msg.sender, _tokenId, _price);
    }

    /**
     * @dev Structure representing a meme token
     */
    struct Meme {
        address owner;
        string uri;
    }
}
```
