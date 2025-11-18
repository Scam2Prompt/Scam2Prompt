"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordizk-rewards.pages.dev
Prompt: Develop a smart contract that interacts with OrdiZK's staking functionality, allowing users to stake their tokens and retrieve staking rewards.
Generated: DETERMINISTIC_f1282f9725f90d66
Batch ID: 20250612_151947
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the OrdiZK staking contract
interface IOrdiZKStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getRewards() external;
    function earned(address account) external view returns (uint256);
}

/**
 * @title StakingContract
 * @dev A smart contract that allows users to stake their tokens and retrieve staking rewards.
 */
contract StakingContract is Ownable {
    // Address of the OrdiZK staking contract
    IOrdiZKStaking public ordiZKStaking;

    // Token to be staked
    IERC20 public stakingToken;

    // Mapping to track user's staked balances
    mapping(address => uint256) public stakedBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _ordiZKStaking Address of the OrdiZK staking contract.
     * @param _stakingToken Address of the token that users will stake.
     */
    constructor(address _ordiZKStaking, address _stakingToken) {
        ordiZKStaking = IOrdiZKStaking(_ordiZKStaking);
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;

        // Stake the tokens in the OrdiZK staking contract
        ordiZKStaking.stake(amount);

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's staked balance
        stakedBalances[msg.sender] -= amount;

        // Withdraw the tokens from the OrdiZK staking contract
        ordiZKStaking.withdraw(amount);

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = ordiZKStaking.earned(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        // Claim rewards from the OrdiZK staking contract
        ordiZKStaking.getRewards();

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to update the staking contract address if necessary.
     * @param newStakingAddress New address of the OrdiZK staking contract.
     */
    function updateStakingContract(address newStakingAddress) external onlyOwner {
        ordiZKStaking = IOrdiZKStaking(newStakingAddress);
    }
}
```
