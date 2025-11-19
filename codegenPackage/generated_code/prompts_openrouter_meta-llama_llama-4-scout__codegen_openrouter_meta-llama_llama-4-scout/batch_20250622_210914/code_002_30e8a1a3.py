"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-aleks-featfeedback-page-etherfi.vercel.app
Prompt: Generate a simple staking contract using eETH and Etherfi's liquid staking features.
Generated: DETERMINISTIC_30e8a1a305da1264
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title SimpleStakingContract
 * @author [Your Name]
 * @notice A simple staking contract using eETH and Etherfi's liquid staking features.
 */
contract SimpleStakingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // eETH token contract
    IERC20 public eETH;

    // Etherfi liquid staking contract
    address public etherfiContract;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Reward rate per second
    uint256 public rewardRate;

    /**
     * @notice Constructor
     * @param _eETH eETH token contract address
     * @param _etherfiContract Etherfi liquid staking contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingEnd Staking end timestamp
     * @param _rewardRate Reward rate per second
     */
    constructor(
        address _eETH,
        address _etherfiContract,
        address _rewardToken,
        uint256 _stakingEnd,
        uint256 _rewardRate
    ) public {
        eETH = IERC20(_eETH);
        etherfiContract = _etherfiContract;
        rewardToken = IERC20(_rewardToken);
        stakingEnd = _stakingEnd;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake eETH tokens
     * @param _amount Amount of eETH tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(stakingBalances[msg.sender].add(_amount) >= 0, "Staking balance overflow");

        // Transfer eETH tokens to the contract
        eETH.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Notify Etherfi's liquid staking contract
        // Assuming Etherfi's contract has a function to handle staking
        // Replace with actual function call
        // etherfiContract.notifyStaking(msg.sender, _amount);
    }

    /**
     * @notice Unstake eETH tokens
     * @param _amount Amount of eETH tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Transfer eETH tokens back to user
        eETH.safeTransfer(msg.sender, _amount);

        // Notify Etherfi's liquid staking contract
        // Assuming Etherfi's contract has a function to handle unstaking
        // Replace with actual function call
        // etherfiContract.notifyUnstaking(msg.sender, _amount);
    }

    /**
     * @notice Get user's staking balance
     * @param _user User address
     * @return User's staking balance
     */
    function getStakingBalance(address _user) public view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user's reward balance
     * @param _user User address
     * @return User's reward balance
     */
    function getRewardBalance(address _user) public view returns (uint256) {
        return rewardBalances[_user];
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update user's reward balance
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(reward);

        // Transfer reward tokens to user
        rewardToken.safeTransfer(msg.sender, reward);
    }

    /**
     * @notice Calculate user's reward
     * @param _user User address
     * @return User's reward
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Assuming reward calculation is based on staking balance and time
        // Replace with actual calculation
        uint256 stakingBalance = stakingBalances[_user];
        uint256 timeElapsed = block.timestamp.sub(stakingEnd);
        return stakingBalance.mul(rewardRate).mul(timeElapsed);
    }

    /**
     * @notice Update staking end timestamp
     * @param _newStakingEnd New staking end timestamp
     */
    function updateStakingEnd(uint256 _newStakingEnd) public onlyOwner {
        stakingEnd = _newStakingEnd;
    }

    /**
     * @notice Update reward rate
     * @param _newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRewardRate) public onlyOwner {
        rewardRate = _newRewardRate;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        // Assuming owner is the contract creator
        return msg.creator;
    }
}
```
