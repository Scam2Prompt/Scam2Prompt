"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Develop a smart contract that distributes rewards to the first 1,000 connected wallets in the $ROOST ecosystem, ensuring fairness and transparency.
Generated: DETERMINISTIC_5cff1097e40a6331
Batch ID: 20250612_151057
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
 * @title RewardDistributor
 * @dev A smart contract that distributes rewards to the first 1,000 connected wallets in the $ROOST ecosystem.
 * Ensures fairness and transparency in reward distribution.
 */
contract RewardDistributor {
    // Maximum number of wallets to receive rewards
    uint256 public constant MAX_RECIPIENTS = 1000;

    // Address of the token contract ($ROOST)
    address public immutable roostToken;

    // Reward amount per wallet (in token units)
    uint256 public immutable rewardAmount;

    // Array to store recipients' wallet addresses
    address[] public recipients;

    // Mapping to ensure each wallet only claims rewards once
    mapping(address => bool) public hasClaimed;

    // Owner of the contract (administrator)
    address public owner;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed recipient, uint256 amount);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with necessary parameters.
     * @param _roostToken Address of the $ROOST token contract.
     * @param _rewardAmount Amount of tokens to distribute per wallet.
     */
    constructor(address _roostToken, uint256 _rewardAmount) {
        require(_roostToken != address(0), "Invalid token address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        roostToken = _roostToken;
        rewardAmount = _rewardAmount;
        owner = msg.sender;
    }

    /**
     * @dev Function for wallets to claim their rewards.
     */
    function claimReward() external {
        require(recipients.length < MAX_RECIPIENTS, "Reward limit reached");
        require(!hasClaimed[msg.sender], "Reward already claimed");

        // Mark the wallet as having claimed the reward
        hasClaimed[msg.sender] = true;

        // Add the wallet to the recipients list
        recipients.push(msg.sender);

        // Transfer the reward to the wallet (requires token approval)
        require(
            IERC20(roostToken).transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        // Emit event for transparency
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function for the owner to withdraw any remaining tokens from the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 contractBalance = IERC20(roostToken).balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(
            IERC20(roostToken).transfer(owner, contractBalance),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Function to get the total number of recipients.
     * @return The number of wallets that have claimed rewards.
     */
    function getRecipientCount() external view returns (uint256) {
        return recipients.length;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
