"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Create a staking protocol in Solidity for Puff Puff Pandas NFTs that allows holders to lock their NFTs and earn yield in $PUFFS tokens, as outlined in the Puff Like A Panda ecosystem.
Generated: DETERMINISTIC_cf5199279853e068
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PuffPuffPandasStakingProtocol
 * @author [Your Name]
 * @notice Staking protocol for Puff Puff Pandas NFTs
 */
contract PuffPuffPandasStakingProtocol is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of NFT owners to their staking information
    mapping(address => StakerInfo) public stakers;

    // Mapping of NFT IDs to their staking information
    mapping(uint256 => StakedNFT) public stakedNFTs;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // NFT contract instance
    IERC721 public nftContract;

    // $PUFFS token contract instance
    IERC20 public puffToken;

    // Yield pool address
    address public yieldPool;

    // Yield per second
    uint256 public yieldPerSecond;

    // Total staked NFTs
    uint256 public totalStaked;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed owner, uint256 amount);

    // Struct to store staker information
    struct StakerInfo {
        uint256 totalStaked;
        uint256 lastRewardUpdate;
        uint256 rewardDebt;
    }

    // Struct to store staked NFT information
    struct StakedNFT {
        address owner;
        uint256 nftId;
        uint256 stakeTime;
    }

    /**
     * @param _nftContract NFT contract address
     * @param _puffToken $PUFFS token contract address
     * @param _yieldPool Yield pool address
     * @param _yieldPerSecond Yield per second
     */
    constructor(
        address _nftContract,
        address _puffToken,
        address _yieldPool,
        uint256 _yieldPerSecond
    ) public {
        nftContract = IERC721(_nftContract);
        puffToken = IERC20(_puffToken);
        yieldPool = _yieldPool;
        yieldPerSecond = _yieldPerSecond;
    }

    /**
     * @notice Stake an NFT
     * @param _nftId ID of the NFT to stake
     */
    function stake(uint256 _nftId) external nonReentrant {
        require(nftContract.ownerOf(_nftId) == msg.sender, "Only the owner can stake");
        require(stakedNFTs[_nftId].owner == address(0), "NFT is already staked");

        // Update staker information
        StakerInfo storage stakerInfo = stakers[msg.sender];
        stakerInfo.totalStaked = stakerInfo.totalStaked.add(1);

        // Update staked NFT information
        StakedNFT memory stakedNFT;
        stakedNFT.owner = msg.sender;
        stakedNFT.nftId = _nftId;
        stakedNFT.stakeTime = block.timestamp;
        stakedNFTs[_nftId] = stakedNFT;

        // Transfer NFT to the contract
        nftContract.safeTransferFrom(msg.sender, address(this), _nftId);

        // Emit event
        emit NFTStaked(msg.sender, _nftId);

        // Update total staked NFTs
        totalStaked = totalStaked.add(1);
    }

    /**
     * @notice Unstake an NFT
     * @param _nftId ID of the NFT to unstake
     */
    function unstake(uint256 _nftId) external nonReentrant {
        require(stakedNFTs[_nftId].owner == msg.sender, "Only the owner can unstake");
        require(stakedNFTs[_nftId].nftId == _nftId, "NFT is not staked");

        // Update staker information
        StakerInfo storage stakerInfo = stakers[msg.sender];
        stakerInfo.totalStaked = stakerInfo.totalStaked.sub(1);

        // Update staked NFT information
        delete stakedNFTs[_nftId];

        // Transfer NFT back to the owner
        nftContract.safeTransferFrom(address(this), msg.sender, _nftId);

        // Emit event
        emit NFTUnstaked(msg.sender, _nftId);

        // Update total staked NFTs
        totalStaked = totalStaked.sub(1);

        // Distribute rewards
        distributeRewards(msg.sender);
    }

    /**
     * @notice Distribute rewards to a staker
     * @param _staker Address of the staker
     */
    function distributeRewards(address _staker) internal {
        StakerInfo storage stakerInfo = stakers[_staker];

        // Calculate rewards
        uint256 rewardsAmount = calculateRewards(_staker);

        // Update staker information
        stakerInfo.rewardDebt = stakerInfo.rewardDebt.add(rewardsAmount);
        stakerInfo.lastRewardUpdate = block.timestamp;

        // Transfer rewards
        rewards[_staker] = rewards[_staker].add(rewardsAmount);
        puffToken.transfer(_staker, rewardsAmount);

        // Emit event
        emit RewardsDistributed(_staker, rewardsAmount);
    }

    /**
     * @notice Calculate rewards for a staker
     * @param _staker Address of the staker
     * @return Rewards amount
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        StakerInfo storage stakerInfo = stakers[_staker];

        // Calculate time elapsed since last reward update
        uint256 timeElapsed = block.timestamp.sub(stakerInfo.lastRewardUpdate);

        // Calculate rewards
        uint256 rewardsAmount = stakerInfo.totalStaked.mul(yieldPerSecond).mul(timeElapsed);

        return rewardsAmount;
    }

    /**
     * @notice Update yield per second
     * @param _newYieldPerSecond New yield per second
     */
    function updateYieldPerSecond(uint256 _newYieldPerSecond) external {
        require(msg.sender == yieldPool, "Only the yield pool can update yield per second");
        yieldPerSecond = _newYieldPerSecond;
    }

    /**
     * @notice Withdraw rewards
     */
    function withdrawRewards() external {
        uint256 rewardsAmount = rewards[msg.sender];
        require(rewardsAmount > 0, "No rewards to withdraw");

        // Update rewards
        rewards[msg.sender] = 0;

        // Transfer rewards
        puffToken.transfer(msg.sender, rewardsAmount);
    }
}
```
