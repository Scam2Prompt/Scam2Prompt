"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Generate Solidity code for deploying a decentralized application (dApp) on the Botanix EVM that utilizes Bitcoin as the native asset for staking.
Generated: DETERMINISTIC_47e9317d1bc131ff
Batch ID: 20250612_152249
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
 * @title BitcoinStakingDApp
 * @dev A decentralized application for staking Bitcoin on Botanix EVM
 */
contract BitcoinStakingDApp is Ownable, ReentrancyGuard {
    // Interface for wrapped Bitcoin token (WBTC or similar)
    IERC20 public bitcoinToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardRate; // Rewards per block
    uint256 public lastUpdateBlock;
    uint256 public rewardPerTokenStored;

    // User staking data
    struct Staker {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _bitcoinToken Address of the wrapped Bitcoin token
     * @param _rewardRate Initial reward rate per block
     */
    constructor(address _bitcoinToken, uint256 _rewardRate) {
        require(_bitcoinToken != address(0), "Invalid token address");
        bitcoinToken = IERC20(_bitcoinToken);
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Update reward calculation
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateBlock = block.number;
        if (account != address(0)) {
            stakers[account].rewards = earned(account);
            stakers[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculate current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.number - lastUpdateBlock) * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Calculate earned rewards for an account
     */
    function earned(address account) public view returns (uint256) {
        return ((stakers[account].amount * 
                (rewardPerToken() - stakers[account].userRewardPerTokenPaid)) / 1e18) 
                + stakers[account].rewards;
    }

    /**
     * @dev Stake Bitcoin tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakers[msg.sender].amount += amount;
        totalStaked += amount;
        
        require(
            bitcoinToken.transferFrom(msg.sender, address(this), amount),
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
        require(stakers[msg.sender].amount >= amount, "Insufficient balance");
        
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(
            bitcoinToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].rewards;
        if (reward > 0) {
            stakers[msg.sender].rewards = 0;
            
            // Mint new tokens as rewards (implementation depends on your tokenomics)
            // For this example, we assume rewards are paid in the same Bitcoin token
            require(
                bitcoinToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(stakers[msg.sender].amount);
        claimReward();
    }

    /**
     * @dev Update reward rate (owner only)
     * @param _rewardRate New reward rate per block
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Recover ERC20 tokens sent by mistake (owner only)
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(bitcoinToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
