"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized betting platform that incorporates token staking functionality, similar to the $BCB staking system described on Blockchain Bets.
Generated: DETERMINISTIC_7cfc38d1f64cdce7
Batch ID: 20250612_153420
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
 * @title Decentralized Betting Platform with Token Staking
 * @notice This smart contract allows users to stake tokens, place bets, 
 *         and claim rewards in a decentralized environment.
 */
contract DecentralizedBettingPlatform {
    // Token staking variables
    IERC20 public token;
    uint256 public stakingFeePercentage; // Fee percentage for staking (e.g., 2%)
    uint256 public totalStaked;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Betting variables
    struct Bet {
        uint256 amount;
        uint256 odds; // Odds in percentage (e.g., 150 for 1.5x)
        bool active;
    }
    mapping(address => Bet) public bets;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event BetPlaced(address indexed user, uint256 amount, uint256 odds);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking token and fee percentage.
     * @param _token Address of the ERC20 token used for staking.
     * @param _stakingFeePercentage Fee percentage for staking.
     */
    constructor(IERC20 _token, uint256 _stakingFeePercentage) {
        require(
            _stakingFeePercentage <= 100,
            "Invalid staking fee percentage"
        );
        token = _token;
        stakingFeePercentage = _stakingFeePercentage;
    }

    /**
     * @dev Stakes tokens into the platform.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        uint256 fee = (_amount * stakingFeePercentage) / 100;
        uint256 netAmount = _amount - fee;

        // Transfer tokens from user to contract
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking data
        stakes[msg.sender] += netAmount;
        totalStaked += netAmount;

        emit Staked(msg.sender, netAmount);
    }

    /**
     * @dev Unstakes tokens from the platform.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake");

        // Update staking data
        stakes[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Places a bet on the platform.
     * @param _amount Amount of tokens to bet.
     * @param _odds Odds in percentage (e.g., 150 for 1.5x).
     */
    function placeBet(uint256 _amount, uint256 _odds) external {
        require(_amount > 0, "Cannot bet zero tokens");
        require(_odds > 100, "Odds must be greater than 100%");

        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount >= _amount, "Insufficient staked tokens");

        // Deduct bet amount from user's stake
        stakes[msg.sender] -= _amount;

        // Create or update the bet
        bets[msg.sender] = Bet({
            amount: _amount,
            odds: _odds,
            active: true
        });

        emit BetPlaced(msg.sender, _amount, _odds);
    }

    /**
     * @dev Claims the reward for a winning bet.
     */
    function claimReward() external {
        Bet storage userBet = bets[msg.sender];
        require(userBet.active, "No active bet found");

        // Calculate the reward based on odds
        uint256 reward = (userBet.amount * userBet.odds) / 100;

        // Clear the bet
        userBet.active = false;
        userBet.amount = 0;
        userBet.odds = 0;

        // Transfer the reward to the user
        require(token.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Retrieves the current stake of a user.
     * @param _user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStake(address _user) external view returns (uint256) {
        return stakes[_user];
    }

    /**
     * @dev Retrieves the details of a user's bet.
     * @param _user Address of the user.
     * @return The amount, odds, and active status of the user's bet.
     */
    function getBet(address _user)
        external
        view
        returns (uint256 amount, uint256 odds, bool active)
    {
        Bet memory userBet = bets[_user];
        return (userBet.amount, userBet.odds, userBet.active);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
