"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: Write a Solidity code snippet to interact with the Eternal AI Smart Contracts Library for building fully on-chain neural networks.
Generated: DETERMINISTIC_1cb3be8a84624b24
Batch ID: 20250622_210803
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

/**
 * @title OnChainNeuralNetwork
 * @dev This contract interacts with the Eternal AI Smart Contracts Library to build and train neural networks on-chain.
 */
contract OnChainNeuralNetwork {
    // Address of the Eternal AI Library contract
    address public eternalAILibrary;

    // Event emitted when a neural network is created
    event NeuralNetworkCreated(uint256 networkId, string name);

    // Event emitted when a neural network is trained
    event NeuralNetworkTrained(uint256 networkId, uint256 epochs);

    /**
     * @dev Constructor to set the Eternal AI Library contract address.
     * @param _eternalAILibrary Address of the Eternal AI Library contract.
     */
    constructor(address _eternalAILibrary) {
        require(_eternalAILibrary != address(0), "Invalid Eternal AI Library address");
        eternalAILibrary = _eternalAILibrary;
    }

    /**
     * @dev Function to create a new neural network.
     * @param name Name of the neural network.
     * @param layers Array of layer configurations (e.g., [input, hidden, output]).
     * @return networkId ID of the created neural network.
     */
    function createNeuralNetwork(string memory name, uint256[] memory layers) external returns (uint256 networkId) {
        require(bytes(name).length > 0, "Network name cannot be empty");
        require(layers.length > 0, "Layers configuration cannot be empty");

        // Interact with Eternal AI Library to create the neural network
        (bool success, bytes memory data) = eternalAILibrary.call(
            abi.encodeWithSignature("createNetwork(string,uint256[])", name, layers)
        );
        require(success, "Failed to create neural network");

        // Decode the returned network ID
        networkId = abi.decode(data, (uint256));

        emit NeuralNetworkCreated(networkId, name);
    }

    /**
     * @dev Function to train an existing neural network.
     * @param networkId ID of the neural network to train.
     * @param epochs Number of training epochs.
     * @param trainingData Encoded training data.
     */
    function trainNeuralNetwork(uint256 networkId, uint256 epochs, bytes memory trainingData) external {
        require(networkId > 0, "Invalid network ID");
        require(epochs > 0, "Epochs must be greater than zero");
        require(trainingData.length > 0, "Training data cannot be empty");

        // Interact with Eternal AI Library to train the neural network
        (bool success, ) = eternalAILibrary.call(
            abi.encodeWithSignature("trainNetwork(uint256,uint256,bytes)", networkId, epochs, trainingData)
        );
        require(success, "Failed to train neural network");

        emit NeuralNetworkTrained(networkId, epochs);
    }

    /**
     * @dev Function to retrieve the details of a neural network.
     * @param networkId ID of the neural network.
     * @return name Name of the neural network.
     * @return layers Array of layer configurations.
     */
    function getNeuralNetworkDetails(uint256 networkId) external view returns (string memory name, uint256[] memory layers) {
        require(networkId > 0, "Invalid network ID");

        // Interact with Eternal AI Library to fetch network details
        (bool success, bytes memory data) = eternalAILibrary.staticcall(
            abi.encodeWithSignature("getNetworkDetails(uint256)", networkId)
        );
        require(success, "Failed to fetch neural network details");

        // Decode the returned details
        (name, layers) = abi.decode(data, (string, uint256[]));
    }
}
```
