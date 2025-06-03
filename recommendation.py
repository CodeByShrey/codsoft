import pandas as pd

# Sample data for product recommendations with categories
data = {
    'product': [
        'Wireless Earbuds', 
        'Smartphone', 
        'Gaming Laptop', 
        'Smartwatch',
        'Bluetooth Speaker', 
        '4K Monitor', 
        'Portable Charger',
        'Noise Cancelling Headphones', 
        'DSLR Camera', 
        'Fitness Tracker',
        'Mechanical Keyboard', 
        'Ergonomic Chair', 
        'Electric Toothbrush',
        'Robot Vacuum', 
        'Smart Home Hub', 
        'Streaming Stick',
        'Action Camera', 
        'Smart Light Bulbs', 
        'Winter Jacket',
        'Running Shoes', 
        'Graphic T-Shirt', 
        'Jeans',
        'Microwave Oven', 
        'Dishwasher'
    ],
    'category': [
        'sound', 
        'electronics', 
        'electronics', 
        'wearables',
        'sound', 
        'electronics', 
        'electronics',
        'sound', 
        'photography', 
        'wearables',
        'electronics', 
        'household', 
        'household',
        'household', 
        'household', 
        'electronics',
        'photography', 
        'household', 
        'clothes',
        'clothes', 
        'clothes', 
        'clothes',
        'household', 
        'household'
    ]
}

print("👋 Welcome to the Product Recommendation System!\n")
print("Here are the list of categories:\n")
# Convert to DataFrame
df = pd.DataFrame(data)

def recommend_products():
    categories = sorted(df['category'].unique())
    print("📦 Available Categories:\n")
    for cat in categories:
        print(f"• {cat}")

    while True:
        user_input = input("\nEnter a category (or type 'exit' to quit): ").strip().lower()
        if user_input == "exit":
            print("👋 Thank You For Using My Recommendation System!")
            break

        matched_products = df[df['category'].str.lower() == user_input]

        if not matched_products.empty:
            print(f"\n Products in category '{user_input}':\n")
            for product in matched_products['product'].tolist():
                print(f"  - {product}")
        else:
            print("❌ No products found in that category. Please try again.\n")

# Run the recommendation loop
recommend_products()
