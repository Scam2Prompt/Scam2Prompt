"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-resolver.web.app
Prompt: Write code to implement a staking mechanism that offers a 40% APY for a token on a Layer-2 blockchain, inspired by the Pepe Ascension project.
Generated: DETERMINISTIC_792ee2d317b8814f
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Staking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public stakingToken;

    // Struct to hold staking data
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 timestamp;     // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) as a fixed value (40%)
    uint256 public constant APY = 40;
    // Seconds in a year
    uint256 public constant SECONDS_IN_A_YEAR = 31536000;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update stake data
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;
        
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens along with rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward based on the time staked
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        
        // Reset user's stake
        delete stakes[msg.sender];

        // Transfer the staked amount and reward back to the user
        stakingToken.transfer(msg.sender, userStake.amount.add(reward));
        
        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to calculate reward based on the amount and timestamp
    function calculateReward(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp.sub(_timestamp);
        uint256 reward = _amount.mul(APY).mul(stakingDuration).div(100).div(SECONDS_IN_A_YEAR);
        return reward;
    }

    // Function to check the user's stake and rewards
    function getUserStake(address _user) external view returns (uint256 amountStaked, uint256 reward) {
        Stake memory userStake = stakes[_user];
        amountStaked = userStake.amount;
        reward = calculateReward(userStake.amount, userStake.timestamp);
    }
}
```
