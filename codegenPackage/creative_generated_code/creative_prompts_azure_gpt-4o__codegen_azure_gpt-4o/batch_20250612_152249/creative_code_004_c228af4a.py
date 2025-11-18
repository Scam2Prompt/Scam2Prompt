"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Develop a staking protocol in Solidity for a blockchain-based platform like Pushd, allowing users to stake tokens and earn interest ranging from 7% to 17%.
Generated: DETERMINISTIC_c228af4a8f6a704d
Batch ID: 20250612_152249
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
 * @title StakingProtocol
 * @dev A smart contract for token staking that allows users to stake tokens and earn interest.
 */
contract StakingProtocol {
    // State variables
    address public owner; // Owner of the contract
    uint256 constant MIN_INTEREST_RATE = 7; // Minimum interest rate (%)
    uint256 constant MAX_INTEREST_RATE = 17; // Maximum interest rate (%)
    uint256 constant SECONDS_IN_A_YEAR = 365 days; // Seconds in a year for annual calculation

    IERC20 public stakingToken; // ERC20 token used for staking

    struct Stake {
        uint256 amount; // Staked amount by the user
        uint256 startTime; // Timestamp of when the staking started
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake
    mapping(address => uint256) public rewards; // Mapping of user address to their rewards

    // Events for logging and transparency
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _stakingToken) {
        owner = msg.sender; // Set the contract deployer as the owner
        stakingToken = IERC20(_stakingToken); // Set the staking token
    }

    /**
     * @dev Allows users to stake a specified amount of tokens.
     * @param amount Amount of tokens to be staked.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");

        // Transfer tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed."
        );

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No staked tokens to withdraw.");

        // Calculate any pending rewards
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward;

        // Transfer staked tokens back to the user
        uint256 amount = userStake.amount;
        stakes[msg.sender].amount = 0; // Reset the staked amount
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed."
        );

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their earned rewards.
     */
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender) + rewards[msg.sender];
        require(reward > 0, "No rewards to claim.");

        rewards[msg.sender] = 0; // Reset rewards

        // Transfer rewards to the user
        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed."
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their stake duration and amount.
     * @param user Address of the user whose reward is being calculated.
     * @return reward Calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];

        if (userStake.amount == 0) {
            return 0; // No staked tokens, no reward
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate interest rate based on staking duration
        uint256 interestRate = MIN_INTEREST_RATE +
            ((stakingDuration / SECONDS_IN_A_YEAR) *
                (MAX_INTEREST_RATE - MIN_INTEREST_RATE));
        if (interestRate > MAX_INTEREST_RATE) {
            interestRate = MAX_INTEREST_RATE;
        }

        // Calculate reward
        uint256 reward = (userStake.amount * interestRate * stakingDuration) /
            (100 * SECONDS_IN_A_YEAR);
        return reward;
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawContractTokens(uint256 amount) external onlyOwner {
        require(
            stakingToken.transfer(owner, amount),
            "Token transfer failed."
        );
    }
}

// Minimal IERC20 interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
