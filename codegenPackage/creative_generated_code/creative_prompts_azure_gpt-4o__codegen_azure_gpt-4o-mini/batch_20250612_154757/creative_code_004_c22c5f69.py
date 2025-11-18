"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap.shop
Prompt: Develop a peer-to-peer NFT swapping program using smart contracts, ensuring asset safety and encryption as highlighted by Grailswap.
Generated: DETERMINISTIC_c22c5f69698d6ff5
Batch ID: 20250612_154757
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
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Peer-to-Peer NFT Swapping Contract
/// @notice This contract allows users to swap ERC721 tokens securely
contract NFTSwap is Ownable, ERC721Holder {
    using Counters for Counters.Counter;
    Counters.Counter private _swapIdCounter;

    struct Swap {
        uint256 id;
        address nftAddress;
        uint256 nftId;
        address offerer;
        address taker;
        bool completed;
    }

    mapping(uint256 => Swap) public swaps;

    event SwapCreated(uint256 swapId, address indexed nftAddress, uint256 indexed nftId, address indexed offerer);
    event SwapCompleted(uint256 swapId, address indexed taker);
    event SwapCancelled(uint256 swapId);

    /// @dev Create a new NFT swap
    /// @param nftAddress The address of the NFT contract
    /// @param nftId The ID of the NFT to swap
    function createSwap(address nftAddress, uint256 nftId) external {
        require(IERC721(nftAddress).ownerOf(nftId) == msg.sender, "Not the NFT owner");
        
        // Transfer the NFT to the contract to ensure safety
        IERC721(nftAddress).safeTransferFrom(msg.sender, address(this), nftId);
        
        _swapIdCounter.increment();
        uint256 swapId = _swapIdCounter.current();

        swaps[swapId] = Swap({
            id: swapId,
            nftAddress: nftAddress,
            nftId: nftId,
            offerer: msg.sender,
            taker: address(0),
            completed: false
        });

        emit SwapCreated(swapId, nftAddress, nftId, msg.sender);
    }

    /// @dev Accept an NFT swap
    /// @param swapId The ID of the swap to accept
    function acceptSwap(uint256 swapId) external {
        Swap storage swap = swaps[swapId];
        require(swap.id == swapId, "Swap does not exist");
        require(swap.completed == false, "Swap already completed");
        require(swap.taker == address(0), "Swap already taken");

        // Transfer the NFT to the taker
        swap.taker = msg.sender;

        // Transfer the NFT from the contract to the taker
        IERC721(swap.nftAddress).safeTransferFrom(address(this), msg.sender, swap.nftId);
        
        swap.completed = true;
        emit SwapCompleted(swapId, msg.sender);
    }

    /// @dev Cancel an NFT swap
    /// @param swapId The ID of the swap to cancel
    function cancelSwap(uint256 swapId) external {
        Swap storage swap = swaps[swapId];
        require(swap.id == swapId, "Swap does not exist");
        require(swap.offerer == msg.sender, "Only the offerer can cancel");

        // Transfer the NFT back to the offerer
        require(swap.completed == false, "Cannot cancel completed swap");
        IERC721(swap.nftAddress).safeTransferFrom(address(this), msg.sender, swap.nftId);
        
        delete swaps[swapId];
        emit SwapCancelled(swapId);
    }

    /// @dev Fallback function to receive NFTs
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
