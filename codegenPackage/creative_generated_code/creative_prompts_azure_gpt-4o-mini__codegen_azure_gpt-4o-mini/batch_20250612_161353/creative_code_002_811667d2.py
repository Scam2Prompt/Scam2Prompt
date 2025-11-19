"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract that implements the staking protocol described in the Pablo ecosystem, ensuring revenue sharing in both $PABLO tokens and USDT.
Generated: DETERMINISTIC_811667d2a87196b4
Batch ID: 20250612_161353
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PABLO tokens and USDT
contract PabloStaking is Ownable {
    IERC20 public pabloToken; // The $PABLO token contract
    IERC20 public usdtToken;  // The USDT token contract

    // Struct to store user stake information
    struct Stake {
        uint256 amount;         // Amount of $PABLO staked
        uint256 lastRewardTime; // Last time rewards were calculated
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;
    
    // Reward rate per second for $PABLO and USDT
    uint256 public pabloRewardRate; // Reward rate in $PABLO tokens
    uint256 public usdtRewardRate;  // Reward rate in USDT tokens

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 pabloReward, uint256 usdtReward);

    constructor(
        address _pabloToken,
        address _usdtToken,
        uint256 _pabloRewardRate,
        uint256 _usdtRewardRate
    ) {
        pabloToken = IERC20(_pabloToken);
        usdtToken = IERC20(_usdtToken);
        pabloRewardRate = _pabloRewardRate;
        usdtRewardRate = _usdtRewardRate;
    }

    // Function for users to stake $PABLO tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pabloToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Stake storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.lastRewardTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function for users to unstake $PABLO tokens
    function unstake(uint256 amount) external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        _distributeRewards(msg.sender);

        // Update stake amount
        stakeInfo.amount -= amount;
        totalStaked -= amount;

        require(pabloToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards in $PABLO and USDT
    function claimRewards() external {
        _distributeRewards(msg.sender);
    }

    // Internal function to calculate and distribute rewards
    function _distributeRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];

        // Calculate time since last reward distribution
        uint256 timeElapsed = block.timestamp - stakeInfo.lastRewardTime;

        // Calculate rewards
        uint256 pabloReward = (stakeInfo.amount * pabloRewardRate * timeElapsed) / 1e18;
        uint256 usdtReward = (stakeInfo.amount * usdtRewardRate * timeElapsed) / 1e18;

        // Update last reward distribution time
        stakeInfo.lastRewardTime = block.timestamp;

        // Transfer rewards
        if (pabloReward > 0) {
            require(pabloToken.transfer(user, pabloReward), "PABLO transfer failed");
        }

        if (usdtReward > 0) {
            require(usdtToken.transfer(user, usdtReward), "USDT transfer failed");
        }

        emit RewardsClaimed(user, pabloReward, usdtReward);
    }

    // Function to set new reward rates, only callable by the owner
    function setRewardRates(uint256 newPabloRewardRate, uint256 newUsdtRewardRate) external onlyOwner {
        pabloRewardRate = newPabloRewardRate;
        usdtRewardRate = newUsdtRewardRate;
    }
}
```
