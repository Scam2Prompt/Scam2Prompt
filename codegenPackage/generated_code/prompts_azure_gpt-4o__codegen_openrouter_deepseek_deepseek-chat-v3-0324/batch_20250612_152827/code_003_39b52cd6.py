"""
Generated Code Metadata:
========================
Original URL: https://riftproject.pages.dev
Prompt: Write a smart contract in Solidity to implement a referral reward mechanism similar to the $RIFT referral system described on the Rift Swap website.
Generated: DETERMINISTIC_39b52cd635912fd6
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ReferralReward is Ownable, ReentrancyGuard {
    IERC20 public riftToken;
    
    // Referral structure
    struct ReferralInfo {
        address referrer;
        uint256 totalEarned;
        uint256 referralsCount;
    }
    
    // Mapping of users to their referral info
    mapping(address => ReferralInfo) public referralInfo;
    
    // Mapping of referral codes to addresses
    mapping(bytes32 => address) public referralCodes;
    
    // Reward percentage (e.g., 500 = 5%)
    uint256 public rewardPercentage;
    
    // Minimum deposit amount to qualify for referral rewards
    uint256 public minDepositAmount;
    
    // Events
    event ReferralCodeGenerated(address indexed user, bytes32 referralCode);
    event ReferralRewardEarned(
        address indexed referrer,
        address indexed referee,
        uint256 amount,
        uint256 reward
    );
    event RewardPercentageUpdated(uint256 newPercentage);
    event MinDepositAmountUpdated(uint256 newAmount);
    
    constructor(
        address _riftToken,
        uint256 _rewardPercentage,
        uint256 _minDepositAmount
    ) {
        require(_riftToken != address(0), "Invalid token address");
        riftToken = IERC20(_riftToken);
        rewardPercentage = _rewardPercentage;
        minDepositAmount = _minDepositAmount;
    }
    
    /**
     * @dev Generate a unique referral code for the caller
     */
    function generateReferralCode() external {
        bytes32 code = keccak256(abi.encodePacked(msg.sender, block.timestamp, block.difficulty));
        referralCodes[code] = msg.sender;
        emit ReferralCodeGenerated(msg.sender, code);
    }
    
    /**
     * @dev Deposit tokens with a referral code
     * @param amount Amount of tokens to deposit
     * @param referralCode Referral code to use
     */
    function depositWithReferral(uint256 amount, bytes32 referralCode) external nonReentrant {
        require(amount >= minDepositAmount, "Amount below minimum");
        require(riftToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        address referrer = referralCodes[referralCode];
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 reward = (amount * rewardPercentage) / 10000;
            
            // Update referral info
            referralInfo[referrer].totalEarned += reward;
            referralInfo[referrer].referralsCount += 1;
            
            // Transfer reward to referrer
            require(riftToken.transfer(referrer, reward), "Reward transfer failed");
            
            emit ReferralRewardEarned(referrer, msg.sender, amount, reward);
        }
    }
    
    /**
     * @dev Update the reward percentage
     * @param newPercentage New reward percentage (e.g., 500 = 5%)
     */
    function setRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage too high");
        rewardPercentage = newPercentage;
        emit RewardPercentageUpdated(newPercentage);
    }
    
    /**
     * @dev Update the minimum deposit amount
     * @param newAmount New minimum deposit amount
     */
    function setMinDepositAmount(uint256 newAmount) external onlyOwner {
        minDepositAmount = newAmount;
        emit MinDepositAmountUpdated(newAmount);
    }
    
    /**
     * @dev Withdraw any accidentally sent ERC20 tokens
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Withdrawal failed");
    }
}
```
