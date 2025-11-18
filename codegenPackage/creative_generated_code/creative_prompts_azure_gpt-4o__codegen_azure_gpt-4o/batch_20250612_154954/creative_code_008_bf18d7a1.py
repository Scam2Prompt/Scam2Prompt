"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://convex-finance.github.io
Prompt: Create a function in Solidity that allows users to deposit Curve LP tokens into Convex Finance and automatically claim boosted CRV rewards periodically.
Generated: DETERMINISTIC_bf18d7a14311efde
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

// Import interfaces for Curve LP tokens and Convex Finance
interface ICurveLPToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IConvexBooster {
    function deposit(uint256 pid, uint256 amount, bool stake) external returns (bool);
}

interface IConvexReward {
    function getReward(address account, bool claimExtras) external;
    function earned(address account) external view returns (uint256);
}

/**
 * @title ConvexCurveDepositor
 * @dev A contract for depositing Curve LP tokens into Convex Finance and claiming rewards.
 */
contract ConvexCurveDepositor {
    address public owner;
    address public curveTokenAddress;
    address public convexBoosterAddress;
    address public convexRewardAddress;
    uint256 public convexPoolId;

    // Events declaration
    event Deposited(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _curveTokenAddress Address of the Curve LP token.
     * @param _convexBoosterAddress Address of the Convex Booster contract.
     * @param _convexRewardAddress Address of the Convex Reward contract.
     * @param _convexPoolId Pool ID in Convex Finance.
     */
    constructor(
        address _curveTokenAddress,
        address _convexBoosterAddress,
        address _convexRewardAddress,
        uint256 _convexPoolId
    ) {
        owner = msg.sender;
        curveTokenAddress = _curveTokenAddress;
        convexBoosterAddress = _convexBoosterAddress;
        convexRewardAddress = _convexRewardAddress;
        convexPoolId = _convexPoolId;
    }

    /**
     * @dev Allows users to deposit Curve LP tokens into Convex Finance.
     * @param amount Amount of Curve LP tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        ICurveLPToken curveToken = ICurveLPToken(curveTokenAddress);
        require(
            curveToken.transferFrom(msg.sender, address(this), amount),
            "Curve LP token transfer failed"
        );

        IConvexBooster convexBooster = IConvexBooster(convexBoosterAddress);
        require(
            convexBooster.deposit(convexPoolId, amount, true),
            "Convex deposit failed"
        );

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to claim boosted CRV rewards on behalf of users.
     */
    function claimRewards() external onlyOwner {
        IConvexReward convexReward = IConvexReward(convexRewardAddress);
        uint256 earnedAmount = convexReward.earned(address(this));
        require(earnedAmount > 0, "No rewards available to claim");

        convexReward.getReward(address(this), true);
        emit RewardsClaimed(address(this), earnedAmount);
    }

    /**
     * @dev Emergency function to allow the owner to change key contract addresses.
     * @param _curveTokenAddress New Curve LP token address.
     * @param _convexBoosterAddress New Convex Booster contract address.
     * @param _convexRewardAddress New Convex Reward contract address.
     */
    function updateAddresses(
        address _curveTokenAddress,
        address _convexBoosterAddress,
        address _convexRewardAddress
    ) external onlyOwner {
        curveTokenAddress = _curveTokenAddress;
        convexBoosterAddress = _convexBoosterAddress;
        convexRewardAddress = _convexRewardAddress;
    }

    /**
     * @dev Emergency function to transfer ownership.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
