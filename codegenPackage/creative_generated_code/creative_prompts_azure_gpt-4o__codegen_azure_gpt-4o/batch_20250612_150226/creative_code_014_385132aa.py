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

// Import LayerZero's messaging interfaces
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";

/**
 * @title BeamToken
 * @dev A LayerZero-based gaming token for seamless asset transfers between Ethereum
 *      and a custom blockchain network.
 */
contract BeamToken is ILayerZeroReceiver {
    // Token details
    string public constant name = "BeamToken";
    string public constant symbol = "BEAM";
    uint8 public constant decimals = 18;
    
    // Total supply of the token
    uint256 public totalSupply;

    // Token balances mapping
    mapping(address => uint256) public balances;

    // LayerZero endpoint for message passing
    ILayerZeroEndpoint public immutable lzEndpoint;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);
    event ReceivedMessage(uint16 indexed srcChainId, address indexed from, bytes payload);

    /**
     * @dev Constructor sets the LayerZero endpoint and initial supply.
     * @param _endpoint Address of the LayerZero endpoint contract.
     * @param _initialSupply Initial supply to mint to the deployer.
     */
    constructor(address _endpoint, uint256 _initialSupply) {
        require(_endpoint != address(0), "Invalid LayerZero endpoint");
        lzEndpoint = ILayerZeroEndpoint(_endpoint);

        // Mint initial supply to the deployer
        balances[msg.sender] = _initialSupply;
        totalSupply = _initialSupply;
        emit Mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Internal function to transfer tokens.
     * @param _from Sender's address.
     * @param _to Recipient's address.
     * @param _value Amount to transfer.
     */
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Invalid recipient address");
        require(balances[_from] >= _value, "Insufficient balance");

        balances[_from] -= _value;
        balances[_to] += _value;

        emit Transfer(_from, _to, _value);
    }

    /**
     * @dev Transfer tokens to another address.
     * @param _to Recipient's address.
     * @param _value Amount to transfer.
     */
    function transfer(address _to, uint256 _value) external {
        _transfer(msg.sender, _to, _value);
    }

    /**
     * @dev Burn tokens held by the sender.
     * @param _value Amount to burn.
     */
    function burn(uint256 _value) external {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        totalSupply -= _value;

        emit Burn(msg.sender, _value);
    }

    /**
     * @dev Mint new tokens to a specific address.
     * @param _to Recipient's address.
     * @param _value Amount to mint.
     */
    function mint(address _to, uint256 _value) external {
        require(_to != address(0), "Invalid recipient address");
        balances[_to] += _value;
        totalSupply += _value;

        emit Mint(_to, _value);
    }

    /**
     * @dev Receive LayerZero messages.
     * @param _srcChainId Source chain ID.
     * @param _srcAddress Source contract address encoded.
     * @param _nonce Message nonce.
     * @param _payload Message payload.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        require(msg.sender == address(lzEndpoint), "Unauthorized sender");

        // Decode the payload (example: transfer tokens cross-chain)
        (address to, uint256 amount) = abi.decode(_payload, (address, uint256));
        require(to != address(0), "Invalid recipient address");

        // Mint tokens on the destination chain
        balances[to] += amount;
        totalSupply += amount;

        emit ReceivedMessage(_srcChainId, to, _payload);
        emit Mint(to, amount);
    }

    /**
     * @dev Send tokens cross-chain using LayerZero.
     * @param _dstChainId Destination chain ID.
     * @param _to Recipient's address on the destination chain.
     * @param _value Amount to send.
     * @param _adapterParams Additional adapter parameters.
     */
    function sendTokens(
        uint16 _dstChainId,
        bytes calldata _to,
        uint256 _value,
        bytes calldata _adapterParams
    ) external payable {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        require(_to.length > 0, "Invalid recipient address");

        // Burn tokens on the source chain
        balances[msg.sender] -= _value;
        totalSupply -= _value;
        emit Burn(msg.sender, _value);

        // Encode payload (recipient address and token amount)
        bytes memory payload = abi.encode(_to, _value);

        // Send message through LayerZero
        lzEndpoint.send{value: msg.value}(
            _dstChainId, // Destination chain ID
            _to,         // Destination address encoded
            payload,     // Payload to send
            payable(msg.sender), // Refund address for excess gas
            address(0),  // Zero address for future gas refunds
            _adapterParams // Adapter parameters
        );

        emit Transfer(msg.sender, address(0), _value);
    }
}
```
