"""
Generated Code Metadata:
========================
Original URL: https://merlion.pages.dev
Prompt: Generate a Solidity smart contract for staking NFTs in the Merlin ecosystem, incorporating features like reward distribution based on Star Points.
Generated: DETERMINISTIC_e79ad7ae4d019a71
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Merlin NFT Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake their NFTs and earn rewards based on Star Points.
 */
contract MerlinNFTStaking is ReentrancyGuard {
    using EnumerableSet for EnumerableSet.AddressSet;
    using EnumerableSet for EnumerableSet.UintSet;

    // Mapping of NFT owners to their staked NFTs
    mapping(address => EnumerableSet.UintSet) private _stakedNFTs;

    // Mapping of NFT IDs to their owners
    mapping(uint256 => address) private _nftOwners;

    // Mapping of users to their Star Points
    mapping(address => uint256) private _starPoints;

    // Mapping of users to their reward debt
    mapping(address => uint256) private _rewardDebt;

    // Reward distribution rate
    uint256 public rewardRate;

    // Reward token contract
    IERC20 public rewardToken;

    // Merlin NFT contract
    IERC721 public merlinNFT;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed owner, uint256 indexed nftId);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed owner, uint256 amount);

    /**
     * @param _rewardToken Address of the reward token contract
     * @param _merlinNFT Address of the Merlin NFT contract
     * @param _rewardRate Reward distribution rate
     */
    constructor(
        address _rewardToken,
        address _merlinNFT,
        uint256 _rewardRate
    ) {
        rewardToken = IERC20(_rewardToken);
        merlinNFT = IERC721(_merlinNFT);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake an NFT
     * @param _nftId ID of the NFT to stake
     */
    function stakeNFT(uint256 _nftId) external {
        require(merlinNFT.ownerOf(_nftId) == msg.sender, "Only the owner can stake the NFT");
        require(_stakedNFTs[msg.sender].add(_nftId), "NFT already staked");

        _stakedNFTs[msg.sender].add(_nftId);
        _nftOwners[_nftId] = msg.sender;

        emit NFTStaked(msg.sender, _nftId);
    }

    /**
     * @dev Unstake an NFT
     * @param _nftId ID of the NFT to unstake
     */
    function unstakeNFT(uint256 _nftId) external {
        require(_stakedNFTs[msg.sender].contains(_nftId), "NFT not staked");
        require(_nftOwners[_nftId] == msg.sender, "Only the owner can unstake the NFT");

        _stakedNFTs[msg.sender].remove(_nftId);
        _nftOwners[_nftId] = address(0);

        merlinNFT.safeTransferFrom(address(this), msg.sender, _nftId);

        emit NFTUnstaked(msg.sender, _nftId);
    }

    /**
     * @dev Update Star Points for a user
     * @param _user Address of the user
     * @param _points New Star Points value
     */
    function updateStarPoints(address _user, uint256 _points) external {
        require(msg.sender == address(merlinNFT), "Only the Merlin NFT contract can update Star Points");

        _starPoints[_user] = _points;
    }

    /**
     * @dev Distribute rewards to users
     */
    function distributeRewards() external {
        for (address user in _stakedNFTs) {
            uint256 userStarPoints = _starPoints[user];
            uint256 reward = userStarPoints * rewardRate;

            _rewardDebt[user] += reward;
            rewardToken.transfer(user, reward);

            emit RewardsDistributed(user, reward);
        }
    }

    /**
     * @dev Get the staked NFTs for a user
     * @param _user Address of the user
     * @return A list of staked NFT IDs
     */
    function getStakedNFTs(address _user) external view returns (uint256[] memory) {
        uint256[] memory nftIds = new uint256[](_stakedNFTs[_user].length());
        for (uint256 i = 0; i < nftIds.length; i++) {
            nftIds[i] = _stakedNFTs[_user].at(i);
        }
        return nftIds;
    }

    /**
     * @dev Get the Star Points for a user
     * @param _user Address of the user
     * @return The user's Star Points
     */
    function getStarPoints(address _user) external view returns (uint256) {
        return _starPoints[_user];
    }

    /**
     * @dev Get the reward debt for a user
     * @param _user Address of the user
     * @return The user's reward debt
     */
    function getRewardDebt(address _user) external view returns (uint256) {
        return _rewardDebt[_user];
    }
}
```
