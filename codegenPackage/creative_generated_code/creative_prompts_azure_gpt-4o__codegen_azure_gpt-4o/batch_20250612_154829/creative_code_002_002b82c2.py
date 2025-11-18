"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://timcheese.pages.dev
Prompt: Generate code in Solidity to verify ownership of Tim Cheese NFTs and grant access to "The Park" based on token possession.
Generated: DETERMINISTIC_002b82c200aeb690
Batch ID: 20250612_154829
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
 * @title TimCheeseNFTAccess
 * @dev Contract to verify ownership of Tim Cheese NFTs and grant access to "The Park".
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract TimCheeseNFTAccess {
    // Address of the Tim Cheese NFT contract
    address public immutable timCheeseNFT;
    
    // Mapping to keep track of addresses that have access to "The Park"
    mapping(address => bool) public parkAccess;

    // Event emitted when access is granted
    event AccessGranted(address indexed user);
    
    // Modifier to check if the sender owns a specific Tim Cheese NFT
    modifier ownsTimCheeseNFT(uint256 tokenId) {
        require(IERC721(timCheeseNFT).ownerOf(tokenId) == msg.sender, "You do not own the required NFT.");
        _;
    }

    /**
     * @dev Constructor to set the Tim Cheese NFT contract address
     * @param _timCheeseNFT Address of the Tim Cheese NFT contract
     */
    constructor(address _timCheeseNFT) {
        require(_timCheeseNFT != address(0), "Invalid NFT contract address.");
        timCheeseNFT = _timCheeseNFT;
    }
    
    /**
     * @dev Function to grant access to "The Park" based on NFT ownership
     * @param tokenId ID of the Tim Cheese NFT owned by the sender
     */
    function grantParkAccess(uint256 tokenId) external ownsTimCheeseNFT(tokenId) {
        require(!parkAccess[msg.sender], "Access to 'The Park' already granted.");
        
        // Grant access to "The Park"
        parkAccess[msg.sender] = true;
        
        // Emit the access granted event
        emit AccessGranted(msg.sender);
    }

    /**
     * @dev Function to check if an address has access to "The Park"
     * @param user Address to check for park access
     * @return bool indicating whether the user has access
     */
    function hasParkAccess(address user) external view returns (bool) {
        return parkAccess[user];
    }
}
```
