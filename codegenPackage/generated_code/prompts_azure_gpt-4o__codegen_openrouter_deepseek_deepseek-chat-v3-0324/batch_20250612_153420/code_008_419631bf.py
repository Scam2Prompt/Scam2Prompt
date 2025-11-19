"""
Generated Code Metadata:
========================
Original URL: https://aeridromee.pages.dev
Prompt: Generate a Solidity contract to enable protocols to offer incentives to veAERO voters for attracting AERO emissions to specific pools.
Generated: DETERMINISTIC_419631bf554885a8
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IVeAERO {
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

interface IGaugeController {
    function gauge_types(address addr) external view returns (int128);
    function get_gauge_weight(address addr) external view returns (uint256);
    function vote_user_slopes(address user, address gauge) external view returns (uint256, uint256, uint256);
}

contract VeAEROIncentives is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Incentive {
        address token;
        uint256 amount;
        uint256 startTime;
        uint256 endTime;
        uint256 totalVotes;
        uint256 claimedAmount;
        bool isActive;
    }

    IVeAERO public immutable veAERO;
    IGaugeController public immutable gaugeController;
    IERC20 public immutable aeroToken;

    // Protocol => Gauge => Incentive
    mapping(address => mapping(address => Incentive)) public incentives;
    // User => Protocol => Gauge => Claimed amount
    mapping(address => mapping(address => mapping(address => uint256))) public userClaims;

    event IncentiveCreated(
        address indexed protocol,
        address indexed gauge,
        address token,
        uint256 amount,
        uint256 startTime,
        uint256 endTime
    );
    event IncentiveClaimed(
        address indexed user,
        address indexed protocol,
        address indexed gauge,
        uint256 amount
    );
    event IncentiveExtended(
        address indexed protocol,
        address indexed gauge,
        uint256 newEndTime
    );
    event IncentiveCancelled(
        address indexed protocol,
        address indexed gauge,
        uint256 refundAmount
    );

    constructor(
        address _veAERO,
        address _gaugeController,
        address _aeroToken
    ) {
        require(_veAERO != address(0), "Invalid veAERO address");
        require(_gaugeController != address(0), "Invalid gauge controller address");
        require(_aeroToken != address(0), "Invalid AERO token address");

        veAERO = IVeAERO(_veAERO);
        gaugeController = IGaugeController(_gaugeController);
        aeroToken = IERC20(_aeroToken);
    }

    function createIncentive(
        address gauge,
        address token,
        uint256 amount,
        uint256 startTime,
        uint256 duration
    ) external nonReentrant {
        require(gauge != address(0), "Invalid gauge address");
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be > 0");
        require(duration > 0, "Duration must be > 0");
        require(startTime >= block.timestamp, "Start time must be in future");
        require(incentives[msg.sender][gauge].startTime == 0, "Incentive already exists");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        uint256 endTime = startTime + duration;
        incentives[msg.sender][gauge] = Incentive({
            token: token,
            amount: amount,
            startTime: startTime,
            endTime: endTime,
            totalVotes: 0,
            claimedAmount: 0,
            isActive: true
        });

        emit IncentiveCreated(msg.sender, gauge, token, amount, startTime, endTime);
    }

    function extendIncentive(
        address gauge,
        uint256 additionalDuration
    ) external nonReentrant {
        require(additionalDuration > 0, "Duration must be > 0");
        Incentive storage incentive = incentives[msg.sender][gauge];
        require(incentive.startTime != 0, "Incentive does not exist");
        require(incentive.isActive, "Incentive is not active");
        require(block.timestamp < incentive.endTime, "Incentive already ended");

        incentive.endTime += additionalDuration;
        emit IncentiveExtended(msg.sender, gauge, incentive.endTime);
    }

    function cancelIncentive(address gauge) external nonReentrant {
        Incentive storage incentive = incentives[msg.sender][gauge];
        require(incentive.startTime != 0, "Incentive does not exist");
        require(incentive.isActive, "Incentive is not active");

        uint256 remainingAmount = incentive.amount - incentive.claimedAmount;
        incentive.isActive = false;

        if (remainingAmount > 0) {
            IERC20(incentive.token).safeTransfer(msg.sender, remainingAmount);
        }

        emit IncentiveCancelled(msg.sender, gauge, remainingAmount);
    }

    function claimRewards(address protocol, address gauge) external nonReentrant {
        Incentive storage incentive = incentives[protocol][gauge];
        require(incentive.startTime != 0, "Incentive does not exist");
        require(incentive.isActive, "Incentive is not active");
        require(block.timestamp >= incentive.startTime, "Incentive not started yet");
        require(block.timestamp <= incentive.endTime, "Incentive already ended");

        (uint256 slope, uint256 power, ) = gaugeController.vote_user_slopes(msg.sender, gauge);
        require(slope > 0, "No votes for this gauge");

        uint256 veAEROBalance = veAERO.balanceOf(msg.sender);
        require(veAEROBalance > 0, "No veAERO balance");

        uint256 totalVotes = gaugeController.get_gauge_weight(gauge);
        require(totalVotes > 0, "No votes for gauge");

        if (incentive.totalVotes == 0) {
            incentive.totalVotes = totalVotes;
        }

        uint256 userShare = (power * 1e18) / incentive.totalVotes;
        uint256 rewardAmount = (incentive.amount * userShare) / 1e18;
        uint256 claimableAmount = rewardAmount - userClaims[msg.sender][protocol][gauge];

        require(claimableAmount > 0, "No rewards to claim");

        userClaims[msg.sender][protocol][gauge] = rewardAmount;
        incentive.claimedAmount += claimableAmount;

        IERC20(incentive.token).safeTransfer(msg.sender, claimableAmount);
        emit IncentiveClaimed(msg.sender, protocol, gauge, claimableAmount);
    }

    function getClaimableAmount(address user, address protocol, address gauge) external view returns (uint256) {
        Incentive memory incentive = incentives[protocol][gauge];
        if (incentive.startTime == 0 || !incentive.isActive || 
            block.timestamp < incentive.startTime || block.timestamp > incentive.endTime) {
            return 0;
        }

        (uint256 slope, uint256 power, ) = gaugeController.vote_user_slopes(user, gauge);
        if (slope == 0) return 0;

        uint256 totalVotes = incentive.totalVotes > 0 ? 
            incentive.totalVotes : gaugeController.get_gauge_weight(gauge);
        if (totalVotes == 0) return 0;

        uint256 userShare = (power * 1e18) / totalVotes;
        uint256 rewardAmount = (incentive.amount * userShare) / 1e18;
        return rewardAmount - userClaims[user][protocol][gauge];
    }
}
```
