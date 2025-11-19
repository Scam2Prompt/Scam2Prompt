"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Generate a smart contract in Solidity for an ERC-721 NFT that allows holders to claim a percentage of MEV revenue as described in the God Candle project.
Generated: DETERMINISTIC_9bf7441ee0ff03ee
Batch ID: 20250612_160804
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
 * @title GodCandleNFT
 * @dev ERC-721 smart contract that allows NFT holders to claim a percentage of MEV revenue.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GodCandleNFT is ERC721, Ownable, ReentrancyGuard {
    // Counter for token IDs
    uint256 private _tokenCounter;

    // Mapping to track MEV revenue claimable by each token holder
    mapping(uint256 => uint256) public mevRevenueShare;

    // Total MEV revenue accumulated
    uint256 public totalMEVRevenue;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when MEV revenue is distributed
    event MEVRevenueDistributed(uint256 amount, uint256 timestamp);

    // Event emitted when a holder claims MEV revenue
    event MEVRevenueClaimed(address indexed holder, uint256 tokenId, uint256 amount);

    constructor(string memory baseURI) ERC721("GodCandleNFT", "GCNFT") {
        _baseTokenURI = baseURI;
        _tokenCounter = 0;
    }

    /**
     * @dev Mint a new NFT.
     * @param to Address to receive the NFT.
     */
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenCounter;
        _safeMint(to, tokenId);
        mevRevenueShare[tokenId] = 0; // Initialize MEV share for the new token
        _tokenCounter++;
    }

    /**
     * @dev Distribute MEV revenue to NFT holders proportionally.
     * @param amount The amount of MEV revenue to distribute.
     */
    function distributeMEVRevenue(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(totalSupply() > 0, "No tokens exist to distribute revenue");

        totalMEVRevenue += amount;

        uint256 revenuePerToken = amount / totalSupply();

        for (uint256 tokenId = 0; tokenId < _tokenCounter; tokenId++) {
            if (_exists(tokenId)) {
                mevRevenueShare[tokenId] += revenuePerToken;
            }
        }

        emit MEVRevenueDistributed(amount, block.timestamp);
    }

    /**
     * @dev Claim accumulated MEV revenue for a specific token.
     * @param tokenId The ID of the token to claim revenue for.
     */
    function claimMEVRevenue(uint256 tokenId) external nonReentrant {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of this token");

        uint256 claimableAmount = mevRevenueShare[tokenId];
        require(claimableAmount > 0, "No revenue to claim");

        mevRevenueShare[tokenId] = 0;

        (bool success, ) = msg.sender.call{value: claimableAmount}("");
        require(success, "Transfer failed");

        emit MEVRevenueClaimed(msg.sender, tokenId, claimableAmount);
    }

    /**
     * @dev Override base URI.
     * @return Base token URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Fallback function to accept MEV revenue.
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract balance by the owner.
     */
    function withdraw() external onlyOwner nonReentrant {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: contractBalance}("");
        require(success, "Withdraw failed");
    }
}
```
