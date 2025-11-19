"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Generate a smart contract in Solidity for an ERC-721 NFT that allows holders to claim a percentage of MEV revenue as described in the God Candle project.
Generated: DETERMINISTIC_9bf7441ee0ff03ee
Batch ID: 20250612_160804
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GodCandleNFT is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store MEV claim information
    struct MEVClaim {
        uint256 totalClaimed;
        uint256 lastClaimTimestamp;
    }

    // Mapping from token ID to MEV claim data
    mapping(uint256 => MEVClaim) private _mevClaims;

    // Total MEV revenue collected
    uint256 private _totalMEVRevenue;
    
    // MEV revenue per token
    uint256 private _mevPerToken;
    
    // Total tokens minted
    uint256 private _totalSupply;
    
    // Base URI for token metadata
    string private _baseTokenURI;

    // Events
    event MEVDeposited(address indexed depositor, uint256 amount);
    event MEVClaimed(address indexed claimer, uint256 tokenId, uint256 amount);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mints a new NFT to the specified address
     * @param to The address that will receive the NFT
     */
    function mint(address to) external onlyOwner {
        _totalSupply += 1;
        _safeMint(to, _totalSupply);
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Deposits MEV revenue to be distributed to NFT holders
     */
    function depositMEV() external payable nonReentrant {
        require(msg.value > 0, "No ETH sent");
        _totalMEVRevenue = _totalMEVRevenue.add(msg.value);
        _mevPerToken = _totalMEVRevenue.div(_totalSupply);
        
        emit MEVDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Claims available MEV revenue for a specific token
     * @param tokenId The token ID to claim MEV for
     */
    function claimMEV(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(_totalMEVRevenue > 0, "No MEV to claim");

        MEVClaim storage claim = _mevClaims[tokenId];
        uint256 claimableAmount = _mevPerToken.sub(claim.totalClaimed);
        
        require(claimableAmount > 0, "No MEV available to claim");

        claim.totalClaimed = claim.totalClaimed.add(claimableAmount);
        claim.lastClaimTimestamp = block.timestamp;

        (bool success, ) = msg.sender.call{value: claimableAmount}("");
        require(success, "Transfer failed");

        emit MEVClaimed(msg.sender, tokenId, claimableAmount);
    }

    /**
     * @dev Returns the claimable MEV amount for a token
     * @param tokenId The token ID to check
     * @return The claimable amount in wei
     */
    function getClaimableMEV(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        MEVClaim memory claim = _mevClaims[tokenId];
        return _mevPerToken.sub(claim.totalClaimed);
    }

    /**
     * @dev Returns the total MEV revenue collected
     * @return The total MEV revenue in wei
     */
    function getTotalMEVRevenue() external view returns (uint256) {
        return _totalMEVRevenue;
    }

    /**
     * @dev Returns the total supply of NFTs
     * @return The total number of NFTs minted
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
