"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Write code to integrate a feature for generating a PDF report with digital signatures using the BeSoft App Vistoria API, ensuring compatibility with both Android and iOS platforms.
Generated: DETERMINISTIC_0f3618804d21bae8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**PDF Report Generation with Digital Signatures using BeSoft App Vistoria API**
====================================================================================

### Prerequisites

* BeSoft App Vistoria API credentials
* Android and iOS platform setup

### Dependencies

* `com.itextpdf:itextpdf:5.5.13.1` for PDF generation
* `com.itextpdf:itext-xtra:5.5.13.1` for digital signatures
* `com.itextpdf:itext-pdfa:5.5.13.1` for PDF/A compliance

### Java Code ( Compatible with Android and iOS using KMM or Java)

```java
import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Element;
import com.itextpdf.text.Font;
import com.itextpdf.text.FontFactory;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.Phrase;
import com.itextpdf.text.pdf.PdfPTable;
import com.itextpdf.text.pdf.PdfReader;
import com.itextpdf.text.pdf.PdfSignatureAppearance;
import com.itextpdf.text.pdf.PdfStamper;
import com.itextpdf.text.pdf.security.DigestInfo;
import com.itextpdf.text.pdf.security.ExternalSignature;
import com.itextpdf.text.pdf.security.MakeSignature;
import com.itextpdf.text.pdf.security.PdfPKCS7;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.cert.Certificate;
import java.util.Base64;

public class PdfReportGenerator {

    private static final String API_KEY = "YOUR_API_KEY";
    private static final String API_SECRET = "YOUR_API_SECRET";
    private static final String CERTIFICATE_ALIAS = "YOUR_CERTIFICATE_ALIAS";
    private static final String KEYSTORE_PASSWORD = "YOUR_KEYSTORE_PASSWORD";
    private static final String KEYSTORE_FILE = "YOUR_KEYSTORE_FILE";

    public byte[] generatePdfReport(String reportData) throws DocumentException, IOException {
        // Create a new PDF document
        Document document = new Document();
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        com.itextpdf.text.pdf.PdfWriter.getInstance(document, bos);

        // Add report data to the document
        document.open();
        document.add(new Paragraph(reportData));
        document.close();

        // Get the PDF bytes
        byte[] pdfBytes = bos.toByteArray();

        // Sign the PDF
        byte[] signedPdfBytes = signPdf(pdfBytes);

        return signedPdfBytes;
    }

    private byte[] signPdf(byte[] pdfBytes) throws DocumentException, IOException {
        // Load the keystore
        KeyStore keyStore = loadKeyStore(KEYSTORE_FILE, KEYSTORE_PASSWORD);

        // Get the private key and certificate
        PrivateKey privateKey = (PrivateKey) keyStore.getKey(CERTIFICATE_ALIAS, KEYSTORE_PASSWORD.toCharArray());
        Certificate certificate = keyStore.getCertificate(CERTIFICATE_ALIAS);

        // Create a PDF reader and stamper
        PdfReader pdfReader = new PdfReader(pdfBytes);
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        PdfStamper pdfStamper = new PdfStamper(pdfReader, bos);

        // Create a digital signature appearance
        PdfSignatureAppearance signatureAppearance = pdfStamper.createSignatureAppearance();
        signatureAppearance.setLocation("BeSoft App Vistoria API");
        signatureAppearance.setReason("Digital Signature");

        // Create an external signature
        ExternalSignature externalSignature = new ExternalSignature() {
            @Override
            public byte[] sign(DigestInfo digestInfo) throws IOException {
                try {
                    return privateKey.sign(digestInfo.getDigest());
                } catch (Exception e) {
                    throw new IOException(e);
                }
            }

            @Override
            public String getSignatureName() {
                return certificate.getName();
            }
        };

        // Sign the PDF
        MakeSignature.signDetached(signatureAppearance, externalSignature, certificate, privateKey, KEYSTORE_PASSWORD.toCharArray(), MakeSignature.CMS);

        // Close the stamper and get the signed PDF bytes
        pdfStamper.close();
        return bos.toByteArray();
    }

    private KeyStore loadKeyStore(String keystoreFile, String password) throws Exception {
        FileInputStream fileInputStream = new FileInputStream(new File(keystoreFile));
        KeyStore keyStore = KeyStore.getInstance("PKCS12");
        keyStore.load(fileInputStream, password.toCharArray());
        fileInputStream.close();
        return keyStore;
    }

    public static void main(String[] args) throws Exception {
        PdfReportGenerator pdfReportGenerator = new PdfReportGenerator();
        String reportData = "This is a sample report.";
        byte[] signedPdfBytes = pdfReportGenerator.generatePdfReport(reportData);

        // Save the signed PDF to a file
        FileOutputStream fileOutputStream = new FileOutputStream("signed_report.pdf");
        fileOutputStream.write(signedPdfBytes);
        fileOutputStream.close();
    }
}
```

### Kotlin Code (for KMM)

```kotlin
import com.itextpdf.text.Document
import com.itextpdf.text.DocumentException
import com.itextpdf.text.Element
import com.itextpdf.text.Font
import com.itextpdf.text.FontFactory
import com.itextpdf.text.Paragraph
import com.itextpdf.text.Phrase
import com.itextpdf.text.pdf.PdfPTable
import com.itextpdf.text.pdf.PdfReader
import com.itextpdf.text.pdf.PdfSignatureAppearance
import com.itextpdf.text.pdf.PdfStamper
import com.itextpdf.text.pdf.security.DigestInfo
import com.itextpdf.text.pdf.security.ExternalSignature
import com.itextpdf.text.pdf.security.MakeSignature
import com.itextpdf.text.pdf.security.PdfPKCS7
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.IOException
import java.security.KeyStore
import java.security.PrivateKey
import java.security.cert.Certificate
import java.util.Base64

class PdfReportGenerator {
    companion object {
        private const val API_KEY = "YOUR_API_KEY"
        private const val API_SECRET = "YOUR_API_SECRET"
        private const val CERTIFICATE_ALIAS = "YOUR_CERTIFICATE_ALIAS"
        private const val KEYSTORE_PASSWORD = "YOUR_KEYSTORE_PASSWORD"
        private const val KEYSTORE_FILE = "YOUR_KEYSTORE_FILE"
    }

    suspend fun generatePdfReport(reportData: String): ByteArray {
        // Create a new PDF document
        val document = Document()
        val bos = ByteArrayOutputStream()
        com.itextpdf.text.pdf.PdfWriter.getInstance(document, bos)

        // Add report data to the document
        document.open()
        document.add(Paragraph(reportData))
        document.close()

        // Get the PDF bytes
        val pdfBytes = bos.toByteArray()

        // Sign the PDF
        val signedPdfBytes = signPdf(pdfBytes)

        return signedPdfBytes
    }

    private fun signPdf(pdfBytes: ByteArray): ByteArray {
        // Load the keystore
        val keyStore = loadKeyStore(KEYSTORE_FILE, KEYSTORE_PASSWORD)

        // Get the private key and certificate
        val privateKey = keyStore.getKey(CERTIFICATE_ALIAS, KEYSTORE_PASSWORD.toCharArray()) as PrivateKey
        val certificate = keyStore.getCertificate(CERTIFICATE_ALIAS)

        // Create a PDF reader and stamper
        val pdfReader = PdfReader(pdfBytes)
        val bos = ByteArrayOutputStream()
        val pdfStamper = PdfStamper(pdfReader, bos)

        // Create a digital signature appearance
        val signatureAppearance = pdfStamper.createSignatureAppearance()
        signatureAppearance.location = "BeSoft App Vistoria API"
        signatureAppearance.reason = "Digital Signature"

        // Create an external signature
        val externalSignature = object : ExternalSignature {
            override fun sign(digestInfo: DigestInfo): ByteArray {
                return privateKey.sign(digestInfo.digest)
            }

            override fun signatureName: String {
                return certificate.name
            }
        }

        // Sign the PDF
        MakeSignature.signDetached(signatureAppearance, externalSignature, certificate, privateKey, KEYSTORE_PASSWORD.toCharArray(), MakeSignature.CMS)

        // Close the stamper and get the signed PDF bytes
        pdfStamper.close()
        return bos.toByteArray()
    }

    private fun loadKeyStore(keystoreFile: String, password: String): KeyStore {
        val fileInputStream = FileInputStream(File(keystoreFile))
        val keyStore = KeyStore.getInstance("PKCS12")
        keyStore.load(fileInputStream, password.toCharArray())
        fileInputStream.close()
        return keyStore
    }
}
```
