import os
# Remove numpy import since it's causing issues
# import numpy as np
# Remove TensorFlow import since it's causing issues
# import tensorflow as tf
# Remove OpenAI import since it's causing issues
# from openai import OpenAI
from django.conf import settings
from PIL import Image
from io import BytesIO
import random
from .models import WasteCategory

# Mock responses for the chatbot
MOCK_RESPONSES = {
    "hello": "Hello! I'm EcoBot, your waste management assistant. How can I help you today?",
    "hi": "Hi there! I'm EcoBot, your waste management assistant. How can I help you today?",
    "how are you": "I'm functioning well, thank you! How can I assist you with waste management today?",
    "recycle": "Recycling is a process of converting waste materials into new materials and objects. The recyclability of a material depends on its ability to reacquire the properties it had in its original state.",
    "plastic": "Plastic recycling is the process of recovering scrap or waste plastic and reprocessing the material into useful products. Most plastics are labeled with a recycling symbol (1-7) to indicate the type of plastic.",
    "paper": "Paper recycling is the process of converting waste paper into new paper products. It reduces the amount of waste sent to landfills and saves trees from being cut down.",
    "glass": "Glass recycling is the process of turning waste glass into usable products. Glass can be recycled endlessly without loss in quality or purity.",
    "metal": "Metal recycling is the process of separating, cleaning and melting scrap metal so it can be used to create new products. Metals like aluminum and steel can be recycled indefinitely.",
    "electronic waste": "Electronic waste, or e-waste, includes discarded electronic devices. These should be taken to specialized recycling centers as they often contain hazardous materials.",
    "compost": "Composting is a natural process of recycling organic material such as leaves and vegetable scraps into a rich soil amendment.",
    "reduce waste": "To reduce waste, try using reusable items, buying products with less packaging, composting organic waste, and recycling whenever possible.",
    "landfill": "Landfills are sites designated for the disposal of waste materials. Modern landfills are designed to minimize their impact on the environment.",
    "how to recycle batteries": "Batteries should not be thrown in regular trash as they contain hazardous materials. Take them to designated battery recycling points or hazardous waste collection centers.",
    "what can i do with old electronics": "Old electronics should be taken to e-waste recycling centers. Many electronics retailers also offer take-back programs. Before disposing, consider donating working electronics.",
    "how to reduce plastic waste": "To reduce plastic waste: use reusable bags, bottles, and containers; avoid single-use plastics; buy products with minimal packaging; and recycle plastic items properly.",
}

def classify_waste_image(image_file):
    """
    Classify waste image using simple image analysis
    This is a simplified example that returns mock results
    """
    # Open the image
    img = Image.open(image_file)
    img = img.resize((224, 224))
    
    # For demo purposes, we'll return mock results
    # Get all waste categories
    categories = list(WasteCategory.objects.all())
    
    if not categories:
        return None, 0.0
    
    # Simulate prediction by randomly selecting a category with high confidence
    selected_category = random.choice(categories)
    confidence = random.uniform(0.7, 0.98)
    
    return selected_category, confidence

def get_mock_response(user_message):
    """
    Get a mock response based on the user's message
    """
    # Convert user message to lowercase for matching
    user_message_lower = user_message.lower().strip()
    
    # Check for exact matches in our mock responses
    if user_message_lower in MOCK_RESPONSES:
        return MOCK_RESPONSES[user_message_lower]
    
    # Check for partial matches
    for key in MOCK_RESPONSES:
        if key in user_message_lower:
            return MOCK_RESPONSES[key]
    
    # If no match found, return a generic response
    generic_responses = [
        "I'm here to help with waste management questions. Could you ask something about recycling, waste disposal, or environmental sustainability?",
        "That's an interesting question! As a waste management assistant, I can help with recycling, composting, and reducing waste. What would you like to know about these topics?",
        "I'm focused on waste management topics. Feel free to ask about recycling, composting, or how to reduce your environmental footprint.",
        "I don't have information on that specific topic. I'm best at answering questions about waste management, recycling, and environmental sustainability.",
        "I'm still learning about waste management. Could you ask me something about recycling, composting, or reducing waste?"
    ]
    return random.choice(generic_responses)

def get_chatbot_response(user_message, conversation_history=None):
    """
    Get response for waste management chatbot
    Using mock responses only since OpenAI is not available
    """
    if conversation_history is None:
        conversation_history = []
    
    # Use mock responses for all chatbot interactions
    return get_mock_response(user_message) 