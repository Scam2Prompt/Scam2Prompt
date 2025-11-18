"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a smart contract in Solidity that implements a presale mechanism for a cryptocurrency token, ensuring the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_14a07d61a5789210
Batch ID: 20250612_152739
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
 * @title PresaleTokenContract
 * @dev Implements a presale mechanism for a cryptocurrency token.
 */
contract PresaleTokenContract {
    // Token details
    string public name = "PresaleToken";
    string public symbol = "PST";
    uint8 public decimals = 18;

    // Total supply and initial cap
    uint256 public constant MAX_SUPPLY = 100_000_000 * (10 ** uint256(decimals));
    uint256 public totalSupply;

    // Presale variables
    uint256 public presaleRate = 1000; // Number of tokens per 1 ETH
    bool public presaleActive = true;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Address of the contract owner
    address public owner;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event PresaleEnded();

    /**
     * @dev Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to accept ETH during presale.
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Allows the purchase of tokens during the presale period.
     */
    function purchaseTokens() public payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "No ETH sent");

        uint256 tokenAmount = msg.value * presaleRate;

        require(totalSupply + tokenAmount <= MAX_SUPPLY, "Exceeds maximum token supply");

        totalSupply += tokenAmount;
        balances[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Ends the presale. Can only be called by the owner.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");

        presaleActive = false;

        emit PresaleEnded();
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");

        emit OwnershipTransferred(owner, newOwner);

        owner = newOwner;
    }

    /**
     * @dev Withdraws collected ETH from the contract. Can only be called by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Returns the token balance of a specific address.
     * @param account Address to query the balance of.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
