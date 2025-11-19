"""
Generated Code Metadata:
========================
Original URL: https://usdccash.xyz
Prompt: Develop a simple Ethereum smart contract in Solidity that distributes USDC rewards to $UPRINT holders on every transaction, considering the tokenomics and contract address provided.
Generated: DETERMINISTIC_e570ab58cd3545c3
Batch ID: 20250622_212137
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

// Importing the ERC20 interface to interact with the USDC token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for distributing USDC rewards to $UPRINT holders
contract UPRINTRewards {
    // State variables
    IERC20 public usdcToken; // USDC token contract
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Balances of $UPRINT holders
    uint256 public totalSupply; // Total supply of $UPRINT tokens
    uint256 public rewardRate; // Rate of USDC rewards per transaction

    // Events
    event RewardDistributed(address indexed holder, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _usdcToken, uint256 _rewardRate) {
        usdcToken = IERC20(_usdcToken);
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    // Function to distribute rewards to $UPRINT holders
    function distributeRewards() external {
        // Calculate the total rewards to distribute
        uint256 totalRewards = totalSupply * rewardRate;

        // Ensure the contract has enough USDC to distribute
        require(usdcToken.balanceOf(address(this)) >= totalRewards, "Insufficient USDC balance");

        // Distribute rewards to each holder
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i)); // Placeholder for actual holder address retrieval
            uint256 reward = (balances[holder] * rewardRate) / totalSupply;
            if (reward > 0) {
                usdcToken.transfer(holder, reward);
                emit RewardDistributed(holder, reward);
            }
        }
    }

    // Function to update the reward rate (only callable by the owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw USDC from the contract (only callable by the owner)
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient USDC balance");
        usdcToken.transfer(owner, amount);
    }

    // Function to allow $UPRINT holders to update their balance
    function updateBalance(address holder, uint256 amount) external onlyOwner {
        balances[holder] = amount;
    }

    // Function to set the total supply of $UPRINT tokens
    function setTotalSupply(uint256 supply) external onlyOwner {
        totalSupply = supply;
    }
}
```
