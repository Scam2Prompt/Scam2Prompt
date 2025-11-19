"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-lnds-64z.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a presale of NFTs, similar to the $Leonidas presale cap of 1000 ETH.
Generated: DETERMINISTIC_e2aa4b6f2019a027
Batch ID: 20250612_162051
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

// Import the OpenZeppelin ERC721 contract for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Presale contract for NFTs
contract NFTPresale is ERC721Enumerable, Ownable {
    using Address for address;

    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    uint256 public constant PRESALE_CAP = 1000 ether; // Presale cap
    uint256 public totalPresaleRaised; // Total amount raised during presale
    bool public presaleActive = false; // Presale status

    // Mapping to track minted NFTs
    mapping(address => uint256) public presaleBalances;

    // Event for NFT minting
    event NFTMinted(address indexed buyer, uint256 tokenId);

    // Constructor to initialize the NFT collection
    constructor() ERC721("NFTPresale", "NFTP") {}

    // Function to start the presale
    function startPresale() external onlyOwner {
        presaleActive = true;
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    // Function to mint NFTs during the presale
    function mintNFT(uint256 quantity) external payable {
        require(presaleActive, "Presale is not active");
        require(quantity > 0, "Must mint at least one NFT");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value == quantity * 0.1 ether, "Incorrect value sent"); // 0.1 ETH per NFT
        require(totalPresaleRaised + msg.value <= PRESALE_CAP, "Presale cap reached");

        totalPresaleRaised += msg.value;
        presaleBalances[msg.sender] += quantity;

        // Mint NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1;
            _mint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        require(totalPresaleRaised > 0, "No funds to withdraw");
        uint256 amount = totalPresaleRaised;
        totalPresaleRaised = 0;

        // Transfer the amount to the owner
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to get the current presale balance of an address
    function getPresaleBalance(address account) external view returns (uint256) {
        return presaleBalances[account];
    }

    // Fallback function to accept Ether
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
