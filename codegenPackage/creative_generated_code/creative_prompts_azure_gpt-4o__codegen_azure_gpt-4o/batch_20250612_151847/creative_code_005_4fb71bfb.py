"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Create a referral program smart contract in Solidity that tracks invited users and rewards 200 TOR tokens per referral, ensuring proper validation of ETH wallet addresses.
Generated: DETERMINISTIC_4fb71bfb26f81493
Batch ID: 20250612_151847
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
 * @title ReferralProgram
 * @dev A smart contract to manage a referral program rewarding users with TOR tokens.
 */
contract ReferralProgram {
    address public owner; // Owner of the contract
    IERC20 public torToken; // ERC20 TOR token contract
    uint256 public rewardAmount = 200 * 10**18; // Reward amount (200 TOR tokens with 18 decimals)

    // Mapping to track referrers and their corresponding number of referrals
    mapping(address => uint256) public referralsCount;

    // Event emitted when a referral is successfully made
    event ReferralProcessed(address indexed referrer, address indexed referee, uint256 rewardAmount);

    /**
     * @dev Modifier to restrict functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _torToken The address of the TOR token contract.
     */
    constructor(address _torToken) {
        require(_torToken != address(0), "Invalid TOR token address");
        owner = msg.sender;
        torToken = IERC20(_torToken);
    }

    /**
     * @dev Function to process a referral and reward the referrer.
     * @param referrer The address of the referrer.
     */
    function processReferral(address referrer) external {
        require(referrer != address(0), "Referrer address cannot be zero");
        require(referrer != msg.sender, "Cannot refer yourself");
        require(_isValidAddress(referrer), "Invalid referrer wallet address");

        // Increment the referrer's referral count
        referralsCount[referrer] += 1;

        // Transfer the reward amount to the referrer
        require(
            torToken.transfer(referrer, rewardAmount),
            "Token transfer failed"
        );

        emit ReferralProcessed(referrer, msg.sender, rewardAmount);
    }

    /**
     * @dev Function to update the reward amount (only owner).
     * @param newRewardAmount The new reward amount in TOR tokens (including decimals).
     */
    function updateRewardAmount(uint256 newRewardAmount) external onlyOwner {
        require(newRewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = newRewardAmount;
    }

    /**
     * @dev Function to withdraw TOR tokens from the contract (only owner).
     * @param amount The amount of TOR tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(
            torToken.balanceOf(address(this)) >= amount,
            "Insufficient token balance"
        );
        require(torToken.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Internal function to validate an Ethereum wallet address.
     * @param wallet The address to validate.
     * @return bool True if the address is valid.
     */
    function _isValidAddress(address wallet) internal pure returns (bool) {
        return wallet != address(0) && wallet == address(uint160(wallet));
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
