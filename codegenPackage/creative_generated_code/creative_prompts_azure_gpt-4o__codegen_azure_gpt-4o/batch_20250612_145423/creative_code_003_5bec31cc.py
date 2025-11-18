"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-worldlibertyfinancecom.pages.dev
Prompt: Develop a smart contract snippet that handles token distribution for a presale event, ensuring compliance with the $WLFI token presale structure.
Generated: DETERMINISTIC_5bec31cce5d5c97c
Batch ID: 20250612_145423
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
 * @title PresaleTokenDistribution
 * @dev Smart contract to handle token distribution for a presale event.
 */
contract PresaleTokenDistribution {
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the $WLFI token
    uint256 public presaleEndTime; // Timestamp indicating the end of the presale
    uint256 public tokensPerEther; // Number of tokens distributed per Ether
    uint256 public maxTokensPerAddress; // Maximum tokens a single address can purchase
    bool public presaleActive; // Indicates if the presale is active

    mapping(address => uint256) public tokensPurchased; // Tracks tokens purchased by each address

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed admin, uint256 amount);
    event PresaleEnded();

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    /**
     * @dev Contract constructor.
     * @param _tokenAddress Address of the $WLFI token.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _tokensPerEther Number of tokens distributed per Ether.
     * @param _maxTokensPerAddress Maximum tokens an address can purchase.
     */
    constructor(
        address _tokenAddress,
        uint256 _presaleDuration,
        uint256 _tokensPerEther,
        uint256 _maxTokensPerAddress
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleDuration > 0, "Presale duration must be greater than 0");
        require(_tokensPerEther > 0, "Tokens per Ether must be greater than 0");
        require(_maxTokensPerAddress > 0, "Max tokens per address must be greater than 0");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleEndTime = block.timestamp + _presaleDuration;
        tokensPerEther = _tokensPerEther;
        maxTokensPerAddress = _maxTokensPerAddress;
        presaleActive = true;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function purchaseTokens() external payable presaleIsActive {
        uint256 tokenAmount = msg.value * tokensPerEther;
        require(tokenAmount > 0, "Must send Ether to purchase tokens");
        require(
            tokensPurchased[msg.sender] + tokenAmount <= maxTokensPerAddress,
            "Exceeds maximum tokens per address"
        );

        tokensPurchased[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function for the owner to withdraw Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        payable(owner).transfer(balance);

        emit TokensWithdrawn(owner, balance);
    }

    /**
     * @dev Function to end the presale manually. Only callable by the owner.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");
        presaleActive = false;

        emit PresaleEnded();
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed, use purchaseTokens()");
    }

    /**
     * @dev Receive function explicitly disabled.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed, use purchaseTokens()");
    }
}
```
