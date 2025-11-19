"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: Create a smart contract for staking Rascals NFTs to earn $Jelly tokens, ensuring compatibility with the Ethereum blockchain.
Generated: DETERMINISTIC_b56c7b62acbf063f
Batch ID: 20250612_152329
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

// Importing OpenZeppelin contracts for ERC721 and ERC20 standards
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Rascals NFTs to earn $Jelly tokens
contract RascalsStaking is Ownable {
    // Mapping from NFT token ID to the address of the staker
    mapping(uint256 => address) public stakedBy;
    // Mapping from staker address to their staked NFT count
    mapping(address => uint256) public stakedCount;
    // Mapping to track the last time a token was staked
    mapping(uint256 => uint256) public lastStakedTime;

    // The NFT contract interface
    IERC721 public rascalsNFT;
    // The Jelly token contract interface
    IERC20 public jellyToken;

    // Reward rate in Jelly tokens per second
    uint256 public rewardRate = 1e18; // 1 Jelly token per second

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId);
    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the NFT and Jelly token contracts
    constructor(IERC721 _rascalsNFT, IERC20 _jellyToken) {
        rascalsNFT = _rascalsNFT;
        jellyToken = _jellyToken;
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(rascalsNFT.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Transfer the NFT to the contract
        rascalsNFT.transferFrom(msg.sender, address(this), tokenId);
        
        // Update staking information
        stakedBy[tokenId] = msg.sender;
        stakedCount[msg.sender]++;
        lastStakedTime[tokenId] = block.timestamp;

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        // Ensure the caller is the staker of the NFT
        require(stakedBy[tokenId] == msg.sender, "You do not own this staked NFT");
        
        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(tokenId);
        if (rewards > 0) {
            require(jellyToken.balanceOf(address(this)) >= rewards, "Insufficient Jelly tokens in contract");
            jellyToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Update staking information
        delete stakedBy[tokenId];
        stakedCount[msg.sender]--;
        delete lastStakedTime[tokenId];

        // Transfer the NFT back to the user
        rascalsNFT.transferFrom(address(this), msg.sender, tokenId);
        emit Unstaked(msg.sender, tokenId);
    }

    // Function to calculate rewards for a staked NFT
    function calculateRewards(uint256 tokenId) public view returns (uint256) {
        uint256 stakedDuration = block.timestamp - lastStakedTime[tokenId];
        return stakedDuration * rewardRate;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw Jelly tokens from the contract (only owner)
    function withdrawJelly(uint256 amount) external onlyOwner {
        require(jellyToken.balanceOf(address(this)) >= amount, "Insufficient Jelly tokens in contract");
        jellyToken.transfer(msg.sender, amount);
    }
}
```
