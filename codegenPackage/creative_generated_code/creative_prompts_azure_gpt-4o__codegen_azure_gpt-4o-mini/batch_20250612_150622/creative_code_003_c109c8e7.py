"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stklido.com
Prompt: Create a smart contract that integrates with the Lido protocol to automatically stake Ethereum and distribute rewards to multiple users.
Generated: DETERMINISTIC_c109c8e73df44bfd
Batch ID: 20250612_150622
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

// Importing required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Lido's stETH contract
interface ILido {
    function submit(address _referral) external payable returns (uint256);
    function getPooledEthByShares(uint256 shares) external view returns (uint256);
    function getSharesByPooledEth(uint256 pooledEth) external view returns (uint256);
}

// Smart contract for staking Ethereum with Lido protocol and distributing rewards
contract LidoStaker is Ownable {
    // Address of the Lido staking contract
    ILido public lidoContract;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedAmounts;
    // Total amount of Ether staked
    uint256 public totalStaked;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the Lido contract address
    constructor(address _lidoContract) {
        require(_lidoContract != address(0), "Invalid Lido contract address");
        lidoContract = ILido(_lidoContract);
    }

    // Function to stake Ether via Lido
    function stake() external payable {
        require(msg.value > 0, "Must send ETH to stake");

        // Submit ETH to Lido for staking
        uint256 shares = lidoContract.submit{value: msg.value}(address(0));
        
        // Update user's staked amount and total staked amount
        stakedAmounts[msg.sender] += shares;
        totalStaked += msg.value;
    }

    // Function to distribute rewards to users based on their staked amounts
    function distributeRewards() external onlyOwner {
        // Loop through all stakers and distribute rewards
        for (uint256 i = 0; i < totalShares; i++) {
            address user = stakerAddresses[i]; // Assume we have an array of user addresses
            uint256 userShares = stakedAmounts[user];

            // Calculate user's reward based on their shares
            uint256 reward = lidoContract.getPooledEthByShares(userShares);

            // Transfer rewards to the user
            payable(user).transfer(reward);
            emit RewardsDistributed(user, reward);
        }
    }

    // Function to withdraw staked ETH (not implemented for simplicity)
    function withdraw(uint256 amount) external {
        // Logic to withdraw ETH goes here (need to burn shares, etc.)
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```

**Note:** This code is for illustrative purposes only. It assumes the existence of certain variables and logic (like `totalShares` and `stakerAddresses` arrays) that would need to be implemented for a complete production-ready solution. Proper testing and security audits should be conducted before deploying any smart contract on the mainnet.
