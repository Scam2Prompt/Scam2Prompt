"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jesse-9kw.pages.dev
Prompt: Generate a smart contract in Solidity for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
Generated: DETERMINISTIC_09101eea22e89c36
Batch ID: 20250612_161616
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
 * @title JESSE Token Presale Contract
 * @dev This contract manages a presale with a cap of 1000 BASE tokens and a total supply of 100,000,000 JESSE tokens.
 */
contract JesseTokenPresale {
    // State variables
    uint256 public constant TOTAL_SUPPLY = 100_000_000; // Total supply of JESSE tokens
    uint256 public constant BASE_CAP = 1000;           // Maximum BASE tokens that can be contributed during presale
    uint256 public constant RATE = 100;               // Conversion rate: 1 BASE = 100 JESSE

    address public owner;                             // Address of the contract owner
    uint256 public totalContributed;                  // Total amount of BASE tokens contributed
    mapping(address => uint256) public contributions; // Tracks contributions by each participant
    mapping(address => uint256) public balances;      // Tracks JESSE token balances for participants

    // Events
    event TokensPurchased(address indexed buyer, uint256 baseAmount, uint256 tokenAmount);
    event Withdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier withinCap(uint256 _amount) {
        require(totalContributed + _amount <= BASE_CAP, "Contribution exceeds presale cap");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the owner to the address deploying the contract
    }

    /**
     * @dev Purchase JESSE tokens during the presale using BASE tokens.
     * @param _amount The amount of BASE tokens to contribute.
     */
    function purchaseTokens(uint256 _amount) external payable withinCap(_amount) {
        require(_amount > 0, "Contribution amount must be greater than zero");
        require(msg.value == _amount, "Sent value does not match contribution amount");

        // Calculate the number of JESSE tokens to be minted based on the RATE
        uint256 tokenAmount = _amount * RATE;

        // Update state variables
        totalContributed += _amount;
        contributions[msg.sender] += _amount;
        balances[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, _amount, tokenAmount);
    }

    /**
     * @dev Withdraw BASE tokens collected during the presale.
     * Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(owner, contractBalance);
    }

    /**
     * @dev Get the JESSE token balance of a participant.
     * @param _participant The address of the participant.
     * @return The balance of JESSE tokens.
     */
    function getBalance(address _participant) external view returns (uint256) {
        return balances[_participant];
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Fallback function to prevent accidental function calls to non-existent functions.
     */
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
