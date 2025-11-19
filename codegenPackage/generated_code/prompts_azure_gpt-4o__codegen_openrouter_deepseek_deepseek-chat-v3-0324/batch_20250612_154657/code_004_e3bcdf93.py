"""
Generated Code Metadata:
========================
Original URL: https://on1force.web.app
Prompt: Create a smart contract that enforces the rules for transferring 0N1 FRAMES NFTs, ensuring that ownership of the original 0N1 Force NFT automatically transfers the respective Frame.
Generated: DETERMINISTIC_e3bcdf93bae944d3
Batch ID: 20250612_154657
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title 0N1 FRAMES NFT Smart Contract
 * @dev This contract manages the 0N1 FRAMES NFTs and enforces transfer rules
 * where ownership of the original 0N1 Force NFT automatically transfers the respective Frame.
 */
contract OniFrames is ERC721, Ownable {
    using Address for address;

    // Original 0N1 Force NFT contract address
    address public originalOniContract;

    // Mapping from original 0N1 token ID to Frame token ID
    mapping(uint256 => uint256) public originalToFrame;

    // Mapping from Frame token ID to original 0N1 token ID
    mapping(uint256 => uint256) public frameToOriginal;

    // Counter for Frame token IDs
    uint256 private _currentTokenId = 0;

    // Event emitted when a new Frame is minted
    event FrameMinted(uint256 indexed originalTokenId, uint256 indexed frameTokenId);

    /**
     * @dev Constructor
     * @param _originalOniContract Address of the original 0N1 Force NFT contract
     */
    constructor(address _originalOniContract) ERC721("0N1 FRAMES", "0N1FRAME") {
        require(_originalOniContract != address(0), "Invalid contract address");
        originalOniContract = _originalOniContract;
    }

    /**
     * @dev Mint a new Frame NFT for a given original 0N1 NFT
     * @param originalTokenId The token ID of the original 0N1 NFT
     */
    function mintFrame(uint256 originalTokenId) external onlyOwner {
        require(originalToFrame[originalTokenId] == 0, "Frame already exists for this 0N1");
        
        _currentTokenId += 1;
        uint256 frameTokenId = _currentTokenId;
        
        _safeMint(owner(), frameTokenId);
        
        originalToFrame[originalTokenId] = frameTokenId;
        frameToOriginal[frameTokenId] = originalTokenId;
        
        emit FrameMinted(originalTokenId, frameTokenId);
    }

    /**
     * @dev Override transfer functions to enforce transfer rules
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) {
            uint256 originalTokenId = frameToOriginal[tokenId];
            require(originalTokenId != 0, "Invalid Frame token ID");

            // Get owner of the original 0N1 NFT
            address originalOwner = IERC721(originalOniContract).ownerOf(originalTokenId);
            
            // Frame can only be transferred to the owner of the original 0N1 NFT
            require(to == originalOwner, "Frame can only be transferred to owner of original 0N1");
        }
    }

    /**
     * @dev Get the Frame token ID for a given original 0N1 token ID
     * @param originalTokenId The token ID of the original 0N1 NFT
     * @return The corresponding Frame token ID
     */
    function getFrameForOriginal(uint256 originalTokenId) external view returns (uint256) {
        return originalToFrame[originalTokenId];
    }

    /**
     * @dev Get the original 0N1 token ID for a given Frame token ID
     * @param frameTokenId The token ID of the Frame NFT
     * @return The corresponding original 0N1 token ID
     */
    function getOriginalForFrame(uint256 frameTokenId) external view returns (uint256) {
        return frameToOriginal[frameTokenId];
    }
}
```
