"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbulltoken.pages.dev
Prompt: Generate a smart contract in Solidity for staking $BTCBULL tokens that rewards users with Bitcoin airdrops as the price of Bitcoin increases.
Generated: DETERMINISTIC_86bfb30cd9e37375
Batch ID: 20250612_161041
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

/**
 * @title BTCBULL Staking Contract with Bitcoin Rewards
 * @dev This contract allows users to stake their BTCBULL tokens and receive Bitcoin airdrop rewards
 *      based on the price appreciation of Bitcoin.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

interface IPriceFeed {
    function latestPrice() external view returns (uint256);
}

contract BTCBULLStaking {
    IERC20 private immutable btcBullToken;
    IERC20 private immutable bitcoinToken;
    IPriceFeed private immutable priceFeed;

    uint256 public lastRecordedPrice;
    address public owner;

    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 reward);
    event PriceUpdated(uint256 oldPrice, uint256 newPrice);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _btcBullToken, address _bitcoinToken, address _priceFeed) {
        btcBullToken = IERC20(_btcBullToken);
        bitcoinToken = IERC20(_bitcoinToken);
        priceFeed = IPriceFeed(_priceFeed);
        owner = msg.sender;
        lastRecordedPrice = priceFeed.latestPrice();
    }

    /**
     * @dev Allows users to stake BTCBULL tokens.
     * @param _amount The amount of BTCBULL tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        require(btcBullToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake BTCBULL tokens.
     * @param _amount The amount of BTCBULL tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot unstake zero tokens");
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        staker.stakedAmount -= _amount;
        require(btcBullToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distributes Bitcoin rewards to stakers based on the price increase of Bitcoin.
     */
    function distributeRewards() external onlyOwner {
        uint256 currentPrice = priceFeed.latestPrice();
        require(currentPrice > lastRecordedPrice, "Bitcoin price did not increase");

        uint256 priceDifference = currentPrice - lastRecordedPrice;

        for (address account : getAllStakers()) { // getAllStakers() is assumed to return all staking accounts
            Staker storage staker = stakers[account];
