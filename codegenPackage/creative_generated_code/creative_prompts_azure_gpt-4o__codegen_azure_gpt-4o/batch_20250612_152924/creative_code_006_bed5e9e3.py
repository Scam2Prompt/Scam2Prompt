"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Provide an example of a smart contract that includes a "BUY" function for purchasing SHROOM tokens during the presale, with the rate of 0.1 ETH = 99,500 SHROOM.
Generated: DETERMINISTIC_bed5e9e33d8b5cca
Batch ID: 20250612_152924
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
 * @title ShroomTokenPresale
 * @dev A smart contract for purchasing SHROOM tokens during the presale.
 *      The rate is fixed at 0.1 ETH = 99,500 SHROOM.
 */
contract ShroomTokenPresale {
    // Address of the SHROOM token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Presale rate: 0.1 ETH = 99,500 SHROOM
    uint256 public constant RATE = 99500;
    uint256 public constant ETH_PER_TOKEN = 10**17;

    // Total tokens sold during presale
    uint256 public totalTokensSold;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the SHROOM token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to buy SHROOM tokens during the presale.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Calculate the number of SHROOM tokens to purchase
        uint256 tokenAmount = (msg.value * RATE) / ETH_PER_TOKEN;

        // Transfer tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        // Update total tokens sold
        totalTokensSold += tokenAmount;

        // Emit event for purchase
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Function to withdraw ETH collected during the presale.
     */
    function withdrawEth() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No ETH to withdraw");

        // Transfer ETH to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH without function call.
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Interface for ERC20 token interactions.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
