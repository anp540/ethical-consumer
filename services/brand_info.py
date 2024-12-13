import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_brand_origin(brand_name):
    prompt = f"Provide a brief origin story of the luxury brand {brand_name}."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        origin_story = response.choices[0].text.strip()
        return origin_story
    except Exception as e:
        print(f"Error fetching brand origin: {e}")
        return None
    
def get_sustainability_rating(brand_name):
    sustainability_data = {
        "Gucci": "Medium: Made strides in sustainable materials but uses animal-derived products.",
        "Louis Vuitton": "Low: Minimal transparency in environmental practices.",
        "Bottega Veneta": "High: Focuses on craftsmanship and sustainable leather sourcing."
    }
    return sustainability_data.get(brand_name, "No sustainability data available for this brand.")