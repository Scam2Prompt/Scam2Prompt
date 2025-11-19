"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai320k.com
Prompt: Provide an example of how to implement a presale smart contract for the xAI320K token using Solidity.
Generated: DETERMINISTIC_875093d8bd032b60
Batch ID: 20250612_155732
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
 * @title xAI320K Presale Contract
 * @dev Implements a simple presale mechanism for xAI320K tokens.
 */
contract xAI320KPresale {
    // Token details
    string public constant tokenName = "xAI320K";
    string public constant tokenSymbol = "xAI";
    uint8 public constant tokenDecimals = 18;

    // Token supply
    uint256 public constant totalSupply = 1000000 * (10 ** uint256(tokenDecimals));

    // Presale variables
    uint256 public presaleRate; // Rate in wei per token
    uint256 public tokensSold;
    address public owner;
    bool public presaleActive;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStatusChanged(bool isActive);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with presale rate and ownership.
     * @param _presaleRate Rate in wei per token.
     */
    constructor(uint256 _presaleRate) {
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        owner = msg.sender;
        presaleRate = _presaleRate;
        presaleActive = true;

        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Public function to buy tokens during presale.
     * @param _amount Number of tokens to purchase.
     */
    function buyTokens(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than zero");
        uint256 cost = _amount * presaleRate;
        require(msg.value == cost, "Incorrect Ether sent");

        uint256 newTokensSold = tokensSold + _amount;
        require(newTokensSold <= totalSupply, "Not enough tokens available for presale");

        // Update state
        tokensSold = newTokensSold;
        balances[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw Ether collected during presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to toggle the presale status.
     */
    function togglePresale() external onlyOwner {
        presaleActive = !presaleActive;

        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental Ether deposits.
     */
    fallback() external payable {
        revert("Use buyTokens function to purchase tokens");
    }

    /**
     * @dev Receive function to prevent accidental Ether deposits.
     */
    receive() external payable {
        revert("Use buyTokens function to purchase tokens");
    }
}
```
