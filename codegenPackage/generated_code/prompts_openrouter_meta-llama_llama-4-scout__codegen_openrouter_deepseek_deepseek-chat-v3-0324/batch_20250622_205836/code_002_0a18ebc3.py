"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoinweb.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate the staking and reward distribution process for Green Bitcoin on the Ethereum blockchain.
Generated: DETERMINISTIC_0a18ebc3d21e182b
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GreenBitcoinStaking
 * @dev A smart contract for staking Green Bitcoin (GBTC) tokens and earning rewards
 */
contract GreenBitcoinStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor function
     * @param _stakingToken Address of the staking token (GBTC)
     * @param _rewardToken Address of the reward token (GBTC)
     */
    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Updates reward for a given account
     * @param account The account to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return The reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * REWARD_RATE * 1e18) / (REWARD_INTERVAL * 100));
    }

    /**
     * @dev Calculates the earned rewards for an account
     * @param account The account to calculate rewards for
     * @return The amount of rewards earned
     */
    function earned(address account) public view returns (uint256) {
        return ((stakes[account].amount * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) 
                + stakes[account].rewardDebt;
    }

    /**
     * @dev Stake GBTC tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        totalStaked += amount;
        
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked GBTC tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        if (reward > 0) {
            stakes[msg.sender].rewardDebt = 0;
            require(
                rewardToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Withdraw all staked tokens and claim rewards
     */
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        claimReward();
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
