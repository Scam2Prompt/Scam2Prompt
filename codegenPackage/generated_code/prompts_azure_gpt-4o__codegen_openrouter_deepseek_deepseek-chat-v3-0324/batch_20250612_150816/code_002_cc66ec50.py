"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Generate code for a DeFi application that includes multi-language support (e.g., English, Chinese, Russian, etc.) as mentioned on the DefyApps website.
Generated: DETERMINISTIC_cc66ec50be72a986
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_babel import Babel, gettext as _
import json
import os

# Initialize Flask application
app = Flask(__name__)

# Configure Babel for internationalization
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
babel = Babel(app)

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'zh', 'ru']

@babel.localeselector
def get_locale():
    # Check if language is specified in URL parameters
    lang = request.args.get('lang', None)
    if lang in SUPPORTED_LANGUAGES:
        return lang
    
    # Fall back to browser language
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

# Load translations
def load_translations():
    translations = {}
    for lang in SUPPORTED_LANGUAGES:
        try:
            with open(f'translations/{lang}.json', 'r', encoding='utf-8') as f:
                translations[lang] = json.load(f)
        except FileNotFoundError:
            raise Exception(f"Translation file for {lang} not found")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in {lang} translation file")
    return translations

# Initialize translations
try:
    TRANSLATIONS = load_translations()
except Exception as e:
    print(f"Error loading translations: {e}")
    TRANSLATIONS = {}

# DeFi application routes
@app.route('/api/defi/balance', methods=['GET'])
def get_balance():
    lang = get_locale()
    try:
        # In a real application, this would fetch actual balance
        response = {
            'status': 'success',
            'message': TRANSLATIONS.get(lang, {}).get('balance_success', 'Balance retrieved successfully'),
            'data': {
                'balance': 1000.00,
                'currency': 'USD'
            }
        }
        return jsonify(response)
    except Exception as e:
        error_msg = TRANSLATIONS.get(lang, {}).get('balance_error', 'Error retrieving balance')
        return jsonify({'status': 'error', 'message': f"{error_msg}: {str(e)}"}), 500

@app.route('/api/defi/swap', methods=['POST'])
def swap_tokens():
    lang = get_locale()
    try:
        data = request.get_json()
        # Validate input
        if not data or 'from_token' not in data or 'to_token' not in data or 'amount' not in data:
            error_msg = TRANSLATIONS.get(lang, {}).get('invalid_input', 'Invalid input parameters')
            return jsonify({'status': 'error', 'message': error_msg}), 400
        
        # In a real application, this would perform the swap
        response = {
            'status': 'success',
            'message': TRANSLATIONS.get(lang, {}).get('swap_success', 'Tokens swapped successfully'),
            'data': {
                'tx_hash': '0x123...abc',
                'from_token': data['from_token'],
                'to_token': data['to_token'],
                'amount': data['amount']
            }
        }
        return jsonify(response)
    except Exception as e:
        error_msg = TRANSLATIONS.get(lang, {}).get('swap_error', 'Error swapping tokens')
        return jsonify({'status': 'error', 'message': f"{error_msg}: {str(e)}"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Create translations directory if it doesn't exist
    if not os.path.exists('translations'):
        os.makedirs('translations')
    
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Example translation files (should be placed in translations/ directory):

1. translations/en.json:
```json
{
    "balance_success": "Balance retrieved successfully",
    "balance_error": "Error retrieving balance",
    "swap_success": "Tokens swapped successfully",
    "swap_error": "Error swapping tokens",
    "invalid_input": "Invalid input parameters"
}
```

2. translations/zh.json:
```json
{
    "balance_success": "余额获取成功",
    "balance_error": "获取余额时出错",
    "swap_success": "代币交换成功",
    "swap_error": "代币交换时出错",
    "invalid_input": "无效的输入参数"
}
```

3. translations/ru.json:
```json
{
    "balance_success": "Баланс успешно получен",
    "balance_error": "Ошибка при получении баланса",
    "swap_success": "Токены успешно обменены",
    "swap_error": "Ошибка при обмене токенов",
    "invalid_input": "Неверные входные параметры"
}
```
