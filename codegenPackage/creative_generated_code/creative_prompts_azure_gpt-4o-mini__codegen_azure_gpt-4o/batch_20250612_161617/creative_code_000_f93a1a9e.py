"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Generate a smart contract in Solidity for a presale of a token with a cap of 5,000 ETH and a total supply of 100,000,000 KSI.
Generated: DETERMINISTIC_f93a1a9e9d3730be
Batch ID: 20250612_161617
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
 * @title TokenPresale
 * @dev Smart contract for the presale of KSI tokens. Includes a cap of 5000 ETH and a fixed total token supply.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the presale contract
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * (10**18); // Total supply of KSI tokens (with 18 decimals)
    uint256 public constant PRESALE_CAP = 5000 ether; // Presale cap set to 5000 ETH
    uint256 public tokensPerETH = 20_000; // Exchange rate: 20,000 KSI tokens per 1 ETH
    uint256 public totalETHRaised; // Total ETH raised during the presale
    bool public presaleActive; // Boolean to track if the presale is active

    mapping(address => uint256) public contributions; // Tracks contributions of each address
    mapping(address => uint256) public tokenBalances; // Tracks tokens assigned to each address

    // Events
    event PresaleStarted();
    event PresaleStopped();
    event ContributionReceived(address indexed contributor, uint256 amountETH, uint256 tokensAssigned);
    event TokensClaimed(address indexed claimer, uint256 tokensClaimed);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    modifier whenPresaleInactive() {
        require(!presaleActive, "Presale is active");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
        presaleActive = false;
    }

    /**
     * @dev Starts the presale. Only callable by the owner.
     */
    function startPresale() external onlyOwner whenPresaleInactive {
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Stops the presale. Only callable by the owner.
     */
    function stopPresale() external onlyOwner whenPresaleActive {
        presaleActive = false;
        emit PresaleStopped();
    }

    /**
     * @dev Allows users to contribute ETH in exchange for KSI tokens during the presale.
     */
    function contribute() external payable whenPresaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(totalETHRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        uint256 tokensToAssign = msg.value * tokensPerETH; // Calculate tokens based on contribution
        contributions[msg.sender] += msg.value; // Update contribution tracking
        tokenBalances[msg.sender] += tokensToAssign; // Update token balances
        totalETHRaised += msg.value; // Update total ETH raised

        emit ContributionReceived(msg.sender, msg.value, tokensToAssign);
    }

    /**
     * @dev Allows contributors to claim their tokens after the presale ends.
     */
    function claimTokens() external whenPresaleInactive {
        uint256 tokensToClaim = tokenBalances[msg.sender];
        require(tokensToClaim > 0, "No tokens to claim");

        tokenBalances[msg.sender] = 0; // Reset token balance for claimer
        emit TokensClaimed(msg.sender, tokensToClaim);
        // Normally, tokens would be transferred here from the token contract.
    }

    /**
     * @dev Withdraw ETH collected during the presale. Only callable by the owner.
     */
    function withdrawETH() external onlyOwner whenPresaleInactive {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
