"""
Generated Code Metadata:
========================
Original URL: https://staking-wisdomise.pages.dev
Prompt: Generate a Solidity code snippet for a smart contract that implements a 365-day lock term staking pool with a 28.39% reward and 0% NFT boost for WSDM tokens on the Polygon Mainnet.
Generated: DETERMINISTIC_5086561d747dc1c7
Batch ID: 20250622_205836
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
 * @title WSDM Staking Pool
 * @dev Implements a 365-day lock term staking pool with a fixed reward of 28.39%.
 *      No NFT boost is applied. This contract is designed for WSDM tokens on the Polygon Mainnet.
 */
contract WSDMStakingPool {
    // State variables
    address public owner; // Contract owner
    IERC20 public wsdmToken; // WSDM token contract
    uint256 public constant LOCK_PERIOD = 365 days; // Lock period for staking
    uint256 public constant REWARD_RATE = 2839; // Reward rate (28.39% expressed as 2839 basis points)
    uint256 public constant BASIS_POINTS = 10000; // Basis points for reward calculation

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool claimed; // Whether the reward has been claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found for this user");
        _;
    }

    modifier lockPeriodPassed(address _user) {
        require(
            block.timestamp >= stakes[_user].startTime + LOCK_PERIOD,
            "Lock period has not passed yet"
        );
        _;
    }

    // Constructor
    constructor(address _wsdmToken) {
        require(_wsdmToken != address(0), "Invalid token address");
        owner = msg.sender;
        wsdmToken = IERC20(_wsdmToken);
    }

    /**
     * @dev Allows users to stake WSDM tokens.
     * @param _amount The amount of WSDM tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            stakes[msg.sender].amount == 0,
            "You already have an active stake"
        );

        // Transfer WSDM tokens from the user to the contract
        require(
            wsdmToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Record the stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            claimed: false
        });

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to claim their staking rewards after the lock period.
     */
    function claimReward() external hasStake(msg.sender) lockPeriodPassed(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(!userStake.claimed, "Reward already claimed");

        // Calculate reward
        uint256 reward = (userStake.amount * REWARD_RATE) / BASIS_POINTS;

        // Mark reward as claimed
        userStake.claimed = true;

        // Transfer staked amount + reward back to the user
        uint256 totalAmount = userStake.amount + reward;
        require(
            wsdmToken.transfer(msg.sender, totalAmount),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in the contract.
     *      This function should only be used in case of emergency or contract deprecation.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(
            wsdmToken.transfer(owner, _amount),
            "Token transfer failed"
        );
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
