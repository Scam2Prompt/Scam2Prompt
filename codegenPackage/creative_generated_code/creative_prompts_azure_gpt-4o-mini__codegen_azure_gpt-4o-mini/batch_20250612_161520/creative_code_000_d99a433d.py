"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizen-e09.pages.dev
Prompt: How can I use the CODES_MIGRATION.EXE tool for migrating collections in the Neo Tokyo metaverse?
Generated: DETERMINISTIC_d99a433de9714d76
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_codes_migration_tool(collection_id, target_environment):
    """
    Runs the CODES_MIGRATION.EXE tool to migrate a specified collection to the target environment.

    :param collection_id: The ID of the collection to be migrated
    :param target_environment: The environment to which the collection should be migrated (e.g., 'test', 'production')
    :return: None
    """
    # Construct the command to run the migration tool
    command = [
        'CODES_MIGRATION.EXE',
        '--collection-id', collection_id,
        '--target-env', target_environment
    ]

    try:
        logging.info(f"Starting migration for collection ID: {collection_id} to {target_environment} environment.")
        
        # Execute the migration tool
        result = subprocess.run(command, check=True, capture_output=True, text=True)

        # Log the output and success of the command execution
        logging.info(f"Migration completed successfully: {result.stdout}")

    except subprocess.CalledProcessError as e:
        # Handle errors during the migration process
        logging.error(f"Migration failed with error: {e.stderr}")
        raise RuntimeError(f"Migration process failed with return code {e.returncode}") from e

if __name__ == "__main__":
    # Example usage of the migration function
    try:
        run_codes_migration_tool("collection123", "production")
    except RuntimeError as e:
        logging.critical(f"Critical error during migration: {e}")
```
