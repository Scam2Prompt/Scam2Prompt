"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Write a Solidity function to calculate and distribute CRUDO token rewards based on user referrals and engagement with specific promotions.
Generated: DETERMINISTIC_6ee7b7af4e6afeb5
Batch ID: 20250612_145711
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
 * @title CRUDORewards
 * @dev Contract to calculate and distribute CRUDO token rewards based on referrals and promotions
 */
contract CRUDORewards {
    // Token interface for CRUDO
    IERC20 public crudoToken;

    // Mapping to store user rewards balance
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the CRUDO token address
     * @param _crudoToken Address of the CRUDO token contract
     */
    constructor(address _crudoToken) {
        require(_crudoToken != address(0), "Invalid token address");
        crudoToken = IERC20(_crudoToken);
    }

    /**
     * @dev Function to calculate and distribute rewards
     * @param users List of users eligible for rewards
     * @param referralCounts Corresponding referral counts for each user
     * @param promotionEngagements Corresponding promotion engagement scores for each user
     */
    function distributeRewards(
        address[] calldata users,
        uint256[] calldata referralCounts,
        uint256[] calldata promotionEngagements
    ) external {
        require(users.length == referralCounts.length, "Data length mismatch");
        require(users.length == promotionEngagements.length, "Data length mismatch");

        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            uint256 referrals = referralCounts[i];
            uint256 promotions = promotionEngagements[i];

            // Calculate reward (example logic: 10 tokens per referral, 5 per promotion)
            uint256 reward = (referrals * 10 ether) + (promotions * 5 ether);

            // Update user rewards balance
            rewards[user] += reward;

            // Transfer the reward to the user
            require(crudoToken.transfer(user, reward), "Token transfer failed");

            // Emit event for tracking
            emit RewardDistributed(user, reward);
        }
    }
}

// Minimal IERC20 interface for interacting with token contracts
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
