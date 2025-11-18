"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-daomars-com.pages.dev
Prompt: Write a Solidity contract for an Initial Wallet Offering (IWO) platform similar to the MDAO Maker described in the MarsDAO ecosystem.
Generated: DETERMINISTIC_a7eca580344548d9
Batch ID: 20250612_152439
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
 * @title Initial Wallet Offering (IWO) Contract
 * @dev A contract to facilitate token offerings similar to MDAO Maker within the MarsDAO ecosystem.
 */
contract InitialWalletOffering {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the token being offered
    uint256 public tokenRate; // Token rate (tokens per ETH)
    uint256 public totalTokensSold; // Total tokens sold
    uint256 public startTime; // Start time of the IWO
    uint256 public endTime; // End time of the IWO
    bool public offeringActive; // Flag for offering status

    mapping(address => uint256) public contributions; // Tracks contributions for each wallet

    event TokensPurchased(address indexed buyer, uint256 amount);
    event OfferingStarted(uint256 startTime, uint256 endTime);
    event OfferingStopped();

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier offeringActiveCheck() {
        require(offeringActive == true, "Offering is not active");
        require(block.timestamp >= startTime, "Offering has not started");
        require(block.timestamp <= endTime, "Offering has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the token being offered.
     * @param _tokenRate Rate of tokens per ETH.
     */
    constructor(address _tokenAddress, uint256 _tokenRate) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenRate > 0, "Token rate must be greater than zero");
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenRate = _tokenRate;
    }

    /**
     * @dev Start the Initial Wallet Offering.
     * @param _startTime Start time of the offering (Unix timestamp).
     * @param _endTime End time of the offering (Unix timestamp).
     */
    function startOffering(uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        startTime = _startTime;
        endTime = _endTime;
        offeringActive = true;

        emit OfferingStarted(_startTime, _endTime);
    }

    /**
     * @dev Stop the offering, making it inactive.
     */
    function stopOffering() external onlyOwner {
        offeringActive = false;
        emit OfferingStopped();
    }

    /**
     * @dev Purchase tokens during the offering.
     */
    function purchaseTokens() external payable offeringActiveCheck {
        require(msg.value > 0, "ETH value sent must be greater than zero");

        uint256 tokensToBuy = msg.value * tokenRate; // Calculate token amount based on ETH sent
        require(tokensToBuy > 0, "Token amount must be greater than zero");

        // Check token balance of the contract
        uint256 contractTokenBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(contractTokenBalance >= tokensToBuy, "Not enough tokens available in contract");

        // Transfer tokens to the buyer
        bool success = IERC20(tokenAddress).transfer(msg.sender, tokensToBuy);
        require(success, "Token transfer failed");

        // Update state variables
        contributions[msg.sender] += msg.value;
        totalTokensSold += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Withdraw ETH collected in the contract to the owner's wallet.
     */
    function withdrawETH() external onlyOwner {
        uint256 contractETHBalance = address(this).balance;
        require(contractETHBalance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: contractETHBalance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Withdraw remaining tokens in the contract to the owner's wallet after the offering ends.
     */
    function withdrawTokens() external onlyOwner {
        require(block.timestamp > endTime, "Cannot withdraw tokens before offering ends");

        uint256 remainingTokens = IERC20(tokenAddress).balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");

        bool success = IERC20(tokenAddress).transfer(owner, remainingTokens);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

/**
 * @dev ERC20 Interface for interacting with token contracts.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
