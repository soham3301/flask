
from flask import Flask, render_template, abort

app = Flask(__name__)

recipes_dict = {
    "1": {
        "id": "1",
        "name": "Butter Chicken",
        "description": "Butter chicken, or murgh makhani, is a world-renowned Indian dish consisting of tender, marinated chicken that is charred or grilled and then simmered in a velvety, spiced tomato-and-butter sauce",
        "ingredients": [
            "Chicken",
            "Yogurt",
            "Ginger Garlic Paste",
            "Kashmiri Red Chilli Powder",
            "Turmeric",
            "Garam Masala",
            "1 tsp Salt",
            "1 tbsp oil",
            "1 tbsp butter or ghee",
            "Some tomatos and cashews"
        ],
        "instructions": [
            "Marinate the Chicken",
            "Sear the Chicken",
            "Build the Gravy Base",
            "Simmer the tomatos and Cashews",
            "Blend until Silky",
            "Combine and Finish"
        ],
        "category": "Indian Curry",
    },
    "2": {
        "id": "2",
        "name": "Shawarma",
        "description": "Shawarma is a popular Middle Eastern street food consisting of thinly sliced, marinated meat stacked into an inverted cone and slow-roasted on a vertical rotating spit",
        "ingredients": [
            "Chicken",
            "Olive Oil",
            "Lemon Juice",
            "Garlic",
            "1 tbsp ground Cumin",
            "1 tbsp ground Coriander",
            "1 tbsp ground Cardamon",
            "2 tsp Paprika",
            "2 tsp Salt",
            "Some Black Papper"
        ],
        "instructions": [
            "Prepare the Marinade",
            "Marinate the Chicken",
            "Cock the Chicken",
            "Make the Garlic Yogurt Sauce",
            "Assemble the Wraps",
        ],
        "category": "Arabian Street Food"
    }
}

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/recipes")
def recipes_page():
    return render_template('recipes.html', all_recipes = recipes_dict)

@app.route("/recipe/<the_id>")
def recipe_page(the_id):
    if the_id in recipes_dict:
        return render_template('recipe.html', recipe = recipes_dict[the_id])

#! template inheritance ---> base.html

if __name__ == "__main__":
    app.run(debug=True)