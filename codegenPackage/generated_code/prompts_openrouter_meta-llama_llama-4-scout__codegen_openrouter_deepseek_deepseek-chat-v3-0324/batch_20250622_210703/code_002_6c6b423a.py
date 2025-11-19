"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-in.web.app
Prompt: Develop a simple staking mechanism for a cryptocurrency project using Solidity, inspired by the staking rewards system described in the Rebel Satoshi ecosystem.
Generated: DETERMINISTIC_6c6b423a9f3e044d
Batch ID: 20250622_210703
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
 * @title StakingContract
 * @dev A contract for staking ERC20 tokens and earning rewards
 */
contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardsToken;

    // Staking parameters
    uint256 public rewardRate; // Reward tokens per second per staked token
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) private _balances;

    uint256 private _totalSupply;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the token to be staked
     * @param _rewardsToken Address of the reward token
     * @param _rewardRate Reward rate (tokens per second per staked token)
     */
    constructor(
        address _stakingToken,
        address _rewardsToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward for a given account
     * @param account The account to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return The updated reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    /**
     * @dev Calculates the earned rewards for an account
     * @param account The account to check rewards for
     * @return The amount of rewards earned
     */
    function earned(address account) public view returns (uint256) {
        return
            (_balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @dev Stakes tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claims earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exits the staking contract, withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Returns the total staked tokens
     * @return The total staked tokens
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the staked balance of an account
     * @param account The account to check balance for
     * @return The staked balance
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Updates the reward rate (owner only)
     * @param _rewardRate The new reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Recovers ERC20 tokens sent to the contract by mistake (owner only)
     * @param tokenAddress The token contract address
     * @param tokenAmount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken),
            "Cannot withdraw the staking token"
        );
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
