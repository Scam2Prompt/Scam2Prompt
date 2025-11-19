"""
Generated Code Metadata:
========================
Original URL: https://tenon-restore.pages.dev
Prompt: Create a smart contract that integrates the DeFi Protocol's "Whitelist/Presale" feature for token sales, including validation and metadata restoration.
Generated: DETERMINISTIC_a17fc24bc6f5d84a
Batch ID: 20250612_153526
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a token sale with whitelist and presale features
contract WhitelistPresale is ERC20, Ownable {
    // State variables
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price per token in wei
    mapping(address => bool) public whitelistedAddresses; // Whitelist mapping
    mapping(address => uint256) public contributions; // Track contributions of whitelisted addresses
    uint256 public totalContributions; // Total contributions during presale
    bool public presaleActive; // Flag to check if presale is active

    // Events
    event Whitelisted(address indexed account);
    event Unwhitelisted(address indexed account);
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token and presale parameters
    constructor(string memory name, string memory symbol, uint256 _tokenPrice) ERC20(name, symbol) {
        tokenPrice = _tokenPrice;
    }

    // Modifier to check if presale is active
    modifier onlyDuringPresale() {
        require(presaleActive, "Presale is not active");
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not within the valid time frame");
        _;
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + duration;
        presaleActive = true;
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    // Function to whitelist an address
    function whitelistAddress(address account) external onlyOwner {
        require(!whitelistedAddresses[account], "Address is already whitelisted");
        whitelistedAddresses[account] = true;
        emit Whitelisted(account);
    }

    // Function to remove an address from the whitelist
    function unwhitelistAddress(address account) external onlyOwner {
        require(whitelistedAddresses[account], "Address is not whitelisted");
        whitelistedAddresses[account] = false;
        emit Unwhitelisted(account);
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 tokenAmount) external payable onlyDuringPresale {
        require(whitelistedAddresses[msg.sender], "You are not whitelisted");
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether value sent");

        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        // Mint tokens to the buyer
        _mint(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to restore metadata (if needed)
    function restoreMetadata(string memory name, string memory symbol) external onlyOwner {
        // This function can be used to update the token's name and symbol if required
        _name = name;
        _symbol = symbol;
    }
}
```
