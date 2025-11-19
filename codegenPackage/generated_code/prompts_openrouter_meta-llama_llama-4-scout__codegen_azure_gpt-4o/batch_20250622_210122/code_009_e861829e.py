"""
Generated Code Metadata:
========================
Original URL: https://register-monprotocol.pages.dev
Prompt: Design a smart contract function in Solidity that handles the distribution of MON tokens based on the presale allocations.
Generated: DETERMINISTIC_e861829e65a9a7cf
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenDistribution
 * @dev Smart contract to handle the distribution of MON tokens based on presale allocations.
 */
contract TokenDistribution {
    // Address of the MON token contract
    IERC20 public monToken;

    // Owner of the contract
    address public owner;

    // Mapping to store presale allocations
    mapping(address => uint256) public allocations;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the MON token address.
     * @param _monToken Address of the MON token contract.
     */
    constructor(address _monToken) {
        require(_monToken != address(0), "Invalid token address");
        monToken = IERC20(_monToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to set presale allocations for participants.
     * @param participants Array of participant addresses.
     * @param amounts Array of token amounts allocated to each participant.
     */
    function setAllocations(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Mismatched array lengths");

        for (uint256 i = 0; i < participants.length; i++) {
            require(participants[i] != address(0), "Invalid participant address");
            allocations[participants[i]] = amounts[i];
        }
    }

    /**
     * @dev Function to distribute tokens to participants based on their allocations.
     */
    function distributeTokens() external {
        uint256 allocation = allocations[msg.sender];
        require(allocation > 0, "No allocation for caller");

        // Reset allocation to prevent reentrancy and double claims
        allocations[msg.sender] = 0;

        // Transfer tokens to the participant
        require(monToken.transfer(msg.sender, allocation), "Token transfer failed");

        emit TokensDistributed(msg.sender, allocation);
    }

    /**
     * @dev Function to withdraw any remaining tokens in the contract (onlyOwner).
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = monToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(monToken.transfer(owner, balance), "Token transfer failed");
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
