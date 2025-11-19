"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: Generate a code snippet for a smart contract that can mint NFTs similar to the 10K immutable NFTs described on the ABC - Abracadabra website.
Generated: DETERMINISTIC_dc956ae1dabd1547
Batch ID: 20250612_163945
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
 * @title NFTMintingContract
 * @dev A smart contract for minting immutable NFTs similar to the 10K NFT collection model.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for NFT metadata
    string private baseURI;

    // Minting price for an NFT
    uint256 public mintPrice = 0.05 ether;

    // Track whether minting has started
    bool public mintingActive = false;

    constructor(string memory _name, string memory _symbol, string memory _baseURI) ERC721(_name, _symbol) {
        baseURI = _baseURI;
    }

    /**
     * @dev Modifier to check if minting is active.
     */
    modifier isMintingActive() {
        require(mintingActive, "Minting is not active");
        _;
    }

    /**
     * @dev Function to toggle minting active state.
     * Only callable by the contract owner.
     */
    function toggleMinting() external onlyOwner {
        mintingActive = !mintingActive;
    }

    /**
     * @dev Set the mint price for an NFT.
     * Only callable by the contract owner.
     * @param _mintPrice The new mint price in wei.
     */
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    /**
     * @dev Mint an NFT to the sender's address.
     * @param _amount Number of NFTs to mint.
     */
    function mintNFT(uint256 _amount) external payable isMintingActive {
        require(_amount > 0, "Must mint at least 1 NFT");
        require(totalSupply() + _amount <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value >= mintPrice * _amount, "Insufficient funds");

        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalSupply() + 1; // Start token IDs at 1
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Withdraw the contract balance to the owner.
     * Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Override base URI for computing {tokenURI}.
     * @return Base URI of the contract.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Set the base URI for NFT metadata.
     * Only callable by the contract owner.
     * @param _baseURI The new base URI.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }
}
```
