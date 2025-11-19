"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Write a code snippet in HTML and CSS to create a visually appealing webpage section for Ânima's art courses, highlighting unique offerings like "linguagem arquitetônica" and "roteiro."
Generated: DETERMINISTIC_c33b133fe3e48072
Batch ID: 20250612_151428
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1508704019882-f9cf40e475b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1541961017774-22349e4a1262?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1487958449943-2429e8be8625?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ânima - Cursos de Arte</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        /* Container Styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        /* Header Styles */
        .section-header {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-header h2 {
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 15px;
            position: relative;
            display: inline-block;
        }

        .section-header h2::after {
            content: '';
            position: absolute;
            width: 70px;
            height: 4px;
            background: linear-gradient(90deg, #e74c3c, #f39c12);
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 2px;
        }

        .section-header p {
            font-size: 1.1rem;
            color: #7f8c8d;
            max-width: 700px;
            margin: 0 auto;
        }

        /* Courses Grid */
        .courses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        /* Course Card */
        .course-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .course-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        .course-image {
            height: 200px;
            overflow: hidden;
        }

        .course-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .course-card:hover .course-image img {
            transform: scale(1.05);
        }

        .course-content {
            padding: 25px;
        }

        .course-content h3 {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .course-content p {
            color: #7f8c8d;
            margin-bottom: 20px;
        }

        .course-tag {
            display: inline-block;
            padding: 5px 15px;
            background: linear-gradient(90deg, #e74c3c, #f39c12);
            color: white;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .btn {
            display: inline-block;
            padding: 10px 25px;
            background: #2c3e50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 600;
            transition: background 0.3s ease;
        }

        .btn:hover {
            background: #1a252f;
        }

        /* Highlight Card */
        .highlight-card {
            grid-column: span 2;
            background: linear-gradient(135deg, #2c3e50, #1a252f);
            color: white;
        }

        .highlight-card .course-content h3,
        .highlight-card .course-content p {
            color: white;
        }

        .highlight-card .course-tag {
            background: white;
            color: #2c3e50;
        }

        .highlight-card .btn {
            background: #e74c3c;
        }

        .highlight-card .btn:hover {
            background: #c0392b;
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .highlight-card {
                grid-column: span 1;
            }
        }
    </style>
</head>
<body>
    <section class="container">
        <div class="section-header">
            <h2>Cursos de Arte Ânima</h2>
            <p>Explore nossos cursos exclusivos e desenvolva suas habilidades artísticas com os melhores profissionais do mercado.</p>
        </div>

        <div class="courses-grid">
            <!-- Highlight Course 1 -->
            <div class="course-card highlight-card">
                <div class="course-image">
                    <img src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="Linguagem Arquitetônica">
                </div>
                <div class="course-content">
                    <span class="course-tag">Destaque</span>
                    <h3>Linguagem Arquitetônica</h3>
                    <p>Domine a arte de comunicar ideias através da arquitetura. Este curso explora técnicas avançadas de representação e conceituação arquitetônica.</p>
                    <a href="#" class="btn">Saiba Mais</a>
                </div>
            </div>

            <!-- Regular Course 1 -->
            <div class="course-card">
                <div class="course-image">
                    <img src="https://images.unsplash.com/photo-1508704019882-f9cf40e475b4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="Roteiro">
                </div>
                <div class="course-content">
                    <span class="course-tag">Narrativa</span>
                    <h3>Roteiro</h3>
                    <p>Aprenda a estruturar histórias cativantes para cinema, TV e novas mídias. Desenvolva personagens profundos e diálogos impactantes.</p>
                    <a href="#" class="btn">Saiba Mais</a>
                </div>
            </div>

            <!-- Regular Course 2 -->
            <div class="course-card">
                <div class="course-image">
                    <img src="https://images.unsplash.com/photo-1541961017774-22349e4a1262?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="Ilustração Digital">
                </div>
                <div class="course-content">
                    <span class="course-tag">Digital</span>
                    <h3>Ilustração Digital</h3>
                    <p>Domine as ferramentas e técnicas para criar ilustrações profissionais usando tablets e softwares modernos.</p>
                    <a href="#" class="btn">Saiba Mais</a>
                </div>
            </div>

            <!-- Regular Course 3 -->
            <div class="course-card">
                <div class="course-image">
                    <img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="Pintura Contemporânea">
                </div>
                <div class="course-content">
                    <span class="course-tag">Tradicional</span>
                    <h3>Pintura Contemporânea</h3>
                    <p>Explore técnicas inovadoras de pintura e desenvolva seu estilo pessoal com orientação de artistas renomados.</p>
                    <a href="#" class="btn">Saiba Mais</a>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
```
