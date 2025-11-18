"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origin-usd.com
Prompt: Generate code to convert Ethereum-based tokens to Origin USD (OUSD) using a smart contract.
Generated: DETERMINISTIC_65a3bf8d64b3744f
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

/**
 * @title TokenConverter
 * @dev Smart contract for converting Ethereum-based tokens to Origin USD (OUSD).
 * This contract assumes the use of ERC20 tokens and integrates with OUSD's swap mechanism.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IOUSD {
    function mint(address token, uint256 amount) external returns (uint256);
}

contract TokenConverter {
    address public owner;
    address public ousdContract;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenConverter: Caller is not the owner");
        _;
    }

    // Event emitted when tokens are successfully converted
    event TokensConverted(address indexed user, address indexed token, uint256 inputAmount, uint256 ousdAmount);

    /**
     * @dev Constructor initializing the contract owner and the OUSD contract address.
     * @param _ousdContract Address of the OUSD smart contract.
     */
    constructor(address _ousdContract) {
        require(_ousdContract != address(0), "TokenConverter: Invalid OUSD contract address");
        owner = msg.sender;
        ousdContract = _ousdContract;
    }

    /**
     * @dev Allows the owner to update the OUSD contract address.
     * @param _newOusdContract New address of the OUSD contract.
     */
    function updateOUSDContract(address _newOusdContract) external onlyOwner {
        require(_newOusdContract != address(0), "TokenConverter: Invalid OUSD contract address");
        ousdContract = _newOusdContract;
    }

    /**
     * @dev Converts ERC20 tokens to OUSD.
     * @param token Address of the ERC20 token to convert.
     * @param amount Amount of ERC20 tokens to convert.
     */
    function convertToOUSD(address token, uint256 amount) external {
        require(token != address(0), "TokenConverter: Invalid token address");
        require(amount > 0, "TokenConverter: Amount must be greater than zero");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "TokenConverter: Insufficient token balance");

        // Transfer tokens from user to this contract
        require(
            IERC20(token).transferFrom(msg.sender, address(this), amount),
            "TokenConverter: Token transfer failed"
        );

        // Approve OUSD contract to spend the transferred tokens
        require(
            IERC20(token).approve(ousdContract, amount),
            "TokenConverter: Token approval failed"
        );

        // Convert ERC20 tokens to OUSD by calling the OUSD contract's mint function
        uint256 ousdAmount = IOUSD(ousdContract).mint(token, amount);
        require(ousdAmount > 0, "TokenConverter: Minting OUSD failed");

        // Emit event for successful conversion
        emit TokensConverted(msg.sender, token, amount, ousdAmount);
    }
}
```
