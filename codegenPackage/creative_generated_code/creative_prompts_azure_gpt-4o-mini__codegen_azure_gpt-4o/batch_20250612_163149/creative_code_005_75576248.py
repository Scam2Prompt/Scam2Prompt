"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Write a Solidity function that allows users to claim their $BTFD tokens after the presale ends, ensuring that the smart contract is immutable and secure.
Generated: DETERMINISTIC_75576248e9b48da0
Batch ID: 20250612_163149
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
 * @title TokenPresaleClaim
 * @dev Smart contract that allows users to claim their $BTFD tokens after the presale ends.
 */
contract TokenPresaleClaim {
    // Address of the $BTFD token contract
    address public immutable tokenAddress;

    // Owner of the smart contract
    address public immutable owner;

    // Timestamp when the presale ends
    uint256 public immutable presaleEndTime;

    // Mapping to track claimed balances
    mapping(address => uint256) public claimedTokens;

    // Total token allocations for each user
    mapping(address => uint256) public tokenAllocations;

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the $BTFD token contract.
     * @param _presaleEndTime Timestamp when the presale will end.
     */
    constructor(address _tokenAddress, uint256 _presaleEndTime) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleEndTime > block.timestamp, "Presale end time must be in the future");

        tokenAddress = _tokenAddress;
        presaleEndTime = _presaleEndTime;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to ensure only the contract owner can call certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure the presale has ended.
     */
    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        _;
    }

    /**
     * @dev Function to allocate tokens to users. Can only be called by the owner before presale ends.
     * @param recipient Address of the user receiving the token allocation.
     * @param amount Amount of tokens allocated to the user.
     */
    function allocateTokens(address recipient, uint256 amount) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Cannot allocate tokens after presale ends");
        require(recipient != address(0), "Invalid recipient");
        require(amount > 0, "Invalid allocation amount");

        tokenAllocations[recipient] += amount;
    }

    /**
     * @dev Function for users to claim their allocated tokens after the presale ends.
     */
    function claimTokens() external presaleEnded {
        uint256 allocatedAmount = tokenAllocations[msg.sender];
        uint256 claimedAmount = claimedTokens[msg.sender];

        require(allocatedAmount > claimedAmount, "No tokens left to claim");

        uint256 claimableAmount = allocatedAmount - claimedAmount;
        claimedTokens[msg.sender] = allocatedAmount; // Update claimed amount

        // Transfer tokens to the user
        require(
            IERC20(tokenAddress).transfer(msg.sender, claimableAmount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Function to withdraw leftover tokens from the contract (only callable by the owner after presale ends).
     */
    function withdrawLeftoverTokens() external onlyOwner presaleEnded {
        uint256 contractBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(
            IERC20(tokenAddress).transfer(owner, contractBalance),
            "Token withdrawal failed"
        );
    }
}

/**
 * @dev IERC20 interface to interact with ERC20 tokens.
 */
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
