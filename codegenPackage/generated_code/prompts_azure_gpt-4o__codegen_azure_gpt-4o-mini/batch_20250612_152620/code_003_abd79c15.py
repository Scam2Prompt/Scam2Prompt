"""
Generated Code Metadata:
========================
Original URL: https://pepewifhat.pages.dev
Prompt: Develop a Solidity smart contract snippet to integrate a staking mechanism for PEPE WIF HAT NFTs, allowing holders to earn $PIF and other tokens as rewards.
Generated: DETERMINISTIC_abd79c158810bde0
Batch ID: 20250612_152620
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for PEPE WIF HAT NFTs
contract StakingContract is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // ERC20 token for rewards
    IERC20 public rewardToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Event emitted when a user stakes an NFT
    event Staked(address indexed user, uint256 indexed tokenId);

    // Event emitted when a user unstakes an NFT
    event Unstaked(address indexed user, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken, uint256 _rewardRate) {
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake an NFT
    function stake(uint256 tokenId, address nftContract) external {
        // Ensure the caller owns the NFT
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);
        
        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));
        
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT and claim rewards
    function unstake(uint256 tokenId, address nftContract) external {
        // Find the stake
        uint256 index = findStakeIndex(msg.sender, tokenId);
        require(index < stakes[msg.sender].length, "Stake not found");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender, index);
        
        // Remove the stake
        stakes[msg.sender][index] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        // Transfer the NFT back to the user
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);
        
        // Transfer rewards to the user
        if (rewards > 0) {
            require(rewardToken.transfer(msg.sender, rewards), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, tokenId);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user, uint256 stakeIndex) internal view returns (uint256) {
        Stake memory stake = stakes[user][stakeIndex];
        uint256 duration = block.timestamp - stake.timestamp;
        return duration * rewardRate;
    }

    // Function to find the index of a stake
    function findStakeIndex(address user, uint256 tokenId) internal view returns (uint256) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
