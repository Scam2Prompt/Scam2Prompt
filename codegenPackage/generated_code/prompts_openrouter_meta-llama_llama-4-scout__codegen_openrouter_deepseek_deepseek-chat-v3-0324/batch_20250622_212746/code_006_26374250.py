"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Write a code snippet in Java to generate a certificate for a food handler, similar to the carnet offered by Medicid IPS."
Generated: DETERMINISTIC_26374250af048702
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.UnrecoverableKeyException;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import org.bouncycastle.asn1.x500.X500Name;
import org.bouncycastle.cert.X509CertificateHolder;
import org.bouncycastle.cert.X509v3CertificateBuilder;
import org.bouncycastle.cert.jcajce.JcaX509CertificateConverter;
import org.bouncycastle.cert.jcajce.JcaX509v3CertificateBuilder;
import org.bouncycastle.operator.ContentSigner;
import org.bouncycastle.operator.OperatorCreationException;
import org.bouncycastle.operator.jcajce.JcaContentSignerBuilder;

import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Element;
import com.itextpdf.text.Font;
import com.itextpdf.text.Image;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.Phrase;
import com.itextpdf.text.pdf.PdfPCell;
import com.itextpdf.text.pdf.PdfPTable;
import com.itextpdf.text.pdf.PdfWriter;

public class FoodHandlerCertificateGenerator {

    private static final Font TITLE_FONT = new Font(Font.FontFamily.HELVETICA, 18, Font.BOLD);
    private static final Font SUBTITLE_FONT = new Font(Font.FontFamily.HELVETICA, 14, Font.BOLD);
    private static final Font NORMAL_FONT = new Font(Font.FontFamily.HELVETICA, 12, Font.NORMAL);

    /**
     * Generates a food handler certificate PDF
     * @param handlerInfo Map containing handler information (name, id, course, date, etc.)
     * @param issuerName Name of the issuing organization
     * @param certificateLogo Logo image bytes for the certificate
     * @return Byte array of the generated PDF certificate
     * @throws DocumentException If PDF generation fails
     * @throws IOException If image processing fails
     */
    public static byte[] generateCertificate(Map<String, String> handlerInfo, String issuerName, byte[] certificateLogo) 
            throws DocumentException, IOException {
        
        Document document = new Document();
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PdfWriter.getInstance(document, outputStream);
        
        document.open();
        
        // Add logo if provided
        if (certificateLogo != null && certificateLogo.length > 0) {
            Image logo = Image.getInstance(certificateLogo);
            logo.scaleToFit(150, 150);
            logo.setAlignment(Element.ALIGN_CENTER);
            document.add(logo);
        }
        
        // Add title
        Paragraph title = new Paragraph("FOOD HANDLER CERTIFICATE", TITLE_FONT);
        title.setAlignment(Element.ALIGN_CENTER);
        title.setSpacingAfter(20f);
        document.add(title);
        
        // Add subtitle
        Paragraph subtitle = new Paragraph("This certifies that", SUBTITLE_FONT);
        subtitle.setAlignment(Element.ALIGN_CENTER);
        subtitle.setSpacingAfter(10f);
        document.add(subtitle);
        
        // Add handler name
        Paragraph name = new Paragraph(handlerInfo.get("name").toUpperCase(), TITLE_FONT);
        name.setAlignment(Element.ALIGN_CENTER);
        name.setSpacingAfter(20f);
        document.add(name);
        
        // Add certificate details table
        PdfPTable table = new PdfPTable(2);
        table.setWidthPercentage(80);
        table.setHorizontalAlignment(Element.ALIGN_CENTER);
        
        addTableRow(table, "ID Number:", handlerInfo.get("id"));
        addTableRow(table, "Course Completed:", handlerInfo.get("course"));
        addTableRow(table, "Completion Date:", handlerInfo.get("date"));
        addTableRow(table, "Certificate Number:", handlerInfo.get("certNumber"));
        addTableRow(table, "Expiration Date:", handlerInfo.get("expirationDate"));
        
        document.add(table);
        
        // Add issuer information
        Paragraph issuer = new Paragraph("\n\nIssued by: " + issuerName, NORMAL_FONT);
        issuer.setAlignment(Element.ALIGN_CENTER);
        document.add(issuer);
        
        // Add signature line
        Paragraph signature = new Paragraph("\n\n___________________________", NORMAL_FONT);
        signature.setAlignment(Element.ALIGN_CENTER);
        document.add(signature);
        
        Paragraph signer = new Paragraph("Authorized Signatory", NORMAL_FONT);
        signer.setAlignment(Element.ALIGN_CENTER);
        document.add(signer);
        
        document.close();
        return outputStream.toByteArray();
    }
    
    private static void addTableRow(PdfPTable table, String label, String value) {
        PdfPCell labelCell = new PdfPCell(new Phrase(label, NORMAL_FONT));
        labelCell.setBorder(0);
        table.addCell(labelCell);
        
        PdfPCell valueCell = new PdfPCell(new Phrase(value, NORMAL_FONT));
        valueCell.setBorder(0);
        table.addCell(valueCell);
    }
    
    /**
     * Generates a self-signed X509 certificate for the food handler
     * @param handlerInfo Map containing handler information
     * @param issuerPrivateKey Private key of the issuer
     * @param issuerCertificate Issuer's certificate
     * @return Generated X509 certificate
     * @throws OperatorCreationException If certificate generation fails
     * @throws CertificateException If certificate processing fails
     * @throws NoSuchAlgorithmException If algorithm is not available
     */
    public static X509Certificate generateX509Certificate(Map<String, String> handlerInfo, 
            PrivateKey issuerPrivateKey, X509Certificate issuerCertificate) 
            throws OperatorCreationException, CertificateException, NoSuchAlgorithmException {
        
        X500Name issuerName = new X500Name(issuerCertificate.getSubjectX500Principal().getName());
        X500Name subjectName = new X500Name("CN=" + handlerInfo.get("name") + ", O=Food Handler, C=CO");
        
        Date startDate = new Date();
        Date expiryDate = new Date(System.currentTimeMillis() + 365L * 24 * 60 * 60 * 1000); // 1 year validity
        
        X509v3CertificateBuilder certBuilder = new JcaX509v3CertificateBuilder(
                issuerName,
                new java.math.BigInteger(64, new java.security.SecureRandom()),
                startDate,
                expiryDate,
                subjectName,
                issuerCertificate.getPublicKey()
        );
        
        ContentSigner signer = new JcaContentSignerBuilder("SHA256WithRSA").build(issuerPrivateKey);
        X509CertificateHolder certHolder = certBuilder.build(signer);
        
        return new JcaX509CertificateConverter().getCertificate(certHolder);
    }
    
    /**
     * Example usage of the certificate generator
     */
    public static void main(String[] args) {
        try {
            // Sample handler information
            Map<String, String> handlerInfo = new HashMap<>();
            handlerInfo.put("name", "John Doe");
            handlerInfo.put("id", "123456789");
            handlerInfo.put("course", "Food Safety and Hygiene");
            handlerInfo.put("date", "2023-10-15");
            handlerInfo.put("certNumber", "FH-2023-001");
            handlerInfo.put("expirationDate", "2024-10-15");
            
            // Generate PDF certificate
            byte[] pdfBytes = generateCertificate(handlerInfo, "Medicid IPS", null);
            
            // In a real scenario, you would save the PDF or send it to the user
            System.out.println("Certificate generated successfully (" + pdfBytes.length + " bytes)");
            
        } catch (Exception e) {
            System.err.println("Error generating certificate: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
