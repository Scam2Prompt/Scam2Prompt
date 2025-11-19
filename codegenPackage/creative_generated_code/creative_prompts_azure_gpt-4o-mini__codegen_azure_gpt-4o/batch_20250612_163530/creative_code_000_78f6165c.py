"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Generate a smart contract in Solidity for the pre-sale of the $SRIZE token, ensuring it includes features for minimum and maximum buy limits as described on the Solnarize website.
Generated: DETERMINISTIC_78f6165caaa059c8
Batch ID: 20250612_163530
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
 * @title SRIZE Token Presale Smart Contract
 * @author Solnarize
 * @dev Handles the pre-sale of $SRIZE tokens with minimum and maximum buy limits.
 */
contract SRIZEPresale {
    // Address of the token owner
    address public owner;

    // Token to be sold in the presale
    address public tokenAddress;

    // Price of $SRIZE in wei per token
    uint256 public tokenPrice;

    // Minimum and maximum purchase amounts in wei
    uint256 public minPurchaseAmount;
    uint256 public maxPurchaseAmount;

    // Total funds collected during the presale
    uint256 public totalFunds;

    // Mapping to track individual contributions
    mapping(address => uint256) public contributions;

    // Presale status
    bool public isPresaleActive;

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale parameters.
     * @param _tokenAddress Address of the $SRIZE token contract.
     * @param _tokenPrice Price of the token in wei.
     * @param _minPurchaseAmount Minimum purchase limit in wei.
     * @param _maxPurchaseAmount Maximum purchase limit in wei.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _minPurchaseAmount,
        uint256 _maxPurchaseAmount
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(
            _minPurchaseAmount > 0 && _maxPurchaseAmount > _minPurchaseAmount,
            "Invalid purchase limits"
        );

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        minPurchaseAmount = _minPurchaseAmount;
        maxPurchaseAmount = _maxPurchaseAmount;
        isPresaleActive = false;
    }

    /**
     * @dev Start the presale.
     */
    function startPresale() external onlyOwner {
        require(!isPresaleActive, "Presale is already active");
        isPresaleActive = true;
    }

    /**
     * @dev Stop the presale.
     */
    function stopPresale() external onlyOwner {
        require(isPresaleActive, "Presale is not active");
        isPresaleActive = false;
    }

    /**
     * @dev Purchase $SRIZE tokens during presale.
     */
    function purchaseTokens() external payable {
        require(isPresaleActive, "Presale is not active");
        require(
            msg.value >= minPurchaseAmount && msg.value <= maxPurchaseAmount,
            "Amount must be within purchase limits"
        );

        uint256 tokenAmount = (msg.value * 10**18) / tokenPrice;
        require(tokenAmount > 0, "Token amount must be greater than 0");

        // Update contributions and total funds
        contributions[msg.sender] += msg.value;
        totalFunds += msg.value;

        // Transfer tokens to buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Withdraw collected funds to the owner's wallet.
     */
    function withdrawFunds() external onlyOwner {
        require(totalFunds > 0, "No funds to withdraw");
        uint256 balance = address(this).balance;
        totalFunds = 0;

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Emergency function for the owner to withdraw all tokens back from the contract.
     */
    function emergencyWithdrawTokens() external onlyOwner {
        uint256 balance = IERC20(tokenAddress).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(
            IERC20(tokenAddress).transfer(owner, balance),
            "Token withdrawal failed"
        );
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
