"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yooshi-io.pages.dev
Prompt: Write a Solidity contract for an NFT farming system inspired by YooShi's model, where transaction fees are injected into the farming pool and profits are distributed based on NFT rarity.
Generated: DETERMINISTIC_49c1df6820bafe52
Batch ID: 20250612_152527
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTFarm is Ownable {
    using SafeMath for uint256;

    // Struct to represent an NFT with its rarity score
    struct NFT {
        uint256 rarity;
        address owner;
        bool isStaked;
    }

    // Mapping from NFT tokenId to its details
    mapping(uint256 => NFT) public nftDetails;

    // The token that will be used for farming rewards
    IERC20 public rewardToken;

    // Total amount of rewards available for farming
    uint256 public totalRewards;

    // Event that is emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed tokenId, uint256 rarity);
    
    // Event that is emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards);

    // Constructor to initialize the contract with the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Stake an NFT for farming.
     * @param tokenId The ID of the NFT to stake.
     * @param rarity The rarity score of the NFT.
     */
    function stakeNFT(uint256 tokenId, uint256 rarity) external {
        require(nftDetails[tokenId].owner == address(0), "NFT is already staked");
        
        // Create a new NFT entry
        nftDetails[tokenId] = NFT({
            rarity: rarity,
            owner: msg.sender,
            isStaked: true
        });

        emit NFTStaked(msg.sender, tokenId, rarity);
    }

    /**
     * @dev Unstake an NFT, and distribute rewards.
     * @param tokenId The ID of the NFT to unstake.
     */
    function unstakeNFT(uint256 tokenId) external {
        NFT storage nft = nftDetails[tokenId];
        require(nft.owner == msg.sender, "You do not own this NFT");
        require(nft.isStaked, "NFT is not staked");

        // Calculate rewards based on rarity
        uint256 reward = calculateRewards(nft.rarity);
        totalRewards = totalRewards.sub(reward);

        // Transfer rewards to the owner
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Mark the NFT as unstaked
        nft.isStaked = false;
        nft.owner = address(0);

        emit RewardsDistributed(reward);
    }

    /**
     * @dev Allows the owner to inject fees into the farming pool.
     * @param amount The amount of rewards to add.
     */
    function injectRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalRewards = totalRewards.add(amount);
    }

    /**
     * @dev Calculate rewards based on NFT rarity.
     * @param rarity The rarity score of the NFT.
     * @return The calculated reward amount.
     */
    function calculateRewards(uint256 rarity) internal view returns (uint256) {
        // Simple reward calculation based on rarity
        return rarity.mul(10 ** 18); // Customize reward multiplier as needed
    }

    /**
     * @dev Get the current balance of rewards available for distribution.
     * @return The total rewards balance.
     */
    function getRewardBalance() external view returns (uint256) {
        return totalRewards;
    }
}
```
