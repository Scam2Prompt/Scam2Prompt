"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Generate code for a referral system in a cryptocurrency smart contract where users earn rewards in USDC based on purchases made using their referral code, as described in MoonBag's referral program.
Generated: DETERMINISTIC_9a5cf31bdec41ea1
Batch ID: 20250612_150902
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
 * @dev A smart contract for a referral system where users earn USDC rewards based on purchases made using their referral code.
 */
contract ReferralProgram {
    // USDC token interface
    IERC20 public usdcToken;

    // Owner of the contract
    address public owner;

    // Referral structure
    struct Referral {
        uint256 rewardBalance; // Reward balance in USDC
        uint256 totalPurchases; // Total purchases made through the referral
    }

    // Mapping of referral codes to referrers' addresses
    mapping(string => address) public referralCodes;

    // Mapping of referrers' addresses to their referral details
    mapping(address => Referral) public referrals;

    // Event emitted when a referral reward is issued
    event ReferralRewardIssued(address indexed referrer, uint256 rewardAmount, string referralCode);

    // Event emitted for a successful purchase
    event PurchaseMade(address indexed buyer, uint256 purchaseAmount, string referralCode);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the initial USDC token.
     * @param _usdcToken Address of the USDC token contract.
     */
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        usdcToken = IERC20(_usdcToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to register a referral code.
     * @param _referralCode The referral code to register.
     */
    function registerReferralCode(string memory _referralCode) external {
        require(referralCodes[_referralCode] == address(0), "Referral code already exists");
        referralCodes[_referralCode] = msg.sender;
    }

    /**
     * @dev Function to make a purchase and issue rewards to the referrer.
     * @param _purchaseAmount Amount of purchase in USDC.
     * @param _referralCode Referral code used for the purchase.
     */
    function makePurchase(uint256 _purchaseAmount, string memory _referralCode) external {
        require(referralCodes[_referralCode] != address(0), "Invalid referral code");
        require(_purchaseAmount > 0, "Purchase amount must be greater than zero");

        // Transfer USDC from the buyer to the contract
        require(usdcToken.transferFrom(msg.sender, address(this), _purchaseAmount), "USDC transfer failed");

        // Calculate reward (e.g., 5% of purchase amount)
        uint256 rewardAmount = (_purchaseAmount * 5) / 100;

        // Find the referrer using the referral code
        address referrer = referralCodes[_referralCode];

        // Update referrer details
        referrals[referrer].rewardBalance += rewardAmount;
        referrals[referrer].totalPurchases += _purchaseAmount;

        // Emit purchase event
        emit PurchaseMade(msg.sender, _purchaseAmount, _referralCode);

        // Issue reward to referrer
        issueReferralReward(referrer, rewardAmount, _referralCode);
    }

    /**
     * @dev Internal function to issue rewards to the referrer.
     * @param _referrer Referrer's address.
     * @param _rewardAmount Amount of reward in USDC.
     * @param _referralCode Referral code used.
     */
    function issueReferralReward(address _referrer, uint256 _rewardAmount, string memory _referralCode) internal {
        require(usdcToken.transfer(_referrer, _rewardAmount), "USDC reward transfer failed");
        emit ReferralRewardIssued(_referrer, _rewardAmount, _referralCode);
    }

    /**
     * @dev Function to withdraw accumulated USDC rewards.
     */
    function withdrawRewards() external {
        uint256 rewardBalance = referrals[msg.sender].rewardBalance;
        require(rewardBalance > 0, "No rewards available for withdrawal");

        // Reset reward balance
        referrals[msg.sender].rewardBalance = 0;

        // Transfer rewards
        require(usdcToken.transfer(msg.sender, rewardBalance), "USDC transfer failed");
    }

    /**
     * @dev Owner function to withdraw contract's USDC balance if necessary.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= _amount, "Insufficient USDC balance in contract");
        require(usdcToken.transfer(owner, _amount), "USDC withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 tokens (simplified).
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
