"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a smart contract for a cryptocurrency token presale with a cap of 1000 ETH, similar to the $ALIEN PRE-SALE.
Generated: DETERMINISTIC_9075e39d0ad35728
Batch ID: 20250622_205836
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
 * @title TokenPresale
 * @dev A smart contract for a capped cryptocurrency token presale.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the presale contract
    uint256 public constant CAP = 1000 ether; // Maximum amount of ETH that can be raised
    uint256 public totalRaised; // Total ETH raised so far
    uint256 public tokenRate; // Number of tokens per 1 ETH
    bool public presaleActive; // Flag to indicate if presale is active
    IERC20 public token; // ERC20 token being sold

    mapping(address => uint256) public contributions; // Tracks contributions per address

    // Events
    event PresaleStarted();
    event PresaleEnded();
    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

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
        require(!presaleActive, "Presale is already active");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _tokenRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenRate > 0, "Token rate must be greater than zero");

        owner = msg.sender;
        token = IERC20(_tokenAddress);
        tokenRate = _tokenRate;
        presaleActive = false;
    }

    /**
     * @dev Start the presale.
     */
    function startPresale() external onlyOwner whenPresaleInactive {
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev End the presale.
     */
    function endPresale() external onlyOwner whenPresaleActive {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale.
     */
    function purchaseTokens() external payable whenPresaleActive {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= CAP, "Presale cap exceeded");

        uint256 tokenAmount = msg.value * tokenRate; // Calculate token amount
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        // Update state
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to buyer
        token.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Withdraw funds raised during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
