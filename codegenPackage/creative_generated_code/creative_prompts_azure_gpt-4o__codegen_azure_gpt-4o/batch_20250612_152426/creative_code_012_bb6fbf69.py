"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mpeppe.web.app
Prompt: Develop a smart contract in Solidity for distributing rewards earned from the $MPEPE gaming and sports betting platform, ensuring user safety and compliance with the audited contract.
Generated: DETERMINISTIC_bb6fbf696441073f
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title RewardDistributor
 * @dev A smart contract for distributing rewards earned from the $MPEPE gaming and sports betting platform.
 *      Ensures user safety and compliance with audited contracts.
 */
contract RewardDistributor {
    // Address of the owner (administrator) of the contract
    address public owner;

    // Tracks the reward balances of users
    mapping(address => uint256) private rewardBalances;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Event emitted when the owner withdraws funds
    event OwnerWithdrawal(address indexed owner, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Caller is not the owner");
        _;
    }

    // Modifier to validate non-zero values
    modifier nonZeroAmount(uint256 _amount) {
        require(_amount > 0, "Invalid amount: Must be greater than zero");
        _;
    }

    // Constructor: Initializes the contract and sets the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to a specific user.
     * @param recipient The address of the user receiving the reward.
     * @param amount The amount of $MPEPE rewards to distribute.
     */
    function distributeRewards(address recipient, uint256 amount)
        external
        onlyOwner
        nonZeroAmount(amount)
    {
        require(recipient != address(0), "Invalid recipient: Cannot be zero address");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Update the recipient's reward balance
        rewardBalances[recipient] += amount;

        // Emit the event
        emit RewardsDistributed(recipient, amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     *      Transfers the reward balance to the caller and resets their balance.
     */
    function claimRewards() external {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available for claiming");

        // Reset the user's reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer the rewards to the user
        payable(msg.sender).transfer(reward);
    }

    /**
     * @dev Function for the owner to withdraw remaining contract funds.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount)
        external
        onlyOwner
        nonZeroAmount(amount)
    {
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the funds to the owner
        payable(owner).transfer(amount);

        // Emit the event
        emit OwnerWithdrawal(owner, amount);
    }

    /**
     * @dev Fallback function to receive Ether directly into the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to check the reward balance of a user.
     * @param user Address of the user whose reward balance is being queried.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
