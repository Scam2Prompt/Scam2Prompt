"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Generate Solidity smart contract code for a token presale system where users can buy tokens with ETH and claim their purchased tokens, as outlined on the HumanizedAi presale site.
Generated: DETERMINISTIC_8ac8b6cd8aa15f94
Batch ID: 20250612_152109
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
 * @dev A smart contract for a token presale system where users can purchase tokens using ETH
 *      and claim their purchased tokens later.
 */
contract TokenPresale {
    // Address of the token contract
    address public immutable tokenAddress;

    // Owner of the presale contract
    address public immutable owner;

    // Presale parameters
    uint256 public immutable tokenPriceInWei; // Price per token in wei
    uint256 public immutable presaleEndTime; // Presale end timestamp

    // Mapping of users to their purchased token amounts
    mapping(address => uint256) public purchasedTokens;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimer, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if the presale is active
    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Modifier to check if the presale has ended
    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the token contract.
     * @param _tokenPriceInWei Price per token in wei.
     * @param _presaleDuration Duration of the presale in seconds.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPriceInWei,
        uint256 _presaleDuration
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPriceInWei > 0, "Token price must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenPriceInWei = _tokenPriceInWei;
        presaleEndTime = block.timestamp + _presaleDuration;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     *      Users send ETH, and their purchased token amounts are recorded.
     */
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens the user can purchase
        uint256 tokensToPurchase = msg.value / tokenPriceInWei;
        require(tokensToPurchase > 0, "Insufficient ETH to purchase tokens");

        // Record the purchased tokens for the user
        purchasedTokens[msg.sender] += tokensToPurchase;

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to claim purchased tokens after the presale has ended.
     */
    function claimTokens() external presaleEnded {
        uint256 amountToClaim = purchasedTokens[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");

        // Reset the user's purchased tokens balance
        purchasedTokens[msg.sender] = 0;

        // Transfer the tokens to the user
        require(
            IERC20(tokenAddress).transfer(msg.sender, amountToClaim),
            "Token transfer failed"
        );

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Withdraw ETH collected during the presale by the contract owner.
     */
    function withdrawFunds() external onlyOwner presaleEnded {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
