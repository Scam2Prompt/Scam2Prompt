"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Provide a step-by-step tutorial for deploying a staking mechanism for $WAI tokens on the Ethereum network, ensuring compatibility with MetaMask and other wallets.
Generated: DETERMINISTIC_0ad2fb0d3b830612
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for security and standard functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title WAI Staking Contract
/// @dev This contract allows users to stake their WAI tokens and earn rewards.
contract WAIStaking is Ownable {
    // ERC20 token to be used for staking
    IERC20 public waiToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 startTime;   // Timestamp when the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Events for logging staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /// @param _waiToken Address of the WAI token contract
    constructor(IERC20 _waiToken) {
        waiToken = _waiToken;
    }

    /// @notice Function to stake WAI tokens
    /// @param _amount Amount of tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(waiToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /// @notice Function to unstake WAI tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;

        // Transfer tokens back to user
        require(waiToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /// @notice Function to calculate rewards (example: 1% per day)
    /// @param user Address of the user to calculate rewards for
    /// @return uint256 Total rewards earned by the user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 rewardRate = 1; // 1% reward per day
        return (userStake.amount * rewardRate * stakingDuration) / (1 days * 100);
    }

    /// @notice Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer the rewards to the user
        require(waiToken.transfer(msg.sender, rewards), "Transfer failed");

        // Emit event for claiming rewards
        emit RewardsClaimed(msg.sender, rewards);
    }

    /// @notice Function to withdraw any ERC20 tokens accidentally sent to this contract
    /// @param token Address of the ERC20 token to withdraw
    /// @param amount Amount to withdraw
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

### Deployment Instructions

1. **Set up your development environment**:
   - Install Node.js and npm.
   - Install Truffle or Hardhat for smart contract deployments.

2. **Install dependencies**:
   ```bash
   npm install @openzeppelin/contracts
   ```

3. **Compile the contract**:
   - Use Truffle/Hardhat to compile the smart contract.

4. **Deploy the contract**:
   - Write a migration script to deploy the WAIStaking contract on the Ethereum network.

5. **Connect to MetaMask**:
   - Ensure MetaMask is configured with the appropriate network (e.g., Rinkeby, Mainnet).
   - Users can interact with your deployed contract through a web interface that connects to MetaMask. Use ethers.js or web3.js for integration.

6. **Testing**:
   - Thoroughly test the staking and reward claiming functionalities. Consider edge cases like edge balances and zero stakes.

7. **Security Audits**:
   - Before going into production, consider a third-party audit for the smart contract to ensure security and best practices.

8. **Deploy on mainnet**:
   - Once testing is complete and any issues are resolved, deploy the contract on the Ethereum mainnet.
