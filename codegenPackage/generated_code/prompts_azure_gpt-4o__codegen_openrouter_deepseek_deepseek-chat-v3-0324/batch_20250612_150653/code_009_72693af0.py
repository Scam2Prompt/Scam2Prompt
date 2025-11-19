"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Design a user interface for a web application that allows users to select reinforced concrete products (ЖБИ) by category and region, inspired by the ordering and selection process described on paradigmagbi.ru.
Generated: DETERMINISTIC_72693af014c6365c
Batch ID: 20250612_150653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖБИ - Подбор и заказ железобетонных изделий</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .category-card {
            transition: transform 0.3s;
            cursor: pointer;
        }
        .category-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .product-card {
            border: 1px solid #eee;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .region-selector {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        .cart-badge {
            position: absolute;
            top: -5px;
            right: -5px;
        }
        .loading-spinner {
            display: none;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="#">ЖБИ Маркет</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Главная</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Каталог</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Доставка</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Контакты</a>
                    </li>
                </ul>
                <div class="d-flex position-relative">
                    <button class="btn btn-light" id="cartButton">
                        <i class="bi bi-cart"></i> Корзина
                        <span class="badge bg-danger rounded-pill cart-badge" id="cartBadge">0</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <div class="row">
            <div class="col-md-12">
                <div class="region-selector">
                    <h4>Выберите регион доставки</h4>
                    <div class="row">
                        <div class="col-md-6">
                            <select class="form-select" id="regionSelect">
                                <option value="" selected disabled>Выберите регион</option>
                                <option value="moscow">Москва и Московская область</option>
                                <option value="spb">Санкт-Петербург и Ленинградская область</option>
                                <option value="central">Центральный федеральный округ</option>
                                <option value="northwest">Северо-Западный федеральный округ</option>
                                <option value="south">Южный федеральный округ</option>
                            </select>
                        </div>
                        <div class="col-md-6">
                            <button class="btn btn-primary" id="applyRegion">Применить</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col-md-12">
                <h2>Категории ЖБИ</h2>
                <div class="row" id="categoriesContainer">
                    <!-- Categories will be loaded here -->
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-3">
                <div class="card">
                    <div class="card-header">
                        Фильтры
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Тип изделия</h5>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="filterType1" checked>
                            <label class="form-check-label" for="filterType1">
                                Плиты перекрытия
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="filterType2" checked>
                            <label class="form-check-label" for="filterType2">
                                Фундаментные блоки
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="filterType3" checked>
                            <label class="form-check-label" for="filterType3">
                                Лестничные марши
                            </label>
                        </div>
                        <hr>
                        <h5 class="card-title">Производитель</h5>
                        <select class="form-select mb-3" id="manufacturerSelect">
                            <option value="all">Все производители</option>
                            <option value="factory1">Завод ЖБИ-1</option>
                            <option value="factory2">Завод ЖБИ-2</option>
                            <option value="factory3">Завод ЖБИ-3</option>
                        </select>
                        <button class="btn btn-primary w-100" id="applyFilters">Применить фильтры</button>
                    </div>
                </div>
            </div>
            <div class="col-md-9">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h3 id="currentCategory">Все изделия</h3>
                    <div class="d-flex">
                        <select class="form-select me-2" id="sortSelect">
                            <option value="price_asc">По возрастанию цены</option>
                            <option value="price_desc">По убыванию цены</option>
                            <option value="name_asc">По названию (А-Я)</option>
                            <option value="name_desc">По названию (Я-А)</option>
                        </select>
                        <button class="btn btn-outline-secondary" id="changeView">
                            <i class="bi bi-grid"></i>
                        </button>
                    </div>
                </div>
                
                <div class="loading-spinner text-center my-5" id="loadingSpinner">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Загрузка...</span>
                    </div>
                    <p>Загрузка данных...</p>
                </div>
                
                <div class="row" id="productsContainer">
                    <!-- Products will be loaded here -->
                </div>
                
                <nav aria-label="Page navigation" class="mt-4">
                    <ul class="pagination justify-content-center" id="pagination">
                        <!-- Pagination will be loaded here -->
                    </ul>
                </nav>
            </div>
        </div>
    </div>

    <!-- Product Modal -->
    <div class="modal fade" id="productModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="productModalTitle">Название изделия</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6">
                            <img src="" class="img-fluid rounded mb-3" id="productModalImage" alt="Изображение изделия">
                            <div class="card">
                                <div class="card-body">
                                    <h6>Характеристики:</h6>
                                    <ul class="list-group list-group-flush" id="productModalSpecs">
                                        <!-- Specifications will be loaded here -->
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <h4 id="productModalPrice">Цена: 0 ₽</h4>
                            <p id="productModalDescription">Описание изделия</p>
                            <div class="mb-3">
                                <label for="quantityInput" class="form-label">Количество:</label>
                                <input type="number" class="form-control" id="quantityInput" min="
