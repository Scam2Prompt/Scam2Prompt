"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-c5i.pages.dev
Prompt: Create a smart contract that enables liquidity providers to deposit tokens and claim AERO emissions as rewards, following Aerodrome Finance's liquidity incentive structure.
Generated: DETERMINISTIC_ed47ff2f211d81d8
Batch ID: 20250612_153517
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AEROLiquidityPool
 * @dev Smart contract for liquidity providers to deposit tokens and receive AERO emissions as rewards.
 */
contract AEROLiquidityPool is Ownable {
    // Event emitted when tokens are deposited
    event TokensDeposited(address indexed provider, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed provider, uint256 amount);
    
    // Token for liquidity provision
    IERC20 public liquidityToken;

    // Token for rewards (AERO)
    IERC20 public rewardToken;

    // Struct to hold provider information
    struct Provider {
        uint256 depositedAmount;
        uint256 rewardsAccumulated;
        uint256 lastClaimedBlock;
    }

    // Mapping from provider's address to their information
    mapping(address => Provider) public providers;

    // Total deposits in the liquidity pool
    uint256 public totalDeposits;

    // Emission rate of rewards (in AERO per block)
    uint256 public emissionRate;

    /**
     * @dev Constructor to initialize the contract with the liquidity and reward tokens.
     * @param _liquidityToken Address of the liquidity token (ERC20)
     * @param _rewardToken Address of the reward token (AERO)
     * @param _emissionRate Emission rate of AERO rewards per block
     */
    constructor(
        address _liquidityToken,
        address _rewardToken,
        uint256 _emissionRate
    ) {
        liquidityToken = IERC20(_liquidityToken);
        rewardToken = IERC20(_rewardToken);
        emissionRate = _emissionRate;
    }

    /**
     * @dev Function for liquidity providers to deposit tokens into the pool.
     * @param amount Amount of tokens to be deposited
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from provider to contract
        liquidityToken.transferFrom(msg.sender, address(this), amount);
        
        // Update provider information
        Provider storage provider = providers[msg.sender];
        provider.depositedAmount += amount;
        totalDeposits += amount;
        provider.lastClaimedBlock = block.number;

        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Function for liquidity providers to claim their rewards.
     */
    function claimRewards() external {
        Provider storage provider = providers[msg.sender];
        
        // Calculate rewards based on the number of blocks since last claim
        uint256 blocksSinceLastClaim = block.number - provider.lastClaimedBlock;
        uint256 rewards = blocksSinceLastClaim * emissionRate * provider.depositedAmount / totalDeposits;

        require(rewards > 0, "No rewards to claim");

        // Update provider information
        provider.rewardsAccumulated += rewards;
        provider.lastClaimedBlock = block.number;

        // Transfer rewards to the provider
        require(rewardToken.balanceOf(address(this)) >= rewards, "Insufficient reward balance in contract");
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to withdraw deposited tokens (only owner can withdraw).
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(amount <= liquidityToken.balanceOf(address(this)), "Insufficient balance in contract");

        liquidityToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to change the emission rate.
     * @param newEmissionRate New emission rate of AERO rewards per block
     */
    function updateEmissionRate(uint256 newEmissionRate) external onlyOwner {
        emissionRate = newEmissionRate;
    }
}
```
