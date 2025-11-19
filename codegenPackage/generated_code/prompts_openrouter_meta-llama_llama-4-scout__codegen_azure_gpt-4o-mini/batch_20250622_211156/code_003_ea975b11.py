"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Generate an example of a ParaSwap implementation in a Solidity smart contract that includes best practices for safety and security, such as checking caller contracts and forwarding ERC1967 proxy upgrade checks.
Generated: DETERMINISTIC_ea975b11097ef415
Batch ID: 20250622_211156
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Upgrade.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ParaSwap
interface IParaSwap {
    function swap(
        address srcToken,
        address destToken,
        uint256 amount,
        uint256 minReturn,
        address payable destAddress,
        bytes calldata data
    ) external returns (uint256);
}

// Main contract for ParaSwap implementation
contract ParaSwapImplementation is Initializable, Ownable, ERC1967Upgrade {
    IParaSwap public paraSwap;

    // Event emitted after a successful swap
    event SwapExecuted(address indexed srcToken, address indexed destToken, uint256 amount, uint256 returnAmount);

    // Modifier to check if the caller is a contract
    modifier onlyContract() {
        require(msg.sender == tx.origin, "Caller must be a contract");
        _;
    }

    // Initialize the contract with the ParaSwap address
    function initialize(address _paraSwap) external initializer {
        require(_paraSwap != address(0), "Invalid ParaSwap address");
        paraSwap = IParaSwap(_paraSwap);
    }

    // Function to execute a swap using ParaSwap
    function executeSwap(
        address srcToken,
        address destToken,
        uint256 amount,
        uint256 minReturn,
        address payable destAddress,
        bytes calldata data
    ) external onlyOwner returns (uint256) {
        require(srcToken != address(0) && destToken != address(0), "Invalid token addresses");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the owner to this contract
        IERC20(srcToken).transferFrom(msg.sender, address(this), amount);

        // Approve the ParaSwap contract to spend the tokens
        IERC20(srcToken).approve(address(paraSwap), amount);

        // Execute the swap
        uint256 returnAmount = paraSwap.swap(srcToken, destToken, amount, minReturn, destAddress, data);

        // Emit the swap event
        emit SwapExecuted(srcToken, destToken, amount, returnAmount);

        return returnAmount;
    }

    // Function to upgrade the contract
    function upgradeTo(address newImplementation) external onlyOwner {
        require(newImplementation != address(0), "Invalid implementation address");
        _upgradeTo(newImplementation);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(msg.sender, amount);
    }
}
```
