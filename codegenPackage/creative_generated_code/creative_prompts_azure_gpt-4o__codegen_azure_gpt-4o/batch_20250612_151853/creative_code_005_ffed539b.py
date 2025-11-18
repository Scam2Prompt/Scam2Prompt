"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-worldlibertfinancialcom.pages.dev
Prompt: Create a smart contract function to distribute tokens during a presale event, referencing the $WLFI Token Presale process where $10,000,000 $WLFI tokens are distributed.
Generated: DETERMINISTIC_ffed539b57f484ff
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a smart contract function written in Solidity that handles the token distribution during a presale event:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title WLFI Presale Contract
 * @dev This contract handles the distribution of $WLFI tokens during a presale event.
 */
contract WLFI_Presale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant TOTAL_TOKENS = 10_000_000 * (10 ** 18); // Total $WLFI tokens for presale
    uint256 public tokensDistributed; // Tracks the number of tokens distributed
    address public tokenAddress; // Address of the $WLFI token contract

    mapping(address => uint256) public contributions; // Keeps track of each participant's contribution

    bool public presaleActive; // Flag to indicate whether the presale is active

    // Events
    event TokensDistributed(address indexed participant, uint256 amount);
    event PresaleStatusChanged(bool isActive);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active.");
        _;
    }

    // Constructor
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address.");
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleActive = true;
    }

    /**
     * @dev Distribute tokens to presale participants.
     * @param participant Address of the participant to distribute tokens to.
     * @param amount Amount of tokens to distribute.
     */
    function distributeTokens(address participant, uint256 amount) external onlyOwner presaleIsActive {
        require(participant != address(0), "Invalid participant address.");
        require(amount > 0, "Amount must be greater than zero.");
        require(tokensDistributed + amount <= TOTAL_TOKENS, "Exceeds total presale token supply.");

        // Update state
        tokensDistributed += amount;
        contributions[participant] += amount;

        // Transfer tokens from the owner to the participant
        require(IERC20(tokenAddress).transfer(participant, amount), "Token transfer failed.");

        // Emit an event for transparency
        emit TokensDistributed(participant, amount);
    }

    /**
     * @dev Toggle the presale status (active/inactive).
     */
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Withdraw remaining tokens after presale ends.
     * @param recipient Address to send the remaining tokens to.
     */
    function withdrawRemainingTokens(address recipient) external onlyOwner {
        require(!presaleActive, "Presale must be inactive to withdraw remaining tokens.");
        require(recipient != address(0), "Invalid recipient address.");

        uint256 remainingTokens = TOTAL_TOKENS - tokensDistributed;

        if (remainingTokens > 0) {
            require(IERC20(tokenAddress).transfer(recipient, remainingTokens), "Token transfer failed.");
        }
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
