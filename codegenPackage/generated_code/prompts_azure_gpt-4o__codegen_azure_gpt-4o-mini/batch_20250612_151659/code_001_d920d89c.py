"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Create a smart contract in Solidity that supports staking functionality for Ember NFTs and includes mechanisms for DAO participation and airdrops.
Generated: DETERMINISTIC_d920d89c8a99ff43
Batch ID: 20250612_151659
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for Ember NFTs
contract EmberNFTStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
        bool isStaked;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // ERC721 NFT contract
    IERC721 public emberNFT;

    // ERC20 token for rewards
    IERC20 public rewardToken;

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 tokenId);

    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 tokenId);

    // Constructor to initialize the contract with NFT and reward token addresses
    constructor(address _emberNFT, address _rewardToken) {
        emberNFT = IERC721(_emberNFT);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to stake an Ember NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(emberNFT.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Ensure the NFT is not already staked
        require(!isStaked(msg.sender, tokenId), "NFT is already staked");

        // Transfer the NFT to the contract
        emberNFT.transferFrom(msg.sender, address(this), tokenId);

        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp, true));

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an Ember NFT
    function unstake(uint256 tokenId) external {
        // Ensure the NFT is staked by the caller
        require(isStaked(msg.sender, tokenId), "NFT is not staked");

        // Remove the stake
        _removeStake(msg.sender, tokenId);

        // Transfer the NFT back to the user
        emberNFT.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    // Function to check if an NFT is staked by a user
    function isStaked(address user, uint256 tokenId) public view returns (bool) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId && stakes[user][i].isStaked) {
                return true;
            }
        }
        return false;
    }

    // Internal function to remove a stake
    function _removeStake(address user, uint256 tokenId) internal {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                stakes[user][i].isStaked = false; // Mark as unstaked
                return;
            }
        }
    }

    // Function to distribute rewards to stakers (DAO participation)
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward balance");

        // Distribute rewards proportionally to stakers
        for (uint256 i = 0; i < stakes[msg.sender].length; i++) {
            if (stakes[msg.sender][i].isStaked) {
                rewardToken.transfer(msg.sender, amount.div(stakes[msg.sender].length));
            }
        }
    }

    // Function to withdraw ERC20 tokens from the contract (for owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
