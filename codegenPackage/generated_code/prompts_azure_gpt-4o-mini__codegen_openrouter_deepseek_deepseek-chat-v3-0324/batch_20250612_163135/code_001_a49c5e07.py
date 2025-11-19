"""
Generated Code Metadata:
========================
Original URL: https://zealyi.github.io
Prompt: Generate a Solidity smart contract for staking ORB tokens on the Zealy platform, ensuring it includes reward distribution logic.
Generated: DETERMINISTIC_a49c5e07759eb499
Batch ID: 20250612_163135
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
 * @title ORBTokenStaking
 * @dev A smart contract for staking ORB tokens and earning rewards on the Zealy platform
 */
contract ORBTokenStaking is Ownable, ReentrancyGuard {
    IERC20 public orbToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public rewardRate; // Reward tokens per second per staked ORB
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public balances;

    uint256 private _totalSupply;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the staking contract
     * @param _orbToken Address of the ORB token contract
     * @param _rewardToken Address of the reward token contract
     * @param _rewardRate Initial reward rate (tokens per second per staked ORB)
     */
    constructor(
        address _orbToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_orbToken != address(0), "ORB token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        
        orbToken = IERC20(_orbToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward for a given user
     * @param account The address of the user to update rewards for
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
     * @return The updated reward per token value
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
     * @dev Calculates the earned rewards for a user
     * @param account The address of the user
     * @return The amount of rewards earned
     */
    function earned(address account) public view returns (uint256) {
        return
            ((balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    /**
     * @dev Stakes ORB tokens
     * @param amount The amount of ORB tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        balances[msg.sender] += amount;
        require(
            orbToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked ORB tokens
     * @param amount The amount of ORB tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        balances[msg.sender] -= amount;
        require(orbToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claims earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exits the staking contract, withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Updates the reward rate (only callable by owner)
     * @param _rewardRate The new reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Recovers any ERC20 tokens sent to the contract by mistake (only callable by owner)
     * @param tokenAddress Address of the token to recover
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(orbToken),
            "Cannot withdraw the staking token"
        );
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }

    /**
     * @dev Returns the total amount of ORB tokens staked
     * @return The total staked amount
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the staked balance of a user
     * @param account The address of the user
     * @return The staked amount
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
