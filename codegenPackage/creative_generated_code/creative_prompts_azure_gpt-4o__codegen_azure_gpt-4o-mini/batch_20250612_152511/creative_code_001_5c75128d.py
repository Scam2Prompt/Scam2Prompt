"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Generate a Solidity smart contract example that implements a token referral system similar to $PORTAL, where users can earn rewards for inviting friends to participate in an airdrop.
Generated: DETERMINISTIC_5c75128ded8b410b
Batch ID: 20250612_152511
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

// Importing OpenZeppelin's ERC20 implementation for the token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple token contract implementing a referral system
contract ReferralToken is ERC20, Ownable {
    // Event for logging referral rewards
    event ReferralReward(address indexed referrer, address indexed referee, uint256 reward);

    // Mapping to track the referrer of each user
    mapping(address => address) public referrerOf;
    // Mapping to track rewards earned by referrers
    mapping(address => uint256) public rewards;

    // Reward amount for a successful referral
    uint256 public constant REFERRAL_REWARD = 10 * (10 ** decimals()); // 10 tokens

    constructor() ERC20("ReferralToken", "RFT") {
        // Mint initial supply to contract owner
        _mint(msg.sender, 1000000 * (10 ** decimals())); // Mint 1 million tokens
    }

    // Function to allow users to register a referral
    function registerReferral(address _referrer) external {
        // Ensure the referrer is not the caller and is a valid address
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(_referrer != address(0), "Invalid referrer address");
        require(referrerOf[msg.sender] == address(0), "Referral already registered");

        // Register the referrer
        referrerOf[msg.sender] = _referrer;
        // Reward the referrer
        rewards[_referrer] += REFERRAL_REWARD;

        // Emit the referral reward event
        emit ReferralReward(_referrer, msg.sender, REFERRAL_REWARD);
    }

    // Function for the referrer to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Resetting rewards to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the referrer
        _transfer(address(this), msg.sender, rewardAmount);
    }

    // Function to airdrop tokens to new users
    function airdropTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Invalid amount");

        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(msg.sender, recipients[i], amount);
            // Automatic referral registration if the recipient has a referrer
            if (referrerOf[recipients[i]] != address(0)) {
                registerReferral(referrerOf[recipients[i]]);
            }
        }
    }

    // Function to check the balance of the contract for token transfers
    function availableTokens() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
