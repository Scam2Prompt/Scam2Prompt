"""
Generated Code Metadata:
========================
Original URL: https://astoricrypto.com
Prompt: Create a market analysis report for a cryptocurrency trading group, including daily trade alerts, market insights, and learning resources, similar to those offered by AstoriCrypto.
Generated: DETERMINISTIC_94d96d6d0d05fe06
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import yfinance as yf
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('market_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MarketAnalysisReport:
    """
    Generates a comprehensive cryptocurrency market analysis report.
    Includes trade alerts, market insights, and learning resources.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the MarketAnalysisReport with configuration.
        
        Args:
            config_path: Path to configuration file
        """
        try:
            with open(config_path) as f:
                self.config = json.load(f)
            logger.info("Configuration loaded successfully")
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise
        
        self.crypto_symbols = self.config.get('crypto_symbols', ['BTC-USD', 'ETH-USD'])
        self.email_config = self.config.get('email', {})
        self.news_sources = self.config.get('news_sources', [])
        self.learning_resources = self.config.get('learning_resources', [])
        
    def get_crypto_data(self, days: int = 7) -> pd.DataFrame:
        """
        Fetch cryptocurrency price data for specified symbols.
        
        Args:
            days: Number of days of historical data to fetch
            
        Returns:
            DataFrame containing OHLCV data for specified cryptos
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            data = yf.download(
                self.crypto_symbols,
                start=start_date.strftime('%Y-%m-%d'),
                end=end_date.strftime('%Y-%m-%d'),
                group_by='ticker'
            )
            
            logger.info("Successfully fetched crypto data")
            return data
        except Exception as e:
            logger.error(f"Error fetching crypto data: {e}")
            raise
    
    def generate_technical_analysis(self, data: pd.DataFrame) -> Dict:
        """
        Generate technical analysis indicators for each cryptocurrency.
        
        Args:
            data: DataFrame containing price data
            
        Returns:
            Dictionary containing technical analysis for each crypto
        """
        analysis = {}
        
        for symbol in self.crypto_symbols:
            try:
                symbol_data = data[symbol]
                
                # Calculate simple moving averages
                sma_20 = symbol_data['Close'].rolling(window=20).mean()
                sma_50 = symbol_data['Close'].rolling(window=50).mean()
                
                # Calculate RSI
                delta = symbol_data['Close'].diff()
                gain = delta.where(delta > 0, 0)
                loss = -delta.where(delta < 0, 0)
                avg_gain = gain.rolling(window=14).mean()
                avg_loss = loss.rolling(window=14).mean()
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
                
                analysis[symbol] = {
                    'SMA_20': sma_20.iloc[-1],
                    'SMA_50': sma_50.iloc[-1],
                    'RSI': rsi.iloc[-1],
                    'current_price': symbol_data['Close'].iloc[-1],
                    'support_level': symbol_data['Low'].rolling(window=14).min().iloc[-1],
                    'resistance_level': symbol_data['High'].rolling(window=14).max().iloc[-1]
                }
                
                logger.info(f"Generated technical analysis for {symbol}")
            except Exception as e:
                logger.error(f"Error generating analysis for {symbol}: {e}")
                continue
                
        return analysis
    
    def get_market_news(self) -> List[Dict]:
        """
        Fetch latest cryptocurrency market news from configured sources.
        
        Returns:
            List of news articles with title, source, and summary
        """
        news_items = []
        
        for source in self.news_sources:
            try:
                response = requests.get(source['url'], headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.text, 'html.parser')
                
                articles = soup.find_all(source.get('article_tag', 'article'), 
                                       class_=source.get('article_class', ''))
                
                for article in articles[:5]:  # Limit to 5 articles per source
                    title = article.find(source.get('title_tag', 'h2')).text.strip()
                    link = article.find('a')['href']
                    
                    if not link.startswith('http'):
                        link = source['url'] + link
                    
                    summary_tag = article.find(source.get('summary_tag', 'p'))
                    summary = summary_tag.text.strip() if summary_tag else "No summary available"
                    
                    news_items.append({
                        'title': title,
                        'source': source['name'],
                        'summary': summary,
                        'link': link
                    })
                
                logger.info(f"Fetched news from {source['name']}")
            except Exception as e:
                logger.error(f"Error fetching news from {source['name']}: {e}")
                continue
                
        return news_items
    
    def generate_trade_alerts(self, analysis: Dict) -> List[Dict]:
        """
        Generate trade alerts based on technical analysis.
        
        Args:
            analysis: Technical analysis data
            
        Returns:
            List of trade alerts with recommendations
        """
        alerts = []
        
        for symbol, data in analysis.items():
            try:
                alert = {
                    'symbol': symbol,
                    'current_price': data['current_price'],
                    'recommendation': 'HOLD',
                    'reason': ''
                }
                
                # Generate buy/sell signals based on technical indicators
                if data['RSI'] < 30 and data['current_price'] > data['SMA_20']:
                    alert['recommendation'] = 'BUY'
                    alert['reason'] = 'Oversold condition with price above SMA20'
                elif data['RSI'] > 70 and data['current_price'] < data['SMA_50']:
                    alert['recommendation'] = 'SELL'
                    alert['reason'] = 'Overbought condition with price below SMA50'
                elif data['current_price'] < data['support_level'] * 1.01:
                    alert['recommendation'] = 'BUY'
                    alert['reason'] = 'Approaching support level'
                elif data['current_price'] > data['resistance_level'] * 0.99:
                    alert['recommendation'] = 'SELL'
                    alert['reason'] = 'Approaching resistance level'
                
                alerts.append(alert)
                logger.info(f"Generated trade alert for {symbol}")
            except Exception as e:
                logger.error(f"Error generating trade alert for {symbol}: {e}")
                continue
                
        return alerts
    
    def generate_price_charts(self, data: pd.DataFrame) -> List[str]:
        """
        Generate price charts for each cryptocurrency.
        
        Args:
            data: DataFrame containing price data
            
        Returns:
            List of file paths to saved charts
        """
        chart_paths = []
        
        for symbol in self.crypto_symbols:
            try:
                symbol_data = data[symbol]
                
                plt.figure(figsize=(12, 6))
                plt.plot(symbol_data['Close'], label='Price')
                plt.plot(symbol_data['Close'].rolling(window=20).mean(), label='20-day SMA')
                plt.plot(symbol_data['Close'].rolling(window=50).mean(), label='50-day SMA')
                
                plt.title(f'{symbol} Price Chart')
                plt.xlabel('Date')
                plt.ylabel('Price (USD)')
                plt.legend()
                plt.grid(True)
                
                chart_path = f'{symbol}_chart.png'
                plt.savefig(chart_path)
                plt.close()
                
                chart_paths.append(chart_path)
                logger.info(f"Generated price chart for {symbol}")
            except Exception as e:
                logger.error(f"Error generating chart for {symbol}: {e}")
                continue
                
        return chart_paths
    
    def generate_report_html(self, analysis: Dict, alerts: List[Dict], 
                           news: List[Dict], chart_paths: List[str]) -> str:
        """
        Generate HTML report from analysis components.
        
        Args:
            analysis: Technical analysis data
            alerts: Trade alerts
            news: Market news
            chart_paths: Paths to price charts
            
        Returns:
            HTML string of the complete report
        """
        try:
            # HTML header
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Crypto Market Analysis Report</title>
                <style>
                    body { font-family: Arial, sans-serif; line-height:
