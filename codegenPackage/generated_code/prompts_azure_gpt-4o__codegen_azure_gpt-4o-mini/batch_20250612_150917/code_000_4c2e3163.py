"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Write a smart contract example using the Data Ownership Protocol (DOP) to selectively disclose ERC20 token holdings while maintaining privacy for other assets.
Generated: DETERMINISTIC_4c2e3163ef95d776
Batch ID: 20250612_150917
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Data Ownership Protocol (DOP)
interface IDataOwnershipProtocol {
    function discloseData(address user, bytes32 dataHash) external;
    function verifyData(address user, bytes32 dataHash) external view returns (bool);
}

// Smart contract for selective disclosure of ERC20 token holdings
contract SelectiveDisclosure {
    // State variable to store the DOP contract address
    IDataOwnershipProtocol public dop;

    // Mapping to store user token balances
    mapping(address => mapping(address => uint256)) private _balances;

    // Event emitted when data is disclosed
    event DataDisclosed(address indexed user, bytes32 dataHash);

    // Constructor to set the DOP contract address
    constructor(address dopAddress) {
        require(dopAddress != address(0), "Invalid DOP address");
        dop = IDataOwnershipProtocol(dopAddress);
    }

    // Function to deposit ERC20 tokens into the contract
    function depositTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        _balances[msg.sender][token] += amount;
    }

    // Function to disclose token holdings selectively
    function discloseHoldings(address token) external {
        require(_balances[msg.sender][token] > 0, "No holdings to disclose");

        // Create a hash of the user's token balance
        bytes32 dataHash = keccak256(abi.encodePacked(msg.sender, token, _balances[msg.sender][token]));

        // Disclose the data using the DOP
        dop.discloseData(msg.sender, dataHash);

        // Emit an event for the disclosure
        emit DataDisclosed(msg.sender, dataHash);
    }

    // Function to verify disclosed data
    function verifyHoldings(address user, address token) external view returns (bool) {
        bytes32 dataHash = keccak256(abi.encodePacked(user, token, _balances[user][token]));
        return dop.verifyData(user, dataHash);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender][token] >= amount, "Insufficient balance");

        // Update the user's balance before transferring
        _balances[msg.sender][token] -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to check the balance of a user for a specific token
    function balanceOf(address user, address token) external view returns (uint256) {
        return _balances[user][token];
    }
}
```
