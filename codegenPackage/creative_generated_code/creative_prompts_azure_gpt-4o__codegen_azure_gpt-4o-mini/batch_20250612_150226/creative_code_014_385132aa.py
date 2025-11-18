"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Create a Solidity contract for a LayerZero-based gaming token that supports seamless asset transfers between Ethereum and a custom blockchain network, referencing the `Beam` use case.
Generated: DETERMINISTIC_385132aa0292960b
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

// Import LayerZero interface for cross-chain functionality
import "@layerZero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerZero/contracts/interfaces/ILayerZeroReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GamingToken
 * @dev A LayerZero-based gaming token that supports asset transfers between Ethereum and a custom blockchain.
 */
contract GamingToken is ERC20, Ownable, ILayerZeroReceiver {
    ILayerZeroEndpoint public endpoint; // LayerZero endpoint for cross-chain communication

    // Event emitted when tokens are transferred to another chain
    event TokensTransferred(address indexed recipient, uint256 amount, uint16 indexed dstChainId);

    /**
     * @param _name The name of the token
     * @param _symbol The symbol of the token
     * @param _endpoint The LayerZero endpoint address
     */
    constructor(string memory _name, string memory _symbol, address _endpoint) ERC20(_name, _symbol) {
        require(_endpoint != address(0), "Invalid endpoint address");
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    /**
     * @dev Mint new tokens to the specified address
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        _mint(to, amount);
    }

    /**
     * @dev Transfer tokens to another chain
     * @param to The address to receive tokens on the destination chain
     * @param amount The amount of tokens to transfer
     * @param dstChainId The destination chain ID
     */
    function transferToChain(address to, uint256 amount, uint16 dstChainId) external payable {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(to != address(0), "Invalid recipient address");

        // Burn the tokens locally
        _burn(msg.sender, amount);

        // Encode the payload containing the recipient address and amount
        bytes memory payload = abi.encode(to, amount);

        // Send the payload through LayerZero
        (uint256 nativeFee, ) = endpoint.estimateFees(dstChainId, address(this), payload, false, "");
        require(msg.value >= nativeFee, "Insufficient native token for fee");

        endpoint.send{value: msg.value}(dstChainId, address(this), payload, payable(msg.sender), address(0), new bytes(0));
        emit TokensTransferred(to, amount, dstChainId);
    }

    /**
     * @dev Receive tokens from another chain
     * @param _srcChainId The source chain ID
     * @param _srcAddress The address of the token contract on the source chain
     * @param _payload The payload containing recipient address and amount
     */
    function lzReceive(uint16 _srcChainId, bytes memory _srcAddress, uint64, bytes memory _payload) external override {
        // Ensure that the message comes from the LayerZero endpoint
        require(msg.sender == address(endpoint), "Unauthorized endpoint");

        // Decode the payload to get recipient address and amount
        (address recipient, uint256 amount) = abi.decode(_payload, (address, uint256));

        // Mint tokens to the recipient
        _mint(recipient, amount);
    }

    /**
     * @dev Withdraw native tokens from the contract
     * @param amount The amount of native tokens to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}
}
```
