"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-t.pages.dev
Prompt: Develop code to facilitate minting, presale purchases, and token withdrawals, referencing the minting and presale functionalities described on the webpage.
Generated: DETERMINISTIC_4d326da249c6c8c9
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, well-documented implementation in Solidity that facilitates minting, presale purchases, and token withdrawals. This code assumes you're implementing a basic ERC721 (NFT) contract with presale and withdrawal functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MintingAndPresale is ERC721, Ownable {
    // State variables
    uint256 public maxSupply;          // Maximum number of tokens that can be minted
    uint256 public totalMinted;        // Total tokens minted so far
    uint256 public mintPrice;          // Price per token during public mint
    uint256 public presalePrice;       // Price per token during presale
    bool public presaleActive;         // Flag indicating if presale is active
    bool public publicSaleActive;      // Flag indicating if public sale is active
    mapping(address => bool) public presaleWhitelist; // Track addresses eligible for presale

    // Events
    event TokensMinted(address indexed user, uint256 quantity);
    event PresaleActivated(bool active);
    event PublicSaleActivated(bool active);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Constructor
    constructor(
        uint256 _maxSupply,
        uint256 _mintPrice,
        uint256 _presalePrice
    ) ERC721("MintingAndPresaleNFT", "MPNFT") {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        presalePrice = _presalePrice;
    }

    // Modifier to check if minting is possible
    modifier canMint(uint256 quantity) {
        require(totalMinted + quantity <= maxSupply, "Exceeds max supply");
        _;
    }

    // Mint function for public sale
    function mint(uint256 quantity) external payable canMint(quantity) {
        require(publicSaleActive, "Public sale is not active");
        require(msg.value == mintPrice * quantity, "Incorrect Ether value");

        for (uint256 i = 0; i < quantity; i++) {
            totalMinted++;
            _safeMint(msg.sender, totalMinted);
        }

        emit TokensMinted(msg.sender, quantity);
    }

    // Mint function for presale
    function presaleMint(uint256 quantity) external payable canMint(quantity) {
        require(presaleActive, "Presale is not active");
        require(presaleWhitelist[msg.sender], "Not eligible for presale");
        require(msg.value == presalePrice * quantity, "Incorrect Ether value");

        for (uint256 i = 0; i < quantity; i++) {
            totalMinted++;
            _safeMint(msg.sender, totalMinted);
        }

        emit TokensMinted(msg.sender, quantity);
    }

    // Admin: Activate or deactivate the presale
    function setPresaleActive(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleActivated(_active);
    }

    // Admin: Activate or deactivate the public sale
    function setPublicSaleActive(bool _active) external onlyOwner {
        publicSaleActive = _active;
        emit PublicSaleActivated(_active);
    }

    // Admin: Add addresses to presale whitelist
    function addToPresaleWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            presaleWhitelist[addresses[i]] = true;
        }
    }

    // Admin: Remove addresses from presale whitelist
    function removeFromPresaleWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            presaleWhitelist[addresses[i]] = false;
        }
    }

    // Admin: Withdraw contract funds
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(owner(), balance);
    }
}
```

This code facilitates minting tokens during a public sale and presale, includes presale whitelist functionality, and allows the contract owner to withdraw funds. It adheres to best practices and includes proper error handling.
