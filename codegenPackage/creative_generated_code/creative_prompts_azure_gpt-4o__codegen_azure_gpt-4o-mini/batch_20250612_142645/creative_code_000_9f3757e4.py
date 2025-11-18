"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: Write a smart contract in Solidity that enables an NFT staking mechanism similar to the "Jelly Staking" feature described on the Jelly Babies NFT website, allowing users to earn $Jelly tokens as rewards.
Generated: DETERMINISTIC_9f3757e49928e344
Batch ID: 20250612_142645
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

// Importing required libraries and interfaces
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JellyStaking is Ownable {
    // Token to be earned
    IERC20 public jellyToken;
    
    // NFT contract to be staked
    IERC721 public nftContract;

    // Structure to keep track of staked NFTs and rewards
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;
    // Mapping from user address to the total earned rewards
    mapping(address => uint256) public rewards;

    // Event emitted when NFTs are staked
    event Staked(address indexed user, uint256 indexed tokenId);
    // Event emitted when NFTs are unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Reward rate (in terms of tokens per second)
    uint256 public rewardRate = 1e18; // Example rate (adjustable)

    constructor(IERC20 _jellyToken, IERC721 _nftContract) {
        jellyToken = _jellyToken;
        nftContract = _nftContract;
    }

    /**
     * @dev Stakes a specific NFT.
     * @param tokenId The ID of the NFT to stake.
     */
    function stake(uint256 tokenId) external {
        // Ensure that the caller owns the NFT and has approved the contract
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(nftContract.isApprovedForAll(msg.sender, address(this)), "Contract not approved");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));

        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Unstakes a specific NFT and claims rewards.
     * @param tokenId The ID of the NFT to unstake.
     */
    function unstake(uint256 tokenId) external {
        // Find the stake and validate ownership
        uint256 index = findStake(msg.sender, tokenId);
        require(index < stakes[msg.sender].length, "Stake not found");

        // Calculate and claim rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward;

        // Remove the stake from the user's stakes
        removeStake(msg.sender, index);

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Claims rewards for the caller.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards to zero
        rewards[msg.sender] += reward;

        // Transfer the rewards to the user
        jellyToken.transfer(msg.sender, rewards[msg.sender]);
        rewards[msg.sender] = 0;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the total reward for the user.
     * @param user The address of the user to calculate rewards for.
     * @return The total rewards earned.
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 totalReward = 0;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stakeInfo = stakes[user][i];
            uint256 duration = block.timestamp - stakeInfo.timestamp;
            totalReward += (duration * rewardRate) / 1e18; // Convert to correct decimals
        }
        return totalReward + rewards[user];
    }

    /**
     * @dev Finds the index of a stake for a given user and tokenId.
     * @param user The address of the user.
     * @param tokenId The ID of the NFT.
     * @return The index of the stake.
     */
    function findStake(address user, uint256 tokenId) internal view returns (uint256) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    /**
     * @dev Removes a stake from the user's stakes.
     * @param user The address of the user.
     * @param index The index of the stake to remove.
     */
    function removeStake(address user, uint256 index) internal {
        // Move the last stake to the index position
        if (index < stakes[user].length - 1) {
            stakes[user][index] = stakes[user][stakes[user].length - 1];
        }
        stakes[user].pop(); // Remove last element
    }

    /**
     * @dev Allows the owner to set a new reward rate.
     * @param newRate The new reward rate (in tokens per second).
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
