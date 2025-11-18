"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Write a smart contract for a multichain token similar to $FROP, ensuring transparency and security. Include functionality for staking and rewards as described in the Popo ecosystem.
Generated: DETERMINISTIC_8b111178c907c577
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready smart contract for a multichain token with staking and rewards functionality. The code is written in Solidity, following best practices for Ethereum-compatible blockchains. You can deploy it on EVM-compatible chains.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MultichainToken
 * @dev ERC20 Token with staking and rewards functionality for multichain support.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MultichainToken is ERC20, Ownable, ReentrancyGuard {
    // Staking structure
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 since;         // Timestamp when staking started
        bool active;           // Is the stake active
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) private stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per year (e.g., 10% = 0.1)
    uint256 public rewardRate = 10; // Default annual reward rate (10%)

    // Reward multiplier (to handle decimals in reward calculation)
    uint256 private constant REWARD_MULTIPLIER = 100;

    // Events
    event TokensStaked(address indexed user, uint256 amount, uint256 time);
    event TokensUnstaked(address indexed user, uint256 amount, uint256 reward, uint256 time);
    event RewardRateChanged(uint256 oldRate, uint256 newRate);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     */
    constructor() ERC20("MultichainToken", "MCT") {
        // Mint an initial supply to the contract owner (for example: 1 million tokens)
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance to stake");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), _amount);

        // Update the stake record
        if (stakes[msg.sender].active) {
            // If the user already has an active stake, calculate rewards first
            uint256 pendingReward = calculateReward(msg.sender);
            stakes[msg.sender].amount += pendingReward; // Compound rewards
        }

        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].since = block.timestamp;
        stakes[msg.sender].active = true;

        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        require(stakes[msg.sender].active, "No active stake found");

        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 reward = calculateReward(msg.sender);

        // Reset stake record
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].since = 0;
        stakes[msg.sender].active = false;

        totalStaked -= stakedAmount;

        // Transfer the staked tokens and rewards back to the user
        _transfer(address(this), msg.sender, stakedAmount + reward);

        emit TokensUnstaked(msg.sender, stakedAmount, reward, block.timestamp);
    }

    /**
     * @dev Function to calculate the reward for a user based on their stake.
     * @param _user Address of the user.
     * @return Reward amount in tokens.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        if (!userStake.active) {
            return 0;
        }

        uint256 stakingTime = block.timestamp - userStake.since; // Time in seconds
        uint256 annualReward = (userStake.amount * rewardRate) / REWARD_MULTIPLIER;

        // Rewards are proportional to the staking time (seconds in a year = 365 * 24 * 60 * 60)
        uint256 reward = (stakingTime * annualReward) / (365 days);

        return reward;
    }

    /**
     * @dev Function to change the reward rate (only owner).
     * @param _newRate New annual reward rate (e.g., 10% = 10).
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate >= 0, "Reward rate must be non-negative");
        emit RewardRateChanged(rewardRate, _newRate);
        rewardRate = _newRate;
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to the contract (only owner).
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(this), "Cannot recover staking token");
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```

### Key Features
- The contract includes staking and rewards functionality.
- Uses OpenZeppelin libraries for security and modularity.
- Implements `stake`, `unstake`, and `calculateReward` for staking logic.
- Allows the owner to modify the reward rate dynamically.
- Prevents reentrancy attacks with `ReentrancyGuard`.
- Includes a function to recover tokens accidentally sent to the contract.

### Deployment and Testing
Make sure to test the contract thoroughly on a testnet before deploying it on the mainnet. Use tools like Hardhat or Truffle for automated testing and auditing.
