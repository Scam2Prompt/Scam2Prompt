"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Provide an example of a presale purchase script in Solidity for BTCETF tokens, ensuring the presale price is set at $0.005 per token.
Generated: DETERMINISTIC_07a4e52908ba68f7
Batch ID: 20250612_152249
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
 * @title BTCETF Presale Contract
 * @dev A presale purchase contract for BTCETF tokens, allowing users to purchase tokens at a fixed presale price.
 */
contract BTCETFPresale {
    // Token presale price in wei (0.005 USD per token, assuming 1 USD = 1 Ether for simplicity)
    uint256 public constant PRESALE_PRICE = 5000000000000000; // 0.005 ETH per token

    // Address where the BTCETF tokens will be sent from
    address public tokenAddress;

    // Owner of the contract (presale administrator)
    address public owner;

    // Event for token purchase logging
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract with the token address.
     * @param _tokenAddress Address of the BTCETF token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Purchase BTCETF tokens during the presale.
     * The amount of tokens purchased is calculated based on the amount of ETH sent.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Calculate the amount of tokens
        uint256 tokenAmount = (msg.value * 10**18) / PRESALE_PRICE;

        // Transfer tokens from the token contract to the buyer
        ERC20 token = ERC20(tokenAddress);
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        // Emit event for logging purposes
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    /**
     * @dev Withdraw the contract's ETH balance to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Allow the owner to update the token address in case of emergency.
     * @param _newTokenAddress The new token contract address.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _newTokenAddress;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external {
        revert("Fallback function not supported");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

// Interface for ERC20 token contract
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
