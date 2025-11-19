"""
Generated Code Metadata:
========================
Original URL: https://presale-alainetwork.pages.dev
Prompt: Generate a smart contract code in Solidity that handles token staking and dividend distribution for a cryptocurrency platform like ALAI Network.
Generated: DETERMINISTIC_f7e3d9fe44ee761e
Batch ID: 20250622_212813
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for token staking and dividend distribution
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastClaimed;  // Last time dividends were claimed
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // The token used for staking
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when dividends are claimed
    event DividendsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimed = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim dividends based on staked amount
    function claimDividends() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 dividends = calculateDividends(msg.sender);
        require(dividends > 0, "No dividends to claim");

        // Update last claimed time
        staker.lastClaimed = block.timestamp;

        // Transfer dividends to the staker
        require(stakingToken.transfer(msg.sender, dividends), "Transfer failed");

        emit DividendsClaimed(msg.sender, dividends);
    }

    // Internal function to calculate dividends for a staker
    function calculateDividends(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        // Example dividend calculation (this should be replaced with actual logic)
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        uint256 dividendRate = 1e18; // Example rate (1 token per second per staked token)
        return (staker.amountStaked * timeStaked * dividendRate) / 1e18;
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
