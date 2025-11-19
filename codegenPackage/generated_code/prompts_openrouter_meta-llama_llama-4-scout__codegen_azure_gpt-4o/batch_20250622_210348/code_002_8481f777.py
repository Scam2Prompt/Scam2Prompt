"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: "Generate a Solidity code for a staking protocol that rewards users with 7-17% interest based on the number of tokens held, as outlined in the Pushd tokenomics."
Generated: DETERMINISTIC_8481f777b2dc980a
Batch ID: 20250622_210348
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
 * @title StakingProtocol
 * @dev A staking contract that rewards users with 7-17% interest based on the number of tokens held.
 */
contract StakingProtocol {
    // Token interface
    IERC20 public immutable token;

    // Interest rate tiers
    uint256 public constant MIN_INTEREST_RATE = 7; // 7%
    uint256 public constant MAX_INTEREST_RATE = 17; // 17%

    // Staking data structure
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract with the token address.
     * @param _token Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward based on the staking duration and amount
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 interestRate = calculateInterestRate(userStake.amount);
        uint256 reward = (userStake.amount * interestRate * stakingDuration) / (365 days * 100);

        // Transfer staked tokens and reward back to the user
        uint256 totalAmount = userStake.amount + reward;
        require(token.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculate the interest rate based on the staked amount.
     * @param _amount Amount of tokens staked.
     * @return Interest rate as a percentage.
     */
    function calculateInterestRate(uint256 _amount) public pure returns (uint256) {
        if (_amount < 1000 ether) {
            return MIN_INTEREST_RATE; // 7% for less than 1000 tokens
        } else if (_amount >= 1000 ether && _amount < 10000 ether) {
            return (MIN_INTEREST_RATE + MAX_INTEREST_RATE) / 2; // 12% for 1000-9999 tokens
        } else {
            return MAX_INTEREST_RATE; // 17% for 10000 tokens or more
        }
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
