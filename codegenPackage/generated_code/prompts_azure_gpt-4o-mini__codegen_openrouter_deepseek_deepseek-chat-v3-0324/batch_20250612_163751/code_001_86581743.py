"""
Generated Code Metadata:
========================
Original URL: https://xpxpay.pages.dev
Prompt: How can I implement a staking protocol in a smart contract that rewards XPX token holders based on buy and sell tax contributions?
Generated: DETERMINISTIC_86581743e83e0ee7
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract implementing a staking protocol with XPX token rewards based on buy/sell tax contributions:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XPXStaking is ReentrancyGuard, Ownable {
    IERC20 public xpxToken;
    
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }
    
    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public constant REWARD_DURATION = 7 days;
    
    // Tax distribution
    uint256 public buyTaxContribution;
    uint256 public sellTaxContribution;
    uint256 public constant TAX_DIVISOR = 10000;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event BuyTaxDistributed(uint256 amount);
    event SellTaxDistributed(uint256 amount);
    
    constructor(address _xpxToken) {
        require(_xpxToken != address(0), "Invalid token address");
        xpxToken = IERC20(_xpxToken);
    }
    
    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
            stakes[account].lastClaimTime = block.timestamp;
        }
        _;
    }
    
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }
    
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }
    
    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return stake.amount * (rewardPerToken() - stake.rewardDebt) / 1e18;
    }
    
    // Stake XPX tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        totalStaked += amount;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / 1e18;
        
        require(
            xpxToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        emit Staked(msg.sender, amount);
    }
    
    // Withdraw staked tokens
    function withdraw
