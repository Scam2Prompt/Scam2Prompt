"""
Generated Code Metadata:
========================
Original URL: https://merlion.pages.dev
Prompt: Generate a smart contract code for a new token launchpad on MerlinSwap, incorporating features from Merlin's Spellbook.
Generated: DETERMINISTIC_cb41faeab8c04464
Batch ID: 20250622_210803
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
 * @title TokenLaunchpad
 * @dev A smart contract for launching new tokens on MerlinSwap, incorporating features from Merlin's Spellbook.
 */
contract TokenLaunchpad {
    // Struct to store token details
    struct TokenDetails {
        string name;
        string symbol;
        uint256 totalSupply;
        address tokenAddress;
        address owner;
        bool isListed;
    }

    // Mapping to store tokens launched on the platform
    mapping(address => TokenDetails) public tokens;

    // Event emitted when a new token is launched
    event TokenLaunched(
        string name,
        string symbol,
        uint256 totalSupply,
        address indexed tokenAddress,
        address indexed owner
    );

    // Event emitted when a token is listed on MerlinSwap
    event TokenListed(address indexed tokenAddress);

    // Modifier to restrict access to token owner
    modifier onlyTokenOwner(address _tokenAddress) {
        require(
            tokens[_tokenAddress].owner == msg.sender,
            "Caller is not the token owner"
        );
        _;
    }

    /**
     * @dev Launch a new token on the platform.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _totalSupply Total supply of the token.
     * @param _tokenAddress Address of the token contract.
     */
    function launchToken(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        address _tokenAddress
    ) external {
        require(
            tokens[_tokenAddress].tokenAddress == address(0),
            "Token already exists"
        );
        require(_tokenAddress != address(0), "Invalid token address");

        // Store token details
        tokens[_tokenAddress] = TokenDetails({
            name: _name,
            symbol: _symbol,
            totalSupply: _totalSupply,
            tokenAddress: _tokenAddress,
            owner: msg.sender,
            isListed: false
        });

        emit TokenLaunched(_name, _symbol, _totalSupply, _tokenAddress, msg.sender);
    }

    /**
     * @dev List a token on MerlinSwap.
     * @param _tokenAddress Address of the token contract.
     */
    function listToken(address _tokenAddress) external onlyTokenOwner(_tokenAddress) {
        require(
            tokens[_tokenAddress].tokenAddress != address(0),
            "Token does not exist"
        );
        require(!tokens[_tokenAddress].isListed, "Token is already listed");

        // Mark the token as listed
        tokens[_tokenAddress].isListed = true;

        emit TokenListed(_tokenAddress);
    }

    /**
     * @dev Get details of a token.
     * @param _tokenAddress Address of the token contract.
     * @return TokenDetails Struct containing token details.
     */
    function getTokenDetails(address _tokenAddress)
        external
        view
        returns (TokenDetails memory)
    {
        require(
            tokens[_tokenAddress].tokenAddress != address(0),
            "Token does not exist"
        );
        return tokens[_tokenAddress];
    }
}
```
