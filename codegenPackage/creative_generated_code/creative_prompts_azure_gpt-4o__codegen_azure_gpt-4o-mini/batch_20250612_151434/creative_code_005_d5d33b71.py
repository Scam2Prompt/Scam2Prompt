"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-doge.web.app
Prompt: Create a smart contract snippet for handling the minting process of SolDoge tokens, ensuring compliance with the whitelist and public price conditions mentioned on the webpage.
Generated: DETERMINISTIC_d5d33b712ca3e5ce
Batch ID: 20250612_151434
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract SolDogeToken is ERC20, Ownable {
    using ECDSA for bytes32;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed recipient, uint256 amount);

    // Whitelist mapping to track eligible addresses
    mapping(address => bool) public whitelist;

    // Public sale price per token
    uint256 public publicSalePrice = 0.01 ether;
    
    // Maximum supply of tokens
    uint256 public constant MAX_SUPPLY = 1000000 * 10 ** 18;

    // Total tokens minted
    uint256 public totalMinted;

    // Modifier to check if the address is whitelisted
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Address not whitelisted");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("SolDoge", "SDOGE") {
        _mint(msg.sender, 10000 * 10 ** 18); // Mint initial supply to owner
    }

    // Function to mint tokens for whitelisted addresses
    function mintTokens(uint256 amount) external payable onlyWhitelisted {
        // Check if the amount requested does not exceed the maximum supply
        require(totalMinted + amount <= MAX_SUPPLY, "Max supply exceeded");

        // Check if the correct amount of Ether was sent
        require(msg.value == amount * publicSalePrice, "Incorrect Ether amount");

        // Mint the tokens to the sender
        _mint(msg.sender, amount * 10 ** 18);
        totalMinted += amount;

        // Emit the minting event
        emit TokensMinted(msg.sender, amount);
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
    }

    // Function to remove an address from the whitelist
    function removeFromWhitelist(address account) external onlyOwner {
        whitelist[account] = false;
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
