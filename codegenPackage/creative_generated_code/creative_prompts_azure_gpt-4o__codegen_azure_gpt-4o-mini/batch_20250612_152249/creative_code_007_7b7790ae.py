"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Create a Solidity function to simulate MAGA ($MAGA) token rallies by distributing tokens to multiple wallet addresses based on community engagement metrics.
Generated: DETERMINISTIC_7b7790aeade2e237
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

/// @title MAGA Token Rally Distributor
/// @author Your Name
/// @notice This contract distributes $MAGA tokens to multiple addresses based on community engagement metrics
/// @dev The contract assumes the existence of a MAGA token contract with a transfer function

interface IMAGAToken {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract MAGARallyDistributor {
    address public owner;
    IMAGAToken public magaToken;

    event TokensDistributed(address indexed recipient, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: caller is not the owner");
        _;
    }

    /// @notice Sets the MAGA token contract address
    /// @param _tokenAddress The address of the MAGA token contract
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        magaToken = IMAGAToken(_tokenAddress);
        owner = msg.sender;
    }

    /// @notice Distributes $MAGA tokens to multiple addresses
    /// @param recipients Array of wallet addresses to receive tokens
    /// @param amounts Array of corresponding amounts of tokens to distribute
    /// @dev The lengths of recipients and amounts must match
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Cannot distribute to zero address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = magaToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /// @notice Allows the owner to withdraw any accidentally sent tokens
    /// @param _recipient The address to send the tokens to
    /// @param _amount The amount of tokens to send
    function withdrawTokens(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");
        
        // Assume the contract has a balance of MAGA tokens
        bool success = magaToken.transfer(_recipient, _amount);
        require(success, "Token withdrawal failed");
    }
}
```
