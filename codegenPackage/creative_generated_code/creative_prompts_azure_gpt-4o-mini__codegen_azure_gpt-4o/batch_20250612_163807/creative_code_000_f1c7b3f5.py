"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlana-token.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the presale and token distribution for the Poodlana cryptocurrency, ensuring all tokens are unlocked from day one.
Generated: DETERMINISTIC_f1c7b3f5105b0904
Batch ID: 20250612_163807
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
 * @title Poodlana Presale Smart Contract
 * @dev This contract handles the presale of Poodlana tokens and ensures immediate token unlock.
 */
contract PoodlanaPresale {
    // Token contract interface
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Presale parameters
    uint256 public presaleRate; // Number of tokens per 1 ETH
    uint256 public presaleCap;  // Maximum number of tokens available for presale
    uint256 public totalTokensSold; // Total tokens sold during presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Withdrawn(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _token Address of the Poodlana token contract.
     * @param _presaleRate Number of tokens per 1 ETH.
     * @param _presaleCap Maximum number of tokens available for presale.
     */
    constructor(
        IERC20 _token,
        uint256 _presaleRate,
        uint256 _presaleCap
    ) {
        require(address(_token) != address(0), "Invalid token address");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        token = _token;
        presaleRate = _presaleRate;
        presaleCap = _presaleCap;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during presale.
     */
    function buyTokens() external payable {
        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = msg.value * presaleRate;

        // Ensure sale does not exceed presale cap
        require(
            totalTokensSold + tokensToPurchase <= presaleCap,
            "Presale cap exceeded"
        );

        // Ensure there are enough tokens in the contract
        require(
            token.balanceOf(address(this)) >= tokensToPurchase,
            "Insufficient tokens in contract"
        );

        // Update total tokens sold
        totalTokensSold += tokensToPurchase;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokensToPurchase);

        // Emit event for purchase
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to withdraw collected funds (ETH) by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to the owner
        payable(owner).transfer(balance);

        // Emit event for withdrawal
        emit Withdrawn(owner, balance);
    }

    /**
     * @dev Function to update presale rate by the owner.
     * @param _newRate New rate of tokens per 1 ETH.
     */
    function updatePresaleRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than zero");
        presaleRate = _newRate;
    }

    /**
     * @dev Function to update presale cap by the owner.
     * @param _newCap New presale cap.
     */
    function updatePresaleCap(uint256 _newCap) external onlyOwner {
        require(_newCap > 0, "Cap must be greater than zero");
        require(_newCap >= totalTokensSold, "New cap must be greater than total tokens sold");
        presaleCap = _newCap;
    }

    /**
     * @dev Function to recover any ERC20 tokens sent to the contract by mistake.
     * @param _token Address of the ERC20 token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverERC20(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner, _amount);
    }

    /**
     * @dev Fallback function to handle any ETH sent directly to the contract.
     */
    receive() external payable {
        buyTokens();
    }
}

/**
 * @dev Minimal implementation of an ERC20 interface for interaction.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
