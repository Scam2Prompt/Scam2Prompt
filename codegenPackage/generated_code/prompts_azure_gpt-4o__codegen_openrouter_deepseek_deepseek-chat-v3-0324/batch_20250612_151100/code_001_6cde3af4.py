"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to build and test a package in the Agoric SDK using `yarn install`, `yarn build`, and `yarn test` commands. Include steps to resolve mismatched workspace dependencies as mentioned in the documentation.
Generated: DETERMINISTIC_6cde3af43fb6d55a
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Agoric SDK Package Builder and Tester
# This script handles installation, building, and testing of Agoric SDK packages
# with proper dependency resolution for workspaces.

set -euo pipefail

# Define colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to handle errors
handle_error() {
    local exit_code=$1
    local command=$2
    echo -e "${RED}Error: Command '${command}' failed with exit code ${exit_code}${NC}" >&2
    exit "${exit_code}"
}

# Function to resolve workspace dependencies
resolve_workspace_deps() {
    echo -e "${YELLOW}Resolving workspace dependencies...${NC}"
    
    # Check if we're in a yarn workspace
    if [ -f "package.json" ] && [ -d "node_modules" ]; then
        echo -e "${YELLOW}Found existing node_modules, checking for mismatches...${NC}"
        
        # Check for mismatched dependencies
        if yarn check --verify-tree; then
            echo -e "${GREEN}No dependency mismatches found.${NC}"
        else
            echo -e "${YELLOW}Dependency mismatches detected. Attempting to resolve...${NC}"
            
            # Remove existing node_modules and lock file
            rm -rf node_modules
            rm -f yarn.lock
            
            # Reinstall dependencies
            if ! yarn install; then
                handle_error $? "yarn install (dependency resolution)"
            fi
        fi
    else
        # Fresh installation
        if ! yarn install; then
            handle_error $? "yarn install (fresh install)"
        fi
    fi
}

# Main execution
main() {
    echo -e "${GREEN}Starting Agoric SDK package build and test process...${NC}"
    
    # Step 1: Resolve workspace dependencies
    resolve_workspace_deps
    
    # Step 2: Build the package
    echo -e "${YELLOW}Building package...${NC}"
    if ! yarn build; then
        handle_error $? "yarn build"
    fi
    echo -e "${GREEN}Build successful.${NC}"
    
    # Step 3: Test the package
    echo -e "${YELLOW}Running tests...${NC}"
    if ! yarn test; then
        handle_error $? "yarn test"
    fi
    echo -e "${GREEN}Tests passed successfully.${NC}"
    
    echo -e "${GREEN}All steps completed successfully.${NC}"
}

# Execute main function
main "$@"
```
