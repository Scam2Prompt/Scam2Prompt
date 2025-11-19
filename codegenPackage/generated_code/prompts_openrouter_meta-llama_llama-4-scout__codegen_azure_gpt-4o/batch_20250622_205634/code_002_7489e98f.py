"""
Generated Code Metadata:
========================
Original URL: https://presale-x.com
Prompt: Generate code for a smart contract that handles token sales and risk disclosures for accredited investors under Regulation D of the U.S. Securities Act.
Generated: DETERMINISTIC_7489e98fb412d415
Batch ID: 20250622_205634
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
 * @title TokenSaleWithRiskDisclosure
 * @dev Smart contract for token sales with risk disclosures for accredited investors under Regulation D.
 */
contract TokenSaleWithRiskDisclosure {
    // Token details
    string public constant tokenName = "RegDToken";
    string public constant tokenSymbol = "RDT";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Token price in wei
    uint256 public tokenPrice = 0.01 ether;

    // Owner of the contract
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Accredited investor whitelist
    mapping(address => bool) public accreditedInvestors;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount);
    event InvestorWhitelisted(address indexed investor);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to restrict access to accredited investors
    modifier onlyAccreditedInvestor() {
        require(accreditedInvestors[msg.sender], "You must be an accredited investor to purchase tokens");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Function to whitelist an accredited investor.
     * @param _investor Address of the investor to whitelist.
     */
    function whitelistInvestor(address _investor) external onlyOwner {
        require(_investor != address(0), "Invalid investor address");
        accreditedInvestors[_investor] = true;
        emit InvestorWhitelisted(_investor);
    }

    /**
     * @dev Function to purchase tokens.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable onlyAccreditedInvestor {
        require(_amount > 0, "Token amount must be greater than zero");
        uint256 cost = _amount * tokenPrice;
        require(msg.value == cost, "Incorrect Ether value sent");
        require(balances[owner] >= _amount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        balances[owner] -= _amount;
        balances[msg.sender] += _amount;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
