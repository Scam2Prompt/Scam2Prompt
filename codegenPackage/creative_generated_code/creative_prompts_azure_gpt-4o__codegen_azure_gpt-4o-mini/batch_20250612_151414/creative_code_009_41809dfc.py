"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Write a Solidity contract for managing fractional ownership of NFTs, inspired by the acquisition model of "NiftyKit" by カイカイキキ.
Generated: DETERMINISTIC_41809dfc2e67a2e2
Batch ID: 20250612_151414
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FractionalNFT
 * @dev A contract for managing fractional ownership of NFTs. 
 * Each NFT can be owned by multiple stakeholders, represented through ERC20 tokens.
 */
contract FractionalNFT is Ownable {
    using SafeMath for uint256;

    // Struct representing an NFT and its total shares
    struct NFT {
        address nftContract;       // Address of the NFT contract
        uint256 tokenId;           // ID of the specific NFT
        uint256 totalShares;       // Total shares available for the NFT
        mapping(address => uint256) shares; // Mapping of owner addresses to their shares
    }

    // Mapping of NFT IDs to their details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when a new fractional NFT is created
    event NFTCreated(address indexed nftContract, uint256 indexed tokenId, uint256 totalShares);

    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed tokenId, address indexed buyer, uint256 sharesPurchased);

    // Event emitted when shares are redeemed
    event SharesRedeemed(uint256 indexed tokenId, address indexed owner, uint256 sharesRedeemed);

    /**
     * @dev Creates a new fractional NFT entry
     * @param _nftContract Address of the NFT contract
     * @param _tokenId ID of the NFT
     * @param _totalShares Total number of shares to be created
     */
    function createFractionalNFT(address _nftContract, uint256 _tokenId, uint256 _totalShares) external onlyOwner {
        require(_totalShares > 0, "Total shares must be greater than zero");
        require(nfts[_tokenId].totalShares == 0, "NFT already fractionalized");

        // Initialize NFT struct
        NFT storage newNFT = nfts[_tokenId];
        newNFT.nftContract = _nftContract;
        newNFT.tokenId = _tokenId;
        newNFT.totalShares = _totalShares;

        emit NFTCreated(_nftContract, _tokenId, _totalShares);
    }

    /**
     * @dev Allows users to purchase shares of a fractionalized NFT
     * @param _tokenId ID of the NFT to purchase shares in
     * @param _shares Number of shares to purchase
     */
    function purchaseShares(uint256 _tokenId, uint256 _shares) external {
        NFT storage nft = nfts[_tokenId];
        require(nft.totalShares > 0, "NFT not fractionalized");
        require(_shares > 0, "Shares must be greater than zero");
        require(nft.shares[msg.sender].add(_shares) <= nft.totalShares, "Exceeds total shares");

        // Update shares for the buyer
        nft.shares[msg.sender] = nft.shares[msg.sender].add(_shares);

        emit SharesPurchased(_tokenId, msg.sender, _shares);
    }

    /**
     * @dev Allows users to redeem their shares
     * @param _tokenId ID of the NFT to redeem shares from
     * @param _shares Number of shares to redeem
     */
    function redeemShares(uint256 _tokenId, uint256 _shares) external {
        NFT storage nft = nfts[_tokenId];
        require(nft.shares[msg.sender] >= _shares, "Insufficient shares to redeem");

        // Update shares for the owner
        nft.shares[msg.sender] = nft.shares[msg.sender].sub(_shares);

        emit SharesRedeemed(_tokenId, msg.sender, _shares);
    }

    /**
     * @dev Returns the number of shares an address holds for a specific NFT
     * @param _tokenId ID of the NFT
     * @param _owner Address of the owner
     * @return Number of shares owned
     */
    function getShares(uint256 _tokenId, address _owner) external view returns (uint256) {
        return nfts[_tokenId].shares[_owner];
    }
}
```
