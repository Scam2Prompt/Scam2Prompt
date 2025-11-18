"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Develop a Solidity smart contract snippet to integrate a staking mechanism for PEPE WIF HAT NFTs, allowing holders to earn $PIF and other tokens as rewards.
Generated: DETERMINISTIC_abd79c158810bde0
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    // Address of the NFT contract
    IERC721 public pepeWifHatNFT;

    // Address of the reward token contract ($PIF)
    IERC20 public rewardToken;

    // Struct to hold staking details for each user
    struct Stake {
        uint256[] tokenIds; // List of staked token IDs
        uint256 rewardDebt; // Reward debt of the user
    }

    // Mapping to track stakes per user
    mapping(address => Stake) public stakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per token staked (this would be calculated based on your reward logic)
    uint256 public rewardPerToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256[] tokenIds);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256[] tokenIds);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC721 _pepeWifHatNFT, IERC20 _rewardToken) {
        pepeWifHatNFT = _pepeWifHatNFT;
        rewardToken = _rewardToken;
    }

    // Function to stake NFTs
    function stake(uint256[] calldata tokenIds) external nonReentrant {
        require(tokenIds.length > 0, "No tokens to stake");

        // Transfer the NFTs to the contract
        for (uint256 i = 0; i < tokenIds.length; i++) {
            pepeWifHatNFT.transferFrom(msg.sender, address(this), tokenIds[i]);
        }

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.tokenIds = tokenIds;
        totalStaked += tokenIds.length;

        emit Staked(msg.sender, tokenIds);
    }

    // Function to unstake NFTs
    function unstake(uint256[] calldata tokenIds) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.tokenIds.length > 0, "No tokens staked");

        // Transfer the NFTs back to the user
        for (uint256 i = 0; i < tokenIds.length; i++) {
            require(
                _existsInStake(userStake.tokenIds, tokenIds[i]),
                "Token not staked"
            );
            pepeWifHatNFT.transferFrom(address(this), msg.sender, tokenIds[i]);
        }

        // Remove tokens from user's stake
        userStake.tokenIds = _removeFromArray(userStake.tokenIds, tokenIds);

        totalStaked -= tokenIds.length;

        emit Unstaked(msg.sender, tokenIds);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.tokenIds.length > 0, "No tokens staked");

        uint256 reward = (userStake.tokenIds.length * rewardPerToken) - userStake.rewardDebt;
        require(reward > 0, "No rewards available");

        // Update the reward debt
        userStake.rewardDebt += reward;

        // Transfer rewards to the user
        bool success = rewardToken.transfer(msg.sender, reward);
        require(success, "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to check if a token exists in an array
    function _existsInStake(uint256[] memory array, uint256 tokenId) internal pure returns (bool) {
        for (uint256 i = 0; i < array.length; i++) {
            if (array[i] == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Internal function to remove tokens from user's stake array
    function _removeFromArray(uint256[] storage array, uint256[] calldata tokenIds) internal returns (uint256[] memory) {
        for (uint256 i = 0; i < tokenIds.length; i++) {
            for (uint256 j = 0; j < array.length; j++) {
                if (array[j] == tokenIds[i]) {
                    array[j] = array[array.length - 1]; // Replace it with the last element
                    array.pop(); // Remove the last element
                    break;
                }
            }
        }
        return array;
    }

    // Admin function to set reward per token rate
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        rewardPerToken = _rewardPerToken;
    }
}
```
