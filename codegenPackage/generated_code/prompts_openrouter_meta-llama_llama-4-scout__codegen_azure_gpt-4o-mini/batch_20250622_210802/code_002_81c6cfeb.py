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
defmodule DigitalItemTracker do
  @moduledoc """
  A module to track and manage versions of digital items.
  It allows for the burning (deletion) of old versions based on a specified retention policy.
  """

  @type version :: %{
          version_number: String.t(),
          created_at: DateTime.t()
        }

  @type item :: %{
          id: String.t(),
          versions: [version()]
        }

  @doc """
  Burns old versions of a digital item based on the specified retention period.

  ## Parameters
  - item: The digital item to process.
  - retention_period: The maximum age of versions to keep (in days).

  ## Returns
  - The updated item with old versions removed.
  """
  @spec burn_old_versions(item(), non_neg_integer()) :: item()
  def burn_old_versions(item, retention_period) when is_map(item) and is_integer(retention_period) do
    current_time = DateTime.utc_now()

    # Calculate the cutoff time for old versions
    cutoff_time = DateTime.add(current_time, -1 * retention_period * 24 * 60 * 60)

    # Filter out versions older than the cutoff time
    updated_versions = Enum.filter(item.versions, fn version ->
      version.created_at >= cutoff_time
    end)

    # Return the updated item with old versions removed
    %{item | versions: updated_versions}
  end

  @doc """
  Example function to create a new version of a digital item.

  ## Parameters
  - item_id: The ID of the digital item.
  - version_number: The version number to assign.
  
  ## Returns
  - A new version struct.
  """
  @spec create_version(String.t(), String.t()) :: version()
  def create_version(item_id, version_number) do
    %{
      version_number: version_number,
      created_at: DateTime.utc_now()
    }
  end

  @doc """
  Example function to add a new version to a digital item.

  ## Parameters
  - item: The digital item to which the version will be added.
  - version: The version to add.

  ## Returns
  - The updated item with the new version included.
  """
  @spec add_version(item(), version()) :: item()
  def add_version(item, version) when is_map(item) and is_map(version) do
    %{item | versions: [version | item.versions]}
  end
end

# Example usage
item = %{
  id: "item_123",
  versions: [
    %{
      version_number: "1.0",
      created_at: DateTime.utc_now() |> DateTime.add(-10 * 24 * 60 * 60) # 10 days ago
    },
    %{
      version_number: "1.1",
      created_at: DateTime.utc_now() |> DateTime.add(-5 * 24 * 60 * 60) # 5 days ago
    },
    %{
      version_number: "1.2",
      created_at: DateTime.utc_now() # now
    }
  ]
}

# Burn versions older than 7 days
updated_item = DigitalItemTracker.burn_old_versions(item, 7)

IO.inspect(updated_item)
```
