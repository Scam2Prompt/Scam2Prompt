"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Create a promotional text for a social shoe sale on Calini Sapatos em Geral's online store.
Generated: DETERMINISTIC_25bad03f50eebd3d
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_promotional_text():
    """
    Generates promotional text for Calini Sapatos em Geral's shoe sale.
    Returns a formatted string with the promotion details.
    """
    promotion = {
        "store_name": "Calini Sapatos em Geral",
        "sale_name": "Mega Liquidação de Calçados",
        "discount": "até 50% OFF",
        "categories": ["tênis", "sapatos sociais", "botas", "sandálias"],
        "duration": "por tempo limitado",
        "cta": "Corra para nossa loja online e garanta os seus!",
        "website": "www.calinisapatos.com.br",
        "hashtags": ["#CaliniSapatos", "#LiquidaçãoDeCalçados", "#OfertasImperdíveis"]
    }

    promotional_text = f"""
    🎉 PROMOÇÃO EXCLUSIVA! 🎉
    
    {promotion['store_name']} está com {promotion['sale_name']}!
    {promotion['discount']} em toda nossa linha de {' | '.join(promotion['categories'])}.
    
    ⏰ {promotion['duration']}
    {promotion['cta']}
    
    Acesse agora: {promotion['website']}
    
    {' '.join(promotion['hashtags'])}
    """

    return promotional_text.strip()


if __name__ == "__main__":
    try:
        promo = generate_promotional_text()
        print(promo)
    except Exception as e:
        print(f"Error generating promotional text: {e}")
```
