"""
Generated Code Metadata:
========================
Original URL: https://front-1.pointech.cloud
Prompt: Develop a PointPay Token (PXP) utility function in Solidity, enabling token holders to pay trading fees and earn higher yields from staking.
Generated: DETERMINISTIC_2748535188ba0149
Batch ID: 20250622_204749
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

/**
 * @title PointPay Token Utility Contract
 * @dev This contract enables PXP token holders to pay trading fees and earn higher yields from staking.
 */
contract PointPayTokenUtility {
    // State variables
    address public owner; // Contract owner
    IERC20 public pxpToken; // PXP token contract address
    uint256 public tradingFeeRate; // Trading fee rate in percentage (e.g., 1% = 100)
    uint256 public stakingYieldRate; // Staking yield rate in percentage (e.g., 5% = 500)

    mapping(address => uint256) public stakedBalances; // Tracks staked balances of users
    mapping(address => uint256) public stakingStartTime; // Tracks staking start time for users

    // Events
    event TradingFeePaid(address indexed user, uint256 amount);
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount, uint256 yieldEarned);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(address _pxpToken, uint256 _tradingFeeRate, uint256 _stakingYieldRate) {
        require(_pxpToken != address(0), "Invalid token address");
        require(_tradingFeeRate > 0, "Trading fee rate must be greater than zero");
        require(_stakingYieldRate > 0, "Staking yield rate must be greater than zero");

        owner = msg.sender;
        pxpToken = IERC20(_pxpToken);
        tradingFeeRate = _tradingFeeRate;
        stakingYieldRate = _stakingYieldRate;
    }

    /**
     * @dev Allows users to pay trading fees using PXP tokens.
     * @param amount The amount of trading fees to pay.
     */
    function payTradingFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        uint256 fee = (amount * tradingFeeRate) / 10000; // Calculate fee based on rate
        require(pxpToken.transferFrom(msg.sender, address(this), fee), "Token transfer failed");

        emit TradingFeePaid(msg.sender, fee);
    }

    /**
     * @dev Allows users to stake PXP tokens to earn higher yields.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pxpToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim yield.
     */
    function unstakeTokens() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 yieldEarned = (stakedAmount * stakingYieldRate * stakingDuration) / (10000 * 365 days);

        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        require(pxpToken.transfer(msg.sender, stakedAmount + yieldEarned), "Token transfer failed");

        emit TokensUnstaked(msg.sender, stakedAmount, yieldEarned);
    }

    /**
     * @dev Updates the trading fee rate. Only callable by the owner.
     * @param _tradingFeeRate The new trading fee rate.
     */
    function updateTradingFeeRate(uint256 _tradingFeeRate) external onlyOwner {
        require(_tradingFeeRate > 0, "Trading fee rate must be greater than zero");
        tradingFeeRate = _tradingFeeRate;
    }

    /**
     * @dev Updates the staking yield rate. Only callable by the owner.
     * @param _stakingYieldRate The new staking yield rate.
     */
    function updateStakingYieldRate(uint256 _stakingYieldRate) external onlyOwner {
        require(_stakingYieldRate > 0, "Staking yield rate must be greater than zero");
        stakingYieldRate = _stakingYieldRate;
    }

    /**
     * @dev Withdraws PXP tokens from the contract. Only callable by the owner.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(pxpToken.transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
