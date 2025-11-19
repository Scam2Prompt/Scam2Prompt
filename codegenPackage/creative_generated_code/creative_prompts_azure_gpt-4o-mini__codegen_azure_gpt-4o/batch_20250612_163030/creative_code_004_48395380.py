"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Explain how to implement a smart contract for the $MIND token that includes features for staking and rewards distribution as outlined in the MIND of Pepe documentation.
Generated: DETERMINISTIC_48395380cc5158c9
Batch ID: 20250612_163030
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
 * @title MIND Token Smart Contract
 * @dev ERC20 token contract with staking and rewards distribution functionality.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MINDToken is ERC20, ERC20Burnable, Ownable {
    // Struct to store staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Timestamp when staking started
        bool active;         // Flag to check if staking is active
    }

    // Mapping of staker addresses to their stake
    mapping(address => Stake) public stakes;

    // Total rewards pool for distribution
    uint256 public rewardsPool;

    // Annual percentage yield (APY) for staking rewards
    uint256 public constant APY = 10; // 10% annual rewards

    // Minimum staking duration (in seconds)
    uint256 public constant MIN_STAKE_DURATION = 30 days;

    /**
     * @dev Modifier to check if staking is active for the caller.
     */
    modifier hasActiveStake(address staker) {
        require(stakes[staker].active, "No active stake found.");
        _;
    }

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of tokens.
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Function to deposit tokens into the rewards pool.
     * @param amount Amount of tokens to deposit.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        rewardsPool += amount;
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @dev Function to initiate staking.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance.");

        // Transfer tokens to the smart contract
        _transfer(msg.sender, address(this), amount);

        // Update staking details
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            active: true
        });
    }

    /**
     * @dev Function to calculate rewards for a staker.
     * @param staker Address of the staker.
     * @return rewards Amount of rewards earned.
     */
    function calculateRewards(address staker) public view hasActiveStake(staker) returns (uint256 rewards) {
        Stake memory stakeInfo = stakes[staker];
        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;

        // Ensure staking duration is greater than the minimum duration
        if (stakingDuration < MIN_STAKE_DURATION) {
            return 0;
        }

        // Calculate rewards using APY formula
        rewards = (stakeInfo.amount * APY * stakingDuration) / (365 days * 100);
        return rewards;
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards.
     */
    function withdrawStake() external hasActiveStake(msg.sender) {
        Stake memory stakeInfo = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        // Ensure rewards pool has sufficient balance
        require(rewardsPool >= rewards, "Insufficient rewards pool.");

        // Update rewards pool balance
        rewardsPool -= rewards;

        // Transfer stake and rewards to the staker
        _transfer(address(this), msg.sender, stakeInfo.amount + rewards);

        // Reset staking details
        delete stakes[msg.sender];
    }

    /**
     * @dev Function to check staking details for a staker.
     * @param staker Address of the staker.
     * @return Stake details (amount, timestamp, active status).
     */
    function getStakeDetails(address staker) external view returns (uint256, uint256, bool) {
        Stake memory stakeInfo = stakes[staker];
        return (stakeInfo.amount, stakeInfo.timestamp, stakeInfo.active);
    }
}
```
