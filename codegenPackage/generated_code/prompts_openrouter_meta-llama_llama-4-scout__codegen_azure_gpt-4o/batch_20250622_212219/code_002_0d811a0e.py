"""
Generated Code Metadata:
========================
Original URL: https://unichaincrew.club
Prompt: Generate a smart contract code for an NFT project on Unichain, inspired by the Unichain Crew Club collection.
Generated: DETERMINISTIC_0d811a0ea62a1a2b
Batch ID: 20250622_212219
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

/**
 * @title UnichainCrewNFT
 * @dev A smart contract for an NFT collection inspired by the Unichain Crew Club.
 */
contract UnichainCrewNFT {
    // Importing OpenZeppelin's ERC721 implementation
    import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
    import "@openzeppelin/contracts/access/Ownable.sol";

    contract UnichainCrewNFT is ERC721Enumerable, Ownable {
        using Strings for uint256;

        // Base URI for metadata
        string private baseURI;
        // Maximum supply of NFTs
        uint256 public constant MAX_SUPPLY = 10000;
        // Price per NFT
        uint256 public constant PRICE = 0.05 ether;
        // Maximum number of NFTs per transaction
        uint256 public constant MAX_PER_TX = 5;
        // Sale status
        bool public saleIsActive = false;

        // Events
        event NFTMinted(address indexed minter, uint256 quantity);
        event BaseURISet(string newBaseURI);
        event SaleStatusChanged(bool newStatus);

        /**
         * @dev Constructor to initialize the contract with a name and symbol.
         */
        constructor(string memory _name, string memory _symbol, string memory _initBaseURI) ERC721(_name, _symbol) {
            setBaseURI(_initBaseURI);
        }

        /**
         * @dev Modifier to check if the sale is active.
         */
        modifier saleActive() {
            require(saleIsActive, "Sale is not active");
            _;
        }

        /**
         * @dev Internal function to return the base URI for metadata.
         */
        function _baseURI() internal view override returns (string memory) {
            return baseURI;
        }

        /**
         * @dev Public function to mint NFTs.
         * @param _quantity Number of NFTs to mint.
         */
        function mint(uint256 _quantity) external payable saleActive {
            require(_quantity > 0, "Quantity must be greater than zero");
            require(_quantity <= MAX_PER_TX, "Exceeds max per transaction");
            require(totalSupply() + _quantity <= MAX_SUPPLY, "Exceeds max supply");
            require(msg.value >= PRICE * _quantity, "Insufficient payment");

            for (uint256 i = 0; i < _quantity; i++) {
                uint256 tokenId = totalSupply() + 1;
                _safeMint(msg.sender, tokenId);
            }

            emit NFTMinted(msg.sender, _quantity);
        }

        /**
         * @dev Public function to set the base URI for metadata.
         * @param _newBaseURI New base URI.
         */
        function setBaseURI(string memory _newBaseURI) public onlyOwner {
            baseURI = _newBaseURI;
            emit BaseURISet(_newBaseURI);
        }

        /**
         * @dev Public function to toggle the sale status.
         */
        function toggleSaleStatus() external onlyOwner {
            saleIsActive = !saleIsActive;
            emit SaleStatusChanged(saleIsActive);
        }

        /**
         * @dev Public function to withdraw contract balance to the owner's address.
         */
        function withdraw() external onlyOwner {
            uint256 balance = address(this).balance;
            require(balance > 0, "No funds to withdraw");
            payable(owner()).transfer(balance);
        }

        /**
         * @dev Fallback function to prevent accidental ETH transfers.
         */
        receive() external payable {
            revert("Direct payments not allowed");
        }
    }
}
```
