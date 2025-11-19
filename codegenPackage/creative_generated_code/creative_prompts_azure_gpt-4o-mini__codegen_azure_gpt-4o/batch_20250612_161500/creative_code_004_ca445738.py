"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhozali.pages.dev
Prompt: Provide an example of a smart contract for a memecoin that incorporates NFT features, inspired by the Ghozali 404 project.
Generated: DETERMINISTIC_ca445738edf97757
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title MemecoinWithNFT
 * @dev A smart contract for a memecoin that incorporates NFT features.
 * Inspired by the Ghozali 404 project.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemecoinWithNFT is ERC20, ERC20Burnable, ERC721, ERC721Enumerable, Ownable {
    // Maximum supply of the memecoin
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18;

    // Mint price for an NFT
    uint256 public constant NFT_MINT_PRICE = 0.01 ether;

    // Token ID counter for NFTs
    uint256 private _tokenIdCounter;

    // Mapping to track NFT ownership
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Memecoin constructor initializes ERC20 and ERC721 tokens
     * and mints the initial memecoin supply to the contract owner.
     */
    constructor() ERC20("MemecoinWithNFT", "MEME") ERC721("MemecoinNFT", "MNFT") {
        // Mint the maximum supply of memecoin to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Allows users to mint an NFT by paying the specified mint price.
     * The NFT ID is auto-incremented and the URI is provided by the minter.
     * @param _uri A string representing the metadata URI for the minted NFT.
     */
    function mintNFT(string memory _uri) external payable {
        require(msg.value == NFT_MINT_PRICE, "Incorrect Ether value sent");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter++;
        _safeMint(msg.sender, tokenId);

        // Store the URI for the NFT
        _tokenURIs[tokenId] = _uri;
    }

    /**
     * @dev Returns the URI associated with a specific NFT token ID.
     * @param tokenId The ID of the NFT whose URI is being queried.
     * @return The metadata URI for the queried NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Allows the contract owner to withdraw Ether from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer the balance to the contract owner
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Override functions required by Solidity due to multiple inheritance
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20)
    {
        super._beforeTokenTransfer(from, to, amount);
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _afterTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20)
    {
        // Additional logic for ERC20 token transfers can be added here if needed
        super._afterTokenTransfer(from, to, amount);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    // Fallback function to accept Ether for NFT minting
    receive() external payable {}
}
```
