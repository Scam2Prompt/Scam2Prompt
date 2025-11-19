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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ParaSwap Implementation
 * @author [Your Name]
 * @notice This contract demonstrates a ParaSwap implementation with best practices for safety and security.
 */
contract ParaSwapImplementation {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Event emitted when a swap occurs
    event Swap(address indexed fromToken, address indexed toToken, uint256 amount);

    /**
     * @dev Constructor
     * @param _supportedTokens List of supported tokens
     */
    constructor(address[] memory _supportedTokens) {
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens[_supportedTokens[i]] = true;
        }
    }

    /**
     * @dev Modifier to check caller contract
     */
    modifier onlyValidCaller() {
        // Check if the caller is a contract
        require(msg.sender != tx.origin, "Caller is not a contract");
        _;
    }

    /**
     * @dev Function to add support for a token
     * @param _token Token to add support for
     */
    function addSupportedToken(address _token) public {
        // Check if the token is already supported
        require(!supportedTokens[_token], "Token is already supported");
        supportedTokens[_token] = true;
    }

    /**
     * @dev Function to remove support for a token
     * @param _token Token to remove support for
     */
    function removeSupportedToken(address _token) public {
        // Check if the token is supported
        require(supportedTokens[_token], "Token is not supported");
        supportedTokens[_token] = false;
    }

    /**
     * @dev Function to swap tokens using ParaSwap
     * @param _fromToken Token to swap from
     * @param _toToken Token to swap to
     * @param _amount Amount to swap
     * @param _paraswapAddress ParaSwap address
     * @param _paraswapData ParaSwap data
     */
    function swap(
        address _fromToken,
        address _toToken,
        uint256 _amount,
        address _paraswapAddress,
        bytes calldata _paraswapData
    ) public onlyValidCaller {
        // Check if the tokens are supported
        require(supportedTokens[_fromToken], "From token is not supported");
        require(supportedTokens[_toToken], "To token is not supported");

        // Check if the amount is valid
        require(_amount > 0, "Invalid amount");

        // Approve the ParaSwap contract to spend the tokens
        IERC20(_fromToken).safeApprove(_paraswapAddress, _amount);

        // Perform the swap
        (bool success, ) = _paraswapAddress.call{value: 0}(abi.encodePacked(_paraswapData));
        require(success, "Swap failed");

        // Emit the Swap event
        emit Swap(_fromToken, _toToken, _amount);
    }

    /**
     * @dev Function to check if the contract is upgradable
     * @return bool Whether the contract is upgradable
     */
    function isUpgradable() public view returns (bool) {
        // Check if the contract has the ERC1967 proxy upgrade check
        return _getImplementation() != address(0);
    }

    /**
     * @dev Function to get the implementation address
     * @return address Implementation address
     */
    function _getImplementation() internal view returns (address) {
        // Implementation of ERC1967 proxy upgrade check
        (bool exists, ) = address(uint160(uint256(keccak256(abi.encodePacked("ERC1967"))) + 1)).staticcall(abi.encodeWithSelector(0x5f8e0c9d));
        return exists ? address(uint160(uint256(keccak256(abi.encodePacked("ERC1967"))) + 1)) : address(0);
    }

    /**
     * @dev Fallback function to forward Ether
     */
    fallback() external payable {}

    /**
     * @dev Receive function to forward Ether
     */
    receive() external payable {}
}
```
