"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.pages.dev
Prompt: Write Solidity code for an ERC-20 token contract that integrates with ERC-404 functionality, as outlined on the God Candle webpage.
Generated: DETERMINISTIC_51f4107f6dd2bc0a
Batch ID: 20250612_152827
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/IERC721.sol": {
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

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/IERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol";

/**
 * @title ERC404 Token Contract
 * @author [Your Name]
 * @notice This contract implements an ERC-20 token that integrates with ERC-404 functionality.
 */
contract ERC404Token is ERC20 {
    using SafeMath for uint256;

    // Mapping of user balances and ownership
    mapping(address => uint256) public balances;
    mapping(address => mapping(uint256 => uint256)) public ownership;

    // Mapping of token IDs to owner addresses
    mapping(uint256 => address) public tokenOwners;

    // Total supply of tokens
    uint256 public totalSupply;

    // Total supply of tokens that are owned
    uint256 public ownedSupply;

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when a token is minted
    event Mint(address indexed to, uint256 value);

    // Event emitted when a token is burned
    event Burn(address indexed from, uint256 value);

    /**
     * @notice Constructor function
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @notice Mints tokens to an address
     * @param to Address to mint tokens to
     * @param value Amount of tokens to mint
     */
    function mint(address to, uint256 value) public {
        // Increase the total supply
        totalSupply = totalSupply.add(value);

        // Update the balances and ownership
        balances[to] = balances[to].add(value);
        ownership[to][0] = ownership[to][0].add(value);

        // Emit the mint event
        emit Mint(to, value);
        emit Transfer(address(0), to, value);
    }

    /**
     * @notice Burns tokens from an address
     * @param from Address to burn tokens from
     * @param value Amount of tokens to burn
     */
    function burn(address from, uint256 value) public {
        // Decrease the total supply
        totalSupply = totalSupply.sub(value);

        // Update the balances and ownership
        balances[from] = balances[from].sub(value);
        ownership[from][0] = ownership[from][0].sub(value);

        // Emit the burn event
        emit Burn(from, value);
        emit Transfer(from, address(0), value);
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param value Amount of tokens to transfer
     */
    function transfer(address from, address to, uint256 value) public {
        // Check if the from address has sufficient balance
        require(balances[from] >= value, "Insufficient balance");

        // Update the balances and ownership
        balances[from] = balances[from].sub(value);
        balances[to] = balances[to].add(value);

        // Emit the transfer event
        emit Transfer(from, to, value);
    }

    /**
     * @notice Transfers ERC-721 tokens
     * @param tokenId ID of the token to transfer
     * @param to Address to transfer the token to
     */
    function transferERC721(uint256 tokenId, address to) public {
        // Check if the token exists and is owned by the sender
        require(tokenOwners[tokenId] == msg.sender, "Token not owned by sender");

        // Update the token owner
        tokenOwners[tokenId] = to;

        // Emit the transfer event
        emit Transfer(msg.sender, to, 0);
    }

    /**
     * @notice Gets the balance of an address
     * @param owner Address to get the balance of
     * @return Balance of the address
     */
    function balanceOf(address owner) public view returns (uint256) {
        return balances[owner];
    }

    /**
     * @notice Gets the owner of a token
     * @param tokenId ID of the token
     * @return Owner of the token
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        return tokenOwners[tokenId];
    }
}
```
