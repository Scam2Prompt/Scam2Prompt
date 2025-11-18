"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Create a Solidity smart contract for staking NFTs in the ParaX platform's NFT Staking Pool, ensuring compatibility with ERC-721 tokens and integration with Chainlink price feeds.
Generated: DETERMINISTIC_b7a901f4fc3a8edb
Batch ID: 20250612_145619
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

// Import OpenZeppelin's libraries for ERC-721 handling and SafeMath
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Import Chainlink's Aggregator interface for price feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title ParaX NFT Staking Pool
 * @dev A smart contract to allow users to stake their ERC-721 NFTs and earn rewards based on Chainlink price feeds.
 */
contract ParaXNFTStakingPool is ERC721Holder, Ownable {
    using SafeMath for uint256;

    struct StakeInfo {
        address owner;
        uint256 stakedAt; // Timestamp of when the NFT was staked
        uint256 rewardClaimed; // Tracks rewards already claimed
    }

    // Mapping of NFT contract address => Token ID => StakeInfo
    mapping(address => mapping(uint256 => StakeInfo)) public stakes;

    // Chainlink price feed oracle
    AggregatorV3Interface private priceFeed;

    // Reward rate (e.g., 1 reward token per day per 100 USD of NFT price)
    uint256 public rewardRatePer100USDPerDay = 1e18; // Reward rate in wei

    // Events
    event NFTStaked(address indexed staker, address indexed nftAddress, uint256 indexed tokenId, uint256 timestamp);
    event NFTUnstaked(address indexed staker, address indexed nftAddress, uint256 indexed tokenId, uint256 timestamp);
    event RewardClaimed(address indexed staker, uint256 rewardAmount, uint256 timestamp);

    /**
     * @dev Constructor to set the Chainlink price feed oracle.
     * @param _priceFeed Address of the Chainlink price feed contract.
     */
    constructor(address _priceFeed) {
        require(_priceFeed != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    /**
     * @dev Allows a user to stake their NFT.
     * @param nftAddress Address of the ERC-721 contract.
     * @param tokenId ID of the token to stake.
     */
    function stakeNFT(address nftAddress, uint256 tokenId) external {
        require(nftAddress != address(0), "Invalid NFT address");
        require(IERC721(nftAddress).ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer the NFT to the contract
        IERC721(nftAddress).safeTransferFrom(msg.sender, address(this), tokenId);

        // Record the staking information
        stakes[nftAddress][tokenId] = StakeInfo({
            owner: msg.sender,
            stakedAt: block.timestamp,
            rewardClaimed: 0
        });

        emit NFTStaked(msg.sender, nftAddress, tokenId, block.timestamp);
    }

    /**
     * @dev Allows a user to unstake their NFT.
     * @param nftAddress Address of the ERC-721 contract.
     * @param tokenId ID of the token to unstake.
     */
    function unstakeNFT(address nftAddress, uint256 tokenId) external {
        StakeInfo memory stake = stakes[nftAddress][tokenId];
        require(stake.owner == msg.sender, "You are not the owner of this staked NFT");

        // Claim any pending rewards before unstaking
        claimRewards(nftAddress, tokenId);

        // Remove staking information
        delete stakes[nftAddress][tokenId];

        // Transfer the NFT back to the owner
        IERC721(nftAddress).safeTransferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, nftAddress, tokenId, block.timestamp);
    }

    /**
     * @dev Allows a user to claim rewards for a staked NFT.
     * @param nftAddress Address of the ERC-721 contract.
     * @param tokenId ID of the staked token.
     */
    function claimRewards(address nftAddress, uint256 tokenId) public {
        StakeInfo storage stake = stakes[nftAddress][tokenId];
        require(stake.owner == msg.sender, "You are not the owner of this staked NFT");

        uint256 reward = calculateRewards(nftAddress, tokenId);
        require(reward > 0, "No rewards available");

        // Update the rewardClaimed to prevent double-claiming
        stake.rewardClaimed = stake.rewardClaimed.add(reward);

        // Transfer the reward to the user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward, block.timestamp);
    }

    /**
     * @dev Calculates the rewards for a staked NFT.
     * @param nftAddress Address of the ERC-721 contract.
     * @param tokenId ID of the staked token.
     * @return reward The amount of rewards the user is entitled to claim.
     */
    function calculateRewards(address nftAddress, uint256 tokenId) public view returns (uint256 reward) {
        StakeInfo memory stake = stakes[nftAddress][tokenId];
        if (stake.stakedAt == 0) return 0;

        // Get the current price of the NFT from Chainlink
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price feed data");

        uint256 stakingDuration = block.timestamp.sub(stake.stakedAt); // Staking duration in seconds
        uint256 stakingDurationInDays = stakingDuration.div(1 days); // Convert to days

        // Calculate reward based on price and duration
        reward = uint256(price).mul(stakingDurationInDays).mul(rewardRatePer100USDPerDay).div(1e8).div(100); // Chainlink price is in 8 decimals
        reward = reward.sub(stake.rewardClaimed); // Subtract already claimed rewards
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRate New reward rate per 100 USD per day.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRatePer100USDPerDay = _newRate;
    }

    /**
     * @dev Fallback function to receive Ether (for rewards distribution).
     */
    receive() external payable {}
}
```
