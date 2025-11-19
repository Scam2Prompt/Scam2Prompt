"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Outline the steps to implement a staking mechanism for GOFURS tokens, considering the automatic NFT minting and burning features of the ERC404 standard.
Generated: DETERMINISTIC_5a82a61238c295db
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GOFURSStaking is ReentrancyGuard, Ownable {
    // Struct to store staker information
    struct Staker {
        uint256 amountStaked;
        uint256 timeOfLastUpdate;
        uint256 unclaimedRewards;
        uint256[] stakedNFTs;
    }

    // Interfaces for ERC20 and ERC404 (ERC721) tokens
    IERC20 public immutable stakingToken;
    IERC721 public immutable nftToken;

    // Staking rewards parameters
    uint256 public rewardRate; // Reward rate per second
    uint256 public minStakeDuration; // Minimum stake duration in seconds

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event NFTMinted(address indexed user, uint256 tokenId);
    event NFTBurned(address indexed user, uint256 tokenId);

    constructor(
        address _stakingToken,
        address _nftToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) Ownable(msg.sender) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_nftToken != address(0), "Invalid NFT token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        
        stakingToken = IERC20(_stakingToken);
        nftToken = IERC721(_nftToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
    }

    // Calculate rewards for a staker
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.amountStaked == 0) {
            return staker.unclaimedRewards;
        }

        uint256 secondsStaked = block.timestamp - staker.timeOfLastUpdate;
        return staker.unclaimedRewards + (staker.amountStaked * rewardRate * secondsStaked) / 1e18;
    }

    // Update rewards for a staker
    function _updateRewards(address _staker) internal {
        stakers[_staker].unclaimedRewards = calculateRewards(_staker);
        stakers[_staker].timeOfLastUpdate = block.timestamp;
    }

    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        _updateRewards(msg.sender);
        
        // Transfer tokens from staker to this contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staker's balance
        stakers[msg.sender].amountStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");
        require(
            block.timestamp - staker.timeOfLastUpdate >= minStakeDuration,
            "Minimum stake duration not met"
        );

        _updateRewards(msg.sender);

        // Transfer tokens back to staker
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        // Update staker's balance
        staker.amountStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 rewards = stakers[msg.sender].unclaimedRewards;
        require(rewards > 0, "No rewards to claim");

        stakers[msg.sender].unclaimedRewards = 0;
        
        // Transfer rewards to staker
        bool success = stakingToken.transfer(msg.sender, rewards);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    // Mint NFT based on staking rewards (to be called by ERC404 contract)
    function mintNFT(address _to) external onlyOwner {
        require(_to != address(0), "Invalid address");
        
        // In a real implementation, this would interact with the ERC404 contract
        // to mint an NFT. This is a placeholder for that functionality.
        uint256 tokenId = 0; // Would be generated by ERC404 contract
        emit NFTMinted(_to, tokenId);
    }

    // Burn NFT (to be called by ERC404 contract)
    function burnNFT(address _from, uint256 _tokenId) external onlyOwner {
        require(_from != address(0), "Invalid address");
        
        // In a real implementation, this would interact with the ERC404 contract
        // to burn an NFT. This is a placeholder for that functionality.
        emit NFTBurned(_from, _tokenId);
    }

    // Admin function to update reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }

    // Admin function to update minimum stake duration
    function setMinStakeDuration(uint256 _minStakeDuration) external onlyOwner {
        minStakeDuration = _minStakeDuration;
    }

    // Emergency withdraw function (only owner)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
