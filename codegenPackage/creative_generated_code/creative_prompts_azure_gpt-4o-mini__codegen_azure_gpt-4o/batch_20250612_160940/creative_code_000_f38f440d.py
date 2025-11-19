"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token sale that includes a presale cap of 1000 ETH and a conversion rate of 1 ETH to 99,500 BCKR.
Generated: DETERMINISTIC_f38f440d9d85d7fb
Batch ID: 20250612_160940
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
 * @title TokenSale
 * @dev A smart contract for selling tokens with a presale cap and conversion rate.
 */
contract TokenSale {
    // Conversion rate: 1 ETH = 99,500 BCKR
    uint256 public constant CONVERSION_RATE = 99500;
    
    // Presale cap in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;
    
    // Address of the token being sold
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Amount of ETH raised during presale
    uint256 public totalETHRaised;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amountETH, uint256 amountTokens);

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token address and contract owner.
     * @param _tokenAddress Address of the token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to handle direct ETH transfers for purchasing tokens.
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase tokens. Converts ETH to tokens and updates presale cap.
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "No ETH sent");
        require(totalETHRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to be purchased
        uint256 tokensToTransfer = msg.value * CONVERSION_RATE;

        // Update the total ETH raised
        totalETHRaised += msg.value;

        // Transfer tokens to the buyer
        require(IToken(tokenAddress).transfer(msg.sender, tokensToTransfer), "Token transfer failed");

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, msg.value, tokensToTransfer);
    }

    /**
     * @dev Function to withdraw all ETH collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Function to update the token address (onlyOwner).
     * @param _newTokenAddress New address of the token contract.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        tokenAddress = _newTokenAddress;
    }
}

/**
 * @title IToken
 * @dev Interface for interacting with the token contract.
 */
interface IToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
