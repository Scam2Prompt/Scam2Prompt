"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Describe how to build a decentralized application (dApp) on Berachain using its modular EVM-compatible features.
Generated: DETERMINISTIC_0c02e4adde49c211
Batch ID: 20250612_160853
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title Berachain dApp Example
 * @dev A simple ERC20 token with staking functionality demonstrating Berachain's EVM compatibility
 */
contract BerachainDapp is ERC20, Ownable {
    using Address for address payable;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Token parameters
    uint256 public constant MAX_SUPPLY = 1_000_000 ether;
    uint256 public constant STAKING_REWARD_RATE = 10; // 10% annual reward

    // Staking state
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    // Events
    event TokensMinted(address indexed to, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Constructor that mints initial supply to contract deployer
     */
    constructor() ERC20("Berachain Token", "BRC") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate pending reward before updating stake
        uint256 pendingReward = calculateReward(msg.sender);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update stake
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            timestamp: block.timestamp
        });

        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update stake
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked -= amount;

        // Transfer staked tokens and reward back to user
        _transfer(address(this), msg.sender, amount);
        _mint(msg.sender, reward);

        emit TokensUnstaked(msg.sender, amount, reward);
    }

    /**
     * @dev Calculate current reward for a staker
     * @param staker Address of the staker
     * @return reward The calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256 reward) {
        Stake memory stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        uint256 annualReward = (stakeInfo.amount * STAKING_REWARD_RATE) / 100;
        reward = (annualReward * stakingDuration) / 365 days;
    }

    /**
     * @dev Claim rewards without unstaking
     */
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Mint reward tokens
        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token contract
     * @param amount Amount to withdraw
     */
    function rescueTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}

/**
 * @title Berachain dApp Factory
 * @dev Factory contract to deploy multiple instances of BerachainDapp
 */
contract BerachainDappFactory {
    address[] public deployedDapps;

    event DappCreated(address indexed dappAddress, address indexed creator);

    /**
     * @dev Create a new BerachainDapp instance
     */
    function createDapp() external returns (address) {
        BerachainDapp newDapp = new BerachainDapp();
        deployedDapps.push(address(newDapp));
        emit DappCreated(address(newDapp), msg.sender);
        return address(newDapp);
    }

    /**
     * @dev Get count of deployed dApps
     */
    function getDappCount() external view returns (uint256) {
        return deployedDapps.length;
    }
}
```
