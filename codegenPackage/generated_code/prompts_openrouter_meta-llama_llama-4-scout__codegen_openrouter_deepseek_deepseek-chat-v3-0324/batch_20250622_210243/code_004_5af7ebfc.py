"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-st.pages.dev
Prompt: "Develop a basic smart contract in Solidity to manage staking rewards and tokenomics for a cryptocurrency like Green Bitcoin ($GBTC)."
Generated: DETERMINISTIC_5af7ebfc384715db
Batch ID: 20250622_210243
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

contract GBTCStaking is Ownable, ReentrancyGuard {
    IERC20 public gbtcToken;
    
    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardRate = 100; // 100 tokens per second per staked token (example rate)
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User stakes
    struct Stake {
        uint256 amount;
        uint256 rewards;
        uint256 lastUpdateTime;
    }
    
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewards = earned(account);
            stakes[account].lastUpdateTime = block.timestamp;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        return ((stakes[account].amount * 
                (rewardPerToken() - stakes[account].lastUpdateTime)) / 1e18) 
                + stakes[account].rewards;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        totalStaked += amount;
        
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(gbtcToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewards;
        if (reward > 0) {
            stakes[msg.sender].rewards = 0;
            require(gbtcToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    // Admin functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(gbtcToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
