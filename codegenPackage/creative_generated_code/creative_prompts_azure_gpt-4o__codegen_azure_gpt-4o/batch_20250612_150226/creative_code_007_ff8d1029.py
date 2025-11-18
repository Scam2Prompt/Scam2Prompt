"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Provide a Solidity implementation for transferring tokens across multiple blockchains using LayerZero's OFT standard, ensuring compatibility with Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_ff8d10297fc69815
Batch ID: 20250612_150226
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

// Import LayerZero OFT contracts
import "@layerzerolabs/oft/contracts/extension/OFTV2.sol";

// Token contract extending LayerZero's OFTV2 standard for cross-chain transfers
contract MultiChainToken is OFTV2 {
    // Token details
    string public constant name = "MultiChain Token";
    string public constant symbol = "MCT";
    uint8 public constant decimals = 18;

    // Constructor to initialize the token and LayerZero endpoint
    // `_endpoint` is the LayerZero endpoint address (varies across chains)
    // `_initialSupply` is the total supply of the token
    constructor(address _endpoint, uint256 _initialSupply) OFTV2(name, symbol, decimals, _endpoint) {
        // Mint initial supply to the deployer of the contract
        _mint(msg.sender, _initialSupply);
    }

    // Override functions to ensure compatibility with LayerZero's OFT standard
    // The implementation includes all necessary LayerZero cross-chain logic,
    // and inherits the functionality from OFTV2.
    
    // Fallback function to receive Ether (useful for gas refunds on specific chains)
    receive() external payable {}
    
    /**
     * @dev Withdraw any accidentally sent Ether (ownership required).
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        (bool success, ) = payable(msg.sender).call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to this contract by mistake.
     * @param _token Address of the ERC20 token.
     */
    function recoverERC20(address _token) external onlyOwner {
        require(_token != address(this), "Cannot recover native token");
        uint256 balance = IERC20(_token).balanceOf(address(this));
        require(balance > 0, "No tokens to recover");
        bool success = IERC20(_token).transfer(msg.sender, balance);
        require(success, "Token recovery failed");
    }
}
```

### Notes:
- Replace `@layerzerolabs/oft/contracts/extension/OFTV2.sol` with the appropriate path for OFTV2 if the LayerZero repository changes its directory structure.
- `_endpoint` should be the LayerZero endpoint specific to the blockchain where the contract is deployed (e.g., Ethereum, Binance Smart Chain).
- `_initialSupply` should be defined when deploying the contract to set the total token supply.
