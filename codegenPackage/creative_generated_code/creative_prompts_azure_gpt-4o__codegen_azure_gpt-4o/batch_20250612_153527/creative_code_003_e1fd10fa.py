"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchainairdrop1.pages.dev
Prompt: Create a smart contract in Solidity for Lightchain AI’s token presale, incorporating features like discounted pricing, governance voting rights, and referral bonuses.
Generated: DETERMINISTIC_e1fd10fa28df7921
Batch ID: 20250612_153527
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
 * @title Lightchain AI Token Presale Contract
 * @dev A smart contract for managing the presale of Lightchain AI tokens.
 *      Includes features like discounted pricing, governance voting rights, and referral bonuses.
 */
contract LightchainAITokenPresale {
    // Token details
    string public constant NAME = "Lightchain AI Token";
    string public constant SYMBOL = "LAI";
    uint8 public constant DECIMALS = 18;

    // Presale parameters
    uint256 public constant PRESALE_PRICE = 0.01 ether; // Discounted price per token
    uint256 public constant REFERRAL_BONUS_PERCENT = 5; // Referral bonus in percentage
    uint256 public constant MAX_SUPPLY = 1_000_000 * (10 ** uint256(DECIMALS)); // Max token supply
    uint256 public tokensSold;

    // Governance voting rights mapping
    mapping(address => uint256) public governanceWeight;

    // Referral tracking
    mapping(address => uint256) public referralEarnings;

    // Contract owner
    address public owner;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 tokensAmount, uint256 paidAmount);
    event ReferralReward(address indexed referrer, uint256 rewardAmount);
    event GovernanceUpdated(address indexed participant, uint256 weight);

    /**
     * @dev Modifier to restrict functions to owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Function to purchase tokens during the presale.
     *      Handles discounted pricing and referral bonuses.
     * @param referrer Address of the referrer (optional, can be zero address).
     */
    function buyTokens(address referrer) external payable {
        require(msg.value >= PRESALE_PRICE, "Insufficient funds to purchase tokens.");
        require(tokensSold < MAX_SUPPLY, "Presale has reached the maximum token supply.");

        // Calculate the number of tokens being purchased
        uint256 tokensAmount = (msg.value * (10 ** uint256(DECIMALS))) / PRESALE_PRICE;

        // Ensure the tokens do not exceed the maximum supply
        require(tokensSold + tokensAmount <= MAX_SUPPLY, "Purchase exceeds max token supply.");

        // Update governance voting weight
        governanceWeight[msg.sender] += tokensAmount;

        // Award referral bonus if applicable
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralBonus = (msg.value * REFERRAL_BONUS_PERCENT) / 100;
            referralEarnings[referrer] += referralBonus;
            emit ReferralReward(referrer, referralBonus);
        }

        // Update the total tokens sold
        tokensSold += tokensAmount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensAmount, msg.value);
        emit GovernanceUpdated(msg.sender, governanceWeight[msg.sender]);
    }

    /**
     * @dev Function to withdraw funds collected in the presale.
     *      Restricted to the contract owner.
     * @param amount Amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Not enough balance to withdraw.");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed.");
    }

    /**
     * @dev Receive function to handle ether transfers (e.g., from wallets or exchanges).
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed.");
    }
}
```
