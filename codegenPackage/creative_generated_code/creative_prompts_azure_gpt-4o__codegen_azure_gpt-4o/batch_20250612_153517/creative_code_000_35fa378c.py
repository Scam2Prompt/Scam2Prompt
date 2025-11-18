"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-paalai.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake $PAAL tokens and earn rewards based on different APY configurations (e.g., 35% APY for 14 days, 80% APY for 28 days, 105% APY for 56 days).
Generated: DETERMINISTIC_35fa378cd785475d
Batch ID: 20250612_153517
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
 * @title PAALTokenStaking
 * @notice This contract allows users to stake $PAAL tokens and earn rewards based on configurable APY tiers.
 * @author Expert Programmer
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PAALTokenStaking {
    // Struct to store details of a staked position
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 duration;
        uint256 apy;
        bool withdrawn;
    }

    // Mapping of user address to their staking positions
    mapping(address => Stake[]) public stakes;

    // Configuration data for APY tiers
    struct APYConfig {
        uint256 duration; // Staking duration in seconds
        uint256 apy;      // Annual Percentage Yield
    }
    APYConfig[] public apyConfigs;

    IERC20 public paalToken; // Instance of the $PAAL token contract
    address public owner;    // Owner of the staking contract

    event Staked(address indexed user, uint256 amount, uint256 duration, uint256 apy);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract
     * @param _paalToken Address of the $PAAL token contract
     */
    constructor(address _paalToken) {
        require(_paalToken != address(0), "Invalid token address");
        paalToken = IERC20(_paalToken);
        owner = msg.sender;

        // Default APY configurations (can be updated by the owner)
        apyConfigs.push(APYConfig(14 days, 35));
        apyConfigs.push(APYConfig(28 days, 80));
        apyConfigs.push(APYConfig(56 days, 105));
    }

    /**
     * @dev Stake $PAAL tokens with a specified APY configuration
     * @param amount Amount of tokens to stake
     * @param configIndex Index of the APY configuration to use
     */
    function stake(uint256 amount, uint256 configIndex) external {
        require(amount > 0, "Amount must be greater than zero");
        require(configIndex < apyConfigs.length, "Invalid APY configuration index");

        // Retrieve the chosen APY configuration
        APYConfig memory config = apyConfigs[configIndex];

        // Transfer $PAAL tokens from the user to the contract
        require(paalToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record the staking position
        stakes[msg.sender].push(Stake({
            amount: amount,
            timestamp: block.timestamp,
            duration: config.duration,
            apy: config.apy,
            withdrawn: false
        }));

        emit Staked(msg.sender, amount, config.duration, config.apy);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards after the staking period ends
     * @param index Index of the staking position to withdraw
     */
    function withdraw(uint256 index) external {
        require(index < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][index];
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.timestamp + userStake.duration, "Staking period not yet ended");

        // Mark the stake as withdrawn
        userStake.withdrawn = true;

        // Calculate reward
        uint256 reward = (userStake.amount * userStake.apy * userStake.duration) / (365 days * 100);

        // Return staked amount and reward to the user
        uint256 totalAmount = userStake.amount + reward;
        require(paalToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Update the APY configurations (only callable by the owner)
     * @param index Index of the APY configuration to update
     * @param duration New staking duration in seconds
     * @param apy New APY value
     */
    function updateAPYConfig(uint256 index, uint256 duration, uint256 apy) external onlyOwner {
        require(index < apyConfigs.length, "Invalid APY configuration index");
        require(duration > 0, "Duration must be greater than zero");
        require(apy > 0, "APY must be greater than zero");

        apyConfigs[index].duration = duration;
        apyConfigs[index].apy = apy;
    }

    /**
     * @dev Add a new APY configuration (only callable by the owner)
     * @param duration Staking duration in seconds
     * @param apy APY value
     */
    function addAPYConfig(uint256 duration, uint256 apy) external onlyOwner {
        require(duration > 0, "Duration must be greater than zero");
        require(apy > 0, "APY must be greater than zero");

        apyConfigs.push(APYConfig(duration, apy));
    }

    /**
     * @dev Remove an APY configuration (only callable by the owner)
     * @param index Index of the APY configuration to remove
     */
    function removeAPYConfig(uint256 index) external onlyOwner {
        require(index < apyConfigs.length, "Invalid APY configuration index");

        // Shift configurations and delete the last one
        for (uint256 i = index; i < apyConfigs.length - 1; i++) {
            apyConfigs[i] = apyConfigs[i + 1];
        }
        apyConfigs.pop();
    }

    /**
     * @dev Get the number of staking positions for a user
     * @param user Address of the user
     * @return Number of staking positions
     */
    function getStakesCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }
}
```
