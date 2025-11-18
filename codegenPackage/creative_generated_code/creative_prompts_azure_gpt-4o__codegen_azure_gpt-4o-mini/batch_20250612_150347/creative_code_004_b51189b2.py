"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-popofrog.pages.dev
Prompt: Write a step-by-step guide in Solidity for implementing a multichain token bridge for $FROP tokens, ensuring secure transfer between networks like Avalanche and Solana.
Generated: DETERMINISTIC_b51189b27a1dd3d9
Batch ID: 20250612_150347
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the bridge
interface IBridge {
    function transferTokens(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _destinationChainId
    ) external;

    function receiveTokens(
        address _token,
        uint256 _amount,
        address _from,
        uint256 _sourceChainId
    ) external;
}

// FROP Token Bridge contract
contract FROPBridge is Ownable, IBridge {
    using SafeMath for uint256;

    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed token, address indexed to, uint256 amount, uint256 destinationChainId);
    
    // Event emitted when tokens are received
    event TokensReceived(address indexed token, address indexed from, uint256 amount, uint256 sourceChainId);

    // Mapping to track tokens that can be bridged
    mapping(address => bool) public supportedTokens;

    // Modifier to check if token is supported
    modifier onlySupportedToken(address _token) {
        require(supportedTokens[_token], "Token not supported");
        _;
    }

    // Function to add supported tokens
    function addSupportedToken(address _token) external onlyOwner {
        supportedTokens[_token] = true;
    }

    // Function to remove supported tokens
    function removeSupportedToken(address _token) external onlyOwner {
        supportedTokens[_token] = false;
    }

    // Transfer tokens to another chain
    function transferTokens(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _destinationChainId
    ) external override onlySupportedToken(_token) {
        require(_amount > 0, "Amount must be greater than 0");
        require(IERC20(_token).balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from the sender to the bridge contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Emit event for transferred tokens
        emit TokensTransferred(_token, _to, _amount, _destinationChainId);
    }

    // Receive tokens from another chain (to be called by a trusted bridge contract)
    function receiveTokens(
        address _token,
        uint256 _amount,
        address _from,
        uint256 _sourceChainId
    ) external override onlySupportedToken(_token) {
        // Transfer tokens to the user from the bridge contract
        require(IERC20(_token).balanceOf(address(this)) >= _amount, "Insufficient tokens in bridge");
        
        // Transfer tokens to the user
        IERC20(_token).transfer(_from, _amount);

        // Emit event for received tokens
        emit TokensReceived(_token, _from, _amount, _sourceChainId);
    }
}
```
