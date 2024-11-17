from services.brand_info import get_brand_origin

def fetch_brand_origin(brand_name):
    return get_brand_origin(brand_name)


# utils/response_formatter.py
def format_origin_response(brand_name, origin_story):
    if origin_story:
        return {
            "brand": brand_name,
            "origin_story": origin_story
        }
    else:
        return {
            "brand": brand_name,
            "error": "Unable to fetch origin story at this time."
        }