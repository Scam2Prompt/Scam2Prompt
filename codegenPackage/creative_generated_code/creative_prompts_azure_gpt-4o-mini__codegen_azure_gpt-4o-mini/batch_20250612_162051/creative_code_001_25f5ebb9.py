"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Write a Java code snippet that interfaces with a Bluetooth thermal printer, similar to the Blueprint BP-LITE58, as detailed on the Central Multi Computer site.
Generated: DETERMINISTIC_25f5ebb925a5ca3e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.util.Log;

import java.io.IOException;
import java.io.OutputStream;
import java.util.UUID;

public class BluetoothPrinter {

    // UUID for Serial Port Profile (SPP)
    private static final UUID SPP_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    private BluetoothAdapter bluetoothAdapter;
    private BluetoothSocket bluetoothSocket;
    private OutputStream outputStream;

    /**
     * Initializes the BluetoothPrinter with the default Bluetooth adapter.
     */
    public BluetoothPrinter() {
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        if (bluetoothAdapter == null) {
            throw new UnsupportedOperationException("Bluetooth not supported on this device.");
        }
    }

    /**
     * Connects to a Bluetooth printer using its MAC address.
     *
     * @param deviceAddress The MAC address of the Bluetooth printer.
     * @throws IOException If there is an error during connection.
     */
    public void connect(String deviceAddress) throws IOException {
        BluetoothDevice printerDevice = bluetoothAdapter.getRemoteDevice(deviceAddress);
        bluetoothSocket = printerDevice.createRfcommSocketToServiceRecord(SPP_UUID);

        // Attempt to connect to the device
        try {
            bluetoothSocket.connect();
            outputStream = bluetoothSocket.getOutputStream();
        } catch (IOException e) {
            Log.e("BluetoothPrinter", "Unable to connect to the Bluetooth printer.", e);
            closeConnection();
            throw e;
        }
    }

    /**
     * Sends data to the connected Bluetooth printer.
     *
     * @param data The data to print as a byte array.
     * @throws IOException If there is an error during printing.
     */
    public void print(byte[] data) throws IOException {
        if (outputStream == null) {
            throw new IllegalStateException("Output stream is not initialized. Please connect to a printer first.");
        }
        outputStream.write(data);
        outputStream.flush();
    }

    /**
     * Closes the connection to the Bluetooth printer.
     */
    public void closeConnection() {
        try {
            if (outputStream != null) {
                outputStream.close();
            }
            if (bluetoothSocket != null) {
                bluetoothSocket.close();
            }
        } catch (IOException e) {
            Log.e("BluetoothPrinter", "Error closing Bluetooth connection.", e);
        }
    }
}
```
