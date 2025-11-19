"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharxsharky.web.app
Prompt: Explain how to grow a Sharx NFT into a whale sharx using the $FISHY token in a smart contract.
Generated: DETERMINISTIC_f384d10daf5e3e59
Batch ID: 20250612_161017
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
 * @title SharxNFTGrowth
 * @dev This smart contract allows users to grow their Sharx NFT into a Whale Sharx using the $FISHY token.
 */
contract SharxNFTGrowth {
    // Define state variables
    address public owner; // Owner of the contract
    address public fishyTokenAddress; // Address of the $FISHY token contract
    address public sharxNFTAddress; // Address of the Sharx NFT contract

    mapping(uint256 => bool) public isWhaleSharx; // Tracks whether a Sharx NFT is upgraded to Whale Sharx
    uint256 public growthCost; // Cost in $FISHY tokens to grow Sharx NFT into a Whale Sharx

    // Events
    event SharxUpgraded(address indexed user, uint256 indexed tokenId);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(address _fishyTokenAddress, address _sharxNFTAddress, uint256 _growthCost) {
        owner = msg.sender;
        fishyTokenAddress = _fishyTokenAddress;
        sharxNFTAddress = _sharxNFTAddress;
        growthCost = _growthCost;
    }

    /**
     * @dev Function to grow a Sharx NFT into a Whale Sharx.
     * @param tokenId The ID of the Sharx NFT to upgrade.
     */
    function growSharx(uint256 tokenId) external {
        // Check that the Sharx NFT is not already a Whale Sharx
        require(!isWhaleSharx[tokenId], "This Sharx NFT is already a Whale Sharx");

        // Check ownership of the Sharx NFT
        require(IERC721(sharxNFTAddress).ownerOf(tokenId) == msg.sender, "You don't own this Sharx NFT");

        // Transfer $FISHY tokens from the user to the contract
        bool success = IERC20(fishyTokenAddress).transferFrom(msg.sender, address(this), growthCost);
        require(success, "$FISHY token transfer failed");

        // Mark the Sharx NFT as upgraded
        isWhaleSharx[tokenId] = true;

        // Emit event
        emit SharxUpgraded(msg.sender, tokenId);
    }

    /**
     * @dev Allows the contract owner to update the $FISHY token address.
     * @param _fishyTokenAddress The new address of the $FISHY token contract.
     */
    function updateFishyTokenAddress(address _fishyTokenAddress) external onlyOwner {
        fishyTokenAddress = _fishyTokenAddress;
    }

    /**
     * @dev Allows the contract owner to update the growth cost.
     * @param _growthCost The new cost in $FISHY tokens to grow Sharx NFT.
     */
    function updateGrowthCost(uint256 _growthCost) external onlyOwner {
        growthCost = _growthCost;
    }

    /**
     * @dev Allows the contract owner to withdraw any $FISHY tokens accumulated in the contract.
     * @param amount The amount of $FISHY tokens to withdraw.
     */
    function withdrawFishyTokens(uint256 amount) external onlyOwner {
        bool success = IERC20(fishyTokenAddress).transfer(owner, amount);
        require(success, "$FISHY token transfer failed");
    }

    /**
     * @dev Allows the contract owner to transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}

/**
 * @dev Minimal interface for ERC20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @dev Minimal interface for ERC721 token.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
