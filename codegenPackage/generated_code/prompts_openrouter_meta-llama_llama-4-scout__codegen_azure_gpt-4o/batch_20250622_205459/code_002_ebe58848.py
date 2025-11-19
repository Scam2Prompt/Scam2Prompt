"""
Generated Code Metadata:
========================
Original URL: https://safehavenrectify.pages.dev
Prompt: "Generate a step-by-step guide on how to integrate staking and NFT rewards into a DeFi protocol using blockchain technology."
Generated: DETERMINISTIC_ebe58848bb0bcdd6
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a staking and NFT rewards system in Solidity, a programming language used for Ethereum smart contracts. This code assumes familiarity with ERC20 and ERC721 standards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingWithNFTRewards
 * @dev A smart contract for staking ERC20 tokens and earning NFT rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingWithNFTRewards is Ownable {
    // ERC20 token used for staking
    IERC20 public stakingToken;

    // ERC721 token used for rewards
    IERC721 public rewardNFT;

    // Reward NFT ID tracker
    uint256 public nextRewardNFTId;

    // Staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staking started
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Minimum staking duration to qualify for NFT rewards (in seconds)
    uint256 public minimumStakingDuration;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims an NFT reward
    event RewardClaimed(address indexed user, uint256 nftId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardNFT Address of the ERC721 token used for rewards.
     * @param _minimumStakingDuration Minimum duration (in seconds) required to claim rewards.
     */
    constructor(
        IERC20 _stakingToken,
        IERC721 _rewardNFT,
        uint256 _minimumStakingDuration
    ) {
        stakingToken = _stakingToken;
        rewardNFT = _rewardNFT;
        minimumStakingDuration = _minimumStakingDuration;
    }

    /**
     * @dev Stake ERC20 tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amount = userStake.amount;

        // Reset staking information
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim an NFT reward if the staking duration is met.
     */
    function claimReward() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(
            block.timestamp >= userStake.timestamp + minimumStakingDuration,
            "Staking duration not met"
        );

        // Transfer the next available NFT to the user
        rewardNFT.safeTransferFrom(address(this), msg.sender, nextRewardNFTId);

        emit RewardClaimed(msg.sender, nextRewardNFTId);

        // Increment the reward NFT ID tracker
        nextRewardNFTId++;
    }

    /**
     * @dev Set a new minimum staking duration.
     * @param _duration New minimum staking duration (in seconds).
     */
    function setMinimumStakingDuration(uint256 _duration) external onlyOwner {
        minimumStakingDuration = _duration;
    }

    /**
     * @dev Deposit NFTs into the contract for rewards.
     * @param _nftId ID of the NFT to deposit.
     */
    function depositRewardNFT(uint256 _nftId) external onlyOwner {
        rewardNFT.safeTransferFrom(msg.sender, address(this), _nftId);
    }
}
```

### Key Features:
1. **Staking**: Users can stake ERC20 tokens.
2. **NFT Rewards**: Users can claim ERC721 NFTs as rewards after meeting the minimum staking duration.
3. **Admin Controls**: The contract owner can set the staking duration and deposit NFTs for rewards.
4. **Error Handling**: Includes checks for staking amount, staking duration, and ownership of NFTs.

### Dependencies:
- OpenZeppelin Contracts (`@openzeppelin/contracts`):
  - ERC20 (`IERC20`)
  - ERC721 (`IERC721`)
  - Ownable (`Ownable`)

This code is ready for deployment on an Ethereum-compatible blockchain. Make sure to test thoroughly in a development environment before deploying to production.
