"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babygrokai.pages.dev
Prompt: Write a tutorial-style prompt to guide the implementation of Baby Grok token staking rewards using Solidity and Web3.js.
Generated: DETERMINISTIC_0f8c1b2efae9b900
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Solidity Contract (BabyGrokTokenStaking.sol)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BabyGrokTokenStaking
 * @dev A staking contract for Baby Grok tokens that allows users to stake tokens
 * for rewards based on duration and amount staked.
 */
contract BabyGrokTokenStaking {
    // Token interface
    IERC20 public immutable token;

    // Reward rate per second (e.g., 100 tokens per second)
    uint256 public immutable rewardRate;

    // Struct to store staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewards;
    }

    // Mapping of user addresses to their stake details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewardsClaimed);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _token Address of the Baby Grok ERC20 token.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Calculate pending rewards
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.rewards += _calculateRewards(msg.sender);
        }

        // Update stake details
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        // Transfer tokens from user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 rewards = _calculateRewards(msg.sender) + userStake.rewards;

        // Update stake details
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;
        userStake.rewards = 0;

        // Transfer tokens and rewards back to the user
        require(token.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        require(token.transfer(msg.sender, rewards), "Reward transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param user The address of the user.
     * @return The calculated reward amount.
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 duration = block.timestamp - userStake.startTime;
        return userStake.amount * rewardRate * duration / 1e18;
    }
}

/**
 * @dev ERC20 Interface for token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

---

### Web3.js Script (staking.js)

```javascript
const Web3 = require('web3');
const web3 = new Web3('<YOUR_INFURA_OR_RPC_ENDPOINT>');
const abi = /* Contract ABI */;
const contractAddress = '<CONTRACT_ADDRESS>';
const contract = new web3.eth.Contract(abi, contractAddress);

// User's wallet address
const userAddress = '<USER_WALLET_ADDRESS>';
const privateKey = '<PRIVATE_KEY>';

// Stake tokens
async function stakeTokens(amount) {
  try {
    const data = contract.methods.stake(web3.utils.toWei(amount.toString(), 'ether')).encodeABI();
    
    const tx = {
      from: userAddress,
      to: contractAddress,
      data: data,
      gas: 2000000,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Stake transaction successful:', receipt);
  } catch (error) {
    console.error('Error staking tokens:', error);
  }
}

// Unstake tokens
async function unstakeTokens() {
  try {
    const data = contract.methods.unstake().encodeABI();
    
    const tx = {
      from: userAddress,
      to: contractAddress,
      data: data,
      gas: 2000000,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Unstake transaction successful:', receipt);
  } catch (error) {
    console.error('Error unstaking tokens:', error);
  }
}

// Example usage
(async () => {
  // Replace with actual amounts and wallet details
  await stakeTokens(100); // Stake 100 tokens
  await unstakeTokens();  // Unstake tokens and claim rewards
})();
```

Replace placeholders (`<`) with actual values such as your Infura endpoint, contract address, wallet address, and private key.
