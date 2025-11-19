"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://speedcow.top
Prompt: Write a Java code snippet that demonstrates how to configure the Translation plugin in IntelliJ IDEA to use Google Translate via a proxy, as described on LittleCow's blog.
Generated: DETERMINISTIC_cfc6328bc1655273
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import com.intellij.openapi.components.ServiceManager;
import com.intellij.openapi.project.Project;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import cn.yiiguxing.plugin.translate.settings.TranslatorSettings;
import cn.yiiguxing.plugin.translate.trans.google.GoogleTranslator;

import java.net.InetSocketAddress;
import java.net.Proxy;

/**
 * A utility class to configure the Translation plugin in IntelliJ IDEA.
 * This demonstrates how to set up Google Translate via a proxy.
 */
public class TranslationPluginConfigurator {

    /**
     * Configures the Translation plugin to use Google Translate with the specified proxy settings.
     *
     * @param project          The current IntelliJ IDEA project instance.
     * @param proxyHost        The proxy host address.
     * @param proxyPort        The proxy port number.
     * @param proxyType        The proxy type (e.g., Proxy.Type.HTTP or Proxy.Type.SOCKS).
     */
    public static void configureGoogleTranslateWithProxy(@Nullable Project project,
                                                         @NotNull String proxyHost,
                                                         int proxyPort,
                                                         @NotNull Proxy.Type proxyType) {
        try {
            // Retrieve the translator settings
            TranslatorSettings translatorSettings = ServiceManager.getService(TranslatorSettings.class);
            if (translatorSettings == null) {
                throw new IllegalStateException("TranslatorSettings service not found. Ensure the Translation plugin is installed.");
            }

            // Set Google Translate as the translator
            translatorSettings.setTranslator(new GoogleTranslator());

            // Configure proxy settings
            Proxy proxy = new Proxy(proxyType, new InetSocketAddress(proxyHost, proxyPort));
            GoogleTranslator googleTranslator = (GoogleTranslator) translatorSettings.getTranslator();
            googleTranslator.setProxy(proxy);

            System.out.println("Translation plugin configured successfully to use Google Translate with proxy.");
        } catch (Exception ex) {
            // Log or handle errors in a production-ready system.
            System.err.println("Failed to configure Translation plugin: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        configureGoogleTranslateWithProxy(null, "proxy.example.com", 8080, Proxy.Type.HTTP);
    }
}
```

Note:
- Ensure that the Translation plugin dependency (`cn.yiiguxing.plugin.translate`) is added to your project.
- Replace `proxy.example.com` and `8080` with the actual proxy settings in your environment.
