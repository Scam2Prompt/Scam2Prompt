"""
Generated Code Metadata:
========================
Original URL: https://zeek.social
Prompt: Generate a smart contract in Solidity for managing referral codes and rewards distribution, inspired by Zeek Network's SocialFi model.
Generated: DETERMINISTIC_7f09e77a92dfcac4
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralCodeManager
 * @author [Your Name]
 * @notice A smart contract for managing referral codes and rewards distribution.
 */
contract ReferralCodeManager is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of referral codes to their corresponding owners
    mapping (string => address) public referralCodes;

    // Mapping of users to their referrer codes
    mapping (address => string) public userReferralCodes;

    // Mapping of users to their reward balances
    mapping (address => uint256) public rewardBalances;

    // IERC20 token for rewards distribution
    IERC20 public rewardsToken;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event emitted when a new referral code is created
    event NewReferralCode(string indexed code, address indexed owner);

    // Event emitted when a user joins with a referral code
    event UserJoinedWithReferralCode(address indexed user, string indexed code);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _rewardsToken Address of the IERC20 token for rewards distribution
     */
    constructor(address _rewardsToken) public {
        require(_rewardsToken != address(0), "Rewards token address cannot be zero");
        rewardsToken = IERC20(_rewardsToken);
    }

    /**
     * @notice Creates a new referral code
     * @param _code The referral code to create
     */
    function createReferralCode(string memory _code) public {
        require(bytes(_code).length > 0, "Referral code cannot be empty");
        require(referralCodes[_code] == address(0), "Referral code already exists");

        referralCodes[_code] = msg.sender;
        emit NewReferralCode(_code, msg.sender);
    }

    /**
     * @notice Joins with a referral code
     * @param _code The referral code to join with
     */
    function joinWithReferralCode(string memory _code) public {
        require(bytes(_code).length > 0, "Referral code cannot be empty");
        require(referralCodes[_code] != address(0), "Referral code does not exist");

        userReferralCodes[msg.sender] = _code;
        emit UserJoinedWithReferralCode(msg.sender, _code);

        // Distribute rewards to the referrer
        address referrer = referralCodes[_code];
        uint256 rewardAmount = 100; // Example reward amount
        rewardBalances[referrer] = rewardBalances[referrer].add(rewardAmount);
        totalRewardsDistributed = totalRewardsDistributed.add(rewardAmount);

        // Transfer rewards to the referrer
        require(rewardsToken.transfer(referrer, rewardAmount), "Rewards transfer failed");
        emit RewardsDistributed(referrer, rewardAmount);
    }

    /**
     * @notice Distributes rewards to a user
     * @param _user The user to distribute rewards to
     * @param _amount The amount of rewards to distribute
     */
    function distributeRewards(address _user, uint256 _amount) public {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewardBalances[_user] = rewardBalances[_user].add(_amount);
        totalRewardsDistributed = totalRewardsDistributed.add(_amount);

        // Transfer rewards to the user
        require(rewardsToken.transfer(_user, _amount), "Rewards transfer failed");
        emit RewardsDistributed(_user, _amount);
    }

    /**
     * @notice Withdraws rewards from the contract
     * @param _amount The amount of rewards to withdraw
     */
    function withdrawRewards(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(rewardBalances[msg.sender] >= _amount, "Insufficient reward balance");

        rewardBalances[msg.sender] = rewardBalances[msg.sender].sub(_amount);

        // Transfer rewards to the user
        require(rewardsToken.transfer(msg.sender, _amount), "Rewards transfer failed");
    }
}
```
