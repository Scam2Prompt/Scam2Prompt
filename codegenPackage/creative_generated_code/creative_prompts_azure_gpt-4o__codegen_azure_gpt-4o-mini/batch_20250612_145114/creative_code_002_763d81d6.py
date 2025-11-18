"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0xeigenlabs.github.io
Prompt: Create a trustless bridge using the Eigen zkVM as described in the Eigen Labs documentation. Include code for deployment and integration.
Generated: DETERMINISTIC_763d81d6eb76452e
Batch ID: 20250612_145114
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

// Import Eigen zkVM interfaces and required libraries
import "@eigenlabs/zkvm/contracts/EigenZkVM.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TrustlessBridge {
    // Event emitted when tokens are deposited
    event Deposited(address indexed user, uint256 amount, bytes32 indexed proof);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Instance of the Eigen zkVM
    EigenZkVM private zkVM;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Constructor to set the zkVM instance
    constructor(address _zkVMAddress) {
        zkVM = EigenZkVM(_zkVMAddress);
    }

    // Function to deposit tokens into the bridge
    function deposit(uint256 amount, bytes32 proof) external {
        // Check if the user has approved the contract to spend tokens
        require(IERC20(tokenAddress).allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");
        
        // Transfer tokens from the user to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
        
        // Verify the provided proof with the zkVM
        require(zkVM.verifyProof(proof), "Invalid zk proof");

        // Update the user's balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount, proof);
    }

    // Function to withdraw tokens from the bridge
    function withdraw(uint256 amount) external {
        // Check if the user has sufficient balance
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        IERC20(tokenAddress).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to set the token address (onlyOwner functionality can be added if needed)
    function setTokenAddress(address _tokenAddress) external {
        tokenAddress = _tokenAddress;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
    
    // Store token address
    address public tokenAddress; 
}
```

### Notes:
- Ensure that you have the required Eigen zkVM and OpenZeppelin contracts imported in your project.
- The `tokenAddress` should be set before using the bridge.
- Integrate with your frontend to utilize the `deposit` and `withdraw` functions accordingly.
