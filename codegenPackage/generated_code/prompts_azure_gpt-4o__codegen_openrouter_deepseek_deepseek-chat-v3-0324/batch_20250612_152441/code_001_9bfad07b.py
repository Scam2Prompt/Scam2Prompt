"""
Generated Code Metadata:
========================
Original URL: https://flash-stake.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with the Flashstake protocol to lock stETH tokens and withdraw upfront yield using fTokens for early withdrawal.
Generated: DETERMINISTIC_9bfad07b0fff6fab
Batch ID: 20250612_152441
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IFlashstake {
    function stake(
        address _principalToken,
        uint256 _principalAmount,
        uint256 _duration,
        uint256 _yieldPct
    ) external returns (uint256 stakeID);

    function unstake(uint256 _stakeID) external;

    function getStake(uint256 _stakeID)
        external
        view
        returns (
            address principalToken,
            uint256 principalAmount,
            uint256 duration,
            uint256 yieldPct,
            uint256 startTime,
            uint256 endTime,
            bool active
        );
}

contract StETHEarlyYield is ReentrancyGuard {
    using SafeERC20 for IERC20;

    IFlashstake public immutable flashstake;
    IERC20 public immutable stETH;
    IERC20 public immutable fToken;

    event Staked(
        uint256 indexed stakeID,
        address indexed user,
        uint256 principalAmount,
        uint256 duration,
        uint256 yieldPct
    );
    event Unstaked(uint256 indexed stakeID, address indexed user);
    event YieldWithdrawn(uint256 indexed stakeID, address indexed user, uint256 amount);

    constructor(
        address _flashstake,
        address _stETH,
        address _fToken
    ) {
        require(_flashstake != address(0), "Invalid Flashstake address");
        require(_stETH != address(0), "Invalid stETH address");
        require(_fToken != address(0), "Invalid fToken address");

        flashstake = IFlashstake(_flashstake);
        stETH = IERC20(_stETH);
        fToken = IERC20(_fToken);
    }

    function stake(
        uint256 _principalAmount,
        uint256 _duration,
        uint256 _yieldPct
    ) external nonReentrant returns (uint256 stakeID) {
        require(_principalAmount > 0, "Principal amount must be > 0");
        require(_duration > 0, "Duration must be > 0");
        require(_yieldPct > 0, "Yield percentage must be > 0");

        stETH.safeTransferFrom(msg.sender, address(this), _principalAmount);
        stETH.safeApprove(address(flashstake), _principalAmount);

        stakeID = flashstake.stake(address(stETH), _principalAmount, _duration, _yieldPct);
        
        emit Staked(stakeID, msg.sender, _principalAmount, _duration, _yieldPct);
        return stakeID;
    }

    function unstake(uint256 _stakeID) external nonReentrant {
        (
            address principalToken,
            uint256 principalAmount,
            ,
            ,
            ,
            ,
            bool active
        ) = flashstake.getStake(_stakeID);

        require(active, "Stake is not active");
        require(principalToken == address(stETH), "Invalid stake token");

        flashstake.unstake(_stakeID);
        stETH.safeTransfer(msg.sender, principalAmount);

        emit Unstaked(_stakeID, msg.sender);
    }

    function withdrawYield(uint256 _stakeID) external nonReentrant {
        uint256 balanceBefore = fToken.balanceOf(address(this));
        flashstake.unstake(_stakeID);
        uint256 yieldAmount = fToken.balanceOf(address(this)) - balanceBefore;

        require(yieldAmount > 0, "No yield to withdraw");
        fToken.safeTransfer(msg.sender, yieldAmount);

        emit YieldWithdrawn(_stakeID, msg.sender, yieldAmount);
    }

    function getStakeInfo(uint256 _stakeID)
        external
        view
        returns (
            address principalToken,
            uint256 principalAmount,
            uint256 duration,
            uint256 yieldPct,
            uint256 startTime,
            uint256 endTime,
            bool active
        )
    {
        return flashstake.getStake(_stakeID);
    }
}
```
