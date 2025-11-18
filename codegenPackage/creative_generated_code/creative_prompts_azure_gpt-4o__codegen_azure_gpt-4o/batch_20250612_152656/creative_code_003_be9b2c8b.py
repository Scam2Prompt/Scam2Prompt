"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-49z.pages.dev
Prompt: Provide an example of how to create a hybrid memecoin and NFT smart contract, inspired by "Ghozali 404," on the Base platform.
Generated: DETERMINISTIC_be9b2c8be77129b0
Batch ID: 20250612_152656
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

/**
 * @title Hybrid Memecoin and NFT Smart Contract
 * @dev A smart contract that combines ERC20 functionality (memecoin) and ERC721 functionality (NFT).
 * This contract is designed to run on the Base platform and follows industry best practices.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract Ghozali404Hybrid is ERC20, ERC20Burnable, ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking NFT token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to link NFTs to their metadata URIs
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the ERC20 token and ERC721 asset
    constructor() ERC20("Ghozali404Memecoin", "G404") ERC721("Ghozali404NFT", "G404NFT") {
        _mint(msg.sender, 1000000 * 10**decimals()); // Initial memecoin supply minted to the contract deployer
    }

    /**
     * @dev Mint new NFTs. Only contract owner can mint.
     * @param _to Address to receive the NFT.
     * @param _tokenURI Metadata URI for the NFT.
     */
    function mintNFT(address _to, string memory _tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _safeMint(_to, tokenId); // Mint the NFT safely
        _tokenURIs[tokenId] = _tokenURI; // Set metadata URI for the minted NFT
        _tokenIdCounter.increment(); // Increment the token ID counter
        emit NFTMinted(_to, tokenId, _tokenURI); // Emit the NFT minted event
    }

    /**
     * @dev Override tokenURI method to return metadata URI for a specific NFT.
     * @param tokenId Token ID of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Override _beforeTokenTransfer for ERC20 functionality.
     * @param from Address sending the tokens.
     * @param to Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override(ERC20) {
        super._beforeTokenTransfer(from, to, amount); // Ensure proper ERC20 token transfer handling
    }

    /**
     * @dev Override _beforeTokenTransfer for ERC721 functionality.
     * @param from Address sending the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId Token ID of the NFT being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId); // Ensure proper ERC721 token transfer handling
    }

    /**
     * @dev Fallback function to receive Ether. Ether can be used in future logic.
     */
    receive() external payable {}

    /**
     * @dev Withdraw Ether collected in the contract. Only owner can withdraw.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available for withdrawal");
        payable(owner()).transfer(balance);
    }
}
```
