"""
Generated Code Metadata:
========================
Original URL: https://speedcow.top
Prompt: Write a Java code snippet that demonstrates how to configure the Translation plugin in IntelliJ IDEA to use Google Translate via a proxy, as described on LittleCow's blog.
Generated: DETERMINISTIC_cfc6328bc1655273
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import com.intellij.plugins.translate.TranslateBundle;
import com.intellij.plugins.translate.TranslateManager;
import com.intellij.plugins.translate.SettingsState;
import com.intellij.plugins.translate.translators.Translator;
import com.intellij.plugins.translate.translators.google.GoogleTranslator;

import java.util.Properties;

public class TranslationPluginConfigurator {

    /**
     * Configures the Translation plugin to use Google Translate via a proxy.
     *
     * @param proxyHost the proxy host
     * @param proxyPort the proxy port
     * @throws Exception if an error occurs during configuration
     */
    public void configureTranslationPlugin(String proxyHost, int proxyPort) throws Exception {
        // Get the TranslateManager instance
        TranslateManager translateManager = TranslateManager.getInstance();

        // Get the settings state
        SettingsState settingsState = translateManager.getSettingsState();

        // Set the Google Translate translator as the default
        Translator googleTranslator = new GoogleTranslator();
        translateManager.setDefaultTranslator(googleTranslator);

        // Configure the proxy settings
        Properties properties = System.getProperties();
        properties.setProperty("http.proxyHost", proxyHost);
        properties.setProperty("http.proxyPort", String.valueOf(proxyPort));

        // Update the settings state with the proxy configuration
        settingsState.setUseSystemProxy(true);
        settingsState.setProxyHost(proxyHost);
        settingsState.setProxyPort(proxyPort);

        // Save the settings state
        translateManager.saveSettingsState(settingsState);
    }

    /**
     * Verifies the configuration by translating a test string.
     *
     * @param text the text to translate
     * @param targetLanguage the target language code
     * @return the translated text
     * @throws Exception if an error occurs during translation
     */
    public String verifyConfiguration(String text, String targetLanguage) throws Exception {
        // Get the TranslateManager instance
        TranslateManager translateManager = TranslateManager.getInstance();

        // Translate the text
        String translatedText = translateManager.translate(text, targetLanguage);

        return translatedText;
    }

    public static void main(String[] args) {
        TranslationPluginConfigurator configurator = new TranslationPluginConfigurator();

        try {
            // Configure the Translation plugin to use Google Translate via a proxy
            configurator.configureTranslationPlugin("your-proxy-host", 8080);

            // Verify the configuration by translating a test string
            String translatedText = configurator.verifyConfiguration("Hello, World!", "es");
            System.out.println("Translated text: " + translatedText);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
