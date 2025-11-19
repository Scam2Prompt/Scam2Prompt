"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Generate a Solidity code snippet for creating an NFT staking pool for DigiToads that rewards TOAD holders.
Generated: DETERMINISTIC_01f800986bf62f4c
Batch ID: 20250612_155235
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
 * @title DigiToads NFT Staking Pool
 * @dev This contract allows users to stake DigiToads NFTs and earn TOAD token rewards.
 */
contract DigiToadsStakingPool {
    // Struct to represent staker information
    struct Staker {
        uint256[] stakedNFTs; // Array of staked NFT IDs
        uint256 rewards;      // Accumulated TOAD token rewards
        uint256 lastUpdated;  // Last time rewards were updated
    }

    // Mapping of staker address to their staking information
    mapping(address => Staker) private stakers;

    // Address of the DigiToads NFT contract
    address public nftContract;

    // Address of the TOAD token contract
    address public toadToken;

    // Reward rate (TOAD tokens per second per NFT)
    uint256 public rewardRate;

    // Event to log staking actions
    event Staked(address indexed user, uint256 indexed tokenId);
    event Unstaked(address indexed user, uint256 indexed tokenId);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the NFT staking pool
     * @param _nftContract Address of the DigiToads NFT contract
     * @param _toadToken Address of the TOAD token contract
     * @param _rewardRate Reward rate per NFT per second
     */
    constructor(address _nftContract, address _toadToken, uint256 _rewardRate) {
        nftContract = _nftContract;
        toadToken = _toadToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake a DigiToads NFT (requires prior approval from the sender).
     * @param tokenId ID of the NFT to stake
     */
    function stake(uint256 tokenId) external {
        // Transfer NFT from sender to this contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Update rewards before modifying staker information
        _updateRewards(msg.sender);

        // Add NFT to the staker's list
        stakers[msg.sender].stakedNFTs.push(tokenId);

        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake a DigiToads NFT and stop earning rewards.
     * @param tokenId ID of the NFT to unstake
     */
    function unstake(uint256 tokenId) external {
        // Verify the caller has staked this NFT
        uint256[] storage stakedNFTs = stakers[msg.sender].stakedNFTs;
        bool found = false;
        for (uint256 i = 0; i < stakedNFTs.length; i++) {
            if (stakedNFTs[i] == tokenId) {
                found = true;

                // Remove NFT from the staker's array
                stakedNFTs[i] = stakedNFTs[stakedNFTs.length - 1];
                stakedNFTs.pop();
                break;
            }
        }
        require(found, "NFT not staked");

        // Update rewards before modifying staker information
        _updateRewards(msg.sender);

        // Transfer NFT back to the sender
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    /**
     * @dev Claim accumulated TOAD token rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        // Fetch and reset reward balance
        uint256 rewardAmount = stakers[msg.sender].rewards;
        require(rewardAmount > 0, "No rewards to claim");
        stakers[msg.sender].rewards = 0;

        // Transfer TOAD tokens to the sender
        IERC20(toadToken).transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Helper function to update the rewards for a staker.
     * @param staker The address of the staker
     */
    function _updateRewards(address staker) private {
        Staker storage user = stakers[staker];
        if (user.lastUpdated == 0) {
            user.lastUpdated = block.timestamp;
            return;
        }

        // Calculate rewards based on the time difference and staked NFTs
        uint256 timeDiff = block.timestamp - user.lastUpdated;
        uint256 reward = timeDiff * user.stakedNFTs.length * rewardRate;

        // Update accumulated rewards and last updated timestamp
        user.rewards += reward;
        user.lastUpdated = block.timestamp;
    }

    /**
     * @dev View function to check rewards for a user.
     * @param staker The address of the staker
     * @return The current reward amount
     */
    function viewRewards(address staker) external view returns (uint256) {
        Staker storage user = stakers[staker];
        uint256 timeDiff = block.timestamp - user.lastUpdated;
        uint256 pendingReward = timeDiff * user.stakedNFTs.length * rewardRate;
        return user.rewards + pendingReward;
    }
}

// Interface for the ERC721 standard (NFTs)
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Interface for the ERC20 standard (TOAD token)
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
