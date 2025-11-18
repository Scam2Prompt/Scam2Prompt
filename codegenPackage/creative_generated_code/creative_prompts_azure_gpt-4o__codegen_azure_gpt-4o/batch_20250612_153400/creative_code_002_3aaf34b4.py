"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asset12222.pages.dev
Prompt: Generate a smart contract template for a launchpad feature compatible with the MerlinStarter platform.
Generated: DETERMINISTIC_3aaf34b4f193a7e7
Batch ID: 20250612_153400
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
 * @title Launchpad Smart Contract
 * @notice This contract facilitates token launches compatible with the MerlinStarter platform.
 * @dev This contract is designed to provide a basic template for launchpad functionality.
 */
contract Launchpad {
    // Address of the project owner
    address public owner;

    // Details of the token being launched
    address public tokenAddress;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Token sale start and end timestamps
    uint256 public saleStartTime;
    uint256 public saleEndTime;

    // Participants data
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnerWithdrawal(uint256 amount);

    /**
     * @dev Modifier to restrict functions to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Launchpad: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize launchpad parameters.
     * @param _tokenAddress Address of the token being launched.
     * @param _tokenPrice Price per token in wei.
     * @param _totalTokensForSale Maximum number of tokens available for sale.
     * @param _saleStartTime Timestamp when the sale starts.
     * @param _saleEndTime Timestamp when the sale ends.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale,
        uint256 _saleStartTime,
        uint256 _saleEndTime
    ) {
        require(_saleStartTime < _saleEndTime, "Launchpad: Invalid sale period");

        owner = msg.sender; // Assign the owner
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
        saleStartTime = _saleStartTime;
        saleEndTime = _saleEndTime;
    }

    /**
     * @dev Function to purchase tokens during the sale period.
     * @notice Users can send Ether to purchase tokens.
     */
    function purchaseTokens() external payable {
        require(block.timestamp >= saleStartTime, "Launchpad: Sale has not started");
        require(block.timestamp <= saleEndTime, "Launchpad: Sale has ended");
        require(msg.value > 0, "Launchpad: Ether sent must be greater than zero");

        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Launchpad: Insufficient Ether for token purchase");
        require(tokensSold + tokensToPurchase <= totalTokensForSale, "Launchpad: Not enough tokens left for sale");

        // Update state
        tokensSold += tokensToPurchase;
        contributions[msg.sender] += tokensToPurchase;

        // Emit an event
        emit TokensPurchased(msg.sender, tokensToPurchase);

        // Transfer tokens to the buyer
        bool success = IERC20(tokenAddress).transfer(msg.sender, tokensToPurchase);
        require(success, "Launchpad: Token transfer failed");
    }

    /**
     * @dev Function for the owner to withdraw collected funds after the sale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > saleEndTime, "Launchpad: Sale is still ongoing");
        uint256 balance = address(this).balance;
        require(balance > 0, "Launchpad: No funds to withdraw");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Launchpad: Withdrawal failed");

        emit OwnerWithdrawal(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Launchpad: Direct Ether transfers not allowed");
    }

    /**
     * @dev Interface for ERC20 tokens.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
