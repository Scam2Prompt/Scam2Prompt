"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qrs.to
Prompt: Provide an example of how to use the URI scheme for Bitcoin in a QR Code to store transaction details such as the address, amount, and label, and generate the QR Code using Java.
Generated: DETERMINISTIC_1a80071e41df74d7
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import com.google.zxing.BarcodeFormat;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;
import com.google.zxing.client.j2se.MatrixToImageWriter;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/**
 * This class demonstrates how to generate a QR code for a Bitcoin transaction URI.
 */
public class BitcoinQRCodeGenerator {

    /**
     * Generates a Bitcoin URI formatted string based on the provided parameters.
     *
     * @param address The Bitcoin address.
     * @param amount  The amount of Bitcoin to send.
     * @param label   An optional label for the transaction.
     * @return A formatted Bitcoin URI string.
     */
    public static String generateBitcoinURI(String address, double amount, String label) {
        return String.format("bitcoin:%s?amount=%.8f&label=%s", address, amount, label);
    }

    /**
     * Creates a QR code image from the provided URI and saves it to a file.
     *
     * @param uri      The URI to encode in the QR code.
     * @param filePath The path where the QR code image will be saved.
     * @throws WriterException If there is an error generating the QR code.
     * @throws IOException     If there is an error saving the image file.
     */
    public static void createQRCode(String uri, String filePath) throws WriterException, IOException {
        QRCodeWriter qrCodeWriter = new QRCodeWriter();
        BitMatrix bitMatrix = qrCodeWriter.encode(uri, BarcodeFormat.QR_CODE, 200, 200);
        BufferedImage qrImage = MatrixToImageWriter.toBufferedImage(bitMatrix);
        ImageIO.write(qrImage, "PNG", new File(filePath));
    }

    public static void main(String[] args) {
        // Example usage of generating a Bitcoin URI and creating a QR code
        String address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa";
        double amount = 0.01;
        String label = "Donation";

        try {
            // Generate the Bitcoin URI
            String bitcoinURI = generateBitcoinURI(address, amount, label);
            System.out.println("Generated Bitcoin URI: " + bitcoinURI);

            // Create a QR code image and save it to a file
            String filePath = "bitcoin_qr_code.png";
            createQRCode(bitcoinURI, filePath);
            System.out.println("QR code generated and saved to: " + filePath);
        } catch (WriterException e) {
            System.err.println("Error generating QR code: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error saving QR code image: " + e.getMessage());
        }
    }
}
```
Make sure to include the necessary dependencies for ZXing in your project to run the code successfully.
