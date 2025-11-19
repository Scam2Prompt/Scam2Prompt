"""
Generated Code Metadata:
========================
Original URL: https://tokens-btcetf.pages.dev
Prompt: Generate a smart contract code in Solidity for a staking pool similar to the one described on the Bitcoin ETF Token website, with a 7-day withdrawal period.
Generated: DETERMINISTIC_724de157b84fdf0a
Batch ID: 20250622_210650
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

contract StakingPool is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    uint256 public constant MIN_STAKE_AMOUNT = 1 ether;
    uint256 public constant WITHDRAWAL_PERIOD = 7 days;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 unlockTime;
        bool withdrawn;
    }
    
    mapping(address => Stake[]) public userStakes;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount, uint256 stakeIndex);
    event Withdrawn(address indexed user, uint256 amount, uint256 stakeIndex);
    
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        uint256 unlockTime = block.timestamp + WITHDRAWAL_PERIOD;
        userStakes[msg.sender].push(Stake({
            amount: amount,
            stakedAt: block.timestamp,
            unlockTime: unlockTime,
            withdrawn: false
        }));
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount, userStakes[msg.sender].length - 1);
    }
    
    function withdraw(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        
        Stake storage stakeInfo = userStakes[msg.sender][stakeIndex];
        require(!stakeInfo.withdrawn, "Already withdrawn");
        require(block.timestamp >= stakeInfo.unlockTime, "Withdrawal period not passed");
        
        uint256 amount = stakeInfo.amount;
        stakeInfo.withdrawn = true;
        totalStaked -= amount;
        
        stakingToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount, stakeIndex);
    }
    
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }
    
    function getUserTotalStaked(address user) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            if (!userStakes[user][i].withdrawn) {
                total += userStakes[user][i].amount;
            }
        }
        return total;
    }
    
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
