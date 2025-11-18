"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gomining.cn
Prompt: Create a smart contract that integrates GoMining NFTs to automate Bitcoin reward distribution.
Generated: DETERMINISTIC_9840b3984cded75b
Batch ID: 20250612_154847
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

// Importing necessary OpenZeppelin contracts for ERC721 and Ownable functionality
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GoMiningNFTRewardDistributor
 * @dev A smart contract to automate Bitcoin reward distribution based on GoMining NFTs ownership.
 */
contract GoMiningNFTRewardDistributor is Ownable {
    using SafeMath for uint256;

    // Address of the GoMining NFT contract
    IERC721 public goMiningNFTContract;

    // Mapping to store the last claimed reward for each user
    mapping(address => uint256) public lastClaimed;

    // Total Bitcoin rewards allocated for distribution
    uint256 public totalRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to check if the caller has NFTs
    modifier onlyNFTHolder() {
        require(goMiningNFTContract.balanceOf(msg.sender) > 0, "Caller does not own GoMining NFT");
        _;
    }

    // Constructor to initialize the GoMining NFT contract
    constructor(address _goMiningNFTContract, uint256 _totalRewards) {
        require(_goMiningNFTContract != address(0), "Invalid NFT contract address");
        goMiningNFTContract = IERC721(_goMiningNFTContract);
        totalRewards = _totalRewards;
    }

    /**
     * @dev Allows the contract owner to withdraw excess funds (Bitcoin rewards).
     */
    function withdrawExcessFunds(uint256 amount) external onlyOwner {
        require(amount <= totalRewards, "Cannot withdraw more than total rewards");
        totalRewards = totalRewards.sub(amount);
        // Logic to actually transfer 'amount' in Bitcoin would go here
    }

    /**
     * @dev Distribute rewards to NFT holders based on the number of NFTs they own.
     */
    function distributeRewards() external onlyNFTHolder {
        uint256 nftCount = goMiningNFTContract.balanceOf(msg.sender);
        require(nftCount > 0, "You must hold at least one NFT to claim rewards");

        // Calculate the rewards for the user based on their NFT holdings
        uint256 rewardAmount = calculateReward(nftCount);
        require(rewardAmount > 0, "No rewards available for this user");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Update total rewards balance
        totalRewards = totalRewards.sub(rewardAmount);

        // Emit the rewards distribution event
        emit RewardsDistributed(msg.sender, rewardAmount);

        // Logic to transfer 'rewardAmount' in Bitcoin would go here
    }

    /**
     * @dev Calculate the reward amount based on the number of NFTs owned.
     * @param nftCount Number of NFTs owned by the user.
     * @return uint256 The calculated reward amount.
     */
    function calculateReward(uint256 nftCount) internal view returns (uint256) {
        // Example reward logic: 10 tokens per NFT
        return nftCount.mul(10);
    }
}
```
