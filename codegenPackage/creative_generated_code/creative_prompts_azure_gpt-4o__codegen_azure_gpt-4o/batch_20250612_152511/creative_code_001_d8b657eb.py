"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain4.pages.dev
Prompt: Generate code to deploy an AI model on Swan Chain's decentralized computing network using the AI Container feature for seamless scaling and deployment.
Generated: DETERMINISTIC_d8b657eb04d0d2fa
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import swanchain_sdk as swan
import os

# Define constants for deployment
MODEL_FILE_PATH = "./model/my_ai_model.pkl"  # Path to the AI model file
SCRIPTS_PATH = "./scripts/serve_model.py"   # Path to the serving script
CONTAINER_NAME = "my_ai_model_container"    # Name for the AI container
SWAN_API_KEY = os.getenv("SWAN_API_KEY")    # API key for Swan Chain authentication

def deploy_model_to_swan():
    """
    Deploys an AI model using Swan Chain's AI Container feature.
    """
    try:
        # Initialize Swan Chain client
        client = swan.Client(api_key=SWAN_API_KEY)
        
        # Ensure API key is provided
        if not SWAN_API_KEY:
            raise ValueError("Swan API key is missing. Set the SWAN_API_KEY environment variable.")
        
        # Check if model file exists
        if not os.path.exists(MODEL_FILE_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_FILE_PATH}")
        
        # Check if serving script exists
        if not os.path.exists(SCRIPTS_PATH):
            raise FileNotFoundError(f"Serving script not found at {SCRIPTS_PATH}")
        
        # Create AI container
        container_id = client.create_ai_container(
            name=CONTAINER_NAME,
            model_file_path=MODEL_FILE_PATH,
            serving_script_path=SCRIPTS_PATH
        )
        print(f"AI container created successfully with ID: {container_id}")
        
        # Deploy the container on Swan Chain
        deployment_status = client.deploy_container(container_id)
        if deployment_status["success"]:
            print(f"AI model deployed successfully! Deployment ID: {deployment_status['deployment_id']}")
        else:
            print("Deployment failed. Error: ", deployment_status["error"])

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except swan.SwanChainException as sce:
        print(f"SwanChainException: {sce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    deploy_model_to_swan()
```

### Notes:
- Replace `"./model/my_ai_model.pkl"` and `"./scripts/serve_model.py"` with your actual model file and serving script paths.
- Set the `SWAN_API_KEY` environment variable with your valid Swan Chain API key.
- Make sure to install the `swanchain_sdk` Python package or library and verify connectivity with Swan Chain's API.
