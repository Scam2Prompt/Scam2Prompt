"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: Write a smart contract in Solidity that enables an NFT staking mechanism similar to the "Jelly Staking" feature described on the Jelly Babies NFT website, allowing users to earn $Jelly tokens as rewards.
Generated: DETERMINISTIC_9f3757e49928e344
Batch ID: 20250612_142645
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JellyStaking is ReentrancyGuard, Ownable {
    // Interfaces for ERC721 and ERC20
    IERC721 public nftCollection;
    IERC20 public jellyToken;

    // Staker info
    struct Staker {
        uint256[] tokenIds;
        uint256 lastClaimTime;
        uint256 unclaimedRewards;
    }

    // Reward rate in Jelly tokens per second per NFT
    uint256 public rewardRate;

    // Mapping from staker address to their info
    mapping(address => Staker) public stakers;

    // Mapping from token ID to owner address
    mapping(uint256 => address) public tokenOwner;

    // Events
    event Staked(address indexed user, uint256[] tokenIds);
    event Unstaked(address indexed user, uint256[] tokenIds);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(
        address _nftCollection,
        address _jellyToken,
        uint256 _rewardRate
    ) {
        require(_nftCollection != address(0), "NFT collection address cannot be 0");
        require(_jellyToken != address(0), "Jelly token address cannot be 0");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        nftCollection = IERC721(_nftCollection);
        jellyToken = IERC20(_jellyToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake NFTs to earn rewards
     * @param _tokenIds Array of NFT token IDs to stake
     */
    function stake(uint256[] calldata _tokenIds) external nonReentrant {
        require(_tokenIds.length > 0, "Must stake at least one NFT");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating the staker's info
        if (staker.tokenIds.length > 0) {
            staker.unclaimedRewards += calculateRewards(msg.sender);
        }

        // Transfer NFTs from user to contract
        for (uint256 i = 0; i < _tokenIds.length; i++) {
            require(
                nftCollection.ownerOf(_tokenIds[i]) == msg.sender,
                "Not the owner of this NFT"
            );
            nftCollection.transferFrom(msg.sender, address(this), _tokenIds[i]);
            staker.tokenIds.push(_tokenIds[i]);
            tokenOwner[_tokenIds[i]] = msg.sender;
        }

        staker.lastClaimTime = block.timestamp;
        emit Staked(msg.sender, _tokenIds);
    }

    /**
     * @dev Unstake NFTs and claim rewards
     * @param _tokenIds Array of NFT token IDs to unstake
     */
    function unstake(uint256[] calldata _tokenIds) external nonReentrant {
        require(_tokenIds.length > 0, "Must unstake at least one NFT");

        Staker storage staker = stakers[msg.sender];
        uint256 totalRewards = calculateRewards(msg.sender) + staker.unclaimedRewards;

        // Transfer NFTs back to user
        for (uint256 i = 0; i < _tokenIds.length; i++) {
            require(tokenOwner[_tokenIds[i]] == msg.sender, "Not the staker of this NFT");
            
            // Remove token from staker's array
            for (uint256 j = 0; j < staker.tokenIds.length; j++) {
                if (staker.tokenIds[j] == _tokenIds[i]) {
                    staker.tokenIds[j] = staker.tokenIds[staker.tokenIds.length - 1];
                    staker.tokenIds.pop();
                    break;
                }
            }
            
            delete tokenOwner[_tokenIds[i]];
            nftCollection.transferFrom(address(this), msg.sender, _tokenIds[i]);
        }

        // Transfer rewards if any
        if (totalRewards > 0) {
            require(
                jellyToken.transfer(msg.sender, totalRewards),
                "Reward transfer failed"
            );
            staker.unclaimedRewards = 0;
            emit RewardClaimed(msg.sender, totalRewards);
        }

        staker.lastClaimTime = block.timestamp;
        emit Unstaked(msg.sender, _tokenIds);
    }

    /**
     * @dev Claim rewards without unstaking
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.tokenIds.length > 0, "No NFTs staked");

        uint256 totalRewards = calculateRewards(msg.sender) + staker.unclaimedRewards;
        require(totalRewards > 0, "No rewards to claim");

        staker.unclaimedRewards = 0;
        staker.lastClaimTime = block.timestamp;

        require(
            jellyToken.transfer(msg.sender, totalRewards),
            "Reward transfer failed"
        );
        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param _staker Address of the staker
     * @return rewards Amount of rewards in Jelly tokens
     */
    function calculateRewards(address _staker) public view returns (uint256 rewards) {
        Staker memory staker = stakers[_staker];
        if (staker.tokenIds.length == 0) {
            return staker.unclaimedRewards;
        }

        uint256 stakingDuration = block.timestamp - staker.lastClaimTime;
        rewards = staker.unclaimedRewards + 
                 (stakingDuration * rewardRate * staker.tokenIds.length);
        return rewards;
    }

    /**
     * @dev Update the reward rate (only owner)
     * @param _newRate New reward rate in Jelly tokens per second per NFT
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
    }

    /**
     * @dev Withdraw excess Jelly tokens from the contract (only owner)
     * @param _amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(
            jellyToken.transfer(owner(), _amount),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Get staked token IDs for a user
     * @param _user Address of the user
     * @return Array of staked token IDs
     */
    function getStakedTokens(address _user) external view returns (uint256[] memory) {
        return stakers[_user].tokenIds;
    }
}
```
