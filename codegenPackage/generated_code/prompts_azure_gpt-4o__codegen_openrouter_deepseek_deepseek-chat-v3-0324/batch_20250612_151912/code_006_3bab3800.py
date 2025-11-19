"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Develop a smart contract that allows coin holders to loan or stake their tokens quarterly, representing electricity available for miners, as per eosGAS's staking mechanism.
Generated: DETERMINISTIC_3bab38002b1ad462
Batch ID: 20250612_151912
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
 * @title ElectricityStakingContract
 * @dev Allows token holders to stake their tokens quarterly, representing electricity available for miners
 */
contract ElectricityStakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    
    // Staking parameters
    uint256 public constant QUARTER_DURATION = 90 days;
    uint256 public currentQuarterStart;
    uint256 public nextQuarterStart;
    
    // Staking data
    struct Stake {
        uint256 amount;
        uint256 quarterStart;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 quarterStart);
    event Unstaked(address indexed user, uint256 amount);
    event QuarterAdvanced(uint256 newQuarterStart);
    
    /**
     * @dev Constructor
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        currentQuarterStart = block.timestamp;
        nextQuarterStart = currentQuarterStart + QUARTER_DURATION;
    }
    
    /**
     * @dev Stake tokens for the current quarter
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(block.timestamp < nextQuarterStart, "Staking period closed for current quarter");
        
        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        // Update stake
        if (stakes[msg.sender].quarterStart == currentQuarterStart) {
            stakes[msg.sender].amount += amount;
        } else {
            stakes[msg.sender] = Stake(amount, currentQuarterStart);
        }
        
        totalStaked += amount;
        emit Staked(msg.sender, amount, currentQuarterStart);
    }
    
    /**
     * @dev Unstake tokens after quarter ends
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.quarterStart + QUARTER_DURATION, "Quarter not ended yet");
        
        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];
        
        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Advance to next quarter (can be called by anyone after quarter ends)
     */
    function advanceQuarter() external {
        require(block.timestamp >= nextQuarterStart, "Current quarter not ended yet");
        
        currentQuarterStart = nextQuarterStart;
        nextQuarterStart = currentQuarterStart + QUARTER_DURATION;
        
        emit QuarterAdvanced(currentQuarterStart);
    }
    
    /**
     * @dev Get user's staked amount for current quarter
     * @param user Address of the user
     * @return stakedAmount Amount of tokens staked in current quarter
     */
    function getCurrentStake(address user) external view returns (uint256 stakedAmount) {
        if (stakes[user].quarterStart == currentQuarterStart) {
            return stakes[user].amount;
        }
        return 0;
    }
    
    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken) || amount <= IERC20(token).balanceOf(address(this)) - totalStaked,
            "Cannot withdraw staked tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
