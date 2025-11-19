"""
Generated Code Metadata:
========================
Original URL: https://validationserver.pages.dev
Prompt: "Design a smart contract for a DeFi protocol that handles NFT rewards, staking, and gas fee adjustments on a decentralized network."
Generated: DETERMINISTIC_b4e9a1f32e47e6d8
Batch ID: 20250622_205537
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a DeFi protocol that handles NFT rewards, staking, and gas fee adjustments
contract DeFiNFTStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each staker
    struct Staker {
        uint256 stakedAmount;
        uint256 lastClaimed;
        uint256 rewards;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // NFT contract interface
    IERC721 public nftContract;

    // Reward rate per block
    uint256 public rewardRate = 1e18; // 1 token per block

    // Event emitted when a user stakes NFTs
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes NFTs
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the NFT contract
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }

    // Function to stake NFTs
    function stake(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(stakers[msg.sender].stakedAmount == 0, "Already staked");

        // Transfer NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Update staker information
        stakers[msg.sender].stakedAmount = tokenId;
        stakers[msg.sender].lastClaimed = block.number;

        emit Staked(msg.sender, tokenId);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked NFTs");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed block
        staker.lastClaimed = block.number;
        staker.rewards = staker.rewards.add(reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to unstake NFTs
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked NFTs");

        // Calculate rewards before unstaking
        claimRewards();

        // Transfer NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, staker.stakedAmount);
        
        // Reset staker information
        delete stakers[msg.sender];

        emit Unstaked(msg.sender, staker.stakedAmount);
    }

    // Function to calculate rewards based on blocks staked
    function calculateRewards(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 blocksStaked = block.number.sub(staker.lastClaimed);
        return blocksStaked.mul(rewardRate);
    }

    // Function to adjust the reward rate (only owner can call)
    function adjustRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract (only owner can call)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(nftContract), "Cannot withdraw NFTs");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
