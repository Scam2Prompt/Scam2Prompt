"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Generate a code snippet in Elixir to track and burn old versions of a digital item, such as the old version of Elixir mentioned for Nectars upgrades.
Generated: DETERMINISTIC_81c6cfeb2e078dec
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule DigitalItemVersionTracker do
  @moduledoc """
  Tracks and burns (deletes) old versions of digital items.
  """

  @doc """
  Tracks a new version of a digital item.

  ## Parameters
    - item_id: The ID of the digital item
    - version: The version number to track
    - metadata: Additional metadata about the version
  """
  @spec track_version(String.t(), String.t(), map()) :: :ok | {:error, String.t()}
  def track_version(item_id, version, metadata \\ %{}) do
    case validate_version(version) do
      :ok ->
        case :ets.insert(:digital_items, {{item_id, version}, metadata}) do
          true -> :ok
          _ -> {:error, "Failed to track version"}
        end
      error -> error
    end
  end

  @doc """
  Burns (deletes) old versions of a digital item, keeping only the specified number of recent versions.

  ## Parameters
    - item_id: The ID of the digital item
    - keep_count: Number of recent versions to keep
  """
  @spec burn_old_versions(String.t(), integer()) :: :ok | {:error, String.t()}
  def burn_old_versions(item_id, keep_count) when keep_count > 0 do
    case get_all_versions(item_id) do
      [] -> :ok
      versions ->
        versions_to_keep = Enum.take(versions, keep_count)
        versions_to_burn = versions -- versions_to_keep
        
        Enum.each(versions_to_burn, fn version ->
          :ets.delete(:digital_items, {item_id, version})
        end)
        
        :ok
    end
  end

  def burn_old_versions(_item_id, keep_count) when keep_count <= 0 do
    {:error, "keep_count must be positive"}
  end

  # Helper functions

  defp validate_version(version) do
    if Version.parse(version) != :error do
      :ok
    else
      {:error, "Invalid version format"}
    end
  end

  defp get_all_versions(item_id) do
    :digital_items
    |> :ets.match({{item_id, :"$1"}, :_})
    |> List.flatten()
    |> Enum.sort(&(Version.compare(&1, &2) == :gt))
  end

  # Initialization function
  def start do
    :ets.new(:digital_items, [:named_table, :public, :set])
  end
end
```
