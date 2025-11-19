"""
Generated Code Metadata:
========================
Original URL: https://tonsquare-dapp.vercel.app
Prompt: Develop a smart contract using Solidity to interact with TONSquare's NFT Bag feature, enabling users to store and manage their NFTs.
Generated: DETERMINISTIC_39475fd2906033c0
Batch ID: 20250622_212643
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TONSquare NFT Bag
 * @dev Smart contract for storing and managing NFTs
 */
contract TONSquareNFTBag is ERC721Holder, Ownable, ReentrancyGuard {
    // Mapping from NFT contract address to token ID to owner address
    mapping(address => mapping(uint256 => address)) private _nftOwners;

    // Mapping from owner to their deposited NFTs
    mapping(address => mapping(address => uint256[])) private _ownerNFTs;

    // Events
    event NFTDeposited(address indexed owner, address indexed nftContract, uint256 tokenId);
    event NFTWithdrawn(address indexed owner, address indexed nftContract, uint256 tokenId);

    /**
     * @dev Deposit an NFT into the bag
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT to deposit
     */
    function depositNFT(address nftContract, uint256 tokenId) external nonReentrant {
        require(nftContract != address(0), "Invalid NFT contract address");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Not the NFT owner");

        // Transfer NFT to this contract
        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);

        // Update storage
        _nftOwners[nftContract][tokenId] = msg.sender;
        _ownerNFTs[msg.sender][nftContract].push(tokenId);

        emit NFTDeposited(msg.sender, nftContract, tokenId);
    }

    /**
     * @dev Withdraw an NFT from the bag
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT to withdraw
     */
    function withdrawNFT(address nftContract, uint256 tokenId) external nonReentrant {
        require(nftContract != address(0), "Invalid NFT contract address");
        require(_nftOwners[nftContract][tokenId] == msg.sender, "Not the NFT owner");

        // Transfer NFT back to owner
        IERC721(nftContract).safeTransferFrom(address(this), msg.sender, tokenId);

        // Update storage
        delete _nftOwners[nftContract][tokenId];
        _removeNFTFromOwner(msg.sender, nftContract, tokenId);

        emit NFTWithdrawn(msg.sender, nftContract, tokenId);
    }

    /**
     * @dev Get list of NFTs deposited by an owner for a specific contract
     * @param owner Address of the owner
     * @param nftContract Address of the NFT contract
     * @return Array of token IDs
     */
    function getOwnerNFTs(address owner, address nftContract) external view returns (uint256[] memory) {
        return _ownerNFTs[owner][nftContract];
    }

    /**
     * @dev Check if an NFT is deposited in the bag
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT
     * @return True if deposited, false otherwise
     */
    function isNFTDeposited(address nftContract, uint256 tokenId) external view returns (bool) {
        return _nftOwners[nftContract][tokenId] != address(0);
    }

    /**
     * @dev Internal function to remove an NFT from owner's list
     * @param owner Address of the owner
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT to remove
     */
    function _removeNFTFromOwner(address owner, address nftContract, uint256 tokenId) private {
        uint256[] storage nfts = _ownerNFTs[owner][nftContract];
        for (uint256 i = 0; i < nfts.length; i++) {
            if (nfts[i] == tokenId) {
                nfts[i] = nfts[nfts.length - 1];
                nfts.pop();
                break;
            }
        }
    }

    /**
     * @dev Emergency function to recover accidentally sent ERC721 tokens
     * @param tokenAddress Address of the token contract
     * @param tokenId ID of the token to recover
     */
    function recoverERC721(address tokenAddress, uint256 tokenId) external onlyOwner {
        require(_nftOwners[tokenAddress][tokenId] == address(0), "Token is deposited by a user");
        IERC721(tokenAddress).safeTransferFrom(address(this), owner(), tokenId);
    }
}
```
