"""
Generated Code Metadata:
========================
Original URL: https://defidapp-protocol.web.app
Prompt: "Design a staking system for a Dapp using a synthetic protocol, including NFT staking and a bridge for interoperability, as per the Dapp protocol's features."
Generated: DETERMINISTIC_1d642471815c0d0b
Batch ID: 20250622_210108
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StakingSystem
 * @author [Your Name]
 * @notice A staking system for a Dapp using a synthetic protocol.
 */
contract StakingSystem is ReentrancyGuard {
    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of NFT staking information
    mapping(uint256 => NFTStakingInfo) public nftStakingInfos;

    // Mapping of synthetic token balances
    mapping(address => uint256) public syntheticTokenBalances;

    // Address of the NFT contract
    address public nftContract;

    // Address of the synthetic token contract
    address public syntheticTokenContract;

    // Address of the bridge contract
    address public bridgeContract;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when a user stakes an NFT
    event NFTStaked(address indexed user, uint256 indexed nftId);

    // Event emitted when a user unstakes an NFT
    event NFTUnstaked(address indexed user, uint256 indexed nftId);

    // Event emitted when a user stakes synthetic tokens
    event SyntheticTokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes synthetic tokens
    event SyntheticTokensUnstaked(address indexed user, uint256 amount);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _nftContract Address of the NFT contract
     * @param _syntheticTokenContract Address of the synthetic token contract
     * @param _bridgeContract Address of the bridge contract
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _nftContract,
        address _syntheticTokenContract,
        address _bridgeContract,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        nftContract = _nftContract;
        syntheticTokenContract = _syntheticTokenContract;
        bridgeContract = _bridgeContract;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @dev Stake an NFT
     * @param _nftId ID of the NFT to stake
     */
    function stakeNFT(uint256 _nftId) public nonReentrant {
        // Check if the NFT is owned by the user
        require(ERC721(nftContract).ownerOf(_nftId) == msg.sender, "NFT not owned by user");

        // Transfer the NFT to the staking system
        ERC721(nftContract).safeTransferFrom(msg.sender, address(this), _nftId);

        // Update the user's staking information
        userStakingInfos[msg.sender].stakedNFTs.push(_nftId);

        // Update the NFT staking information
        nftStakingInfos[_nftId].staker = msg.sender;
        nftStakingInfos[_nftId].stakedAt = block.timestamp;

        emit NFTStaked(msg.sender, _nftId);
    }

    /**
     * @dev Unstake an NFT
     * @param _nftId ID of the NFT to unstake
     */
    function unstakeNFT(uint256 _nftId) public nonReentrant {
        // Check if the NFT is staked by the user
        require(nftStakingInfos[_nftId].staker == msg.sender, "NFT not staked by user");

        // Check if the staking duration has passed
        require(block.timestamp - nftStakingInfos[_nftId].stakedAt >= stakingDuration, "Staking duration not passed");

        // Transfer the NFT back to the user
        ERC721(nftContract).safeTransferFrom(address(this), msg.sender, _nftId);

        // Update the user's staking information
        for (uint256 i = 0; i < userStakingInfos[msg.sender].stakedNFTs.length; i++) {
            if (userStakingInfos[msg.sender].stakedNFTs[i] == _nftId) {
                userStakingInfos[msg.sender].stakedNFTs[i] = userStakingInfos[msg.sender].stakedNFTs[userStakingInfos[msg.sender].stakedNFTs.length - 1];
                userStakingInfos[msg.sender].stakedNFTs.pop();
                break;
            }
        }

        // Update the NFT staking information
        delete nftStakingInfos[_nftId];

        emit NFTUnstaked(msg.sender, _nftId);
    }

    /**
     * @dev Stake synthetic tokens
     * @param _amount Amount of synthetic tokens to stake
     */
    function stakeSyntheticTokens(uint256 _amount) public nonReentrant {
        // Check if the user has sufficient synthetic tokens
        require(ERC20(syntheticTokenContract).balanceOf(msg.sender) >= _amount, "Insufficient synthetic tokens");

        // Transfer the synthetic tokens to the staking system
        ERC20(syntheticTokenContract).transferFrom(msg.sender, address(this), _amount);

        // Update the user's synthetic token balance
        syntheticTokenBalances[msg.sender] += _amount;

        // Update the user's staking information
        userStakingInfos[msg.sender].stakedSyntheticTokens += _amount;

        emit SyntheticTokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake synthetic tokens
     * @param _amount Amount of synthetic tokens to unstake
     */
    function unstakeSyntheticTokens(uint256 _amount) public nonReentrant {
        // Check if the user has sufficient staked synthetic tokens
        require(userStakingInfos[msg.sender].stakedSyntheticTokens >= _amount, "Insufficient staked synthetic tokens");

        // Check if the staking duration has passed
        require(block.timestamp - userStakingInfos[msg.sender].stakedAt >= stakingDuration, "Staking duration not passed");

        // Transfer the synthetic tokens back to the user
        ERC20(syntheticTokenContract).transfer(msg.sender, _amount);

        // Update the user's synthetic token balance
        syntheticTokenBalances[msg.sender] -= _amount;

        // Update the user's staking information
        userStakingInfos[msg.sender].stakedSyntheticTokens -= _amount;

        emit SyntheticTokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim reward
     */
    function claimReward() public nonReentrant {
        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer the reward to the user
        ERC20(syntheticTokenContract).transfer(msg.sender, reward);

        // Update the user's staking information
        userStakingInfos[msg.sender].lastClaimedAt = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward
     * @param _user Address of the user
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Calculate the staking duration
        uint256 stakingDuration = block.timestamp - userStakingInfos[_user].stakedAt;

        // Calculate the reward
        uint256 reward = stakingDuration * rewardPerSecond * userStakingInfos[_user].stakedSyntheticTokens;

        return reward;
    }

    /**
     * @dev Bridge synthetic tokens
     * @param _amount Amount of synthetic tokens to bridge
     * @param _destination Destination address
     */
    function bridgeSyntheticTokens(uint256 _amount, address _destination) public nonReentrant {
        // Check if the user has sufficient synthetic tokens
        require(syntheticTokenBalances[msg.sender] >= _amount, "Insufficient synthetic tokens");

        // Transfer the synthetic tokens to the bridge
        ERC20(syntheticTokenContract).transfer(bridgeContract, _amount);

        // Call the bridge contract to bridge the tokens
        Ibridge(bridgeContract).bridge(_amount, _destination);

        emit SyntheticTokensBridged(msg.sender, _amount, _destination);
    }
}

interface Ibridge {
    function bridge(uint256 _amount, address _destination) external;
}

struct UserStakingInfo {
    uint256[] stakedNFTs;
    uint256 stakedSyntheticTokens;
    uint256 stakedAt;
    uint256 lastClaimedAt;
}

struct NFTStakingInfo {
    address staker;
    uint256 stakedAt;
}
```

```solidity
// Bridge contract
contract Bridge {
    // Mapping of synthetic token balances
    mapping(address => uint256) public syntheticTokenBalances;

    // Address of the staking system contract
    address public stakingSystemContract;

    /**
     * @dev Constructor
     * @param _stakingSystemContract Address of the staking system contract
     */
    constructor(address _stakingSystemContract) public {
        stakingSystemContract = _stakingSystemContract;
    }

    /**
     * @dev Bridge synthetic tokens
     * @param _amount Amount of synthetic tokens to bridge
     * @param _destination Destination address
     */
    function bridge(uint256 _amount, address _destination
