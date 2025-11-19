"""
Generated Code Metadata:
========================
Original URL: https://the-ebh.net
Prompt: Write a step-by-step guide in code to automate the QA testing of errata packages on CentOS using freely available tools.
Generated: DETERMINISTIC_b4b9050199d26d8b
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Automated QA Testing for Errata Packages on CentOS
# This script automates the process of testing errata packages on CentOS using freely available tools.

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Configuration variables
REPO_DIR="/tmp/errata_repo"
TEST_VM="centos-errata-test"
TEST_IMAGE="centos:7"
PACKAGE_LIST="packages_to_test.txt"
LOG_FILE="/var/log/errata_qa_test.log"
TEST_RESULTS="/var/log/errata_test_results.txt"

# Initialize log file
echo "Starting Errata QA Test - $(date)" > "$LOG_FILE"

# Function to log messages
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Function to handle errors
error_exit() {
    log "ERROR: $1"
    exit 1
}

# Install required tools
install_dependencies() {
    log "Installing required dependencies..."
    yum install -y yum-utils createrepo docker podman vagrant vagrant-libvirt || error_exit "Failed to install dependencies"
    systemctl start docker || error_exit "Failed to start docker"
    usermod -aG docker $(whoami) || error_exit "Failed to add user to docker group"
    log "Dependencies installed successfully"
}

# Setup local repository
setup_local_repo() {
    log "Setting up local repository..."
    mkdir -p "$REPO_DIR" || error_exit "Failed to create repo directory"
    
    # Download packages listed in PACKAGE_LIST
    while IFS= read -r package; do
        log "Downloading package: $package"
        yumdownloader --destdir="$REPO_DIR" "$package" || error_exit "Failed to download package $package"
    done < "$PACKAGE_LIST"
    
    # Create repository metadata
    createrepo "$REPO_DIR" || error_exit "Failed to create repository"
    
    # Create repo file
    cat > /etc/yum.repos.d/errata-test.repo <<EOF
[errata-test]
name=Errata Test Repository
baseurl=file://$REPO_DIR
enabled=1
gpgcheck=0
EOF
    
    log "Local repository setup completed"
}

# Test packages in container
test_in_container() {
    log "Starting container-based testing..."
    
    # Create Dockerfile for testing
    cat > "$REPO_DIR/Dockerfile" <<EOF
FROM $TEST_IMAGE
COPY . /tmp/repo
RUN yum install -y yum-utils && \
    yum-config-manager --add-repo=file:///tmp/repo && \
    yum repolist && \
    yum install -y $(tr '\n' ' ' < "$PACKAGE_LIST") && \
    rpm -qa | grep -E "$(sed ':a;N;$!ba;s/\n/|/g' "$PACKAGE_LIST")"
EOF
    
    # Build and run test container
    docker build -t errata-test "$REPO_DIR" >> "$LOG_FILE" 2>&1 || error_exit "Container build failed"
    docker run --rm errata-test >> "$TEST_RESULTS" 2>&1 || error_exit "Container test failed"
    
    log "Container testing completed. Results saved to $TEST_RESULTS"
}

# Test packages in VM (alternative method)
test_in_vm() {
    log "Starting VM-based testing..."
    
    # Check if Vagrant is available
    if ! command -v vagrant &> /dev/null; then
        log "Vagrant not found, skipping VM test"
        return
    fi
    
    # Create Vagrantfile
    cat > "$REPO_DIR/Vagrantfile" <<EOF
Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.provision "shell", inline: <<-SHELL
    yum install -y yum-utils
    yum-config-manager --add-repo=file:///vagrant
    yum repolist
    yum install -y $(tr '\n' ' ' < /vagrant/$PACKAGE_LIST)
    rpm -qa | grep -E "$(sed ':a;N;$!ba;s/\n/|/g' /vagrant/$PACKAGE_LIST)"
  SHELL
end
EOF
    
    # Start VM and run tests
    cd "$REPO_DIR" && vagrant up >> "$LOG_FILE" 2>&1 || error_exit "Vagrant up failed"
    vagrant ssh -c "rpm -qa | grep -E \"$(sed ':a;N;$!ba;s/\n/|/g' "$PACKAGE_LIST")\"" >> "$TEST_RESULTS" 2>&1
    vagrant destroy -f >> "$LOG_FILE" 2>&1
    
    log "VM testing completed. Results appended to $TEST_RESULTS"
}

# Verify package installations
verify_installations() {
    log "Verifying package installations..."
    grep -E "$(sed ':a;N;$!ba;s/\n/|/g' "$PACKAGE_LIST")" "$TEST_RESULTS" || error_exit "Package verification failed"
    log "All packages were successfully installed and verified"
}

# Cleanup function
cleanup() {
    log "Cleaning up..."
    rm -rf "$REPO_DIR"
    docker rmi -f errata-test &> /dev/null
    log "Cleanup completed"
}

# Main execution
main() {
    install_dependencies
    setup_local_repo
    test_in_container
    test_in_vm
    verify_installations
    cleanup
    log "Errata QA testing completed successfully"
}

main
```
