"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-onchain.pages.dev
Prompt: Create a smart contract that distributes $onchain tokens as rewards based on users' Chain Links collected in the Telegram Chain Game.
Generated: DETERMINISTIC_badca1c7538fbbd1
Batch ID: 20250612_150946
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
 * @title OnChainTokenRewardDistributor
 * @dev Smart contract to distribute $onchain tokens based on users' Chain Links collected in the Telegram Chain Game.
 */
contract OnChainTokenRewardDistributor {
    // Address of the token contract
    IERC20 public immutable onChainToken;

    // Owner of the contract (admin)
    address public owner;

    // Mapping to store user's Chain Link count
    mapping(address => uint256) public chainLinks;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 rewardAmount);

    // Event emitted when chain links are updated
    event ChainLinksUpdated(address indexed user, uint256 newChainLinkCount);

    // Modifier to restrict access to admin-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract
     * @param tokenAddress Address of the $onchain token contract
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        onChainToken = IERC20(tokenAddress);
        owner = msg.sender;
    }

    /**
     * @notice Updates the Chain Links count for a user
     * @dev Can only be called by the owner
     * @param user Address of the user
     * @param count New Chain Links count
     */
    function updateChainLinks(address user, uint256 count) external onlyOwner {
        require(user != address(0), "Invalid user address");
        chainLinks[user] = count;
        emit ChainLinksUpdated(user, count);
    }

    /**
     * @notice Distributes rewards based on Chain Links collected
     * @dev Users must have a positive Chain Links count to receive rewards
     */
    function distributeRewards(address user) external onlyOwner {
        uint256 linksCollected = chainLinks[user];
        require(linksCollected > 0, "User has no Chain Links");

        uint256 rewardAmount = calculateReward(linksCollected);
        require(
            onChainToken.balanceOf(address(this)) >= rewardAmount,
            "Insufficient token balance in contract"
        );

        // Transfer the calculated reward amount to the user
        onChainToken.transfer(user, rewardAmount);
        emit RewardsDistributed(user, rewardAmount);

        // Reset Chain Links for the user to prevent double rewards
        chainLinks[user] = 0;
    }

    /**
     * @notice Calculates the reward amount based on Chain Links collected
     * @param linksCollected Number of Chain Links collected by the user
     * @return rewardAmount Calculated reward amount in $onchain tokens
     */
    function calculateReward(uint256 linksCollected)
        internal
        pure
        returns (uint256 rewardAmount)
    {
        // Example reward calculation (1 token per Chain Link)
        return linksCollected * 1 ether; // Assuming token has 18 decimals
    }

    /**
     * @notice Withdraws remaining tokens in the contract
     * @dev Can only be called by the owner
     */
    function withdrawTokens() external onlyOwner {
        uint256 remainingBalance = onChainToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        onChainToken.transfer(owner, remainingBalance);
    }
}

// Interface for ERC20 standard functions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
