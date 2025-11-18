"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytradefinance.com
Prompt: Write a smart contract in Solidity for staking $SHE tokens on the Arbitrum blockchain, ensuring the ability to calculate APY and distribute rewards based on the SHE Protocol's yield farming mechanism.
Generated: DETERMINISTIC_ec20bfc9a7ae2e48
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
 * @title SHE Token Staking Contract
 * @dev This contract allows users to stake SHE tokens on the Arbitrum blockchain.
 * It calculates APY and distributes rewards based on the SHE Protocol's yield farming mechanism.
 */
contract SHEStaking {
    // SHE token interface
    IERC20 public sheToken;

    // Data structure for storing staking information for each user
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 startTime;   // Timestamp when staking started
        uint256 rewardDebt;  // Rewards already withdrawn
    }

    // Mapping to track stakes for each address
    mapping(address => Stake) private stakes;

    // APY for staking (e.g., 10% = 1000, 5% = 500)
    uint256 public apy;

    // Number of seconds in a year
    uint256 private constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize SHE token and APY.
     * @param _sheToken Address of the SHE token contract.
     * @param _apy Annual Percentage Yield (APY) for staking rewards.
     */
    constructor(address _sheToken, uint256 _apy) {
        require(_sheToken != address(0), "Invalid SHE token address");
        require(_apy > 0, "APY must be greater than zero");

        sheToken = IERC20(_sheToken);
        apy = _apy;
    }

    /**
     * @dev Stakes SHE tokens in the contract.
     * @param _amount Amount of SHE tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer SHE tokens from sender to contract
        require(sheToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];

        // If user already has active stake, distribute pending rewards before adding new stake
        if (userStake.amount > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            userStake.rewardDebt += pendingReward;
        }

        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes SHE tokens and distributes pending rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        // Calculate pending rewards
        uint256 pendingReward = calculateReward(msg.sender);

        // Transfer staked tokens and rewards back to the user
        uint256 totalRewards = pendingReward + userStake.rewardDebt;
        require(sheToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(sheToken.transfer(msg.sender, totalRewards), "Reward transfer failed");

        emit Unstaked(msg.sender, userStake.amount);
        emit RewardWithdrawn(msg.sender, totalRewards);

        // Reset user's stake
        delete stakes[msg.sender];
    }

    /**
     * @dev Calculates pending rewards for the caller.
     * @return Total rewards earned by the caller.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate time elapsed since staking started
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate rewards based on APY
        uint256 reward = (userStake.amount * apy * stakingDuration) / (SECONDS_IN_YEAR * 10000);

        return reward;
    }

    /**
     * @dev Allows the owner to update APY.
     * @param _newApy New APY for staking rewards.
     */
    function updateAPY(uint256 _newApy) external onlyOwner {
        require(_newApy > 0, "APY must be greater than zero");
        apy = _newApy;
    }

    /**
     * @dev Modifier to check if the caller is the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @dev Returns the contract owner.
     * @return Address of the contract owner.
     */
    function owner() public view returns (address) {
        return tx.origin; // Replace with actual ownership logic for production-grade contract
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

Note: Ensure that ownership-related functionality (`owner` and `onlyOwner`) is replaced with a more robust approach (e.g., using `Ownable` from OpenZeppelin) in production.
