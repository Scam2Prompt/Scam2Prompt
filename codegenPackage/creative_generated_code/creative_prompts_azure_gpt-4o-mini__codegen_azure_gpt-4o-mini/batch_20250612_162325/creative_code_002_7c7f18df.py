"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerfairdrop.vercel.app
Prompt: Create a Solidity smart contract that allows users to claim their $Slerf tokens after the presale, incorporating the refund mechanism outlined in the Slerf Fair Drop documentation.
Generated: DETERMINISTIC_7c7f18dfd8b35a91
Batch ID: 20250612_162325
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

// Import the required OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SlerfTokenClaim
 * @dev A contract for claiming $Slerf tokens after the presale, with a refund mechanism.
 */
contract SlerfTokenClaim is Ownable {
    // State variables
    IERC20 public slerfToken; // The $Slerf token contract
    mapping(address => uint256) public contributions; // User contributions
    mapping(address => bool) public claimed; // Track if a user has claimed their tokens
    uint256 public presaleEndTime; // Presale end time
    uint256 public refundPeriod; // Time period allowed for refunds

    // Events
    event TokensClaimed(address indexed user, uint256 amount);
    event RefundIssued(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token address and presale parameters.
     * @param _slerfToken Address of the $Slerf token contract.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _refundDuration Duration of the refund period in seconds.
     */
    constructor(address _slerfToken, uint256 _presaleDuration, uint256 _refundDuration) {
        slerfToken = IERC20(_slerfToken);
        presaleEndTime = block.timestamp + _presaleDuration;
        refundPeriod = _refundDuration;
    }

    /**
     * @dev Allows users to contribute to the presale.
     * @param amount Amount of tokens to contribute.
     */
    function contribute(uint256 amount) external {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer $Slerf tokens from user to this contract
        slerfToken.transferFrom(msg.sender, address(this), amount);
        contributions[msg.sender] += amount;
    }

    /**
     * @dev Allows users to claim their tokens after the presale.
     */
    function claimTokens() external {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        require(!claimed[msg.sender], "Tokens already claimed");

        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No tokens to claim");

        // Mark as claimed
        claimed[msg.sender] = true;

        // Transfer tokens to the user
        slerfToken.transfer(msg.sender, amount);
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows users to refund their contributions if they haven't claimed yet.
     */
    function refund() external {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        require(block.timestamp <= presaleEndTime + refundPeriod, "Refund period has ended");
        require(!claimed[msg.sender], "Cannot refund after claiming");

        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No contributions to refund");

        // Reset the user's contribution before transferring to prevent re-entrancy
        contributions[msg.sender] = 0;

        // Transfer the tokens back to the user
        slerfToken.transfer(msg.sender, amount);
        emit RefundIssued(msg.sender, amount);
    }

    /**
     * @dev Owner can withdraw any remaining tokens after refund period.
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime + refundPeriod, "Cannot withdraw yet");
        uint256 remainingBalance = slerfToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        // Transfer remaining tokens to the owner
        slerfToken.transfer(owner(), remainingBalance);
    }
}
```
