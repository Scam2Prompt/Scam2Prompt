"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Design a smart contract for a digital collectible platform that includes a referral program, where users can earn a percentage of the minting fee for each successful referral.
Generated: DETERMINISTIC_96bec8cec38c900f
Batch ID: 20250622_212447
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

/**
 * @title DigitalCollectibleWithReferral
 * @dev A smart contract for minting digital collectibles with a referral program.
 */
contract DigitalCollectibleWithReferral {
    // State variables
    address public owner; // Contract owner
    uint256 public mintingFee; // Fee for minting a collectible
    uint256 public referralPercentage; // Percentage of minting fee given to referrer

    mapping(address => uint256) public balances; // Tracks user balances for referral rewards

    // Events
    event CollectibleMinted(address indexed minter, address indexed referrer, uint256 feePaid, uint256 referralReward);
    event Withdrawal(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _mintingFee The fee for minting a collectible.
     * @param _referralPercentage The percentage of the minting fee given to referrers.
     */
    constructor(uint256 _mintingFee, uint256 _referralPercentage) {
        require(_referralPercentage <= 100, "Referral percentage must be between 0 and 100");
        owner = msg.sender;
        mintingFee = _mintingFee;
        referralPercentage = _referralPercentage;
    }

    /**
     * @dev Function to mint a collectible.
     * @param referrer The address of the referrer (can be zero address if no referrer).
     */
    function mintCollectible(address referrer) external payable {
        require(msg.value == mintingFee, "Incorrect minting fee");

        uint256 referralReward = 0;

        // If a valid referrer is provided, calculate and distribute referral reward
        if (referrer != address(0) && referrer != msg.sender) {
            referralReward = (mintingFee * referralPercentage) / 100;
            balances[referrer] += referralReward;
        }

        // Emit event for minting
        emit CollectibleMinted(msg.sender, referrer, mintingFee, referralReward);
    }

    /**
     * @dev Function for users to withdraw their referral rewards.
     */
    function withdrawRewards() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset balance before transferring to prevent reentrancy attacks
        balances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to update the minting fee.
     * @param _newMintingFee The new minting fee.
     */
    function updateMintingFee(uint256 _newMintingFee) external onlyOwner {
        mintingFee = _newMintingFee;
    }

    /**
     * @dev Function for the owner to update the referral percentage.
     * @param _newReferralPercentage The new referral percentage.
     */
    function updateReferralPercentage(uint256 _newReferralPercentage) external onlyOwner {
        require(_newReferralPercentage <= 100, "Referral percentage must be between 0 and 100");
        referralPercentage = _newReferralPercentage;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Function for the owner to withdraw contract balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
