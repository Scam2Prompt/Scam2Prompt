"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20.web.app
Prompt: Explain how to implement a presale claiming mechanism for DOGE20 tokens using Ethereum smart contracts.
Generated: DETERMINISTIC_0a73c55774659785
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PresaleClaimingContract
 * @dev Implements a presale claiming mechanism for DOGE20 tokens.
 * Users can claim tokens during the presale period by sending ETH (or another token if modified).
 */
contract PresaleClaimingContract {
    // Address of the DOGE20 token contract
    address public immutable tokenAddress;

    // Address of the presale owner
    address public immutable owner;

    // Conversion rate: How many DOGE20 tokens per 1 ETH
    uint256 public immutable rate;

    // Presale start and end timestamps
    uint256 public immutable presaleStart;
    uint256 public immutable presaleEnd;

    // Total amount of tokens claimed
    uint256 public totalTokensClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 ethAmount, uint256 tokenAmount);

    // Constructor to initialize the contract
    constructor(
        address _tokenAddress,
        uint256 _rate,
        uint256 _presaleStart,
        uint256 _presaleEnd
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rate > 0, "Rate must be greater than 0");
        require(_presaleStart < _presaleEnd, "Start time must be before end time");

        tokenAddress = _tokenAddress;
        owner = msg.sender; // Set the deployer as the owner
        rate = _rate;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    /**
     * @dev Allows users to claim DOGE20 tokens during the presale.
     * Requires presale to be active and sufficient ETH sent to purchase tokens.
     */
    function claimTokens() external payable {
        require(block.timestamp >= presaleStart, "Presale has not started");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Calculate the number of tokens to be claimed
        uint256 tokenAmount = msg.value * rate;

        // Transfer the DOGE20 tokens to the user
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        // Track total tokens claimed
        totalTokensClaimed += tokenAmount;

        emit TokensClaimed(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw collected ETH after presale ends.
     */
    function withdraw() external {
        require(msg.sender == owner, "Only owner can withdraw");
        require(block.timestamp > presaleEnd, "Presale has not ended");

        // Transfer the collected ETH to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {
        claimTokens();
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
