"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreifcnpktapdtapj76jqfg5h4rszqmvsurv5ynmixd4gjkfrhunxfiu.ipfs.dweb.link
Prompt: Generate a smart contract snippet for distributing $ARROW tokens to IDO participants on Arrow Markets.
Generated: DETERMINISTIC_8e767aa04e7ade6f
Batch ID: 20250612_152249
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
 * @title ArrowTokenDistributor
 * @dev A smart contract for distributing $ARROW tokens to IDO participants on Arrow Markets
 */
contract ArrowTokenDistributor {
    // ERC20 interface for interacting with $ARROW token contract
    interface IERC20 {
        function transfer(address to, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public arrowToken; // The $ARROW token contract
    address public owner; // Contract owner address

    // Event emitted for each successful token distribution
    event TokensDistributed(address indexed participant, uint256 amount);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict functions to only the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $ARROW token contract address
     * @param _arrowToken Address of the $ARROW token contract
     */
    constructor(address _arrowToken) {
        require(_arrowToken != address(0), "Invalid token address");
        arrowToken = IERC20(_arrowToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute $ARROW tokens to multiple participants
     * @param participants Array of participant addresses
     * @param amounts Array of token amounts corresponding to each participant
     */
    function distributeTokens(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Mismatched input arrays");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 amount = amounts[i];

            require(participant != address(0), "Invalid participant address");
            require(amount > 0, "Amount must be greater than zero");

            // Transfer tokens to the participant
            bool success = arrowToken.transfer(participant, amount);
            require(success, "Token transfer failed");

            emit TokensDistributed(participant, amount);
        }
    }

    /**
     * @dev Function to withdraw any remaining $ARROW tokens to the owner
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = arrowToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens left to withdraw");

        bool success = arrowToken.transfer(owner, remainingBalance);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
