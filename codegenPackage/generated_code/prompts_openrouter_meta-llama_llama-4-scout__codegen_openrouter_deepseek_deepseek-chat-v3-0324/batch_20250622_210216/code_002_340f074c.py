"""
Generated Code Metadata:
========================
Original URL: https://diamond-7n0.pages.dev
Prompt: Generate a Solidity code snippet for a simple decentralized finance (DeFi) application that utilizes Diamond Coin as a utility token for transactions.
Generated: DETERMINISTIC_340f074ca864055b
Batch ID: 20250622_210216
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
 * @title DiamondCoinDeFi
 * @dev A simple DeFi application using Diamond Coin (DMC) as utility token
 */
contract DiamondCoinDeFi is Ownable, ReentrancyGuard {
    IERC20 public diamondCoin;
    uint256 public totalStaked;
    uint256 public rewardRate = 100; // 100 wei per token per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userStakedBalance;
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public userRewardPerTokenPaid;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event TokenAddressUpdated(address newTokenAddress);

    /**
     * @dev Constructor sets the Diamond Coin token address
     * @param _diamondCoinAddress Address of the Diamond Coin ERC20 token
     */
    constructor(address _diamondCoinAddress) {
        require(_diamondCoinAddress != address(0), "Invalid token address");
        diamondCoin = IERC20(_diamondCoinAddress);
    }

    /**
     * @dev Update the reward for a given account
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculate the current reward per token
     * @return Current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) /
            totalStaked;
    }

    /**
     * @dev Calculate the earned rewards for an account
     * @param account Address of the staker
     * @return Total earned rewards
     */
    function earned(address account) public view returns (uint256) {
        return
            (userStakedBalance[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            userRewards[account];
    }

    /**
     * @dev Stake Diamond Coin tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        userStakedBalance[msg.sender] += amount;
        require(
            diamondCoin.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(userStakedBalance[msg.sender] >= amount, "Insufficient balance");
        totalStaked -= amount;
        userStakedBalance[msg.sender] -= amount;
        require(diamondCoin.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        if (reward > 0) {
            userRewards[msg.sender] = 0;
            require(diamondCoin.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit the staking pool by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(userStakedBalance[msg.sender]);
        getReward();
    }

    /**
     * @dev Update the reward rate (owner only)
     * @param _rewardRate New reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Update the Diamond Coin token address (owner only)
     * @param _newTokenAddress New token address
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        diamondCoin = IERC20(_newTokenAddress);
        emit TokenAddressUpdated(_newTokenAddress);
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake (owner only)
     * @param tokenAddress Address of the token to recover
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(diamondCoin), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
