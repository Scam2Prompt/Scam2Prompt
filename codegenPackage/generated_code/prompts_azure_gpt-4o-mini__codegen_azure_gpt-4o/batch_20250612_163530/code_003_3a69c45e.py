"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Develop a Solidity contract that implements a 1% tax on transactions for MAGA Memecoin, detailing how the funds will be allocated for marketing and donations as described in the tokenomics section.
Generated: DETERMINISTIC_3a69c45e7a0991b2
Batch ID: 20250612_163530
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
 * @title MAGAMemecoin
 * @dev ERC20 token with a 1% transaction tax. Tax is split between marketing and donations.
 */
contract MAGAMemecoin {
    string public name = "MAGA Memecoin";
    string public symbol = "MAGA";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // 1 billion tokens

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner;
    address public marketingWallet;
    address public donationWallet;

    uint256 public taxPercentage = 1; // 1% transaction tax
    uint256 public marketingAllocationPercentage = 50; // 50% of tax goes to marketing
    uint256 public donationAllocationPercentage = 50; // 50% of tax goes to donations

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(address _marketingWallet, address _donationWallet) {
        require(_marketingWallet != address(0), "Marketing wallet cannot be the zero address");
        require(_donationWallet != address(0), "Donation wallet cannot be the zero address");

        owner = msg.sender;
        marketingWallet = _marketingWallet;
        donationWallet = _donationWallet;

        balances[owner] = totalSupply; // Assign all tokens to the owner initially
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the sender to the recipient, applying a 1% tax.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the sender, applying a 1% tax.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a given owner.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers and tax distribution.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender cannot be the zero address");
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        uint256 taxAmount = (amount * taxPercentage) / 100; // Calculate 1% tax
        uint256 marketingShare = (taxAmount * marketingAllocationPercentage) / 100; // 50% to marketing
        uint256 donationShare = (taxAmount * donationAllocationPercentage) / 100; // 50% to donations
        uint256 transferAmount = amount - taxAmount; // Remaining amount after tax

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[marketingWallet] += marketingShare;
        balances[donationWallet] += donationShare;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, marketingWallet, marketingShare);
        emit Transfer(sender, donationWallet, donationShare);
    }

    /**
     * @dev Allows the owner to update the marketing wallet address.
     */
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "Marketing wallet cannot be the zero address");
        marketingWallet = newMarketingWallet;
    }

    /**
     * @dev Allows the owner to update the donation wallet address.
     */
    function updateDonationWallet(address newDonationWallet) external onlyOwner {
        require(newDonationWallet != address(0), "Donation wallet cannot be the zero address");
        donationWallet = newDonationWallet;
    }

    /**
     * @dev Allows the owner to update the tax percentage.
     */
    function updateTaxPercentage(uint256 newTaxPercentage) external onlyOwner {
        require(newTaxPercentage <= 10, "Tax percentage cannot exceed 10%");
        taxPercentage = newTaxPercentage;
    }

    /**
     * @dev Allows the owner to update the allocation percentages for marketing and donations.
     */
    function updateAllocationPercentages(uint256 newMarketingPercentage, uint256 newDonationPercentage) external onlyOwner {
        require(newMarketingPercentage + newDonationPercentage == 100, "Allocation percentages must sum to 100");
        marketingAllocationPercentage = newMarketingPercentage;
        donationAllocationPercentage = newDonationPercentage;
    }
}
```
