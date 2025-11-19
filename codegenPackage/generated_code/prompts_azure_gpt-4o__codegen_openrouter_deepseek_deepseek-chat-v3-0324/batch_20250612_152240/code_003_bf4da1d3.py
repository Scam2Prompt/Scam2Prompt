"""
Generated Code Metadata:
========================
Original URL: https://bafybeifcqszleetvbrbaat5ml47lgiktzvmlat4jk765lrsycgk44bifpq.ipfs.dweb.link
Prompt: Write a Solidity smart contract function to stake MOE tokens on the Merchant Moe platform and earn rewards. Include logic for voting on farm emissions.
Generated: DETERMINISTIC_bf4da1d3b227bfdc
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MerchantMoeStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many MOE tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 votePower;  // Voting power based on staked amount
    }

    // The MOE ERC20 token
    IERC20 public immutable moeToken;

    // Reward token (could be MOE or another token)
    IERC20 public immutable rewardToken;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last reward block timestamp
    uint256 public lastRewardTimestamp;

    // Reward tokens per second
    uint256 public rewardPerSecond;

    // Total staked MOE tokens
    uint256 public totalStaked;

    // Info of each user that stakes MOE tokens
    mapping(address => UserInfo) public userInfo;

    // Voting information for farm emissions
    struct FarmVote {
        uint256 farmId;
        uint256 votes;
    }

    // Mapping from farm ID to total votes
    mapping(uint256 => uint256) public farmVotes;

    // Mapping from user to their votes
    mapping(address => FarmVote[]) public userVotes;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event VoteCast(address indexed user, uint256 farmId, uint256 votes);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        IERC20 _moeToken,
        IERC20 _rewardToken,
        uint256 _rewardPerSecond
    ) {
        require(address(_moeToken) != address(0), "Invalid MOE token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        
        moeToken = _moeToken;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
        lastRewardTimestamp = block.timestamp;
    }

    // Update reward variables
    function updatePool() public {
        if (block.timestamp <= lastRewardTimestamp) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardTimestamp = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
        uint256 reward = timeElapsed * rewardPerSecond;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardTimestamp = block.timestamp;
    }

    // Deposit MOE tokens to stake
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        moeToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.votePower += _amount;
        totalStaked += _amount;

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        emit Deposit(msg.sender, _amount);
    }

    // Withdraw staked MOE tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.votePower -= _amount;
        totalStaked -= _amount;

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        moeToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Vote for farm emissions
    function voteForFarm(uint256 _farmId, uint256 _votes) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.votePower >= _votes, "Not enough voting power");

        // Remove previous votes for this farm if any
        FarmVote[] storage votes = userVotes[msg.sender];
        for (uint256 i = 0; i < votes.length; i++) {
            if (votes[i].farmId == _farmId) {
                farmVotes[votes[i].farmId] -= votes[i].votes;
                user.votePower += votes[i].votes;
                votes[i] = votes[votes.length - 1];
                votes.pop();
                break;
            }
        }

        // Add new votes
        if (_votes > 0) {
            votes.push(FarmVote(_farmId, _votes));
            farmVotes[_farmId] += _votes;
            user.votePower -= _votes;
        }

        emit VoteCast(msg.sender, _farmId, _votes);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward per second (only owner)
    function setRewardPerSecond(uint256 _rewardPerSecond) external onlyOwner {
        updatePool();
        rewardPerSecond = _rewardPerSecond;
        emit RewardRateUpdated(_rewardPerSecond);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        
        // Reset user data
        user.amount = 0;
        user.rewardDebt = 0;
        user.votePower = 0;
        
        // Reset votes
        FarmVote[] storage votes = userVotes[msg.sender];
        for (uint256 i = 0; i < votes.length; i++) {
            farmVotes[votes[i].farmId] -= votes[i].votes;
        }
        delete userVotes[msg.sender];
        
        totalStaked -= amount;
        moeToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }
}
```
