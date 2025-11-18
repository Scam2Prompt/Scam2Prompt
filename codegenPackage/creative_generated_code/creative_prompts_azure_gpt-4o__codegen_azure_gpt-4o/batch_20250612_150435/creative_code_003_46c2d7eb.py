"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Create a smart contract in Solidity for implementing TG.Casino's buy-back mechanism for `$TGC` tokens as described in the roadmap.
Generated: DETERMINISTIC_46c2d7eb5f1f7e0f
Batch ID: 20250612_150435
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
 * @title TG.Casino Buy-Back Mechanism Smart Contract
 * @dev Implements the buy-back mechanism for `$TGC` tokens in line with TG.Casino's roadmap.
 */
contract TGCBuyBack {
    // Declare state variables
    address public owner; // Owner of the contract
    address public TGC_TOKEN_ADDRESS; // Address of the `$TGC` token contract
    uint256 public buyBackPool; // Amount of Ether available for buy-back
    
    event TokensBoughtBack(address indexed seller, uint256 tokenAmount, uint256 etherAmount);
    event FundsDeposited(address indexed depositor, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the owner and `$TGC` token address.
     * @param _TGC_TOKEN_ADDRESS Address of the `$TGC` token contract.
     */
    constructor(address _TGC_TOKEN_ADDRESS) {
        require(_TGC_TOKEN_ADDRESS != address(0), "Invalid token address");
        owner = msg.sender;
        TGC_TOKEN_ADDRESS = _TGC_TOKEN_ADDRESS;
    }

    /**
     * @dev Deposit Ether into the buy-back pool.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        buyBackPool += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to sell `$TGC` tokens back to the contract for Ether.
     * @param tokenAmount Amount of `$TGC` tokens to sell.
     */
    function sellTokens(uint256 tokenAmount) external {
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Interface for the `$TGC` token contract
        IERC20 TGCToken = IERC20(TGC_TOKEN_ADDRESS);

        // Calculate the Ether value of the tokens (assumes a fixed buy-back rate)
        uint256 etherAmount = getBuyBackRate(tokenAmount);
        require(etherAmount <= buyBackPool, "Insufficient buy-back pool");

        // Transfer `$TGC` tokens from the seller to the contract
        require(TGCToken.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        // Transfer Ether from the pool to the seller
        (bool success, ) = msg.sender.call{value: etherAmount}("");
        require(success, "Ether transfer failed");

        // Update the buy-back pool
        buyBackPool -= etherAmount;

        emit TokensBoughtBack(msg.sender, tokenAmount, etherAmount);
    }

    /**
     * @dev Calculates the buy-back rate for `$TGC` tokens (e.g., fixed rate of 1 TGC = 0.01 Ether).
     * @param tokenAmount Amount of `$TGC` tokens to evaluate.
     * @return Ether amount corresponding to the token amount.
     */
    function getBuyBackRate(uint256 tokenAmount) public pure returns (uint256) {
        // Example fixed rate: 1 TGC = 0.01 Ether
        return tokenAmount * 10**16; // 0.01 Ether per token
    }

    /**
     * @dev Allows the owner to withdraw unused Ether from the buy-back pool.
     * @param amount Amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= buyBackPool, "Insufficient buy-back pool");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
        buyBackPool -= amount;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to handle Ether sent directly to the contract.
     */
    receive() external payable {
        buyBackPool += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }
}

/**
 * @dev Minimal ERC20 interface to interact with the `$TGC` token contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
