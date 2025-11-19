"""
Generated Code Metadata:
========================
Original URL: https://4kg24t7m.s3.amazonaws.com
Prompt: "Provide a code snippet that demonstrates how to save and load a trained neural network model using Axon, including any specific commands or functions."
Generated: DETERMINISTIC_a90959222838f43c
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
# neural_network_model.ex
defmodule NeuralNetworkModel do
  @moduledoc """
  Module for saving and loading trained neural network models using Axon.
  """

  alias Axon.{Serialize, Loop}
  alias Nx.Tensor, as: Tensor

  @doc """
  Trains a simple neural network model and returns the trained model state.

  ## Parameters
    - train_data: Training data as a tensor
    - train_labels: Training labels as a tensor
    - epochs: Number of training epochs (default: 10)

  ## Returns
    - Tuple of {model, model_state}
  """
  def train_model(train_data, train_labels, epochs \\ 10) do
    model =
      Axon.input("input", shape: {nil, 784})
      |> Axon.dense(128, activation: :relu)
      |> Axon.dense(10, activation: :softmax)

    model_state =
      model
      |> Axon.Loop.trainer(:categorical_cross_entropy, Axon.Optimizers.adam(0.01))
      |> Axon.Loop.run(train_data, train_labels, %{}, epochs: epochs, compiler: EXLA)

    {model, model_state}
  end

  @doc """
  Saves a trained Axon model and its state to disk.

  ## Parameters
    - model: The Axon model to save
    - model_state: The trained model state
    - path: Path to save the model (default: "model.axon")

  ## Returns
    - :ok on success, {:error, reason} on failure
  """
  def save_model(model, model_state, path \\ "model.axon") do
    try do
      Serialize.serialize(model, model_state, path)
      :ok
    rescue
      e in File.Error -> {:error, "Failed to save model: #{e.message}"}
    end
  end

  @doc """
  Loads a saved Axon model from disk.

  ## Parameters
    - path: Path to the saved model (default: "model.axon")

  ## Returns
    - {:ok, {model, model_state}} on success
    - {:error, reason} on failure
  """
  def load_model(path \\ "model.axon") do
    try do
      {model, model_state} = Serialize.deserialize(path)
      {:ok, {model, model_state}}
    rescue
      e in File.Error -> {:error, "Failed to load model: #{e.message}"}
      e in RuntimeError -> {:error, "Invalid model file: #{e.message}"}
    end
  end

  @doc """
  Makes predictions using a loaded model.

  ## Parameters
    - model: The loaded Axon model
    - model_state: The loaded model state
    - input_data: Input data tensor for prediction

  ## Returns
    - Prediction tensor
  """
  def predict(model, model_state, input_data) do
    Axon.predict(model, model_state, input_data, compiler: EXLA)
  end
end
```
