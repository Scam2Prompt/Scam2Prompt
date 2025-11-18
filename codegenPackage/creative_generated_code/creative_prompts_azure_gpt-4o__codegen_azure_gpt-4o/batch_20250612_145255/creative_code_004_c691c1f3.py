"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-nakamigos.vercel.app
Prompt: Create a smart contract in Solidity that limits NFT minting to a maximum of 1 set per wallet, as described on the Mint Nakamigos site.
Generated: DETERMINISTIC_c691c1f3b227e416
Batch ID: 20250612_145255
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
 * @title LimitedMintNFT
 * @dev A smart contract that limits NFT minting to a maximum of 1 set per wallet.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedMintNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs a single wallet can mint (1 set per wallet).
    uint256 public constant MAX_PER_WALLET = 1;

    // Token ID to track minting
    uint256 private _currentTokenId;

    // Mapping to track minting status per wallet
    mapping(address => bool) private _hasMinted;

    /**
     * @dev Constructor to initialize the contract and token details.
     * @param name The name of the NFT collection.
     * @param symbol The symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Public mint function to allow users to mint NFTs.
     * Each wallet is restricted to minting only 1 set (MAX_PER_WALLET).
     */
    function mint() external {
        require(!_hasMinted[msg.sender], "Minting limited to 1 set per wallet.");
        
        // Mark the wallet as having minted
        _hasMinted[msg.sender] = true;

        // Increment token ID and safely mint the NFT
        _currentTokenId++;
        _safeMint(msg.sender, _currentTokenId);
    }

    /**
     * @dev Owner-only function to withdraw contract balance.
     * Ensures funds from minting can only be accessed by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct payments not allowed.");
    }
}
```
