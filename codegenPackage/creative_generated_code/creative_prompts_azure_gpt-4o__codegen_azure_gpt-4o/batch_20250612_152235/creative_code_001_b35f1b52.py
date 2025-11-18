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

// @title Moonbirds NFT Staking Contract with Reward Distribution
// @dev Allows users to stake their Moonbirds NFTs and earn rewards
interface IMoonbirds {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract MoonbirdsStaking {
    address public immutable moonbirdsAddress; // Address of the Moonbirds NFT contract
    address public owner; // Contract owner (admin)
    
    uint256 public rewardRate; // Reward rate per staked NFT per second
    mapping(address => uint256) public rewards; // Accumulated rewards per user
    mapping(address => uint256) public lastUpdateTime; // Last time rewards were updated for each user
    mapping(address => uint256) public stakedCount; // Number of NFTs staked by each user
    mapping(uint256 => address) public tokenIdToStaker; // Mapping from tokenID to staker address

    event NFTStaked(address indexed user, uint256 tokenId);
    event NFTUnstaked(address indexed user, uint256 tokenId);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _moonbirdsAddress, uint256 _rewardRate) {
        require(_moonbirdsAddress != address(0), "Invalid Moonbirds contract address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        moonbirdsAddress = _moonbirdsAddress;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // @dev Updates rewards for a user
    function _updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        rewards[user] += stakedCount[user] * rewardRate * timeElapsed;
        lastUpdateTime[user] = block.timestamp;
    }

    // @dev Stake a Moonbirds NFT
    function stake(uint256 tokenId) external {
        _updateRewards(msg.sender);

        IMoonbirds moonbirds = IMoonbirds(moonbirdsAddress);

        // Check ownership
        require(moonbirds.ownerOf(tokenId) == msg.sender, "Caller does not own this NFT");

        // Transfer NFT to this contract
        moonbirds.safeTransferFrom(msg.sender, address(this), tokenId);

        // Update staking records
        tokenIdToStaker[tokenId] = msg.sender;
        stakedCount[msg.sender] += 1;

        emit NFTStaked(msg.sender, tokenId);
    }

    // @dev Unstake a Moonbirds NFT
    function unstake(uint256 tokenId) external {
        require(tokenIdToStaker[tokenId] == msg.sender, "Caller is not the staker of this NFT");

        _updateRewards(msg.sender);

        IMoonbirds moonbirds = IMoonbirds(moonbirdsAddress);

        // Transfer NFT back to the owner
        moonbirds.safeTransferFrom(address(this), msg.sender, tokenId);

        // Update staking records
        tokenIdToStaker[tokenId] = address(0);
        stakedCount[msg.sender] -= 1;

        emit NFTUnstaked(msg.sender, tokenId);
    }

    // @dev Claim accumulated rewards
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer reward to the user (assuming native currency like ETH)
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // @dev Adjust reward rate (only owner can call)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // @dev Withdraw contract balance (only owner can call)
    function withdrawBalance() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to accept ETH (e.g., for funding rewards)
    receive() external payable {}
}
```
