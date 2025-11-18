"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xrplfund.web.app
Prompt: Provide a step-by-step guide to build and run the `rippled` server in reporting mode, as outlined in the XRPL documentation.
Generated: DETERMINISTIC_2b9216697d897f45
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/XRPLF/rippled.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Step-by-step script to build and run the rippled server in reporting mode
# Rippled is the reference implementation of the XRP Ledger server.
# Ensure the necessary dependencies and environment are set up.
# This script assumes you are using a Linux environment.

set -e  # Exit immediately if a command exits with a non-zero status

# Step 1: Install system dependencies
echo "Installing system dependencies..."
sudo apt-get update && sudo apt-get install -y \
    git \
    cmake \
    g++ \
    wget \
    curl \
    libboost-all-dev \
    openssl \
    libssl-dev \
    protobuf-compiler \
    libprotobuf-dev

# Step 2: Clone the rippled repository
echo "Cloning the rippled repository..."
git clone https://github.com/XRPLF/rippled.git
cd rippled

# Step 3: Checkout a stable version or release tag
echo "Checking out a stable version..."
git checkout master  # Change to a specific release tag for production, e.g., `git checkout 1.11.0`

# Step 4: Create a build directory
echo "Creating build directory..."
mkdir -p build && cd build

# Step 5: Configure the build using CMake
echo "Configuring the build..."
cmake -DCMAKE_BUILD_TYPE=Release ..

# Step 6: Build the rippled binary
echo "Building rippled binary..."
cmake --build . --target rippled

# Step 7: Verify the build
echo "Verifying the built binary..."
if [ ! -f ./rippled ]; then
    echo "Error: rippled binary not found after build."
    exit 1
fi

echo "Rippled binary successfully built."

# Step 8: Generate a configuration file for reporting mode
echo "Generating configuration file for reporting mode..."
cd ..
mkdir -p ~/.config/rippled
cat <<EOF > ~/.config/rippled/rippled.cfg
[server]
port_rpc_admin_local
port_peer
port_ws_admin_local

[port_rpc_admin_local]
port = 5005
ip = 127.0.0.1
admin = 127.0.0.1

[port_peer]
port = 51235
protocol = peer

[port_ws_admin_local]
port = 6006
ip = 127.0.0.1
admin = 127.0.0.1

[node_db]
type=RocksDB
path=./db
open_files=2500
filter_bits=12
cache_mb=256
file_size_mb=64
file_size_mult=2

[ledger_history]
full

[reporting]
# Configure reporting mode
# Replace '<postgres_connection_string>' with your actual connection string
postgres=<postgres_connection_string>

[database_path]
path=./db

[sntp_servers]
time.windows.com
time.apple.com
time.nist.gov
pool.ntp.org

[validation_seed]
# Add validation seed here if required

[ssl_verify]
1

[decimal]
1
EOF

# Step 9: Run the rippled server in reporting mode
echo "Starting the rippled server in reporting mode..."
./build/rippled --conf ~/.config/rippled/rippled.cfg

echo "Rippled server is now running in reporting mode."
```
