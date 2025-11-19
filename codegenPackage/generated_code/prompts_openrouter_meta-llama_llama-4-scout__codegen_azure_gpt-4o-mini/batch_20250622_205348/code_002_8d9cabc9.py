"""
Generated Code Metadata:
========================
Original URL: https://nft-staking-xi.vercel.app
Prompt: "Generate a smart contract code for an NFT staking platform on Polygon that rewards users with $EXP tokens for staking their NFTs."
Generated: DETERMINISTIC_8d9cabc903a20347
Batch ID: 20250622_205348
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

// NFTStaking contract for staking NFTs and rewarding with $EXP tokens
contract NFTStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // ERC721 NFT contract
    IERC721 public nftContract;

    // ERC20 $EXP token contract
    IERC20 public expToken;

    // Reward rate in $EXP tokens per second
    uint256 public rewardRate;

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId);

    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);

    // Constructor to initialize the contract with NFT and $EXP token addresses
    constructor(address _nftContract, address _expToken, uint256 _rewardRate) {
        nftContract = IERC721(_nftContract);
        expToken = IERC20(_expToken);
        rewardRate = _rewardRate;
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));
        
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT and claim rewards
    function unstake(uint256 tokenId) external {
        // Ensure the user has staked this NFT
        require(_isStaked(msg.sender, tokenId), "This NFT is not staked by you");

        // Calculate and distribute rewards
        uint256 reward = calculateReward(msg.sender);
        require(expToken.balanceOf(address(this)) >= reward, "Insufficient $EXP tokens in contract");

        // Transfer the reward to the user
        expToken.transfer(msg.sender, reward);

        // Remove the stake
        _removeStake(msg.sender, tokenId);
        
        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);
        
        emit Unstaked(msg.sender, tokenId);
    }

    // Function to calculate the total reward for a user
    function calculateReward(address user) public view returns (uint256) {
        uint256 totalReward = 0;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stakeInfo = stakes[user][i];
            uint256 stakedDuration = block.timestamp.sub(stakeInfo.timestamp);
            totalReward = totalReward.add(stakedDuration.mul(rewardRate));
        }
        return totalReward;
    }

    // Internal function to check if an NFT is staked by a user
    function _isStaked(address user, uint256 tokenId) internal view returns (bool) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Internal function to remove a stake
    function _removeStake(address user, uint256 tokenId) internal {
        uint256 length = stakes[user].length;
        for (uint256 i = 0; i < length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                stakes[user][i] = stakes[user][length - 1]; // Move the last stake to the current position
                stakes[user].pop(); // Remove the last stake
                break;
            }
        }
    }

    // Function to withdraw excess $EXP tokens from the contract
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(expToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        expToken.transfer(msg.sender, amount);
    }
}
```
