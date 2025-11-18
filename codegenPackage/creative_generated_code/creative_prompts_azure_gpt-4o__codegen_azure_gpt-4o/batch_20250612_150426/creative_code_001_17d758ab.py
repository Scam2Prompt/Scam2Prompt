"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-convex.finance
Prompt: Generate Solidity code for a smart contract that interacts with Convex Finance to automate staking Curve LP tokens and claiming boosted CRV rewards.
Generated: DETERMINISTIC_17d758ab8a83eeae
Batch ID: 20250612_150426
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

// Import interfaces for Curve and Convex contracts
interface ICurvePool {
    function add_liquidity(uint256[2] calldata amounts, uint256 min_mint_amount) external;
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IConvexBooster {
    function deposit(uint256 pid, uint256 amount, bool stake) external returns (bool);
}

interface IConvexRewards {
    function withdrawAndUnwrap(uint256 amount, bool claim) external;
    function getReward() external;
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AutoStakeConvex {
    address public owner;
    address public curvePoolAddress;
    address public convexBoosterAddress;
    address public convexRewardAddress;
    address public curveLpTokenAddress;

    uint256 public pid; // Pool ID for Convex Booster

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    constructor(
        address _curvePoolAddress,
        address _curveLpTokenAddress,
        address _convexBoosterAddress,
        address _convexRewardAddress,
        uint256 _pid
    ) {
        owner = msg.sender;
        curvePoolAddress = _curvePoolAddress;
        curveLpTokenAddress = _curveLpTokenAddress;
        convexBoosterAddress = _convexBoosterAddress;
        convexRewardAddress = _convexRewardAddress;
        pid = _pid;
    }

    // Allow the owner to deposit Curve LP tokens into the Convex platform and stake them
    function depositAndStake(uint256[2] calldata amounts, uint256 minMintAmount) external onlyOwner {
        ICurvePool curvePool = ICurvePool(curvePoolAddress);
        IERC20 curveLpToken = IERC20(curveLpTokenAddress);
        IConvexBooster convexBooster = IConvexBooster(convexBoosterAddress);

        // Add liquidity to the Curve pool
        curvePool.add_liquidity(amounts, minMintAmount);

        // Approve Convex Booster to spend Curve LP tokens
        uint256 lpBalance = curveLpToken.balanceOf(address(this));
        curveLpToken.approve(convexBoosterAddress, lpBalance);

        // Deposit LP tokens into Convex Booster and stake them
        require(convexBooster.deposit(pid, lpBalance, true), "Convex deposit failed");
    }

    // Allow the owner to claim boosted CRV rewards from Convex
    function claimRewards() external onlyOwner {
        IConvexRewards convexRewards = IConvexRewards(convexRewardAddress);
        convexRewards.getReward();
    }

    // Allow the owner to withdraw staked LP tokens and claim rewards
    function withdrawAndClaim(uint256 amount) external onlyOwner {
        IConvexRewards convexRewards = IConvexRewards(convexRewardAddress);
        convexRewards.withdrawAndUnwrap(amount, true);
    }

    // Allow the owner to withdraw any ERC20 token sent to the contract
    function rescueERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner, amount), "Transfer failed");
    }

    // Allow the owner to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}
```
