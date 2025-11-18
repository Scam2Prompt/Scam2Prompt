"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Generate a Solidity smart contract for creating a staking mechanism specific to Moonbirds NFTs, including a reward distribution system.
Generated: DETERMINISTIC_b35f1b52ec41f9aa
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Moonbirds NFT
interface IMoonbirds is IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Staking contract for Moonbirds NFTs
contract MoonbirdsStaking is Ownable {
    using SafeMath for uint256;

    // Moonbirds NFT contract address
    IMoonbirds public moonbirdsNFT;

    // Structure to hold staking information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardTime;
    }

    // Mapping of staker address to their staking information
    mapping(address => Staker) public stakers;

    // Total rewards distributed
    uint256 public totalRewards;
    
    // Reward per staked token per second
    uint256 public rewardRate;

    // Event emitted when a user stakes NFTs
    event Staked(address indexed user, uint256 tokenId);
    
    // Event emitted when a user unstakes NFTs
    event Unstaked(address indexed user, uint256 tokenId);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the Moonbirds NFT contract and reward rate
    constructor(address _moonbirdsNFT, uint256 _rewardRate) {
        require(_moonbirdsNFT != address(0), "Invalid NFT address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        moonbirdsNFT = IMoonbirds(_moonbirdsNFT);
        rewardRate = _rewardRate;
    }

    // Function to stake a Moonbird NFT
    function stake(uint256 tokenId) external {
        require(moonbirdsNFT.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Update the staker's information before staking
        updateRewards(msg.sender);
        
        // Transfer the NFT to the contract
        moonbirdsNFT.transferFrom(msg.sender, address(this), tokenId);
        
        // Increase the staked amount
        stakers[msg.sender].stakedAmount += 1;
        stakers[msg.sender].lastRewardTime = block.timestamp;

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake a Moonbird NFT
    function unstake(uint256 tokenId) external {
        require(stakers[msg.sender].stakedAmount > 0, "No staked NFTs");
        
        // Update the staker's information before unstaking
        updateRewards(msg.sender);
        
        // Decrease the staked amount
        stakers[msg.sender].stakedAmount -= 1;
        
        // Transfer the NFT back to the user
        moonbirdsNFT.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset last reward time
        stakers[msg.sender].lastRewardTime = block.timestamp;
        
        // Transfer the rewards to the user
        totalRewards -= rewards;
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update rewards for a given staker
    function updateRewards(address stakerAddress) internal {
        uint256 rewards = calculateRewards(stakerAddress);
        
        // If rewards are calculated, add to total rewards
        if (rewards > 0) {
            totalRewards += rewards;
        }
        
        // Update last reward time
        stakers[stakerAddress].lastRewardTime = block.timestamp;
    }

    // Function to calculate rewards for a given staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp.sub(staker.lastRewardTime);
        return staker.stakedAmount.mul(rewardRate).mul(timeStaked);
    }

    // Function to receive Ether (for reward payments)
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }
}
```
