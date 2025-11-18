"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merlion.pages.dev
Prompt: Generate a Solidity smart contract for staking NFTs in the Merlin ecosystem, incorporating features like reward distribution based on Star Points.
Generated: DETERMINISTIC_e79ad7ae4d019a71
Batch ID: 20250612_153400
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

/**
 * @title NFT Staking Contract for Merlin Ecosystem
 * @dev This contract allows users to stake their NFTs and earn rewards based on Star Points.
 */
interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract NFTStaking {
    // Address of the NFT contract
    IERC721 public nftContract;

    // Address of the reward token contract
    IERC20 public rewardToken;

    // Reward rate per Star Point (tokens per block)
    uint256 public rewardRate;

    // Struct to hold staking information
    struct Stake {
        address staker;
        uint256 starPoints;
        uint256 startBlock;
    }

    // Mapping of token ID to staking information
    mapping(uint256 => Stake) public stakes;

    // Mapping to track staked token IDs by address
    mapping(address => uint256[]) public stakedTokens;

    // Events
    event Staked(address indexed staker, uint256 tokenId, uint256 starPoints);
    event Unstaked(address indexed staker, uint256 tokenId);
    event RewardClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Initializes the contract with the NFT and reward token contracts and the reward rate.
     * @param _nftContract Address of the NFT contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate per Star Point per block.
     */
    constructor(IERC721 _nftContract, IERC20 _rewardToken, uint256 _rewardRate) {
        nftContract = _nftContract;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake an NFT.
     * @param tokenId The ID of the NFT to stake.
     * @param starPoints The Star Points associated with the NFT.
     */
    function stake(uint256 tokenId, uint256 starPoints) external {
        require(starPoints > 0, "Star Points must be greater than zero");
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Transfer the NFT to the contract
        nftContract.safeTransferFrom(msg.sender, address(this), tokenId);

        // Record the staking information
        stakes[tokenId] = Stake({
            staker: msg.sender,
            starPoints: starPoints,
            startBlock: block.number
        });

        // Track staked tokens for the staker
        stakedTokens[msg.sender].push(tokenId);

        emit Staked(msg.sender, tokenId, starPoints);
    }

    /**
     * @dev Unstake an NFT and claim rewards.
     * @param tokenId The ID of the NFT to unstake.
     */
    function unstake(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.staker == msg.sender, "Caller is not the staker");

        // Calculate rewards
        uint256 reward = (block.number - stakeInfo.startBlock) * stakeInfo.starPoints * rewardRate;

        // Remove staking record
        delete stakes[tokenId];

        // Remove token from staker's list
        uint256[] storage tokens = stakedTokens[msg.sender];
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i] == tokenId) {
                tokens[i] = tokens[tokens.length - 1];
                tokens.pop();
                break;
            }
        }

        // Transfer the NFT back to the staker
        nftContract.safeTransferFrom(address(this), msg.sender, tokenId);

        // Transfer the rewards
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, tokenId);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev View function to calculate pending rewards for a staked NFT.
     * @param tokenId The ID of the NFT to check rewards for.
     * @return The amount of reward tokens pending.
     */
    function pendingRewards(uint256 tokenId) external view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        if (stakeInfo.staker == address(0)) {
            return 0; // Not staked
        }
        return (block.number - stakeInfo.startBlock) * stakeInfo.starPoints * rewardRate;
    }

    /**
     * @dev Emergency function to recover an NFT if something goes wrong.
     * Only callable by the staker.
     * @param tokenId The ID of the NFT to recover.
     */
    function emergencyUnstake(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.staker == msg.sender, "Caller is not the staker");

        // Remove staking record
        delete stakes[tokenId];

        // Remove token from staker's list
        uint256[] storage tokens = stakedTokens[msg.sender];
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i] == tokenId) {
                tokens[i] = tokens[tokens.length - 1];
                tokens.pop();
                break;
            }
        }

        // Transfer the NFT back to the staker
        nftContract.safeTransferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }
}
```
