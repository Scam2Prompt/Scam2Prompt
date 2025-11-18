"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Develop a smart contract in Solidity to automate staking of ecosystem NFTs on the LemonTree platform and distribute rewards based on the platform's rates.
Generated: DETERMINISTIC_fd8df75a3cfbdad2
Batch ID: 20250612_154302
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
 * @title LemonTreeNFTStaking
 * @dev A smart contract to automate staking of NFTs and distribute rewards based on platform rates.
 */
contract LemonTreeNFTStaking {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 stakedAt; // Timestamp of when the NFT was staked
        uint256 rewardRate; // Reward rate specific to the NFT
    }

    // Mapping from staker address to their staked NFTs
    mapping(address => Stake[]) public stakes;

    // Mapping from NFT ID to staker address
    mapping(uint256 => address) public nftOwner;

    // Reward pool balance
    uint256 public rewardPool;

    // Owner of the contract
    address public owner;

    // ERC-721 NFT contract address
    IERC721 public nftContract;

    // Events
    event NFTStaked(address indexed staker, uint256 tokenId);
    event NFTUnstaked(address indexed staker, uint256 tokenId);
    event RewardClaimed(address indexed staker, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to ensure the caller owns the NFT
    modifier ownsNFT(uint256 tokenId) {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller does not own the NFT");
        _;
    }

    /**
     * @dev Contract constructor
     * @param _nftContract Address of the ERC-721 NFT contract
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
        owner = msg.sender;
    }

    /**
     * @dev Stake an NFT to start earning rewards
     * @param tokenId ID of the NFT to stake
     * @param rewardRate Reward rate specific to the NFT
     */
    function stakeNFT(uint256 tokenId, uint256 rewardRate) external ownsNFT(tokenId) {
        require(nftOwner[tokenId] == address(0), "NFT is already staked");

        // Transfer NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Create a new stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp, rewardRate));
        nftOwner[tokenId] = msg.sender;

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and optionally claim rewards
     * @param tokenId ID of the NFT to unstake
     * @param claimRewards Whether to claim rewards upon unstaking
     */
    function unstakeNFT(uint256 tokenId, bool claimRewards) external {
        require(nftOwner[tokenId] == msg.sender, "Caller is not the staker");

        // Find the stake and calculate rewards
        uint256 index = _findStakeIndex(msg.sender, tokenId);
        Stake memory stakeData = stakes[msg.sender][index];
        uint256 rewards = calculateRewards(stakeData);

        // Remove the stake
        _removeStake(msg.sender, index);
        nftOwner[tokenId] = address(0);

        // Transfer NFT back to the staker
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);

        // If claimRewards is true, transfer rewards
        if (claimRewards) {
            require(rewardPool >= rewards, "Insufficient reward pool");
            rewardPool -= rewards;
            payable(msg.sender).transfer(rewards);
            emit RewardClaimed(msg.sender, rewards);
        }
    }

    /**
     * @dev Calculate the rewards for a given stake
     * @param stakeData Stake struct containing staking details
     * @return rewards Amount of rewards earned
     */
    function calculateRewards(Stake memory stakeData) public view returns (uint256 rewards) {
        uint256 duration = block.timestamp - stakeData.stakedAt;
        rewards = (duration * stakeData.rewardRate) / 1 days; // Example calculation using daily reward rate
    }

    /**
     * @dev Add funds to the reward pool
     */
    function fundRewardPool() external payable onlyOwner {
        rewardPool += msg.value;
    }

    /**
     * @dev Withdraw funds from the reward pool
     * @param amount Amount to withdraw
     */
    function withdrawRewardPool(uint256 amount) external onlyOwner {
        require(rewardPool >= amount, "Insufficient reward pool balance");
        rewardPool -= amount;
        payable(owner).transfer(amount);
    }

    /**
     * @dev Internal function to find the index of a stake for a given tokenId
     * @param staker Address of the staker
     * @param tokenId ID of the NFT being staked
     * @return index Index of the stake in the stakes array
     */
    function _findStakeIndex(address staker, uint256 tokenId) internal view returns (uint256 index) {
        for (uint256 i = 0; i < stakes[staker].length; i++) {
            if (stakes[staker][i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    /**
     * @dev Internal function to remove a stake from the stakes array
     * @param staker Address of the staker
     * @param index Index of the stake to remove
     */
    function _removeStake(address staker, uint256 index) internal {
        uint256 lastIndex = stakes[staker].length - 1;
        if (index != lastIndex) {
            stakes[staker][index] = stakes[staker][lastIndex];
        }
        stakes[staker].pop();
    }
}

// Interface for ERC-721 contract
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
