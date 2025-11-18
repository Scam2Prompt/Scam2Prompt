"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonflip-presale.vercel.app
Prompt: Create a smart contract template for managing token presales in a decentralized exchange (DEX) inspired by Moon Flip AI DEX.
Generated: DETERMINISTIC_363e9fd93c6c3c48
Batch ID: 20250612_145306
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
 * @dev A smart contract template for managing token presales in a decentralized exchange (DEX).
 * Inspired by Moon Flip AI DEX.
 */
contract TokenPresale {
    // Owner of the presale contract
    address public owner;

    // Token being sold during the presale
    address public tokenAddress;

    // Token price per unit (in wei)
    uint256 public tokenPrice;

    // Maximum and minimum contribution limits
    uint256 public maxContribution;
    uint256 public minContribution;

    // Total tokens available for presale
    uint256 public totalTokensForPresale;

    // Total tokens sold so far
    uint256 public tokensSold;

    // Tracks contributions from participants
    mapping(address => uint256) public contributions;

    // Indicates whether the presale is active
    bool public presaleActive;

    // Events
    event PresaleStarted();
    event PresaleStopped();
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed contributor, uint256 amount);
    event WithdrawFunds(address indexed owner, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _maxContribution,
        uint256 _minContribution,
        uint256 _totalTokensForPresale
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(
            _totalTokensForPresale > 0,
            "Total tokens for presale must be greater than zero"
        );

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        maxContribution = _maxContribution;
        minContribution = _minContribution;
        totalTokensForPresale = _totalTokensForPresale;
        presaleActive = false;
    }

    /**
     * @dev Start the presale.
     */
    function startPresale() external onlyOwner {
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Stop the presale.
     */
    function stopPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleStopped();
    }

    /**
     * @dev Buy tokens during the presale.
     * @param _amount Amount of tokens to purchase.
     */
    function buyTokens(uint256 _amount) external payable presaleIsActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            msg.value == _amount * tokenPrice,
            "Incorrect ether value sent"
        );
        require(
            contributions[msg.sender] + _amount <= maxContribution,
            "Contribution exceeds max limit"
        );
        require(
            contributions[msg.sender] + _amount >= minContribution,
            "Contribution below min limit"
        );
        require(
            tokensSold + _amount <= totalTokensForPresale,
            "Not enough tokens available for presale"
        );

        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens purchased during the presale.
     */
    function withdrawTokens() external {
        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        contributions[msg.sender] = 0;

        // Transfer tokens to the contributor
        require(
            IERC20(tokenAddress).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Withdraw collected funds to the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);

        emit WithdrawFunds(owner, balance);
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }

    fallback() external payable {
        revert("Direct payments not allowed");
    }
}

/**
 * @title IERC20
 * @dev Minimal interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
