"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rolexnft.pages.dev
Prompt: Provide an example of a smart contract in Solidity that implements the minting of NFTs with bonus airdrops for specific quantities, as outlined on the Rolex NFT site.
Generated: DETERMINISTIC_3c9ff544d7d8b3d0
Batch ID: 20250612_151659
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
 * @title RolexNFT
 * @dev A smart contract implementing an ERC721 NFT with minting functionality
 *      and bonus airdrops for specific quantities.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RolexNFT is ERC721Enumerable, Ownable {
    // Token ID counter
    uint256 private _tokenIdCounter;

    // Mapping for bonus thresholds and airdrop amounts
    mapping(uint256 => uint256) public bonusThresholds;

    // Event for bonus airdrops
    event BonusAirdrop(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor initializes the token with a name and symbol.
     */
    constructor() ERC721("RolexNFT", "RLX") {
        // Set default bonus thresholds (can be updated by owner)
        bonusThresholds[10] = 2; // Mint 10, get 2 bonus NFTs
        bonusThresholds[20] = 5; // Mint 20, get 5 bonus NFTs
    }

    /**
     * @dev Public function to mint NFTs. Bonus airdrops are applied based
     *      on the amount minted if thresholds are met.
     * @param quantity The number of NFTs to mint.
     */
    function mintNFT(uint256 quantity) external {
        require(quantity > 0, "Minting quantity must be greater than zero");

        // Mint the requested quantity of NFTs
        for (uint256 i = 0; i < quantity; i++) {
            _mintNFT(msg.sender);
        }

        // Check for bonus threshold and apply airdrops
        if (bonusThresholds[quantity] > 0) {
            uint256 bonusAmount = bonusThresholds[quantity];
            for (uint256 i = 0; i < bonusAmount; i++) {
                _mintNFT(msg.sender);
            }

            // Emit event for the bonus airdrop
            emit BonusAirdrop(msg.sender, bonusAmount);
        }
    }

    /**
     * @dev Internal function to mint a single NFT.
     * @param recipient The address to receive the NFT.
     */
    function _mintNFT(address recipient) internal {
        _tokenIdCounter++;
        _safeMint(recipient, _tokenIdCounter);
    }

    /**
     * @dev Owner-only function to update bonus thresholds.
     * @param threshold The minimum quantity to trigger bonuses.
     * @param bonusAmount The number of bonus NFTs for the threshold.
     */
    function setBonusThreshold(uint256 threshold, uint256 bonusAmount) external onlyOwner {
        require(threshold > 0, "Threshold must be greater than zero");
        bonusThresholds[threshold] = bonusAmount;
    }

    /**
     * @dev Owner-only function to set base URI for metadata.
     * @param baseURI The base URI for the NFT metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _setBaseURI(baseURI);
    }

    /**
     * @dev Override the _baseURI function from ERC721 to allow dynamic base URI.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return super._baseURI();
    }
}
```
