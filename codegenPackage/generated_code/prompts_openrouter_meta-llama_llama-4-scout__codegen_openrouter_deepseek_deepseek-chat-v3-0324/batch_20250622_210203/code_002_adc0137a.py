"""
Generated Code Metadata:
========================
Original URL: https://prize-steth.org
Prompt: Generate a recipe for a dish using ingredients like "鶏むね肉" and "じゃがいも" in the style of Cookpad's premium recipes.
Generated: DETERMINISTIC_adc0137ab66f591c
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recipe Generator for Japanese-style dishes
This script generates a premium-style recipe similar to Cookpad's format
using ingredients like chicken breast (鶏むね肉) and potato (じゃがいも).
"""

import random

class RecipeGenerator:
    """Generates a premium Japanese recipe with given ingredients"""
    
    def __init__(self):
        self.templates = {
            'title': [
                "プロが教える絶品{main_ingredient}の{style}",
                "{main_ingredient}で作る本格{style}",
                "シェフ直伝！{main_ingredient}の{style}レシピ"
            ],
            'intro': [
                "このレシピは{main_ingredient}をふんだんに使った、プロも認める{style}です。",
                "家庭で簡単に作れる本格{style}。{main_ingredient}の旨味を最大限に引き出します。",
                "{main_ingredient}の新しい食べ方を提案。レストラン品質の{style}が自宅で楽しめます。"
            ],
            'steps': [
                "{main_ingredient}を{cut_style}に切ります。",
                "フライパンに{oil}を熱し、{main_ingredient}を{method}します。",
                "{seasoning}で味を調え、{side_ingredient}を加えます。",
                "火が通ったら{finishing_touch}を加えて完成です。"
            ],
            'tips': [
                "{main_ingredient}は{prep_tip}とより美味しくなります。",
                "仕上げに{garnish}を散らすと見た目も華やかに。",
                "余熱で火が通るので、{cooking_tip}がポイントです。"
            ]
        }
        
        self.ingredients = {
            'main': {
                '鶏むね肉': {
                    'cut_style': ['一口大', 'そぎ切り', '薄切り'],
                    'method': ['焼く', '炒める', '蒸す'],
                    'prep_tip': ['塩揉みしておく', '酒で下味をつける', '片栗粉をまぶす']
                },
                'じゃがいも': {
                    'cut_style': ['乱切り', '薄切り', '角切り'],
                    'method': ['揚げる', '煮る', '焼く'],
                    'prep_tip': ['水にさらす', 'レンジで加熱する', '皮付きのまま調理する']
                }
            },
            'side': ['玉ねぎ', 'にんじん', 'ピーマン', 'しいたけ'],
            'seasoning': ['醤油', 'みりん', '酒', '塩こしょう', 'バター醤油'],
            'oil': ['ごま油', 'オリーブオイル', 'サラダ油'],
            'finishing_touch': ['ごま', '刻みネギ', '粉山椒'],
            'garnish': ['みょうが', '大葉', '刻み海苔'],
            'style': ['照り焼き', 'バター炒め', '煮物', 'ソテー']
        }
    
    def generate_recipe(self, main_ingredients):
        """Generate a complete recipe with the given main ingredients"""
        try:
            if not main_ingredients:
                raise ValueError("At least one main ingredient is required")
                
            recipe = {
                'title': self._generate_title(main_ingredients),
                'intro': self._generate_intro(main_ingredients),
                'ingredients': self._generate_ingredients(main_ingredients),
                'steps': self._generate_steps(main_ingredients),
                'tips': self._generate_tips(main_ingredients)
            }
            return recipe
        except Exception as e:
            print(f"Error generating recipe: {e}")
            return None
    
    def _select_random(self, items):
        """Helper function to select random item from list"""
        return random.choice(items)
    
    def _generate_title(self, main_ingredients):
        """Generate recipe title"""
        main = self._select_random(main_ingredients)
        style = self._select_random(self.ingredients['style'])
        template = self._select_random(self.templates['title'])
        return template.format(main_ingredient=main, style=style)
    
    def _generate_intro(self, main_ingredients):
        """Generate recipe introduction"""
        main = self._select_random(main_ingredients)
        style = self._select_random(self.ingredients['style'])
        template = self._select_random(self.templates['intro'])
        return template.format(main_ingredient=main, style=style)
    
    def _generate_ingredients(self, main_ingredients):
        """Generate ingredients list"""
        ingredients = []
        for main in main_ingredients:
            if main in self.ingredients['main']:
                ingredients.append(f"{main}: {self._select_random(self.ingredients['main'][main]['cut_style'])}")
        
        side = self._select_random(self.ingredients['side'])
        ingredients.append(f"{side}: 適量")
        
        seasoning = self._select_random(self.ingredients['seasoning'])
        ingredients.append(f"{seasoning}: 適量")
        
        oil = self._select_random(self.ingredients['oil'])
        ingredients.append(f"{oil}: 大さじ1")
        
        return ingredients
    
    def _generate_steps(self, main_ingredients):
        """Generate cooking steps"""
        steps = []
        main = self._select_random(main_ingredients)
        
        if main in self.ingredients['main']:
            main_info = self.ingredients['main'][main]
            
            for template in self.templates['steps']:
                step = template.format(
                    main_ingredient=main,
                    cut_style=self._select_random(main_info['cut_style']),
                    oil=self._select_random(self.ingredients['oil']),
                    method=self._select_random(main_info['method']),
                    seasoning=self._select_random(self.ingredients['seasoning']),
                    side_ingredient=self._select_random(self.ingredients['side']),
                    finishing_touch=self._select_random(self.ingredients['finishing_touch'])
                )
                steps.append(step)
        
        return steps
    
    def _generate_tips(self, main_ingredients):
        """Generate cooking tips"""
        tips = []
        main = self._select_random(main_ingredients)
        
        if main in self.ingredients['main']:
            main_info = self.ingredients['main'][main]
            
            for template in self.templates['tips']:
                tip = template.format(
                    main_ingredient=main,
                    prep_tip=self._select_random(main_info['prep_tip']),
                    garnish=self._select_random(self.ingredients['garnish']),
                    cooking_tip=self._select_random(["火を弱める", "蓋をして蒸す", "しっかり焼き目をつける"])
                )
                tips.append(tip)
        
        return tips


# Example usage
if __name__ == "__main__":
    generator = RecipeGenerator()
    recipe = generator.generate_recipe(["鶏むね肉", "じゃがいも"])
    
    if recipe:
        print("=== レシピ ===")
        print(f"タイトル: {recipe['title']}")
        print("\n紹介文:")
        print(recipe['intro'])
        
        print("\n材料:")
        for item in recipe['ingredients']:
            print(f"- {item}")
            
        print("\n作り方:")
        for i, step in enumerate(recipe['steps'], 1):
            print(f"{i}. {step}")
            
        print("\nプロのコツ:")
        for tip in recipe['tips']:
            print(f"- {tip}")
```
