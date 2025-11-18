"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenon-restore.pages.dev
Prompt: Create a smart contract that integrates the DeFi Protocol's "Whitelist/Presale" feature for token sales, including validation and metadata restoration.
Generated: DETERMINISTIC_a17fc24bc6f5d84a
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WhitelistPresale
 * @dev A smart contract for managing a token presale with whitelisted addresses.
 */
contract WhitelistPresale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    ERC20 public token;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Price of the token during presale (in wei)
    uint256 public tokenPrice;

    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) public whitelisted;

    // Mapping to track the amount of tokens bought by each address
    mapping(address => uint256) public tokensBought;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _token The address of the ERC20 token being sold
     * @param _presaleStart The start time of the presale
     * @param _presaleEnd The end time of the presale
     * @param _tokenPrice The price of the token during presale
     */
    constructor(
        ERC20 _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");

        token = _token;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Modifier to check if the presale is active
     */
    modifier whenPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    /**
     * @dev Function to add an address to the whitelist
     * @param _address The address to be whitelisted
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Cannot whitelist zero address");
        whitelisted[_address] = true;
    }

    /**
     * @dev Function to remove an address from the whitelist
     * @param _address The address to be removed from the whitelist
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Cannot remove zero address");
        whitelisted[_address] = false;
    }

    /**
     * @dev Function to purchase tokens during the presale
     * @param amount The number of tokens to buy
     */
    function buyTokens(uint256 amount) external payable whenPresaleActive {
        require(whitelisted[msg.sender], "Address is not whitelisted");
        require(msg.value == amount.mul(tokenPrice), "Incorrect Ether amount sent");
        require(tokensBought[msg.sender].add(amount) <= 1000, "Purchase limit exceeded"); // Limit to 1000 tokens per address

        // Update the buyer's token purchase record
        tokensBought[msg.sender] = tokensBought[msg.sender].add(amount);

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to get presale metadata
     * @return The presale details
     */
    function getPresaleDetails() external view returns (
        uint256 start,
        uint256 end,
        uint256 price,
        ERC20 saleToken
    ) {
        return (presaleStart, presaleEnd, tokenPrice, token);
    }
}
```
