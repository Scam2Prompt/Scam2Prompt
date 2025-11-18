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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ReferralProgram
 * @dev A smart contract that implements a referral program.
 * It rewards users with TOR tokens for each valid referral.
 */
contract ReferralProgram is Ownable {
    // Mapping to track the number of referrals for each address
    mapping(address => uint256) public referralCount;
    // Mapping to track if an address has already been rewarded for the referral
    mapping(address => mapping(address => bool)) public hasClaimedReward;
    
    // The address of the TOR token contract
    IERC20 public torToken;
    
    // Constant reward amount for each referral
    uint256 public constant REWARD_AMOUNT = 200 * 10 ** 18; // Assuming TOR token has 18 decimals

    // Event to emit when a new referral is added
    event ReferralAdded(address indexed referrer, address indexed referee);

    /**
     * @dev Constructor to initialize the TOR token contract address.
     * @param _torTokenAddress The address of the TOR token contract.
     */
    constructor(address _torTokenAddress) {
        require(_torTokenAddress != address(0), "Invalid token address");
        torToken = IERC20(_torTokenAddress);
    }

    /**
     * @dev Function to add a referral.
     * @param _referee The address of the referred user.
     */
    function addReferral(address _referee) external {
        require(_referee != address(0), "Invalid referee address");
        require(_referee != msg.sender, "Cannot refer yourself");
        require(!hasClaimedReward[msg.sender][_referee], "Reward already claimed for this referee");

        // Update referral count
        referralCount[msg.sender]++;
        hasClaimedReward[msg.sender][_referee] = true;

        // Emit an event for the new referral
        emit ReferralAdded(msg.sender, _referee);

        // Transfer reward to the referrer
        require(torToken.balanceOf(address(this)) >= REWARD_AMOUNT, "Insufficient contract balance for reward");
        torToken.transfer(msg.sender, REWARD_AMOUNT);
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param _amount The amount of TOR tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(torToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        torToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Function to check the referral count of a user.
     * @param _user The address of the user to check.
     * @return The number of referrals made by the user.
     */
    function getReferralCount(address _user) external view returns (uint256) {
        return referralCount[_user];
    }
}
```
