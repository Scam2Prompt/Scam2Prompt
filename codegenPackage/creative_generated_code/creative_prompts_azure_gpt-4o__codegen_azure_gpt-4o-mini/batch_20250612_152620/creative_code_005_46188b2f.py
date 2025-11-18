"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Develop a smart contract on Ethereum for staking $GBTC tokens, ensuring compatibility with Green Bitcoin's gamified staking rewards system.
Generated: DETERMINISTIC_46188b2f7682fbf0
Batch ID: 20250612_152620
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

// Importing interfaces for ERC20 token and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the gamified staking rewards
interface IRewardsSystem {
    function distributeRewards(address staker, uint256 amount) external;
}

// Smart contract for staking GBTC tokens
contract GBTCStaking is Ownable {
    // Token being staked
    IERC20 public gbtcToken;
    // Rewards distribution system
    IRewardsSystem public rewardsSystem;

    // Struct for staking data
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of staker address to their stakes
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with GBTC token and rewards system
    constructor(IERC20 _gbtcToken, IRewardsSystem _rewardsSystem) {
        gbtcToken = _gbtcToken;
        rewardsSystem = _rewardsSystem;
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer GBTC tokens from user to the contract
        gbtcToken.transferFrom(msg.sender, address(this), amount);

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GBTC tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes found");

        uint256 amountToUnstake = userStake.amount;

        // Reset stake before transferring to prevent reentrancy
        userStake.amount = 0;

        // Transfer GBTC tokens back to the user
        gbtcToken.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to distribute rewards to the stakers
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        for (uint i = 0; i < addresses.length; i++) {
            address staker = addresses[i];
            if (stakes[staker].amount > 0) {
                rewardsSystem.distributeRewards(staker, amount);
                emit RewardsDistributed(staker, amount);
            }
        }
    }

    // Function to get the staking balance of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakingTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
