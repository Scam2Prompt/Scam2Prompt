"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity function that calculates and distributes referral commissions across four levels, using the structure provided in the MinerDog contract.
Generated: DETERMINISTIC_cd47c4dce9684d29
Batch ID: 20250612_154111
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

contract ReferralCommissionDistributor {
    // State variables
    address public owner;

    // Mapping to store referral relationships
    mapping(address => address) public referrer; // Tracks who referred whom
    mapping(address => uint256) public balances; // Tracks user balances

    // Referral commission percentages for each level
    uint256[4] public referralPercentages = [500, 300, 200, 100]; // 5%, 3%, 2%, 1% (scaled by 10000 for precision)

    // Events for logging commission distributions
    event ReferralCommissionPaid(address indexed referrer, address indexed referee, uint256 amount, uint256 level);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Set the referrer for a user. This must be called before the user makes any transaction.
     * @param user The address of the user.
     * @param _referrer The address of the user's referrer.
     */
    function setReferrer(address user, address _referrer) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(_referrer != address(0), "Invalid referrer address");
        require(referrer[user] == address(0), "Referrer already set"); // Cannot overwrite referrer
        referrer[user] = _referrer;
    }

    /**
     * @dev Distribute referral commissions across up to four levels.
     * @param amount The total amount from which commissions will be calculated.
     * @param user The address of the user making the transaction.
     */
    function distributeReferralCommission(uint256 amount, address user) external {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        address currentReferrer = referrer[user];

        for (uint256 i = 0; i < referralPercentages.length; i++) {
            // Exit the loop if there's no referrer at the current level
            if (currentReferrer == address(0)) {
                break;
            }

            // Calculate commission for the current level
            uint256 commission = (amount * referralPercentages[i]) / 10000;

            // Update the referrer's balance
            balances[currentReferrer] += commission;

            // Emit event for logging the transaction
            emit ReferralCommissionPaid(currentReferrer, user, commission, i + 1);

            // Move to the next level referrer
            currentReferrer = referrer[currentReferrer];
        }
    }

    /**
     * @dev Withdraw balance for the caller.
     */
    function withdraw() external {
        uint256 balance = balances[msg.sender];
        require(balance > 0, "Insufficient balance");

        // Reset balance before transfer to prevent re-entrancy attacks
        balances[msg.sender] = 0;

        // Transfer the balance to the caller
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Allow the owner to withdraw contract balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Transfer failed");
    }
}
```
