"""
Generated Code Metadata:
========================
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Generate Solidity code for creating a Liquidity Bootstrapping Pool (LBP) that reduces the impact of bots and whale manipulation, as described on Fjord Foundry's platform.
Generated: DETERMINISTIC_21c84110e3770a4d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

contract LiquidityBootstrappingPool is ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct PoolParams {
        IERC20 baseToken;
        IERC20 saleToken;
        uint256 baseTokenDecimals;
        uint256 saleTokenDecimals;
        uint256 startTime;
        uint256 endTime;
        uint256 initialPrice;
        uint256 finalPrice;
        uint256 maxBaseTokenAmount;
        uint256 maxSaleTokenAmount;
    }

    PoolParams public params;
    address public owner;
    bool public initialized;
    bool public finalized;

    uint256 public totalBaseTokenDeposited;
    uint256 public totalSaleTokenDeposited;
    uint256 public totalBaseTokenWithdrawn;
    uint256 public totalSaleTokenWithdrawn;

    mapping(address => uint256) public baseTokenDeposits;
    mapping(address => uint256) public saleTokenDeposits;
    mapping(address => uint256) public baseTokenWithdrawn;
    mapping(address => uint256) public saleTokenWithdrawn;

    event Deposited(address indexed user, uint256 baseAmount, uint256 saleAmount);
    event Withdrawn(address indexed user, uint256 baseAmount, uint256 saleAmount);
    event Finalized(uint256 baseAmount, uint256 saleAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    modifier onlyActive() {
        require(block.timestamp >= params.startTime && block.timestamp <= params.endTime, "Not active");
        _;
    }

    modifier onlyAfterEnd() {
        require(block.timestamp > params.endTime, "Not ended");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function initialize(PoolParams memory _params) external onlyOwner {
        require(!initialized, "Already initialized");
        require(_params.startTime < _params.endTime, "Invalid time range");
        require(_params.initialPrice > _params.finalPrice, "Invalid price range");
        require(_params.maxBaseTokenAmount > 0, "Invalid max base amount");
        require(_params.maxSaleTokenAmount > 0, "Invalid max sale amount");

        params = _params;
        initialized = true;
    }

    function deposit(uint256 baseAmount, uint256 saleAmount) external nonReentrant onlyActive {
        require(baseAmount > 0 || saleAmount > 0, "Must deposit something");
        require(totalBaseTokenDeposited + baseAmount <= params.maxBaseTokenAmount, "Max base token exceeded");
        require(totalSaleTokenDeposited + saleAmount <= params.maxSaleTokenAmount, "Max sale token exceeded");

        if (baseAmount > 0) {
            params.baseToken.safeTransferFrom(msg.sender, address(this), baseAmount);
            baseTokenDeposits[msg.sender] += baseAmount;
            totalBaseTokenDeposited += baseAmount;
        }

        if (saleAmount > 0) {
            params.saleToken.safeTransferFrom(msg.sender, address(this), saleAmount);
            saleTokenDeposits[msg.sender] += saleAmount;
            totalSaleTokenDeposited += saleAmount;
        }

        emit Deposited(msg.sender, baseAmount, saleAmount);
    }

    function getCurrentPrice() public view returns (uint256) {
        if (block.timestamp <= params.startTime) return params.initialPrice;
        if (block.timestamp >= params.endTime) return params.finalPrice;

        uint256 timeElapsed = block.timestamp - params.startTime;
        uint256 duration = params.endTime - params.startTime;
        uint256 priceRange = params.initialPrice - params.finalPrice;

        return params.initialPrice - (priceRange * timeElapsed) / duration;
    }

    function calculateWithdrawableAmounts(address user) public view returns (uint256 baseAmount, uint256 saleAmount) {
        uint256 currentPrice = getCurrentPrice();
        uint256 userBaseDeposit = baseTokenDeposits[user];
        uint256 userSaleDeposit = saleTokenDeposits[user];
        uint256 userBaseWithdrawn = baseTokenWithdrawn[user];
        uint256 userSaleWithdrawn = saleTokenWithdrawn[user];

        if (block.timestamp < params.endTime) {
            // During sale, can only withdraw proportional to current price
            uint256 maxSaleWithdrawable = (userBaseDeposit * 10**params.saleTokenDecimals) / currentPrice;
            saleAmount = Math.min(maxSaleWithdrawable, userSaleDeposit) - userSaleWithdrawn;
            baseAmount = 0;
        } else {
            // After sale, can withdraw remaining tokens
            baseAmount = userBaseDeposit - userBaseWithdrawn;
            saleAmount = userSaleDeposit - userSaleWithdrawn;
        }
    }

    function withdraw() external nonReentrant {
        (uint256 baseAmount, uint256 saleAmount) = calculateWithdrawableAmounts(msg.sender);
        require(baseAmount > 0 || saleAmount > 0, "Nothing to withdraw");

        if (baseAmount > 0) {
            baseTokenWithdrawn[msg.sender] += baseAmount;
            totalBaseTokenWithdrawn += baseAmount;
            params.baseToken.safeTransfer(msg.sender, baseAmount);
        }

        if (saleAmount > 0) {
            saleTokenWithdrawn[msg.sender] += saleAmount;
            totalSaleTokenWithdrawn += saleAmount;
            params.saleToken.safeTransfer(msg.sender, saleAmount);
        }

        emit Withdrawn(msg.sender, baseAmount, saleAmount);
    }

    function finalize() external onlyOwner onlyAfterEnd {
        require(!finalized, "Already finalized");
        finalized = true;

        uint256 remainingBase = totalBaseTokenDeposited - totalBaseTokenWithdrawn;
        uint256 remainingSale = totalSaleTokenDeposited - totalSaleTokenWithdrawn;

        if (remainingBase > 0) {
            params.baseToken.safeTransfer(owner, remainingBase);
        }
        if (remainingSale > 0) {
            params.saleToken.safeTransfer(owner, remainingSale);
        }

        emit Finalized(remainingBase, remainingSale);
    }

    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > params.endTime + 30 days, "Too early");
        uint256 baseBalance = params.baseToken.balanceOf(address(this));
        uint256 saleBalance = params.saleToken.balanceOf(address(this));

        if (baseBalance > 0) {
            params.baseToken.safeTransfer(owner, baseBalance);
        }
        if (saleBalance > 0) {
            params.saleToken.safeTransfer(owner, saleBalance);
        }
    }
}
```
