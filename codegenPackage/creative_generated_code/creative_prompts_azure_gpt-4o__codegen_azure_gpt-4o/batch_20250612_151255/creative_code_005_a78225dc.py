"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracocollectbase0xdba43fe81b31ba402de5b9a2de6.pages.dev
Prompt: Develop a smart contract that integrates "$ENJOY" token rewards for interactions with "Kaira Mythos: Centaur" NFTs.
Generated: DETERMINISTIC_a78225dcaae1db14
Batch ID: 20250612_151255
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
 * @title Kaira Mythos Reward Contract
 * @dev A smart contract that integrates $ENJOY token rewards for interactions with "Kaira Mythos: Centaur" NFTs.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract KairaMythosReward {
    // Address of the Kaira Mythos NFT contract
    address public kairaMythosNFT;

    // Address of the $ENJOY token contract
    address public enjoyToken;

    // Mapping to track rewards claimed by token IDs
    mapping(uint256 => bool) public rewardsClaimed;

    // Reward amount in $ENJOY tokens for each interaction
    uint256 public rewardAmount;

    // Event to track reward claims
    event RewardClaimed(address indexed user, uint256 indexed tokenId, uint256 amount);

    /**
     * @dev Sets the NFT and token contract addresses, along with the reward amount.
     * @param _kairaMythosNFT Address of the Kaira Mythos NFT contract.
     * @param _enjoyToken Address of the $ENJOY token contract.
     * @param _rewardAmount Amount of $ENJOY tokens to reward.
     */
    constructor(address _kairaMythosNFT, address _enjoyToken, uint256 _rewardAmount) {
        require(_kairaMythosNFT != address(0), "Invalid NFT contract address");
        require(_enjoyToken != address(0), "Invalid token contract address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        
        kairaMythosNFT = _kairaMythosNFT;
        enjoyToken = _enjoyToken;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Allows users to claim $ENJOY tokens as rewards for owning a specific NFT.
     * @param tokenId The ID of the NFT the user is interacting with.
     */
    function claimReward(uint256 tokenId) external {
        // Ensure reward has not already been claimed for this token
        require(!rewardsClaimed[tokenId], "Reward already claimed for this token");

        // Validate ownership of the NFT
        address nftOwner = IERC721(kairaMythosNFT).ownerOf(tokenId);
        require(nftOwner == msg.sender, "Caller is not the owner of this NFT");

        // Mark the token as claimed
        rewardsClaimed[tokenId] = true;

        // Transfer the reward tokens to the caller
        bool success = IERC20(enjoyToken).transfer(msg.sender, rewardAmount);
        require(success, "$ENJOY token transfer failed");

        // Emit the reward claim event
        emit RewardClaimed(msg.sender, tokenId, rewardAmount);
    }

    /**
     * @dev Allows the contract owner to update the reward amount.
     * @param _rewardAmount The new reward amount in $ENJOY tokens.
     */
    function updateRewardAmount(uint256 _rewardAmount) external {
        require(msg.sender == address(this), "Only contract owner can update reward amount");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        rewardAmount = _rewardAmount;
    }
}
```
