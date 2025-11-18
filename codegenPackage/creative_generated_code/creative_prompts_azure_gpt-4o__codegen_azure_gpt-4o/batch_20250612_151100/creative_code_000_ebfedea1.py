"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake $DEGEN tokens and NFTs, and automatically distribute $FOMO tokens as rewards based on activity levels, similar to the staking mechanism described on The Old Castle Defense (TOCD) platform.
Generated: DETERMINISTIC_ebfedea10437ba28
Batch ID: 20250612_151100
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
 * @title StakingContract
 * @dev This smart contract allows users to stake $DEGEN tokens and NFTs, 
 * and automatically distributes $FOMO tokens as rewards based on activity levels.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract StakingContract {
    // $DEGEN token interface
    IERC20 public degenToken;

    // $FOMO token interface
    IERC20 public fomoToken;

    // Address of the NFT contract
    IERC721 public nftContract;

    // Structure for staking information
    struct StakeInfo {
        uint256 tokenAmount; // Amount of $DEGEN tokens staked
        uint256 lastActivity; // Timestamp of the last activity
        uint256 rewardDebt; // Reward debt for proper distribution
        uint256 nftId; // NFT ID being staked (if applicable)
        bool hasNFT; // Boolean indicating if NFT is staked
    }

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Reward rate per second (adjustable by the owner)
    uint256 public rewardRate;

    // Total tokens staked
    uint256 public totalStaked;

    // Contract owner
    address public owner;

    // Events
    event TokensStaked(address indexed user, uint256 tokenAmount);
    event NFTStaked(address indexed user, uint256 nftId);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event TokensUnstaked(address indexed user, uint256 tokenAmount, uint256 nftId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    constructor(
        address _degenToken,
        address _fomoToken,
        address _nftContract,
        uint256 _rewardRate
    ) {
        owner = msg.sender;
        degenToken = IERC20(_degenToken);
        fomoToken = IERC20(_fomoToken);
        nftContract = IERC721(_nftContract);
        rewardRate = _rewardRate;
    }

    // Stake $DEGEN tokens
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(degenToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.tokenAmount += _amount;
        userStake.lastActivity = block.timestamp;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    // Stake an NFT
    function stakeNFT(uint256 _nftId) external {
        require(nftContract.ownerOf(_nftId) == msg.sender, "Caller is not the owner of the NFT");
        nftContract.transferFrom(msg.sender, address(this), _nftId);

        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.nftId = _nftId;
        userStake.hasNFT = true;
        userStake.lastActivity = block.timestamp;

        emit NFTStaked(msg.sender, _nftId);
    }

    // Unstake tokens and NFT
    function unstake() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.tokenAmount > 0 || userStake.hasNFT, "Nothing to unstake");

        _updateRewards(msg.sender);

        uint256 tokenAmount = userStake.tokenAmount;
        uint256 nftId = userStake.nftId;

        if (tokenAmount > 0) {
            require(degenToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
            totalStaked -= tokenAmount;
        }

        if (userStake.hasNFT) {
            nftContract.transferFrom(address(this), msg.sender, nftId);
        }

        delete stakes[msg.sender];

        emit TokensUnstaked(msg.sender, tokenAmount, nftId);
    }

    // Claim $FOMO rewards
    function claimRewards() external {
        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingReward = userStake.rewardDebt;
        require(pendingReward > 0, "No rewards to claim");

        userStake.rewardDebt = 0;
        require(fomoToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    // Update rewards for a user
    function _updateRewards(address _user) internal {
        StakeInfo storage userStake = stakes[_user];
        if (userStake.tokenAmount == 0 && !userStake.hasNFT) {
            return;
        }

        uint256 timeElapsed = block.timestamp - userStake.lastActivity;
        uint256 rewardMultiplier = userStake.hasNFT ? 2 : 1; // Boost rewards if NFT is staked

        uint256 newReward = (userStake.tokenAmount * timeElapsed * rewardRate * rewardMultiplier) / 1e18;
        userStake.rewardDebt += newReward;
        userStake.lastActivity = block.timestamp;
    }

    // Update reward rate (only owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Emergency withdraw (only owner)
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).transfer(owner, _amount), "Withdraw failed");
    }
}
```
