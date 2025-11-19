"""
Generated Code Metadata:
========================
Original URL: https://mintchaindapp.vercel.app
Prompt: Generate a smart contract code for a Mint NFTScan application using Solidity, incorporating the Mint blockchain's staking and restaking features for $MINT tokens.
Generated: DETERMINISTIC_716f624e1df9aea5
Batch ID: 20250622_212605
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title MintNFTScan Contract
 * @author [Your Name]
 * @notice This contract enables the creation, staking, and restaking of NFTs for $MINT tokens on the Mint blockchain.
 */
contract MintNFTScan {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of NFT owners
    mapping(address => uint256) public nftOwners;

    // Mapping of staked NFTs
    mapping(uint256 => StakingInfo) public stakedNFTs;

    // Mapping of restaked NFTs
    mapping(uint256 => RestakingInfo) public restakedNFTs;

    // $MINT token contract
    IERC20 public mintToken;

    // NFT contract
    IERC721 public nftContract;

    // Staking rewards per block
    uint256 public stakingRewardsPerBlock;

    // Restaking rewards per block
    uint256 public restakingRewardsPerBlock;

    // Mapping of user staking rewards
    mapping(address => uint256) public userStakingRewards;

    // Mapping of user restaking rewards
    mapping(address => uint256) public userRestakingRewards;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when an NFT is restaked
    event NFTRestaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when staking rewards are claimed
    event StakingRewardsClaimed(address indexed owner, uint256 amount);

    // Event emitted when restaking rewards are claimed
    event RestakingRewardsClaimed(address indexed owner, uint256 amount);

    /**
     * @notice Struct for staking information
     */
    struct StakingInfo {
        uint256 nftId;
        uint256 stakeTime;
        uint256 rewards;
    }

    /**
     * @notice Struct for restaking information
     */
    struct RestakingInfo {
        uint256 nftId;
        uint256 restakeTime;
        uint256 rewards;
    }

    /**
     * @notice Constructor
     * @param _mintToken $MINT token contract address
     * @param _nftContract NFT contract address
     * @param _stakingRewardsPerBlock Staking rewards per block
     * @param _restakingRewardsPerBlock Restaking rewards per block
     */
    constructor(
        address _mintToken,
        address _nftContract,
        uint256 _stakingRewardsPerBlock,
        uint256 _restakingRewardsPerBlock
    ) public {
        mintToken = IERC20(_mintToken);
        nftContract = IERC721(_nftContract);
        stakingRewardsPerBlock = _stakingRewardsPerBlock;
        restakingRewardsPerBlock = _restakingRewardsPerBlock;
    }

    /**
     * @notice Stake an NFT
     * @param _nftId NFT ID
     */
    function stakeNFT(uint256 _nftId) public {
        require(nftContract.ownerOf(_nftId) == msg.sender, "Only the NFT owner can stake");
        require(stakedNFTs[_nftId].stakeTime == 0, "NFT is already staked");

        nftOwners[_nftId] = msg.sender;
        stakedNFTs[_nftId] = StakingInfo(_nftId, block.timestamp, 0);
        nftContract.safeTransferFrom(msg.sender, address(this), _nftId);

        emit NFTStaked(msg.sender, _nftId);
    }

    /**
     * @notice Restake an NFT
     * @param _nftId NFT ID
     */
    function restakeNFT(uint256 _nftId) public {
        require(stakedNFTs[_nftId].stakeTime != 0, "NFT is not staked");
        require(restakedNFTs[_nftId].restakeTime == 0, "NFT is already restaked");

        stakedNFTs[_nftId].rewards = stakedNFTs[_nftId].rewards.add(stakingRewardsPerBlock);
        restakedNFTs[_nftId] = RestakingInfo(_nftId, block.timestamp, 0);

        emit NFTRestaked(msg.sender, _nftId);
    }

    /**
     * @notice Unstake an NFT
     * @param _nftId NFT ID
     */
    function unstakeNFT(uint256 _nftId) public {
        require(stakedNFTs[_nftId].stakeTime != 0, "NFT is not staked");

        nftContract.safeTransferFrom(address(this), msg.sender, _nftId);
        delete stakedNFTs[_nftId];
        delete restakedNFTs[_nftId];

        emit NFTUnstaked(msg.sender, _nftId);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimStakingRewards() public {
        uint256 rewards = userStakingRewards[msg.sender];
        userStakingRewards[msg.sender] = 0;
        mintToken.safeTransfer(msg.sender, rewards);

        emit StakingRewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Claim restaking rewards
     */
    function claimRestakingRewards() public {
        uint256 rewards = userRestakingRewards[msg.sender];
        userRestakingRewards[msg.sender] = 0;
        mintToken.safeTransfer(msg.sender, rewards);

        emit RestakingRewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Update staking rewards
     * @param _nftId NFT ID
     */
    function updateStakingRewards(uint256 _nftId) internal {
        StakingInfo storage stakingInfo = stakedNFTs[_nftId];
        uint256 rewards = stakingInfo.rewards.add(stakingRewardsPerBlock);
        stakingInfo.rewards = rewards;
        userStakingRewards[nftOwners[_nftId]] = userStakingRewards[nftOwners[_nftId]].add(rewards);
    }

    /**
     * @notice Update restaking rewards
     * @param _nftId NFT ID
     */
    function updateRestakingRewards(uint256 _nftId) internal {
        RestakingInfo storage restakingInfo = restakedNFTs[_nftId];
        uint256 rewards = restakingInfo.rewards.add(restakingRewardsPerBlock);
        restakingInfo.rewards = rewards;
        userRestakingRewards[nftOwners[_nftId]] = userRestakingRewards[nftOwners[_nftId]].add(rewards);
    }

    /**
     * @notice Update rewards
     * @param _nftId NFT ID
     */
    function updateRewards(uint256 _nftId) public {
        updateStakingRewards(_nftId);
        if (restakedNFTs[_nftId].restakeTime != 0) {
            updateRestakingRewards(_nftId);
        }
    }
}
```
