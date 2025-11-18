"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappvix.pages.dev
Prompt: Generate code to enable presale token purchases and claims, including error handling for transaction failures, as outlined in the DApp Synchronizer Panel documentation.
Generated: DETERMINISTIC_27dc3d449831b192
Batch ID: 20250612_152235
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
 * @title TokenPresale
 * @dev Contract to manage presale token purchases and claims
 */
contract TokenPresale {
    // Address of the admin
    address public admin;

    // Token contract address
    address public tokenAddress;

    // Presale configurations
    uint256 public presalePricePerToken; // Price per token in wei
    uint256 public presaleStartTime; // Start time of the presale
    uint256 public presaleEndTime; // End time of the presale

    // Mapping to track purchased tokens per address
    mapping(address => uint256) public purchasedTokens;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);

    /**
     * @dev Modifier to restrict access to admin-only functions
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can execute this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract
     * @param _tokenAddress Address of the token contract
     * @param _presalePricePerToken Price per token in wei
     * @param _presaleStartTime Start time of the presale
     * @param _presaleEndTime End time of the presale
     */
    constructor(
        address _tokenAddress,
        uint256 _presalePricePerToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleStartTime < _presaleEndTime, "Start time must be less than end time");

        admin = msg.sender;
        tokenAddress = _tokenAddress;
        presalePricePerToken = _presalePricePerToken;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
    }

    /**
     * @dev Function to purchase tokens during the presale
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value == tokenAmount * presalePricePerToken, "Incorrect ether sent");

        // Update purchased tokens for the sender
        purchasedTokens[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function to claim purchased tokens after the presale
     */
    function claimTokens() external {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        uint256 amountToClaim = purchasedTokens[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");

        // Reset purchased tokens for the sender
        purchasedTokens[msg.sender] = 0;

        // Transfer tokens to the sender
        (bool success, ) = tokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, amountToClaim)
        );
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Function for the admin to withdraw collected funds after the presale
     */
    function withdrawFunds() external onlyAdmin {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = admin.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers
     */
    fallback() external payable {
        revert("Direct ether transfer not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ether transfers
     */
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
