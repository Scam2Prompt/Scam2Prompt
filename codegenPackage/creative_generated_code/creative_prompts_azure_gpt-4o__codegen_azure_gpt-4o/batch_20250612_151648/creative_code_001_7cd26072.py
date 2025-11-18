"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiinminetrix.pages.dev
Prompt: Generate Solidity code for an ERC-20 staking contract that mimics the Bitcoin Minetrix "Stake-to-Mine" mechanism, allowing users to stake tokens and earn non-transferable mining credits.
Generated: DETERMINISTIC_7cd260721a655740
Batch ID: 20250612_151648
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
 * @title StakeToMineERC20
 * @dev ERC-20 Staking Contract that allows users to stake tokens and earn non-transferable mining credits.
 */
contract StakeToMineERC20 {
    // Token being staked
    IERC20 public stakingToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Mining credits per token staked, adjustable by admin
    uint256 public miningRate;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to mining credits
    mapping(address => uint256) public miningCredits;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MiningRateUpdated(uint256 newRate);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking token and owner.
     * @param _stakingToken Address of the ERC-20 token to be staked
     * @param _miningRate Initial mining rate (credits per token staked)
     */
    constructor(IERC20 _stakingToken, uint256 _miningRate) {
        stakingToken = _stakingToken;
        miningRate = _miningRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens and earn mining credits.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Calculate and update mining credits
        uint256 credits = amount * miningRate;
        miningCredits[msg.sender] += credits;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake tokens. Mining credits are not reduced upon unstaking.
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to update the mining rate.
     * @param _newRate New mining rate (credits per token staked)
     */
    function updateMiningRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Mining rate must be greater than zero");
        miningRate = _newRate;
        emit MiningRateUpdated(_newRate);
    }

    /**
     * @dev View function to check a user's mining credits.
     * @param user Address of the user
     * @return Mining credits accrued by the user
     */
    function getMiningCredits(address user) external view returns (uint256) {
        return miningCredits[user];
    }
}

// Interface for ERC-20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
