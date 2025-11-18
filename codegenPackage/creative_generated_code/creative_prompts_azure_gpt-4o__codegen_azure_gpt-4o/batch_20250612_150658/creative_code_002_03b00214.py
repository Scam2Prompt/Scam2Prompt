"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdart.top
Prompt: Generate a smart contract that facilitates reward distribution when a wallet is connected, as described in the REWARD Portal v2.
Generated: DETERMINISTIC_03b00214ac853558
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a Solidity smart contract for the described functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RewardDistribution
 * @dev This contract facilitates reward distribution to wallets connecting to the portal.
 */
contract RewardDistribution {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardAmount; // Reward amount for each wallet
    mapping(address => bool) private rewardedWallets; // Tracks wallets that have received rewards

    // Events
    event RewardDistributed(address indexed recipient, uint256 amount);

    // Constructor
    constructor(uint256 _rewardAmount) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        owner = msg.sender; // Set the contract deployer as the owner
        rewardAmount = _rewardAmount;
    }

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows the owner to update the reward amount.
     * @param _newRewardAmount The new reward amount.
     */
    function setRewardAmount(uint256 _newRewardAmount) external onlyOwner {
        require(_newRewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _newRewardAmount;
    }

    /**
     * @dev Connect wallet and claim the reward. Only one reward per wallet.
     */
    function connectWalletAndClaimReward() external {
        require(!rewardedWallets[msg.sender], "Wallet has already claimed the reward");
        require(address(this).balance >= rewardAmount, "Insufficient contract balance");

        // Mark wallet as rewarded
        rewardedWallets[msg.sender] = true;

        // Transfer the reward to the wallet
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        // Emit the reward distribution event
        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to deposit Ether into the contract.
     */
    function deposit() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     * @param _amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");

        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to receive Ether directly.
     */
    receive() external payable {}

    /**
     * @dev Returns whether a wallet has already claimed a reward.
     * @param _wallet The wallet address to check.
     * @return True if the wallet has claimed a reward, false otherwise.
     */
    function hasClaimedReward(address _wallet) external view returns (bool) {
        return rewardedWallets[_wallet];
    }
}
```

This code implements a reward distribution smart contract with proper error handling, comments, and adherence to best practices.
