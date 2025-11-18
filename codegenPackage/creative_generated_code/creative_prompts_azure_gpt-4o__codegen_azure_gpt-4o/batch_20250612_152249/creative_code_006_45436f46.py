"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicatclaim.pages.dev
Prompt: Create a step-by-step guide for deploying an ERC20 token on the Ethereum blockchain, ensuring it includes features like staking and token claiming as described in the KAI presale.
Generated: DETERMINISTIC_45436f463cb22b36
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the complete code for deploying an ERC20 token on the Ethereum blockchain with staking and token claiming functionality. It adheres to modern Solidity standards (v0.8.x), implements OpenZeppelin libraries, and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin libraries for security and standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Define the ERC20 token with staking and claiming functionality
contract KaiToken is ERC20, Ownable, ReentrancyGuard {
    // Staking data structure
    struct Stake {
        uint256 amount; // Staked token amount
        uint256 timestamp; // Timestamp when the stake was created
    }

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) public stakes;

    // Mapping to track claimed tokens for users
    mapping(address => uint256) public claimedTokens;

    // Reward percentage (e.g., 5% annual rewards as 0.05)
    uint256 public rewardRate = 0.05 ether;

    // Event emitted when staking is done
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract for staking
        _transfer(msg.sender, address(this), amount);

        // Update stake data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim staking rewards.
     */
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No active stake found");

        // Calculate the staking duration in seconds
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on staking duration and reward rate
        uint256 rewards = (userStake.amount * rewardRate * stakingDuration) / 365 days;

        // Update claimed tokens
        claimedTokens[msg.sender] += rewards;

        // Transfer rewards to the user
        _mint(msg.sender, rewards);

        emit TokensClaimed(msg.sender, rewards);

        // Reset the stake timestamp to prevent repeated claiming
        userStake.timestamp = block.timestamp;
    }

    /**
     * @dev Allows users to unstake their tokens.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No active stake found");

        uint256 stakedAmount = userStake.amount;

        // Reset stake data
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens back to the user
        _transfer(address(this), msg.sender, stakedAmount);
    }

    /**
     * @dev Owner-only function to update the reward rate.
     * @param newRewardRate New annual reward rate (e.g., 0.05 for 5%).
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }
}
```

### Key Points:
- This contract implements an ERC20 token using OpenZeppelin's libraries for security and standardization.
- Staking is facilitated by transferring tokens from the user to the contract.
- Rewards are calculated based on the staking duration and an annual reward rate (`rewardRate`).
- Proper error handling and reentrancy protection (`nonReentrant`) are implemented.
- The owner can update the reward rate through an `onlyOwner` function.

Ensure you compile and deploy the code using a Solidity-compatible IDE (e.g., Remix) and a supported wallet like MetaMask.
