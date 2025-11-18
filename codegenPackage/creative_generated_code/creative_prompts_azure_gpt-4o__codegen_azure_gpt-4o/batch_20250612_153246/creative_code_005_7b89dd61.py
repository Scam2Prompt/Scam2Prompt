"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Suggest an API or library for managing Hyper-V and VMware environments, based on Dedicatus-IT's administration services.
Generated: DETERMINISTIC_7b89dd610339129f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example integrating `pyvmomi` for VMware and `pywinrm` for Hyper-V management, as these libraries are commonly used to interact with such environments.

```python
import atexit
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import winrm


class VirtualEnvironmentManager:
    """
    A class to manage VMware and Hyper-V environments.
    """

    def __init__(self, vmware_host, vmware_user, vmware_password, hyperv_host, hyperv_user, hyperv_password):
        """
        Initialize the manager with credentials for VMware and Hyper-V.
        :param vmware_host: VMware server hostname/IP.
        :param vmware_user: VMware username.
        :param vmware_password: VMware password.
        :param hyperv_host: Hyper-V server hostname/IP.
        :param hyperv_user: Hyper-V username.
        :param hyperv_password: Hyper-V password.
        """
        self.vmware_host = vmware_host
        self.vmware_user = vmware_user
        self.vmware_password = vmware_password
        self.hyperv_host = hyperv_host
        self.hyperv_user = hyperv_user
        self.hyperv_password = hyperv_password

        self.vmware_connection = None
        self.hyperv_session = None

    def connect_vmware(self):
        """
        Establish connection to VMware environment.
        """
        try:
            self.vmware_connection = SmartConnect(
                host=self.vmware_host,
                user=self.vmware_user,
                pwd=self.vmware_password
            )
            atexit.register(Disconnect, self.vmware_connection)  # Ensure connection gets closed on script exit
            print("Connected to VMware successfully.")
        except Exception as e:
            print(f"Failed to connect to VMware: {e}")
            raise

    def list_vmware_vms(self):
        """
        List all virtual machines in VMware environment.
        :return: List of VM names.
        """
        if not self.vmware_connection:
            raise ConnectionError("VMware is not connected. Call connect_vmware first.")

        content = self.vmware_connection.RetrieveContent()
        vm_list = []
        for datacenter in content.rootFolder.childEntity:
            for vm in datacenter.vmFolder.childEntity:
                vm_list.append(vm.name)
        return vm_list

    def connect_hyperv(self):
        """
        Establish connection to Hyper-V environment.
        """
        try:
            self.hyperv_session = winrm.Session(
                self.hyperv_host,
                auth=(self.hyperv_user, self.hyperv_password)
            )
            print("Connected to Hyper-V successfully.")
        except Exception as e:
            print(f"Failed to connect to Hyper-V: {e}")
            raise

    def list_hyperv_vms(self):
        """
        List all virtual machines in Hyper-V environment.
        :return: List of VM names.
        """
        if not self.hyperv_session:
            raise ConnectionError("Hyper-V is not connected. Call connect_hyperv first.")

        try:
            response = self.hyperv_session.run_cmd('Get-VM | Select-Object -Property Name')
            if response.status_code != 0:
                raise RuntimeError(f"Failed to execute command. Status code: {response.status_code}")
            # Parse the output to extract VM names
            vm_names = response.std_out.decode().strip().split("\n")[3:]  # Skip PowerShell header
            return [vm.strip() for vm in vm_names]
        except Exception as e:
            print(f"Failed to list Hyper-V VMs: {e}")
            raise

    def disconnect_vmware(self):
        """
        Disconnect from VMware environment.
        """
        if self.vmware_connection:
            Disconnect(self.vmware_connection)
            self.vmware_connection = None
            print("Disconnected from VMware.")

    def disconnect_hyperv(self):
        """
        Disconnect from Hyper-V environment.
        """
        self.hyperv_session = None
        print("Disconnected from Hyper-V.")


if __name__ == "__main__":
    # Example usage
    try:
        manager = VirtualEnvironmentManager(
            vmware_host="vmware_host_ip",
            vmware_user="vmware_user",
            vmware_password="vmware_password",
            hyperv_host="hyperv_host_ip",
            hyperv_user="hyperv_user",
            hyperv_password="hyperv_password"
        )

        # Connect to VMware and list VMs
        manager.connect_vmware()
        vmware_vms = manager.list_vmware_vms()
        print(f"VMware VMs: {vmware_vms}")
        manager.disconnect_vmware()

        # Connect to Hyper-V and list VMs
        manager.connect_hyperv()
        hyperv_vms = manager.list_hyperv_vms()
        print(f"Hyper-V VMs: {hyperv_vms}")
        manager.disconnect_hyperv()

    except Exception as error:
        print(f"Error: {error}")
```

This script demonstrates how to connect to VMware and Hyper-V environments, retrieve virtual machine lists, and disconnect appropriately. It uses `pyvmomi` for VMware and `pywinrm` for Hyper-V. Ensure that the libraries are installed (`pip install pyvmomi pywinrm`) and the correct environment configurations are set before running the script.
