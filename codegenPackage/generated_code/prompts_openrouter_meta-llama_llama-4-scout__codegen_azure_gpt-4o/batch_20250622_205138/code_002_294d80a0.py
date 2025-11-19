"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract code in Solidity that distributes Ziber tokens to Bitcoin and Ethereum owners as a bonus, based on the snapshot of the blockchain on July 26, 2017.
Generated: DETERMINISTIC_294d80a0246a1674
Batch ID: 20250622_205138
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
 * @title ZiberTokenDistributor
 * @dev A smart contract to distribute Ziber tokens to Bitcoin and Ethereum owners
 *      based on the snapshot of the blockchain on July 26, 2017.
 */
contract ZiberTokenDistributor {
    // Address of the Ziber token contract
    address public ziberTokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to store eligible addresses and their bonus amounts
    mapping(address => uint256) public bonuses;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _ziberTokenAddress Address of the Ziber token contract.
     */
    constructor(address _ziberTokenAddress) {
        require(_ziberTokenAddress != address(0), "Invalid token address");
        ziberTokenAddress = _ziberTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to set bonuses for eligible addresses.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of bonus amounts corresponding to the recipients.
     */
    function setBonuses(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            bonuses[recipients[i]] = amounts[i];
        }
    }

    /**
     * @dev Function to distribute Ziber tokens to eligible addresses.
     */
    function distributeTokens() external {
        uint256 bonusAmount = bonuses[msg.sender];
        require(bonusAmount > 0, "No bonus available for this address");

        // Reset the bonus to prevent re-entrancy
        bonuses[msg.sender] = 0;

        // Call the Ziber token contract to transfer tokens
        (bool success, ) = ziberTokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, bonusAmount)
        );
        require(success, "Token transfer failed");

        emit TokensDistributed(msg.sender, bonusAmount);
    }

    /**
     * @dev Function to withdraw any remaining tokens in the contract (emergency use).
     * @param _to Address to send the remaining tokens.
     */
    function emergencyWithdraw(address _to) external onlyOwner {
        require(_to != address(0), "Invalid address");

        uint256 contractBalance = address(this).balance;
        (bool success, ) = _to.call{value: contractBalance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Function to update the Ziber token contract address (if needed).
     * @param _newTokenAddress New address of the Ziber token contract.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        ziberTokenAddress = _newTokenAddress;
    }
}
```
