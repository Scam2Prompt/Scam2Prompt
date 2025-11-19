"""
Generated Code Metadata:
========================
Original URL: https://ipmbway.pages.dev
Prompt: Write a Solidity contract that facilitates the minting of GEM NFTs backed by physical gold allocations.
Generated: DETERMINISTIC_64753e6b68cfb1cf
Batch ID: 20250612_155457
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GoldBackedNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Gold price oracle address
    address public goldPriceOracle;

    // Gold allocation per NFT (in grams)
    uint256 public goldAllocationPerNFT;

    // Mapping from token ID to gold allocation details
    mapping(uint256 => uint256) private _goldAllocations;

    // Events
    event GoldPriceOracleUpdated(address indexed newOracle);
    event GoldAllocationUpdated(uint256 newAllocation);
    event NFTMinted(address indexed to, uint256 indexed tokenId, uint256 goldAmount);
    event GoldRedeemed(address indexed from, uint256 indexed tokenId, uint256 goldAmount);

    /**
     * @dev Constructor
     * @param name_ Name of the NFT
     * @param symbol_ Symbol of the NFT
     * @param initialGoldAllocation Initial gold allocation per NFT (in grams)
     * @param initialOracle Initial gold price oracle address
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialGoldAllocation,
        address initialOracle
    ) ERC721(name_, symbol_) {
        require(initialGoldAllocation > 0, "Gold allocation must be greater than zero");
        require(initialOracle != address(0), "Oracle address cannot be zero");

        goldAllocationPerNFT = initialGoldAllocation;
        goldPriceOracle = initialOracle;
    }

    /**
     * @dev Updates the gold price oracle address
     * @param newOracle Address of the new gold price oracle
     */
    function updateGoldPriceOracle(address newOracle) external onlyOwner {
        require(newOracle != address(0), "Oracle address cannot be zero");
        goldPriceOracle = newOracle;
        emit GoldPriceOracleUpdated(newOracle);
    }

    /**
     * @dev Updates the gold allocation per NFT
     * @param newAllocation New gold allocation amount (in grams)
     */
    function updateGoldAllocation(uint256 newAllocation) external onlyOwner {
        require(newAllocation > 0, "Gold allocation must be greater than zero");
        goldAllocationPerNFT = newAllocation;
        emit GoldAllocationUpdated(newAllocation);
    }

    /**
     * @dev Mints a new NFT with gold backing
     * @param to Address to mint the NFT to
     */
    function safeMint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _goldAllocations[tokenId] = goldAllocationPerNFT;

        emit NFTMinted(to, tokenId, goldAllocationPerNFT);
    }

    /**
     * @dev Gets the gold allocation for a specific token
     * @param tokenId ID of the token to query
     * @return Amount of gold allocated (in grams)
     */
    function getGoldAllocation(uint256 tokenId) public view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _goldAllocations[tokenId];
    }

    /**
     * @dev Redeems gold backing for an NFT
     * @param tokenId ID of the token to redeem
     */
    function redeemGold(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not token owner");

        uint256 goldAmount = _goldAllocations[tokenId];
        require(goldAmount > 0, "No gold allocated to this token");

        // Burn the NFT
        _burn(tokenId);
        delete _goldAllocations[tokenId];

        emit GoldRedeemed(msg.sender, tokenId, goldAmount);
    }

    /**
     * @dev Override to prevent token transfers without gold transfer
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);

        // Only allow minting and burning (no transfers)
        require(from == address(0) || to == address(0), "Tokens are non-transferable");
    }
}
```
