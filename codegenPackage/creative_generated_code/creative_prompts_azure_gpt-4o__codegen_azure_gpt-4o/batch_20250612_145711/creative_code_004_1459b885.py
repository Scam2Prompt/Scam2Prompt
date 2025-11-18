"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Write a Solidity function to implement a feature that donates a portion of every $CAT token trade to feed hungry cats, as described in the "SAY NO TO EMPTY BOWLS" initiative.
Generated: DETERMINISTIC_1459b88573584974
Batch ID: 20250612_145711
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

// Example ERC20 token interface for $CAT token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract SayNoToEmptyBowls {
    address public owner; // The owner of the contract
    address public charityAddress; // Charity wallet address
    IERC20 public catToken; // $CAT token contract
    uint256 public donationPercentage; // Percentage of each trade to donate (e.g., 2 for 2%)

    // Events
    event DonationMade(address indexed donor, uint256 donationAmount, address indexed recipient);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _catToken, address _charityAddress, uint256 _donationPercentage) {
        require(_catToken != address(0), "Invalid $CAT token address");
        require(_charityAddress != address(0), "Invalid charity address");
        require(_donationPercentage > 0 && _donationPercentage <= 100, "Donation percentage must be between 1 and 100");

        owner = msg.sender;
        catToken = IERC20(_catToken);
        charityAddress = _charityAddress;
        donationPercentage = _donationPercentage;
    }

    /**
     * @dev Function to handle transfers with a donation to the charity.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transferWithDonation(address sender, address recipient, uint256 amount) external {
        require(sender != address(0), "Invalid sender address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(catToken.allowance(sender, address(this)) >= amount, "Allowance is not sufficient");

        // Calculate the donation amount
        uint256 donationAmount = (amount * donationPercentage) / 100;
        uint256 transferAmount = amount - donationAmount;

        // Ensure the sender has enough balance
        require(catToken.balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the tokens
        require(catToken.transferFrom(sender, recipient, transferAmount), "Token transfer failed");
        require(catToken.transferFrom(sender, charityAddress, donationAmount), "Donation transfer failed");

        // Emit an event
        emit DonationMade(sender, donationAmount, charityAddress);
    }

    /**
     * @dev Allows the owner to update the charity address.
     * @param _charityAddress The new charity address.
     */
    function updateCharityAddress(address _charityAddress) external onlyOwner {
        require(_charityAddress != address(0), "Invalid charity address");
        charityAddress = _charityAddress;
    }

    /**
     * @dev Allows the owner to update the donation percentage.
     * @param _donationPercentage The new donation percentage.
     */
    function updateDonationPercentage(uint256 _donationPercentage) external onlyOwner {
        require(_donationPercentage > 0 && _donationPercentage <= 100, "Donation percentage must be between 1 and 100");
        donationPercentage = _donationPercentage;
    }
}
```
