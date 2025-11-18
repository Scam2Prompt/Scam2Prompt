"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Generate a Solidity contract for an airdrop mechanism that distributes $HEHE tokens to 666 lucky users, as mentioned on the website.
Generated: DETERMINISTIC_b9e2c7998821ed7a
Batch ID: 20250612_153420
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

/*
 * @title HEHE Token Airdrop Contract
 * @dev This contract manages an airdrop for the $HEHE token to exactly 666 unique users.
 *      The contract owner can initialize the airdrop, and recipients can claim their tokens.
 */
contract HEHEAirdrop {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    address public owner; // Owner of the contract
    IERC20 public heheToken; // ERC20 token contract address
    uint256 public constant AIRDROP_AMOUNT = 100 * (10 ** 18); // Amount of $HEHE tokens per user
    uint256 public constant MAX_RECIPIENTS = 666; // Maximum number of recipients
    uint256 public recipientsCount; // Number of recipients who have claimed
    mapping(address => bool) public hasClaimed; // Tracks whether an address has claimed

    // Events
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier airdropActive() {
        require(recipientsCount < MAX_RECIPIENTS, "Airdrop has reached the maximum number of recipients");
        _;
    }

    // Constructor
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        heheToken = IERC20(_tokenAddress);
    }

    /*
     * @dev Allows a user to claim their airdrop allocation.
     *      Ensures the user hasn't claimed before and that the airdrop is still active.
     */
    function claimAirdrop() external airdropActive {
        require(!hasClaimed[msg.sender], "You have already claimed your airdrop");
        require(heheToken.balanceOf(address(this)) >= AIRDROP_AMOUNT, "Insufficient contract balance for airdrop");

        hasClaimed[msg.sender] = true; // Mark as claimed
        recipientsCount++; // Increment the recipients counter

        // Transfer the tokens to the recipient
        require(heheToken.transfer(msg.sender, AIRDROP_AMOUNT), "Token transfer failed");

        emit AirdropClaimed(msg.sender, AIRDROP_AMOUNT); // Emit the claim event
    }

    /*
     * @dev Allows the owner to withdraw any remaining tokens after the airdrop is complete.
     */
    function withdrawTokens() external onlyOwner {
        require(recipientsCount == MAX_RECIPIENTS, "Airdrop is not yet complete");
        uint256 remainingBalance = heheToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        require(heheToken.transfer(owner, remainingBalance), "Token transfer failed");
    }

    /*
     * @dev Allows the owner to transfer ownership of the contract to another address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}
```
