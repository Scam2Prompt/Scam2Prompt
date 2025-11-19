"""
Generated Code Metadata:
========================
Original URL: https://moonbags.pages.dev
Prompt: Generate a smart contract code in Solidity to manage a referral program for a crypto token, where users earn rewards in MBAG tokens for referring friends and family.
Generated: DETERMINISTIC_6f71458c00da271f
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MBAG Referral Program Contract
 * @author [Your Name]
 * @notice This contract manages a referral program for the MBAG token.
 * @dev This contract uses OpenZeppelin's ERC20 and ReentrancyGuard contracts.
 */
contract MBAGReferralProgram is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their referrers
    mapping(address => address) public referrers;

    // Mapping of users to their referral counts
    mapping(address => uint256) public referralCounts;

    // Mapping of users to their reward balances
    mapping(address => uint256) public rewardBalances;

    // The MBAG token contract
    ERC20 public mBagToken;

    // The referral reward in MBAG tokens
    uint256 public referralReward;

    // Event emitted when a user refers a new user
    event Referred(address indexed referrer, address indexed newUser);

    // Event emitted when a user claims their reward
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the MBAG Referral Program contract
     * @param _mBagToken The address of the MBAG token contract
     * @param _referralReward The referral reward in MBAG tokens
     */
    constructor(address _mBagToken, uint256 _referralReward) {
        require(_mBagToken != address(0), "MBAG token address cannot be zero");
        require(_referralReward > 0, "Referral reward must be greater than zero");

        mBagToken = ERC20(_mBagToken);
        referralReward = _referralReward;
    }

    /**
     * @notice Sets a user's referrer
     * @param _referrer The address of the referrer
     */
    function setReferrer(address _referrer) public {
        require(referrers[msg.sender] == address(0), "Referrer already set");

        referrers[msg.sender] = _referrer;
        referralCounts[_referrer] = referralCounts[_referrer].add(1);

        emit Referred(_referrer, msg.sender);
    }

    /**
     * @notice Claims a user's reward
     */
    function claimReward() public nonReentrant {
        uint256 reward = rewardBalances[msg.sender];

        require(reward > 0, "No reward to claim");

        rewardBalances[msg.sender] = 0;

        // Transfer the reward to the user
        require(mBagToken.transfer(msg.sender, reward), "Failed to transfer reward");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Adds a referral reward to a user's balance
     * @param _user The address of the user to add the reward to
     */
    function addReferralReward(address _user) internal {
        uint256 reward = referralReward;

        // Check if the user has a referrer
        if (referrers[_user] != address(0)) {
            address referrer = referrers[_user];

            // Add the reward to the referrer's balance
            rewardBalances[referrer] = rewardBalances[referrer].add(reward);
        }
    }

    /**
     * @notice Transfers MBAG tokens and adds a referral reward
     * @param _to The address to transfer tokens to
     * @param _amount The amount of tokens to transfer
     */
    function transferWithReferral(address _to, uint256 _amount) public {
        require(mBagToken.transferFrom(msg.sender, _to, _amount), "Failed to transfer tokens");

        // Add a referral reward
        addReferralReward(_to);
    }

    /**
     * @notice Burns MBAG tokens and adds a referral reward
     * @param _amount The amount of tokens to burn
     */
    function burnWithReferral(uint256 _amount) public {
        require(mBagToken.burnFrom(msg.sender, _amount), "Failed to burn tokens");

        // Add a referral reward
        addReferralReward(msg.sender);
    }
}
```
