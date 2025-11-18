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

/**
 * @title PEPE WIF HAT NFT Staking Contract
 * @notice This contract allows users to stake their PEPE WIF HAT NFTs to earn $PIF and other token rewards.
 * @dev This contract assumes the existence of ERC721 and ERC20 token standards.
 */
contract PEPEWIFHATStaking {
    // Struct to store staking information for a user
    struct Stake {
        uint256 tokenId;  // Token ID of the staked NFT
        uint256 stakedAt; // Timestamp when the NFT was staked
    }

    // ERC721 NFT contract address
    address public nftContract;

    // ERC20 reward token address ($PIF)
    address public rewardToken;

    // Reward rate ($PIF) per NFT per second (e.g., 1 token every second)
    uint256 public rewardRate;

    // Token holder's stakes
    mapping(address => Stake[]) public stakes;

    // Tracks rewards accrued for each staker
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 indexed tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Initializes the contract with NFT and ERC20 token addresses and reward rate.
     * @param _nftContract Address of the ERC721 NFT contract.
     * @param _rewardToken Address of the ERC20 reward token contract.
     * @param _rewardRate Reward rate per NFT per second.
     */
    constructor(address _nftContract, address _rewardToken, uint256 _rewardRate) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        nftContract = _nftContract;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake a PEPE WIF HAT NFT to start earning rewards.
     * @param tokenId The ID of the NFT to be staked.
     */
    function stake(uint256 tokenId) external {
        // Transfer the NFT from the user to the contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Record the staking information
        stakes[msg.sender].push(Stake({tokenId: tokenId, stakedAt: block.timestamp}));

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @notice Unstake a PEPE WIF HAT NFT and claim rewards.
     * @param tokenId The ID of the NFT to be unstaked.
     */
    function unstake(uint256 tokenId) external {
        uint256 index = findStakeIndex(msg.sender, tokenId);
        require(index < stakes[msg.sender].length, "NFT not staked");

        // Calculate pending rewards
        uint256 accruedRewards = calculateRewards(msg.sender, stakes[msg.sender][index].stakedAt);

        // Update rewards mapping
        rewards[msg.sender] += accruedRewards;

        // Remove the stake from the user's stakes
        removeStake(msg.sender, index);

        // Transfer the NFT back to the user
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @notice Claim all accrued rewards in $PIF tokens.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset rewards balance
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        IERC20(rewardToken).transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculates pending rewards for a staked NFT based on the staked time.
     * @param user Address of the staker.
     * @param stakedAt Timestamp when the NFT was staked.
     * @return rewards Amount of pending rewards.
     */
    function calculateRewards(address user, uint256 stakedAt) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakedAt;
        return stakingDuration * rewardRate;
    }

    /**
     * @dev Finds the index of a staked NFT for a particular user.
     * @param user Address of the staker.
     * @param tokenId ID of the staked NFT.
     * @return index Index of the stake in the user's stakes array.
     */
    function findStakeIndex(address user, uint256 tokenId) internal view returns (uint256) {
        Stake[] storage userStakes = stakes[user];
        for (uint256 i = 0; i < userStakes.length; i++) {
            if (userStakes[i].tokenId == tokenId) {
                return i;
            }
        }
        revert("NFT not found in stakes");
    }

    /**
     * @dev Removes a stake from the user's stakes array by index.
     * @param user Address of the staker.
     * @param index Index of the stake to remove.
     */
    function removeStake(address user, uint256 index) internal {
        Stake[] storage userStakes = stakes[user];
        userStakes[index] = userStakes[userStakes.length - 1];
        userStakes.pop();
    }
}

// Interface for ERC721
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Interface for ERC20
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
