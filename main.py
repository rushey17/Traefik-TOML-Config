from fastapi import FastAPI, Query, Path

app = FastAPI()

# Basic endpoint
@app.get("/health")
def read_health():
    return {"status": "healthy"}

# Fetch user profile
@app.get("/api/users/{user_id}")
def read_user_profile(user_id: int = Path(..., description="User ID")):
    users = {
        1: {"username": "alice", "email": "alice@example.com"},
        2: {"username": "bob", "email": "bob@example.com"}
    }
    return users.get(user_id, {"message": "User not found"})

# List available products
@app.get("/api/products")
def list_products(category: str = Query(None, description="Product category")):
    products = {
        "electronics": ["Laptop", "Smartphone", "Tablet"],
        "clothing": ["Shirt", "Jeans", "Dress"]
    }
    if category is None:
        return products
    return products.get(category, {"message": "Category not found"})

# Calculate shipping cost
@app.get("/api/shipping")
def calculate_shipping_cost(weight: float = Query(..., description="Product weight in kg")):
    base_rate = 5.0  # Base shipping rate in dollars
    cost_per_kg = 2.0  # Additional cost per kg in dollars
    shipping_cost = base_rate + (cost_per_kg * weight)
    return {"weight": weight, "shipping_cost": shipping_cost}
