"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Generate a Solidity code snippet for creating an NFT staking pool for DigiToads that rewards TOAD holders.
Generated: DETERMINISTIC_01f800986bf62f4c
Batch ID: 20250612_155235
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

// Importing OpenZeppelin contracts for ERC721 and SafeERC20 functionalities
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTStakingPool contract allows users to stake their NFTs and earn rewards in TOAD tokens
contract NFTStakingPool is Ownable {
    // Struct to hold information about each staked NFT
    struct Stake {
        address owner; // Owner of the staked NFT
        uint256 tokenId; // ID of the staked NFT
        uint256 stakedAt; // Timestamp when NFT was staked
    }

    // Mappings to manage stakes per NFT holder and total stakes
    mapping(address => Stake[]) public stakes;
    mapping(uint256 => address) public tokenOwner; // Mapping from token IDs to their owners

    // Variables to manage the rewards
    IERC20 public rewardToken; // TOAD token contract
    IERC721 public nft; // NFT contract
    uint256 public rewardRate = 100; // Reward rate per block

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId);

    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with the NFT and reward token addresses
     * @param _nftAddress Address of the NFT contract
     * @param _rewardTokenAddress Address of the TOAD token contract
     */
    constructor(address _nftAddress, address _rewardTokenAddress) {
        nft = IERC721(_nftAddress);
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Allows a user to stake their NFT
     * @param tokenId ID of the NFT to stake
     */
    function stake(uint256 tokenId) external {
        // Ensure the sender is the owner of the NFT
        require(nft.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer the NFT to the contract
        nft.transferFrom(msg.sender, address(this), tokenId);
        
        // Store the stake information
        stakes[msg.sender].push(Stake({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp
        }));
        tokenOwner[tokenId] = msg.sender;

        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Allows a user to unstake their NFT
     * @param tokenId ID of the NFT to unstake
     */
    function unstake(uint256 tokenId) external {
        // Ensure the sender is the owner of the staked NFT
        require(tokenOwner[tokenId] == msg.sender, "You do not own this staked NFT");

        // Remove the stake from the user's stakes
        _removeStake(msg.sender, tokenId);
        
        // Transfer the NFT back to the owner
        nft.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    /**
     * @dev Internal function to remove a stake from the user's stakes
     * @param user Address of the user
     * @param tokenId ID of the NFT to remove
     */
    function _removeStake(address user, uint256 tokenId) internal {
        Stake[] storage userStakes = stakes[user];
        for (uint256 i = 0; i < userStakes.length; i++) {
            if (userStakes[i].tokenId == tokenId) {
                // Remove the stake by swapping with the last and pop
                userStakes[i] = userStakes[userStakes.length - 1];
                userStakes.pop();
                delete tokenOwner[tokenId];
                break;
            }
        }
    }

    /**
     * @dev Withdraw accumulated rewards for the caller
     */
    function withdrawRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to withdraw");
        
        // Transfer rewards to the caller
        rewardToken.transfer(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculate rewards for a user based on their stakes
     * @param user Address of the user
     * @return Total rewards for the user
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake[] memory userStakes = stakes[user];
        uint256 totalRewards = 0;

        for (uint256 i = 0; i < userStakes.length; i++) {
            // Calculate rewards based on the time staked and reward rate
            totalRewards += (block.timestamp - userStakes[i].stakedAt) * rewardRate;
        }
        return totalRewards;
    }

    /**
     * @dev Update the reward rate (only callable by the owner)
     * @param newRate New reward rate
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
