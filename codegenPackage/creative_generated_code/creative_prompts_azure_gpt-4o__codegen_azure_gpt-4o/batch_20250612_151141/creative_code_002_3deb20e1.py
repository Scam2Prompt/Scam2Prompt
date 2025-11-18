"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Recommend a blockchain loyalty program implementation for gas stations using CRUDO tokens, including features like cashback, discounts, and referral bonuses. Provide code examples for smart contract development on Binance Smart Chain.
Generated: DETERMINISTIC_3deb20e1e22b0576
Batch ID: 20250612_151141
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
 * @title GasStationLoyaltyProgram
 * @dev A blockchain-based loyalty program for gas stations using CRUDO tokens.
 * Features include cashback, discounts, and referral bonuses.
 */
contract GasStationLoyaltyProgram {
    // Owner of the contract
    address public owner;

    // CRUDO token interface
    IERC20 public crudoToken;

    // Cashback rate (percentage, e.g., 5 for 5%)
    uint256 public cashbackRate;

    // Referral bonus (amount in tokens)
    uint256 public referralBonus;

    // Mapping to track referral relationships
    mapping(address => address) public referrer;

    // Events
    event CashbackPaid(address indexed user, uint256 amount);
    event ReferralBonusPaid(address indexed referrer, uint256 amount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _crudoToken Address of the CRUDO token contract.
     * @param _cashbackRate Cashback percentage (e.g., 5 for 5%).
     * @param _referralBonus Referral bonus (amount in tokens).
     */
    constructor(IERC20 _crudoToken, uint256 _cashbackRate, uint256 _referralBonus) {
        owner = msg.sender;
        crudoToken = _crudoToken;
        cashbackRate = _cashbackRate;
        referralBonus = _referralBonus;
    }

    /**
     * @dev Function to set cashback rate (only by owner).
     * @param _cashbackRate New cashback percentage.
     */
    function setCashbackRate(uint256 _cashbackRate) external onlyOwner {
        cashbackRate = _cashbackRate;
    }

    /**
     * @dev Function to set referral bonus (only by owner).
     * @param _referralBonus New referral bonus amount.
     */
    function setReferralBonus(uint256 _referralBonus) external onlyOwner {
        referralBonus = _referralBonus;
    }

    /**
     * @dev Function for users to register their referrer.
     * @param _referrer Address of the referrer.
     */
    function registerReferrer(address _referrer) external {
        require(referrer[msg.sender] == address(0), "Referrer already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");
        referrer[msg.sender] = _referrer;
    }

    /**
     * @dev Function to claim cashback for a gas purchase.
     * @param purchaseAmount Amount of purchase in tokens.
     */
    function claimCashback(uint256 purchaseAmount) external {
        uint256 cashback = (purchaseAmount * cashbackRate) / 100;
        require(crudoToken.balanceOf(address(this)) >= cashback, "Insufficient contract balance");

        // Pay cashback to user
        crudoToken.transfer(msg.sender, cashback);
        emit CashbackPaid(msg.sender, cashback);

        // Pay referral bonus if applicable
        address userReferrer = referrer[msg.sender];
        if (userReferrer != address(0)) {
            uint256 bonus = referralBonus;
            require(crudoToken.balanceOf(address(this)) >= bonus, "Insufficient contract balance");
            crudoToken.transfer(userReferrer, bonus);
            emit ReferralBonusPaid(userReferrer, bonus);
        }
    }

    /**
     * @dev Function to deposit CRUDO tokens into the contract.
     * @param amount Amount of tokens to deposit.
     */
    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        crudoToken.transferFrom(msg.sender, address(this), amount);
    }

    /**
     * @dev Function to withdraw CRUDO tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(crudoToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        crudoToken.transfer(owner, amount);
    }
}

/**
 * @dev Interface for an ERC20 token (CRUDO token).
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
