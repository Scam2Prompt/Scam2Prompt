"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsnodes.pages.dev
Prompt: Provide an example of how to set up NFT staking on the Smart Dapps platform.
Generated: DETERMINISTIC_96b42622967fec24
Batch ID: 20250612_164152
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
 * @title NFTStaking
 * @dev A contract that allows users to stake their NFTs and earn rewards.
 */

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract NFTStaking {
    // Struct to store information about a staked NFT
    struct Stake {
        uint256 tokenId;
        uint256 startTime;
        address owner;
    }

    // Mapping from token ID to staked NFT details
    mapping(uint256 => Stake) public stakes;

    // Rewards per second per NFT (can be adjusted as needed)
    uint256 public rewardsPerSecond = 1 ether;

    // Reference to the NFT contract
    IERC721 public nftContract;

    // Events
    event Staked(address indexed user, uint256 tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 tokenId, uint256 reward, uint256 timestamp);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _nftContract Address of the ERC721 contract being staked.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Function to stake an NFT.
     * @param tokenId ID of the NFT to be staked.
     */
    function stake(uint256 tokenId) external {
        // Ensure that the NFT is owned by the caller
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer the NFT to the staking contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Create the stake record
        stakes[tokenId] = Stake({
            tokenId: tokenId,
            startTime: block.timestamp,
            owner: msg.sender
        });

        // Emit the staking event
        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Function to unstake an NFT and claim rewards.
     * @param tokenId ID of the NFT to be unstaked.
     */
    function unstake(uint256 tokenId) external {
        // Ensure the token is staked and the caller is the staker
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You are not the owner of this staked NFT");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        uint256 reward = stakingDuration * rewardsPerSecond;

        // Remove the stake record
        delete stakes[tokenId];

        // Transfer the NFT back to the owner
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Transfer rewards (in a real implementation, this would involve a token transfer)
        // For now, just emit the unstaking event with the calculated reward
        emit Unstaked(msg.sender, tokenId, reward, block.timestamp);
    }

    /**
     * @dev Function to update rewards rate.
     * @param _rewardsPerSecond New rewards rate per second per NFT.
     */
    function setRewardsRate(uint256 _rewardsPerSecond) external {
        // In a production contract, this should be restricted to an admin role
        require(_rewardsPerSecond > 0, "Rewards rate must be greater than zero");
        rewardsPerSecond = _rewardsPerSecond;
    }
}
```
