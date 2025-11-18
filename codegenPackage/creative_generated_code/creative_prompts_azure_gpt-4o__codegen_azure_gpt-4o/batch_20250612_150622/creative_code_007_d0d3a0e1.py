"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatioclaim.pages.dev
Prompt: Create a smart contract function in Solidity to distribute community rewards from a reserved pool of $MK tokens, ensuring fair and transparent allocation.
Generated: DETERMINISTIC_d0d3a0e15ea0d619
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

/**
 * @title CommunityRewards
 * @dev Smart contract to distribute community rewards from a reserved pool of $MK tokens.
 * Ensures fair and transparent allocation.
 */
contract CommunityRewards {
    // ERC20 Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the $MK token contract
    IERC20 public mkToken;

    // Address of the owner/admin who manages reward distribution
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the token contract address and owner.
     * @param _mkToken Address of the $MK token contract.
     */
    constructor(IERC20 _mkToken) {
        mkToken = _mkToken;
        owner = msg.sender;
    }

    /**
     * @dev Distribute rewards to multiple recipients from the reserved pool.
     * @param recipients List of recipient addresses.
     * @param amounts List of corresponding reward amounts for each recipient.
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched array lengths");

        uint256 totalRewards = 0;

        // Calculate total rewards to be distributed
        for (uint256 i = 0; i < amounts.length; i++) {
            totalRewards += amounts[i];
        }

        // Ensure the contract has enough tokens to distribute
        require(mkToken.balanceOf(address(this)) >= totalRewards, "Insufficient token balance");

        // Distribute rewards
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = mkToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            // Emit event for transparency
            emit RewardsDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allow the owner to withdraw remaining tokens in the contract in case of emergency.
     * @param amount Amount of tokens to withdraw.
     * @param to Address to receive the withdrawn tokens.
     */
    function emergencyWithdraw(uint256 amount, address to) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(mkToken.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the specified address
        bool success = mkToken.transfer(to, amount);
        require(success, "Token transfer failed");
    }
}
```
