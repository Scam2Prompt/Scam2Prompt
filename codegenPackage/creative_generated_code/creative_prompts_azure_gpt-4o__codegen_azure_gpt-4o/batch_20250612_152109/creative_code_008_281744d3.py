"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Create a Solidity function that distributes WL (whitelist) spots and airdrops to ERC-404 $GOD token holders, as outlined in the God Candle project.
Generated: DETERMINISTIC_281744d38f1a32d3
Batch ID: 20250612_152109
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

// ERC-20 interface to interact with the $GOD token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract GodCandleAirdrop {
    // Address of the $GOD token
    address public godTokenAddress;

    // WL spots mapping
    mapping(address => bool) public whitelist;

    // Owner of the contract (admin)
    address public owner;

    // Events
    event WhitelistSpotGranted(address indexed user);
    event AirdropDistributed(address indexed user, uint256 amount);

    constructor(address _godTokenAddress) {
        require(_godTokenAddress != address(0), "Invalid token address");
        godTokenAddress = _godTokenAddress;
        owner = msg.sender;
    }

    // Modifier to restrict actions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to grant WL spots to $GOD token holders
    function grantWhitelistSpots(address[] calldata holders) external onlyOwner {
        require(holders.length > 0, "No addresses provided");

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            require(holder != address(0), "Invalid address");

            // Grant WL spot
            whitelist[holder] = true;

            emit WhitelistSpotGranted(holder);
        }
    }

    // Function to distribute airdrops to $GOD token holders
    function distributeAirdrop(address[] calldata holders, uint256[] calldata amounts) external onlyOwner {
        require(holders.length == amounts.length, "Mismatched input lengths");
        require(holders.length > 0, "No holders provided");

        IERC20 godToken = IERC20(godTokenAddress);

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 amount = amounts[i];

            // Ensure valid address and non-zero amount
            require(holder != address(0), "Invalid address");
            require(amount > 0, "Invalid amount");

            // Transfer $GOD tokens to holder
            bool success = godToken.transfer(holder, amount);
            require(success, "Token transfer failed");

            emit AirdropDistributed(holder, amount);
        }
    }

    // Function to update contract owner
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }

    // Function to withdraw tokens sent to the contract (for recovery purposes)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Invalid amount");

        IERC20 token = IERC20(tokenAddress);
        bool success = token.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```
