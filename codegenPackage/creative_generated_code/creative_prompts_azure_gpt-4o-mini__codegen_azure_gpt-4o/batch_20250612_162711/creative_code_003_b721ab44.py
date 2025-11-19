"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Develop a smart contract that manages the distribution of PWLFI tokens to early participants based on the specified 3x token ratio.
Generated: DETERMINISTIC_b721ab44b44aefda
Batch ID: 20250612_162711
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
 * @title TokenDistribution
 * @dev Smart contract to manage the distribution of PWLFI tokens
 * to early participants based on a 3x token ratio.
 */
contract TokenDistribution {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the PWLFI token contract
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Tracks participants and their allocated tokens
    mapping(address => uint256) public allocations;

    // Events
    event TokensAllocated(address indexed participant, uint256 amount);
    event TokensClaimed(address indexed participant, uint256 amount);

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract address and set the owner.
     * @param _token Address of the PWLFI token contract.
     */
    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Function to allocate tokens to early participants.
     * @param participant Address of the participant.
     * @param baseAmount Amount of tokens the participant initially earned.
     */
    function allocateTokens(address participant, uint256 baseAmount) external onlyOwner {
        require(participant != address(0), "Invalid participant address.");
        require(baseAmount > 0, "Base amount must be greater than zero.");

        // Calculate token allocation based on the 3x ratio
        uint256 allocation = baseAmount * 3;

        // Record the allocation
        allocations[participant] += allocation;

        emit TokensAllocated(participant, allocation);
    }

    /**
     * @dev Function for participants to claim their allocated tokens.
     */
    function claimTokens() external {
        uint256 allocatedAmount = allocations[msg.sender];
        require(allocatedAmount > 0, "No tokens allocated for this address.");
        require(token.balanceOf(address(this)) >= allocatedAmount, "Insufficient contract balance.");

        // Reset the allocation before transferring tokens to prevent re-entrancy attacks
        allocations[msg.sender] = 0;

        // Transfer tokens to the participant
        require(token.transfer(msg.sender, allocatedAmount), "Token transfer failed.");

        emit TokensClaimed(msg.sender, allocatedAmount);
    }

    /**
     * @dev Function to withdraw remaining tokens from the contract. Restricted to the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        require(token.transfer(owner, amount), "Token transfer failed.");
    }
}
```
