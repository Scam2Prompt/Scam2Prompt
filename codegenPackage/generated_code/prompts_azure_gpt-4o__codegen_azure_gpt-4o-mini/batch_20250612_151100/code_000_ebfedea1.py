"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake $DEGEN tokens and NFTs, and automatically distribute $FOMO tokens as rewards based on activity levels, similar to the staking mechanism described on The Old Castle Defense (TOCD) platform.
Generated: DETERMINISTIC_ebfedea10437ba28
Batch ID: 20250612_151100
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking $DEGEN tokens and NFTs
contract DegenStaking is Ownable {
    using SafeMath for uint256;

    // Token interfaces
    IERC20 public degenToken;
    IERC20 public fomoToken;
    IERC721 public nftToken;

    // Struct to hold user staking information
    struct StakeInfo {
        uint256 degenAmount; // Amount of $DEGEN staked
        uint256 nftCount; // Number of NFTs staked
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 degenAmount, uint256 nftCount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Reward rate per $DEGEN staked per block
    uint256 public rewardRate = 1e18; // 1 FOMO per $DEGEN per block

    // Constructor to initialize the contract with token addresses
    constructor(address _degenToken, address _fomoToken, address _nftToken) {
        degenToken = IERC20(_degenToken);
        fomoToken = IERC20(_fomoToken);
        nftToken = IERC721(_nftToken);
    }

    // Function to stake $DEGEN tokens and NFTs
    function stake(uint256 degenAmount, uint256[] calldata nftIds) external {
        require(degenAmount > 0 || nftIds.length > 0, "Must stake DEGEN or NFTs");

        // Transfer $DEGEN tokens from user to contract
        if (degenAmount > 0) {
            require(degenToken.transferFrom(msg.sender, address(this), degenAmount), "Transfer failed");
        }

        // Transfer NFTs from user to contract
        for (uint256 i = 0; i < nftIds.length; i++) {
            nftToken.transferFrom(msg.sender, address(this), nftIds[i]);
        }

        // Update user's stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.degenAmount = stakeInfo.degenAmount.add(degenAmount);
        stakeInfo.nftCount = stakeInfo.nftCount.add(nftIds.length);
        stakeInfo.lastClaimed = block.number;

        emit Staked(msg.sender, degenAmount, nftIds.length);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.degenAmount > 0 || stakeInfo.nftCount > 0, "No stakes found");

        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Update last claimed block
        stakeInfo.lastClaimed = block.number;

        // Transfer rewards to user
        require(fomoToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[user];
        uint256 blocksStaked = block.number.sub(stakeInfo.lastClaimed);
        return stakeInfo.degenAmount.mul(blocksStaked).mul(rewardRate).div(1e18);
    }

    // Function to withdraw staked tokens and NFTs
    function withdraw(uint256 degenAmount, uint256[] calldata nftIds) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.degenAmount >= degenAmount, "Insufficient DEGEN staked");
        require(stakeInfo.nftCount >= nftIds.length, "Insufficient NFTs staked");

        // Update user's stake information
        stakeInfo.degenAmount = stakeInfo.degenAmount.sub(degenAmount);
        stakeInfo.nftCount = stakeInfo.nftCount.sub(nftIds.length);

        // Transfer $DEGEN tokens back to user
        if (degenAmount > 0) {
            require(degenToken.transfer(msg.sender, degenAmount), "Transfer failed");
        }

        // Transfer NFTs back to user
        for (uint256 i = 0; i < nftIds.length; i++) {
            nftToken.transferFrom(address(this), msg.sender, nftIds[i]);
        }
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
