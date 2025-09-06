import os

from dotenv import load_dotenv
import google.generativeai as genai

def simple_gemini_request():
    """
    Simple example of making a Gemini API request and handling the response
    """
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found")
        return None
    
    try:
        # Configure the API key
        genai.configure(api_key=api_key)
        
        # Create the model
        model = genai.GenerativeModel(model_name)
        
        question = "Tell me the contry origin of these moview in a simple json, " \
        "with movie title and country only: " \
        "1. Inception, 2. Parasite, 3. Amelie, 4. Spirited Away, 5. The Godfather"

        # Make the request
        response = model.generate_content(question)
        
        # Extract the AI's response
        ai_message = response.text
        print("AI Response:", ai_message)
        
        return ai_message
        
    except Exception as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    print("Making Gemini API request...")
    response = simple_gemini_request()