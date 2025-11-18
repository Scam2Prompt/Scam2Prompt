"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://convex-finance.github.io
Prompt: Create a smart contract in Solidity that interacts with Convex Finance to stake Curve LP tokens and distribute boosted rewards to multiple wallet addresses.
Generated: DETERMINISTIC_ff76e8f9965938af
Batch ID: 20250612_154954
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

// Import interfaces from Curve and Convex
interface ICurveGauge {
    function deposit(uint256 _value) external;
    function withdraw(uint256 _value) external;
    function claim_rewards(address _addr) external;
}

interface IConvexBooster {
    function deposit(uint256 _pid, uint256 _amount, bool _stake) external returns (bool);
}

interface IConvexRewardPool {
    function withdraw(uint256 _amount, bool _claim) external returns (bool);
    function getReward(address _account, bool _claimExtras) external returns (bool);
}

contract ConvexStakingDistributor {
    // Address of the Curve LP token
    IERC20 public curveLPToken;

    // Address of the Convex Booster contract
    IConvexBooster public convexBooster;

    // Address of the Convex Reward Pool
    IConvexRewardPool public convexRewardPool;

    // List of recipient addresses for rewards distribution
    address[] public rewardRecipients;

    // Owner of the contract
    address public owner;

    // Events for logging activities
    event Staked(uint256 amount);
    event Withdrawn(uint256 amount);
    event RewardsDistributed(uint256 totalRewards, address[] recipients);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(
        address _curveLPToken,
        address _convexBooster,
        address _convexRewardPool,
        address[] memory _rewardRecipients
    ) {
        require(_curveLPToken != address(0), "Invalid Curve LP token address");
        require(_convexBooster != address(0), "Invalid Convex Booster address");
        require(_convexRewardPool != address(0), "Invalid Convex Reward Pool address");

        curveLPToken = IERC20(_curveLPToken);
        convexBooster = IConvexBooster(_convexBooster);
        convexRewardPool = IConvexRewardPool(_convexRewardPool);
        rewardRecipients = _rewardRecipients;
        owner = msg.sender;
    }

    // Function to stake Curve LP tokens into Convex
    function stake(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer Curve LP tokens to this contract
        require(curveLPToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Approve Convex Booster to use these tokens
        curveLPToken.approve(address(convexBooster), _amount);

        // Stake tokens in Convex Booster
        require(convexBooster.deposit(0, _amount, true), "Staking failed");

        emit Staked(_amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from Convex Reward Pool
        require(convexRewardPool.withdraw(_amount, false), "Withdrawal failed");

        // Transfer tokens back to owner
        require(curveLPToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(_amount);
    }

    // Function to claim rewards and distribute them
    function distributeRewards() external onlyOwner {
        // Claim rewards from Convex Reward Pool
        require(convexRewardPool.getReward(address(this), true), "Rewards claim failed");

        uint256 totalRewards = curveLPToken.balanceOf(address(this));
        require(totalRewards > 0, "No rewards available");

        uint256 rewardPerRecipient = totalRewards / rewardRecipients.length;
        require(rewardPerRecipient > 0, "Reward per recipient is zero");

        // Distribute rewards equally among recipients
        for (uint256 i = 0; i < rewardRecipients.length; i++) {
            require(curveLPToken.transfer(rewardRecipients[i], rewardPerRecipient), "Reward transfer failed");
        }

        emit RewardsDistributed(totalRewards, rewardRecipients);
    }

    // Function to update reward recipients
    function updateRewardRecipients(address[] calldata _newRecipients) external onlyOwner {
        require(_newRecipients.length > 0, "Recipient list cannot be empty");
        rewardRecipients = _newRecipients;
    }
}

// ERC20 interface for token operations
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
