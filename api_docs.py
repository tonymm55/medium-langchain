import json

coolio_api_docs = {
    "base_url": "http://127.0.0.1:5000/",
    "endpoints": {
        "/menu": {
            "method": "GET",
            "description": "Retrieve the menu of flavors and customizations.",
            "parameters": None,
            "response": {
                "description": "A JSON object containing available flavors and toppings along with their counts.",
                "content_type": "application/json"
            }
        },
        "/special-offers": {
            "method": "GET",
            "description": "Retrieve current special offers and discounts.",
            "parameters": None,
            "response": {
                "description": "A JSON object listing the current special offers and discounts.",
                "content_type": "application/json"
            }
        },
        "/customer-reviews": {
            "method": "GET",
            "description": "Retrieve customer reviews for the ice cream store.",
            "parameters": None,
            "response": {
                "description": "A JSON object containing customer reviews, ratings, and comments.",
                "content_type": "application/json"
            }
        },
        "/customizations": {
            "method": "GET",
            "description": "Retrieve available ice cream customizations.",
            "parameters": None,
            "response": {
                "description": "A JSON object listing available customizations like toppings and sugar-free options.",
                "content_type": "application/json"
            }
        }
    }
}

# Convert the dictionary to a JSON string
coolio_api_docs = json.dumps(coolio_api_docs, indent=2)