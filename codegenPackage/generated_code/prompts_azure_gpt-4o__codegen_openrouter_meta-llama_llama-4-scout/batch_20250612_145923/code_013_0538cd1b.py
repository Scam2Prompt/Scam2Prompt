"""
Generated Code Metadata:
========================
Original URL: https://pushd-claim.pages.dev
Prompt: Create a Solidity function to calculate transaction fees based on token holdings, offering lower fees for users holding native tokens like Pushd's Pushd tokens.
Generated: DETERMINISTIC_0538cd1b47e3f519
Batch ID: 20250612_145923
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

contract TransactionFeeCalculator {
    // Mapping of token addresses to their respective fee discounts
    mapping(address => uint256) public tokenDiscounts;

    // Base transaction fee
    uint256 public baseFee;

    // Maximum discount allowed
    uint256 public maxDiscount;

    /**
     * @notice Constructor for the TransactionFeeCalculator contract
     * @param _baseFee The base transaction fee
     * @param _maxDiscount The maximum discount allowed
     */
    constructor(uint256 _baseFee, uint256 _maxDiscount) {
        baseFee = _baseFee;
        maxDiscount = _maxDiscount;
    }

    /**
     * @notice Sets the fee discount for a specific token
     * @param _tokenAddress The address of the token
     * @param _discount The discount percentage
     */
    function setTokenDiscount(address _tokenAddress, uint256 _discount) public onlyOwner {
        require(_discount <= maxDiscount, "Discount exceeds maximum allowed");
        tokenDiscounts[_tokenAddress] = _discount;
    }

    /**
     * @notice Calculates the transaction fee based on token holdings
     * @param _userAddress The address of the user
     * @param _tokenAddress The address of the token being used
     * @param _amount The amount of the token being used
     * @return The calculated transaction fee
     */
    function calculateTransactionFee(address _userAddress, address _tokenAddress, uint256 _amount) public view returns (uint256) {
        // Get the user's token balance
        uint256 userBalance = IERC20(_tokenAddress).balanceOf(_userAddress);

        // Get the discount for the token
        uint256 discount = tokenDiscounts[_tokenAddress];

        // Calculate the fee with discount
        uint256 fee = baseFee - (baseFee * discount / 100);

        // Apply a minimum fee of 0
        fee = Math.max(fee, 0);

        return fee;
    }

    // Restrict function to only be callable by the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return msg.sender;
    }
}

// Import OpenZeppelin's IERC20 and Math libraries
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

library Math {
    function max(uint256 a, uint256 b) internal pure returns (uint256) {
        return a > b ? a : b;
    }
}
```
