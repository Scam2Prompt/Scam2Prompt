"""
Generated Code Metadata:
========================
Original URL: https://webstarstudio.com
Prompt: "Generate a pricing table for WordPress services in Russian, including costs for CMS, promotion, and support, similar to WebStar Studio's offerings."
Generated: DETERMINISTIC_16d7f1782e94fbf5
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * WordPress Services Pricing Table
 * 
 * Displays a responsive pricing table for WordPress services in Russian.
 * 
 * @package WordPress
 * @subpackage WebStar_Studio_Pricing_Table
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Register shortcode for pricing table
 */
add_shortcode('webstar_pricing_table', 'webstar_pricing_table_shortcode');

function webstar_pricing_table_shortcode() {
    ob_start();
    ?>
    <div class="webstar-pricing-table">
        <style>
            .webstar-pricing-table {
                font-family: 'Arial', sans-serif;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .webstar-pricing-table h2 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .pricing-plans {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }
            .pricing-plan {
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                padding: 30px;
                flex: 1;
                min-width: 250px;
                max-width: 300px;
                transition: transform 0.3s ease;
            }
            .pricing-plan:hover {
                transform: translateY(-10px);
            }
            .plan-name {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 15px;
                text-align: center;
            }
            .plan-price {
                font-size: 36px;
                font-weight: bold;
                color: #3498db;
                text-align: center;
                margin-bottom: 20px;
            }
            .plan-features {
                list-style: none;
                padding: 0;
                margin-bottom: 30px;
            }
            .plan-features li {
                padding: 8px 0;
                border-bottom: 1px solid #eee;
                color: #555;
            }
            .plan-button {
                display: block;
                text-align: center;
                background: #3498db;
                color: white;
                padding: 12px;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
                transition: background 0.3s ease;
            }
            .plan-button:hover {
                background: #2980b9;
            }
            @media (max-width: 768px) {
                .pricing-plans {
                    flex-direction: column;
                    align-items: center;
                }
                .pricing-plan {
                    width: 100%;
                    max-width: 100%;
                }
            }
        </style>

        <h2>Наши услуги и цены</h2>
        
        <div class="pricing-plans">
            <!-- CMS Plan -->
            <div class="pricing-plan">
                <div class="plan-name">Разработка сайта</div>
                <div class="plan-price">от 30 000 ₽</div>
                <ul class="plan-features">
                    <li>Установка WordPress</li>
                    <li>Настройка CMS</li>
                    <li>Адаптивный дизайн</li>
                    <li>5 страниц</li>
                    <li>Базовые плагины</li>
                    <li>Обучение работе с CMS</li>
                </ul>
                <a href="#contact" class="plan-button">Заказать</a>
            </div>
            
            <!-- Promotion Plan -->
            <div class="pricing-plan">
                <div class="plan-name">Продвижение</div>
                <div class="plan-price">от 15 000 ₽/мес</div>
                <ul class="plan-features">
                    <li>SEO оптимизация</li>
                    <li>Контент-маркетинг</li>
                    <li>Настройка рекламы</li>
                    <li>Аналитика</li>
                    <li>Ежемесячные отчеты</li>
                    <li>Поддержка 24/7</li>
                </ul>
                <a href="#contact" class="plan-button">Заказать</a>
            </div>
            
            <!-- Support Plan -->
            <div class="pricing-plan">
                <div class="plan-name">Поддержка</div>
                <div class="plan-price">от 5 000 ₽/мес</div>
                <ul class="plan-features">
                    <li>Техническая поддержка</li>
                    <li>Обновления CMS</li>
                    <li>Резервное копирование</li>
                    <li>Исправление ошибок</li>
                    <li>Консультации</li>
                    <li>Мониторинг сайта</li>
                </ul>
                <a href="#contact" class="plan-button">Заказать</a>
            </div>
        </div>
    </div>
    <?php
    return ob_get_clean();
}

/**
 * Enqueue styles if needed
 */
add_action('wp_enqueue_scripts', 'webstar_pricing_table_styles');
function webstar_pricing_table_styles() {
    wp_register_style('webstar-pricing-table', false);
    wp_enqueue_style('webstar-pricing-table');
}
```
