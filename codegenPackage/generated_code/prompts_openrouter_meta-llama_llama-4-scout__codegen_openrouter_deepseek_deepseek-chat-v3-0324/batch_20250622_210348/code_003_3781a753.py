"""
Generated Code Metadata:
========================
Original URL: https://4kg24t7m.s3.amazonaws.com
Prompt: "What are the best practices for initializing weights in neural networks using Axon, considering a scenario with 1000 samples and 143 features?"
Generated: DETERMINISTIC_3781a75305fe3556
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule NeuralNetworkInitialization do
  @moduledoc """
  Module containing best practices for weight initialization in neural networks using Axon.
  Handles scenarios with 1000 samples and 143 features.
  """

  alias Axon.{Initializers, Models}
  alias Nx.Tensor, as: Tensor

  @doc """
  Builds a neural network with proper weight initialization for the given scenario.
  
  ## Parameters
    - input_shape: Shape of input tensor {batch_size, num_features}
    - num_classes: Number of output classes
    - hidden_layers: List of hidden layer sizes
  
  ## Returns
    - Axon model with proper weight initialization
  """
  @spec build_model({pos_integer(), pos_integer()}, pos_integer(), list(pos_integer())) ::
          Axon.t()
  def build_model(input_shape, num_classes, hidden_layers) do
    {_batch_size, num_features} = input_shape

    # Xavier/Glorot initialization for sigmoid/tanh activations
    xavier_init = Initializers.glorot_uniform()

    # He initialization for ReLU activations
    he_init = Initializers.he_normal()

    input =
      Axon.input("input", shape: input_shape)
      |> Axon.flatten()

    # Build hidden layers with proper initialization
    hidden_layers
    |> Enum.reduce(input, fn units, model ->
      Axon.dense(model, units,
        kernel_initializer: he_init,
        bias_initializer: xavier_init
      )
      |> Axon.relu()
    end)
    |> Axon.dense(num_classes,
      kernel_initializer: xavier_init,
      bias_initializer: Initializers.zeros()
    )
    |> Axon.softmax()
  end

  @doc """
  Initializes model parameters with proper weight initialization.
  
  ## Parameters
    - model: Axon model
    - template_input: Example input tensor for parameter initialization
  
  ## Returns
    - Initialized model parameters
  """
  @spec initialize_params(Axon.t(), Tensor.t()) :: map()
  def initialize_params(model, template_input) do
    model_state =
      model
      |> Axon.init(compiler: EXLA)
      |> Axon.predict(template_input)

    model_state.params
  end

  @doc """
  Example usage with 1000 samples and 143 features.
  """
  @spec example_usage() :: map()
  def example_usage() do
    # Example configuration
    batch_size = 32
    num_features = 143
    num_classes = 10
    hidden_layers = [128, 64]

    # Build model
    model = build_model({batch_size, num_features}, num_classes, hidden_layers)

    # Create template input
    template_input = Nx.random_uniform({batch_size, num_features})

    # Initialize parameters
    initialize_params(model, template_input)
  end
end
```
