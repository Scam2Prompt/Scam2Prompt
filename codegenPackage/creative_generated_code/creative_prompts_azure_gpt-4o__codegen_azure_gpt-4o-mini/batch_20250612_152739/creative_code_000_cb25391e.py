"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with features similar to $MGLS, including zero buy/sell tax and staking functionality.
Generated: DETERMINISTIC_cb25391eb3c2f56c
Batch ID: 20250612_152739
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

// Importing the OpenZeppelin ERC20 standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// The MGLSToken contract inherits from ERC20, Ownable, and Pausable
contract MGLSToken is ERC20, Ownable, Pausable {
    // Struct to hold staking information for each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping from address to Staker
    mapping(address => Staker) public stakers;
    uint256 public totalStaked; // Total amount of staked tokens
    uint256 public rewardPerToken; // Reward per token staked
    uint256 public constant REWARD_MULTIPLIER = 1e18; // Scaling factor for reward calculations

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MGLS Token", "MGLS") {
        _mint(msg.sender, 1_000_000 * 10**decimals()); // Mint initial supply to the contract owner
    }

    // Function to stake tokens
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Cannot stake zero tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update staker's information
        stakers[msg.sender].amount += amount;
        totalStaked += amount;
        
        // Transfer tokens from the staker to the contract
        _transfer(msg.sender, address(this), amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update staker's information
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards to stakers
    function distributeRewards() external onlyOwner {
        require(totalStaked > 0, "No tokens staked");

        // Calculate rewards based on total staked tokens
        uint256 rewardAmount = address(this).balance; // Assume rewards are sent to the contract balance
        rewardPerToken += (rewardAmount * REWARD_MULTIPLIER) / totalStaked;

        // Reset contract balance
        // This logic assumes rewards are handled differently in your use case

        // Emit event for rewards (if applicable)
        // emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to claim accumulated rewards for the caller
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingReward = (staker.amount * rewardPerToken) / REWARD_MULTIPLIER - staker.rewardDebt;

        // Update reward debt
        staker.rewardDebt = (staker.amount * rewardPerToken) / REWARD_MULTIPLIER;

        // Transfer rewards to the staker
        payable(msg.sender).transfer(pendingReward);

        emit RewardsDistributed(msg.sender, pendingReward);
    }

    // Pause the contract, preventing any staking or unstaking
    function pause() external onlyOwner {
        _pause();
    }

    // Unpause the contract, allowing staking and unstaking again
    function unpause() external onlyOwner {
        _unpause();
    }

    // Function to receive Ether (for rewards)
    receive() external payable {}
}
```
