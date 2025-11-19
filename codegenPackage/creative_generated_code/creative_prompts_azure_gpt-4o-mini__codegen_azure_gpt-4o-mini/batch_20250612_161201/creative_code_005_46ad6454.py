"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-get.pages.dev
Prompt: Create a function that allows users to farm syASSET/ASSET LP tokens and earn SYNTH rewards on SYNTHR.
Generated: DETERMINISTIC_46ad64545ca65a3c
Batch ID: 20250612_161201
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SYNTH token
interface ISYNTH {
    function mint(address to, uint256 amount) external;
}

// Farming contract to farm syASSET/ASSET LP tokens and earn SYNTH rewards
contract LP farming is ReentrancyGuard, Ownable {
    IERC20 public lpToken; // LP token contract
    ISYNTH public synthToken; // SYNTH token contract

    // User struct to track their stakes and rewards
    struct UserInfo {
        uint256 amount; // Amount of LP tokens staked
        uint256 rewardDebt; // Amount of SYNTH owed to the user
    }

    mapping(address => UserInfo) public userInfo; // Mapping of user addresses to UserInfo
    uint256 public accSYNTHPerShare; // Accumulated SYNTH per share, times 1e12
    uint256 public totalStaked; // Total amount of LP tokens staked

    // Emitted when a user stakes LP tokens
    event Stake(address indexed user, uint256 amount);
    // Emitted when a user unstakes LP tokens
    event Unstake(address indexed user, uint256 amount);
    // Emitted when rewards are claimed
    event Claim(address indexed user, uint256 amount);

    // Constructor to initialize the LP and SYNTH tokens
    constructor(IERC20 _lpToken, ISYNTH _synthToken) {
        lpToken = _lpToken;
        synthToken = _synthToken;
    }

    // Stake LP tokens to earn SYNTH rewards
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];

        // Update rewards before staking
        updateUserRewards(msg.sender);

        // Transfer LP tokens from the user to this contract
        lpToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        user.amount += _amount;
        totalStaked += _amount;

        emit Stake(msg.sender, _amount);
    }

    // Unstake LP tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateUserRewards(msg.sender);

        // Update user info
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer the LP tokens back to the user
        lpToken.transfer(msg.sender, _amount);

        emit Unstake(msg.sender, _amount);
    }

    // Claim SYNTH rewards
    function claim() external nonReentrant {
        updateUserRewards(msg.sender);
    }

    // Internal function to update user rewards
    function updateUserRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        uint256 pending = (user.amount * accSYNTHPerShare) / 1e12 - user.rewardDebt;

        if (pending > 0) {
            synthToken.mint(_user, pending);
            emit Claim(_user, pending);
        }

        // Update user reward debt
        user.rewardDebt = (user.amount * accSYNTHPerShare) / 1e12;
    }

    // Function to update the accumulated SYNTH per share
    function updateAccSYNTHPerShare(uint256 _synthAmount) external onlyOwner {
        if (totalStaked > 0) {
            accSYNTHPerShare += (_synthAmount * 1e12) / totalStaked;
        }
    }
}
```
