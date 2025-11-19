"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigknes33h76f7skpeenkp5p5s74x65rjrgymqbdmpd2i3kufhzxqe.ipfs.dweb.link
Prompt: How can I implement an airdrop event for the $SLOTH token using smart contracts?
Generated: DETERMINISTIC_e1d433eb94e7b210
Batch ID: 20250612_160946
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
 * @title SlothTokenAirdrop
 * @dev A contract to implement an airdrop event for the $SLOTH token.
 */
contract SlothTokenAirdrop {
    // Address of the $SLOTH token contract
    IERC20 public slothToken;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Event emitted when tokens are successfully airdropped to an address.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens transferred.
     */
    event Airdrop(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address and set the owner.
     * @param tokenAddress Address of the $SLOTH token contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        slothToken = IERC20(tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Airdrops $SLOTH tokens to a list of recipients.
     * @param recipients List of recipient addresses.
     * @param amounts List of token amounts corresponding to each recipient.
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Recipient address cannot be zero");
            require(amount > 0, "Airdrop amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = slothToken.transfer(recipient, amount);
            require(success, "Token transfer failed");

            // Emit an airdrop event
            emit Airdrop(recipient, amount);
        }
    }

    /**
     * @dev Allows the owner to withdraw tokens accidentally sent to the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Transfer tokens back to the owner
        bool success = slothToken.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
