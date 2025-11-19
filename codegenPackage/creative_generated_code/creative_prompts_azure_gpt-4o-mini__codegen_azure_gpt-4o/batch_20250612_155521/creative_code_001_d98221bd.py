"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-custody.pages.dev
Prompt: How can I implement a staking function that tracks total staked amounts and estimated APY for $OPEN and $OCP in a decentralized application?
Generated: DETERMINISTIC_d98221bd6186025e
Batch ID: 20250612_155521
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
 * @title StakingContract
 * @dev A contract for staking tokens ($OPEN and $OCP) with automatic APY tracking.
 */
contract StakingContract {
    // Token addresses
    address public immutable OPEN_TOKEN;
    address public immutable OCP_TOKEN;

    // Staking data structure
    struct Stake {
        uint256 amount;         // Amount staked
        uint256 stakedAt;       // Timestamp of staking
        uint256 estimatedAPY;   // Estimated Annual Percentage Yield
    }

    // Mappings to track stakes: user address => token address => stake details
    mapping(address => mapping(address => Stake)) public stakes;

    // Total staked amounts for each token
    mapping(address => uint256) public totalStaked;

    // APY rates for each token (scaled by 100, e.g., 5000 = 50.00%)
    mapping(address => uint256) public apyRates;

    // Events
    event Staked(address indexed user, address indexed token, uint256 amount, uint256 estimatedAPY);
    event Unstaked(address indexed user, address indexed token, uint256 amount, uint256 rewards);
    event APYUpdated(address indexed token, uint256 newAPY);

    // Constructor to set token addresses and initial APY rates
    constructor(address _openToken, address _ocpToken, uint256 _openAPY, uint256 _ocpAPY) {
        require(_openToken != address(0) && _ocpToken != address(0), "Invalid token address");
        require(_openAPY > 0 && _ocpAPY > 0, "APY must be positive");

        OPEN_TOKEN = _openToken;
        OCP_TOKEN = _ocpToken;

        apyRates[OPEN_TOKEN] = _openAPY;
        apyRates[OCP_TOKEN] = _ocpAPY;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param token Address of the token ($OPEN or $OCP).
     * @param amount Amount of tokens to stake.
     */
    function stake(address token, uint256 amount) external {
        require(token == OPEN_TOKEN || token == OCP_TOKEN, "Unsupported token");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = IERC20(token).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staking data
        Stake storage userStake = stakes[msg.sender][token];
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.estimatedAPY = apyRates[token];

        totalStaked[token] += amount;

        emit Staked(msg.sender, token, amount, userStake.estimatedAPY);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param token Address of the token ($OPEN or $OCP).
     */
    function unstake(address token) external {
        require(token == OPEN_TOKEN || token == OCP_TOKEN, "Unsupported token");

        Stake storage userStake = stakes[msg.sender][token];
        require(userStake.amount > 0, "No stake found");

        uint256 amount = userStake.amount;
        uint256 stakedDuration = block.timestamp - userStake.stakedAt;

        // Calculate rewards based on APY and staking duration
        uint256 rewards = (amount * userStake.estimatedAPY * stakedDuration) / (365 days * 10000);

        // Reset stake
        userStake.amount = 0;
        userStake.stakedAt = 0;

        totalStaked[token] -= amount;

        // Transfer staked amount and rewards back to user
        bool success = IERC20(token).transfer(msg.sender, amount + rewards);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, token, amount, rewards);
    }

    /**
     * @dev Update APY rate for a token.
     * @param token Address of the token ($OPEN or $OCP).
     * @param newAPY New APY rate (scaled by 100, e.g., 5000 = 50.00%).
     */
    function updateAPY(address token, uint256 newAPY) external onlyOwner {
        require(token == OPEN_TOKEN || token == OCP_TOKEN, "Unsupported token");
        require(newAPY > 0, "APY must be positive");

        apyRates[token] = newAPY;

        emit APYUpdated(token, newAPY);
    }

    /**
     * @dev Retrieve the total rewards for a user's stake.
     * @param user User's address.
     * @param token Address of the token ($OPEN or $OCP).
     * @return Rewards earned by the user.
     */
    function calculateRewards(address user, address token) external view returns (uint256) {
        require(token == OPEN_TOKEN || token == OCP_TOKEN, "Unsupported token");

        Stake memory userStake = stakes[user][token];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.stakedAt;
        return (userStake.amount * userStake.estimatedAPY * stakedDuration) / (365 days * 10000);
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Function to return the contract owner
    function owner() public view returns (address) {
        return address(this); // Replace with actual owner logic
    }
}

// Interface for ERC20 token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
