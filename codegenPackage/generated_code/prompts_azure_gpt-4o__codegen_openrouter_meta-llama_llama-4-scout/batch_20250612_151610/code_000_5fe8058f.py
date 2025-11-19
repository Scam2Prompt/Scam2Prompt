"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Write a Python script to demonstrate the integration of PLC programming for industrial automation, referencing Puma Ipce's expertise in system control and instrumentation calibration.
Generated: DETERMINISTIC_5fe8058f5c13309f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
from pyModbusTCP.client import ModbusClient

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PLCController:
    """
    A class used to control and interact with a PLC device.

    Attributes:
    ----------
    plc_ip : str
        The IP address of the PLC device.
    plc_port : int
        The port number of the PLC device.

    Methods:
    -------
    connect_plc()
        Establishes a connection to the PLC device.
    read_plc_data(register, address)
        Reads data from a specific register on the PLC device.
    write_plc_data(register, address, value)
        Writes data to a specific register on the PLC device.
    """

    def __init__(self, plc_ip, plc_port):
        """
        Initializes the PLCController object.

        Parameters:
        ----------
        plc_ip : str
            The IP address of the PLC device.
        plc_port : int
            The port number of the PLC device.
        """
        self.plc_ip = plc_ip
        self.plc_port = plc_port
        self.client = None

    def connect_plc(self):
        """
        Establishes a connection to the PLC device.

        Returns:
        -------
        bool
            True if the connection is successful, False otherwise.
        """
        try:
            self.client = ModbusClient(self.plc_ip, self.plc_port)
            self.client.open()
            logging.info("Connected to PLC device at {}:{}".format(self.plc_ip, self.plc_port))
            return True
        except Exception as e:
            logging.error("Failed to connect to PLC device: {}".format(str(e)))
            return False

    def read_plc_data(self, register, address):
        """
        Reads data from a specific register on the PLC device.

        Parameters:
        ----------
        register : str
            The type of register (e.g., 'holding', 'input', 'coil', 'discrete').
        address : int
            The address of the register.

        Returns:
        -------
        int
            The value read from the register.
        """
        try:
            if register == 'holding':
                value = self.client.read_holding_registers(address, 1)
            elif register == 'input':
                value = self.client.read_input_registers(address, 1)
            elif register == 'coil':
                value = self.client.read_coils(address, 1)
            elif register == 'discrete':
                value = self.client.read_discrete_inputs(address, 1)
            else:
                logging.error("Invalid register type: {}".format(register))
                return None
            logging.info("Read {} from {} register at address {}".format(value, register, address))
            return value
        except Exception as e:
            logging.error("Failed to read from {} register at address {}: {}".format(register, address, str(e)))
            return None

    def write_plc_data(self, register, address, value):
        """
        Writes data to a specific register on the PLC device.

        Parameters:
        ----------
        register : str
            The type of register (e.g., 'holding', 'coil').
        address : int
            The address of the register.
        value : int
            The value to be written to the register.

        Returns:
        -------
        bool
            True if the write operation is successful, False otherwise.
        """
        try:
            if register == 'holding':
                self.client.write_holding_registers(address, [value])
            elif register == 'coil':
                self.client.write_coils(address, [value])
            else:
                logging.error("Invalid register type: {}".format(register))
                return False
            logging.info("Wrote {} to {} register at address {}".format(value, register, address))
            return True
        except Exception as e:
            logging.error("Failed to write to {} register at address {}: {}".format(register, address, str(e)))
            return False

def main():
    plc_ip = '192.168.1.100'
    plc_port = 1700

    plc_controller = PLCController(plc_ip, plc_port)

    if plc_controller.connect_plc():
        # Read data from holding register at address 0x0001
        holding_register_value = plc_controller.read_plc_data('holding', 0x0001)

        # Write data to holding register at address 0x0002
        plc_controller.write_plc_data('holding', 0x0002, 0x1234)

        # Read data from coil register at address 0x0003
        coil_register_value = plc_controller.read_plc_data('coil', 0x0003)

        # Write data to coil register at address 0x0004
        plc_controller.write_plc_data('coil', 0x0004, 1)

if __name__ == "__main__":
    main()
```
