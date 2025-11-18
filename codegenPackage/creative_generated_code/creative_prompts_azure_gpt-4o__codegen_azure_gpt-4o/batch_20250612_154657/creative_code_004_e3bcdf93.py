"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on1force.web.app
Prompt: Create a smart contract that enforces the rules for transferring 0N1 FRAMES NFTs, ensuring that ownership of the original 0N1 Force NFT automatically transfers the respective Frame.
Generated: DETERMINISTIC_e3bcdf93bae944d3
Batch ID: 20250612_154657
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
 * @title ON1FramesNFT
 * @notice Smart contract to manage the transfer of 0N1 FRAMES NFTs linked to ownership of 0N1 Force NFTs.
 * @dev This contract ensures that ownership of a Frame NFT is automatically transferred with the corresponding Force NFT.
 */
contract ON1FramesNFT {
    // Mapping to store the association between 0N1 Force NFT IDs and Frame NFT IDs
    mapping(uint256 => uint256) public forceToFrame;

    // Address of the 0N1 Force NFT contract
    address public on1ForceContract;

    // Address of the 0N1 Frames NFT contract
    address public on1FramesContract;

    // Event emitted when a Frame NFT is transferred automatically
    event FrameTransferred(uint256 forceNFTId, uint256 frameNFTId, address newOwner);

    /**
     * @dev Modifier to ensure only the owner of a Force NFT can call certain functions.
     */
    modifier onlyForceNFTOwner(uint256 forceNFTId) {
        require(
            IERC721(on1ForceContract).ownerOf(forceNFTId) == msg.sender,
            "Caller is not the owner of the Force NFT"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the addresses of the 0N1 Force and Frames NFT contracts.
     * @param _on1ForceContract Address of the 0N1 Force NFT contract.
     * @param _on1FramesContract Address of the 0N1 Frames NFT contract.
     */
    constructor(address _on1ForceContract, address _on1FramesContract) {
        require(_on1ForceContract != address(0), "Invalid Force contract address");
        require(_on1FramesContract != address(0), "Invalid Frames contract address");

        on1ForceContract = _on1ForceContract;
        on1FramesContract = _on1FramesContract;
    }

    /**
     * @dev Function to link a Force NFT ID to a Frame NFT ID.
     * @param forceNFTId ID of the 0N1 Force NFT.
     * @param frameNFTId ID of the 0N1 Frame NFT.
     */
    function linkFrameToForce(uint256 forceNFTId, uint256 frameNFTId) external onlyForceNFTOwner(forceNFTId) {
        require(
            IERC721(on1FramesContract).ownerOf(frameNFTId) == msg.sender,
            "Caller is not the owner of the Frame NFT"
        );

        forceToFrame[forceNFTId] = frameNFTId;
    }

    /**
     * @dev Hook to be called when a Force NFT is transferred, automatically transferring the linked Frame NFT.
     * @param from Address of the previous owner of the Force NFT.
     * @param to Address of the new owner of the Force NFT.
     * @param forceNFTId ID of the transferred 0N1 Force NFT.
     */
    function onForceTransfer(address from, address to, uint256 forceNFTId) external {
        require(msg.sender == on1ForceContract, "Unauthorized caller");

        uint256 frameNFTId = forceToFrame[forceNFTId];
        if (frameNFTId != 0) {
            IERC721(on1FramesContract).transferFrom(from, to, frameNFTId);
            emit FrameTransferred(forceNFTId, frameNFTId, to);
        }
    }
}

// Interface for ERC721 operations
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
