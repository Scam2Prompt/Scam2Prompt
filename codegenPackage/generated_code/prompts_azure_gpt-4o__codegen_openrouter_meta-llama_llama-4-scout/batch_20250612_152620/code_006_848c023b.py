"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Write a Solidity smart contract to automate token claiming and referral rewards, including 10% $AIT and 10% BNB rewards for referrals, as described in AI Trader's airdrop process.
Generated: DETERMINISTIC_848c023bed490845
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AITReferralSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of users to their referral IDs
    mapping(address => address) public referrals;

    // Mapping of users to their claimed status
    mapping(address => bool) public claimed;

    // AIT token contract
    IERC20 public aitToken;

    // Address of the BNB token (native token)
    address public constant BNB_TOKEN = 0xEeeeeeEeEeEeEeeEeEeEeeEeeEeeE;

    // Reward percentages
    uint256 public constant REFERRAL_REWARD_PERCENTAGE = 10;
    uint256 public constant CLAIM_REWARD_PERCENTAGE = 10;

    // Reward amounts
    uint256 public aitRewardAmount;
    uint256 public bnbRewardAmount;

    // Event emitted when a user claims their reward
    event Claimed(address indexed user, uint256 aitReward, uint256 bnbReward);

    // Event emitted when a user refers a new user
    event Referred(address indexed referrer, address indexed newUser);

    constructor(address _aitTokenAddress) {
        aitToken = IERC20(_aitTokenAddress);
    }

    // Function to set the referral ID for a user
    function setReferral(address _user, address _referrer) public onlyOwner {
        referrals[_user] = _referrer;
    }

    // Function to claim rewards
    function claim() public {
        require(!claimed[msg.sender], "User has already claimed their reward");

        // Calculate reward amounts
        aitRewardAmount = aitToken.balanceOf(address(this)).mul(CLAIM_REWARD_PERCENTAGE).div(100);
        bnbRewardAmount = address(this).balance.mul(CLAIM_REWARD_PERCENTAGE).div(100);

        // Transfer rewards to user
        aitToken.transfer(msg.sender, aitRewardAmount);
        payable(msg.sender).transfer(bnbRewardAmount);

        // Mark user as claimed
        claimed[msg.sender] = true;

        emit Claimed(msg.sender, aitRewardAmount, bnbRewardAmount);
    }

    // Function to refer a new user
    function refer(address _newUser) public {
        address referrer = referrals[msg.sender];
        require(referrer != address(0), "User does not have a referrer");

        // Calculate referral reward amounts
        uint256 aitReferralReward = aitToken.balanceOf(address(this)).mul(REFERRAL_REWARD_PERCENTAGE).div(100);
        uint256 bnbReferralReward = address(this).balance.mul(REFERRAL_REWARD_PERCENTAGE).div(100);

        // Transfer referral rewards to referrer
        aitToken.transfer(referrer, aitReferralReward);
        payable(referrer).transfer(bnbReferralReward);

        emit Referred(referrer, _newUser);
    }

    // Function to deposit AIT tokens
    function depositAIT(uint256 _amount) public {
        aitToken.transferFrom(msg.sender, address(this), _amount);
    }

    // Function to deposit BNB tokens
    function depositBNB() public payable {
        require(msg.value > 0, "BNB deposit amount must be greater than 0");
    }

    // Fallback function to receive BNB tokens
    receive() external payable {}
}
```
