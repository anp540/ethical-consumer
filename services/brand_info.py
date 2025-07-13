# services/brand_info.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_brand_origin(brand_name):
    """Uses OpenAI to generate the brand's origin story."""
    prompt = f"Provide a short but informative origin story for the luxury brand '{brand_name}'. Mention founders, country, and history."
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can switch to GPT-4 via `gpt-4` if needed
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error fetching origin story: {str(e)}"

def get_brand_ethics(brand_name):
    # Dummy placeholder data for now
    ethics_data = {
        "Gucci": "Gucci has made efforts to improve sustainability but still faces criticism for animal-derived materials.",
        "Prada": "Prada has pledged to eliminate fur and improve supply chain transparency.",
        "Chanel": "Chanel has limited public disclosures but banned exotic skins recently."
    }
    return ethics_data.get(brand_name, "No ethical data available yet.")