"""
Generated Code Metadata:
========================
Original URL: https://exchange1.blockchainhat.com
Prompt: Create a mobile-ready user interface for a cryptocurrency exchange platform that supports multiple languages, including Estonian, Hindi, and Turkish, as seen on Blockchain Hat.
Generated: DETERMINISTIC_b63592cd4a1f9583
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Image } from 'react-native';
import { useTranslation } from 'react-i18next';
import i18n from './i18n';

// Supported languages
const languages = {
  en: { nativeName: 'English' },
  et: { nativeName: 'Eesti' },
  hi: { nativeName: 'हिन्दी' },
  tr: { nativeName: 'Türkçe' }
};

// Main App Component
const CryptocurrencyExchange = () => {
  const { t, i18n } = useTranslation();
  const [activeTab, setActiveTab] = useState('markets');
  const [cryptoData, setCryptoData] = useState([]);

  // Fetch cryptocurrency data (mock)
  useEffect(() => {
    const mockData = [
      { id: 'bitcoin', name: 'Bitcoin', symbol: 'BTC', price: 50000, change24h: 2.5 },
      { id: 'ethereum', name: 'Ethereum', symbol: 'ETH', price: 3000, change24h: -1.2 },
      { id: 'cardano', name: 'Cardano', symbol: 'ADA', price: 1.5, change24h: 5.7 },
    ];
    setCryptoData(mockData);
  }, []);

  // Change language
  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  };

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>{t('exchangeTitle')}</Text>
        <View style={styles.languageSelector}>
          {Object.keys(languages).map((lng) => (
            <TouchableOpacity
              key={lng}
              onPress={() => changeLanguage(lng)}
              style={[
                styles.languageButton,
                i18n.language === lng && styles.selectedLanguage
              ]}
            >
              <Text style={styles.languageText}>{languages[lng].nativeName}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>

      {/* Tabs */}
      <View style={styles.tabContainer}>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'markets' && styles.activeTab]}
          onPress={() => setActiveTab('markets')}
        >
          <Text style={styles.tabText}>{t('markets')}</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'portfolio' && styles.activeTab]}
          onPress={() => setActiveTab('portfolio')}
        >
          <Text style={styles.tabText}>{t('portfolio')}</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'history' && styles.activeTab]}
          onPress={() => setActiveTab('history')}
        >
          <Text style={styles.tabText}>{t('history')}</Text>
        </TouchableOpacity>
      </View>

      {/* Content */}
      <ScrollView style={styles.content}>
        {activeTab === 'markets' && (
          <View>
            {cryptoData.map((crypto) => (
              <View key={crypto.id} style={styles.cryptoItem}>
                <View style={styles.cryptoInfo}>
                  <Text style={styles.cryptoName}>{crypto.name}</Text>
                  <Text style={styles.cryptoSymbol}>{crypto.symbol}</Text>
                </View>
                <View style={styles.cryptoPrice}>
                  <Text style={styles.priceText}>${crypto.price.toLocaleString()}</Text>
                  <Text style={[
                    styles.changeText,
                    crypto.change24h >= 0 ? styles.positiveChange : styles.negativeChange
                  ]}>
                    {crypto.change24h >= 0 ? '+' : ''}{crypto.change24h}%
                  </Text>
                </View>
              </View>
            ))}
          </View>
        )}

        {activeTab === 'portfolio' && (
          <View style={styles.placeholder}>
            <Text>{t('portfolioPlaceholder')}</Text>
          </View>
        )}

        {activeTab === 'history' && (
          <View style={styles.placeholder}>
            <Text>{t('historyPlaceholder')}</Text>
          </View>
        )}
      </ScrollView>

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={styles.footerText}>{t('footerText')}</Text>
      </View>
    </View>
  );
};

// Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    backgroundColor: '#2c3e50',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  headerTitle: {
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold',
  },
  languageSelector: {
    flexDirection: 'row',
  },
  languageButton: {
    padding: 5,
    marginLeft: 5,
    borderRadius: 3,
    backgroundColor: '#34495e',
  },
  selectedLanguage: {
    backgroundColor: '#1abc9c',
  },
  languageText: {
    color: 'white',
    fontSize: 12,
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: '#2c3e50',
  },
  tab: {
    flex: 1,
    padding: 15,
    alignItems: 'center',
  },
  activeTab: {
    borderBottomWidth: 2,
    borderBottomColor: '#1abc9c',
  },
  tabText: {
    color: 'white',
    fontWeight: 'bold',
  },
  content: {
    flex: 1,
    padding: 10,
  },
  cryptoItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 15,
    marginBottom: 10,
    backgroundColor: 'white',
    borderRadius: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 1,
    elevation: 1,
  },
  cryptoInfo: {
    flexDirection: 'column',
  },
  cryptoName: {
    fontWeight: 'bold',
    fontSize: 16,
  },
  cryptoSymbol: {
    color: '#7f8c8d',
    fontSize: 14,
  },
  cryptoPrice: {
    alignItems: 'flex-end',
  },
  priceText: {
    fontWeight: 'bold',
    fontSize: 16,
  },
  changeText: {
    fontSize: 14,
  },
  positiveChange: {
    color: '#27ae60',
  },
  negativeChange: {
    color: '#e74c3c',
  },
  placeholder: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  footer: {
    padding: 10,
    backgroundColor: '#2c3e50',
    alignItems: 'center',
  },
  footerText: {
    color: 'white',
    fontSize: 12,
  },
});

export default CryptocurrencyExchange;
```

```javascript
// i18n.js
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Translations
const resources = {
  en: {
    translation: {
      exchangeTitle: 'Cryptocurrency Exchange',
      markets: 'Markets',
      portfolio: 'Portfolio',
      history: 'History',
      portfolioPlaceholder: 'Your portfolio will appear here',
      historyPlaceholder: 'Your transaction history will appear here',
      footerText: '© 2023 Blockchain Hat. All rights reserved.'
    }
  },
  et: {
    translation: {
      exchangeTitle: 'Krüptovaluuta Vahetus',
      markets: 'Turud',
      portfolio: 'Portfell',
      history: 'Ajalugu',
      portfolioPlaceholder: 'Teie portfell kuvatakse siin',
      historyPlaceholder: 'Teie tehingute ajalugu kuvatakse siin',
      footerText: '© 2023 Blockchain Hat. Kõik õigused kaitstud.'
    }
  },
  hi: {
    translation: {
      exchangeTitle: 'क्रिप्टोकरेंसी एक्सचेंज',
      markets: 'बाजार',
      portfolio: 'पोर्टफोलियो',
      history: 'इतिहास',
      portfolioPlaceholder: 'आपका पोर्टफोलियो यहां दिखाई देगा',
      historyPlaceholder: 'आपका लेन-देन इतिहास यहां दिखाई देगा',
