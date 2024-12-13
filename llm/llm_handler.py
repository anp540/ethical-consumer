from services.brand_info import get_brand_origin
from services.brand_info import get_brand_origin, get_sustainability_rating

def fetch_brand_origin(brand_name):
    return get_brand_origin(brand_name)

def fetch_brand_info(brand_name):
    origin = get_brand_origin(brand_name)
    sustainability = get_sustainability_rating(brand_name)
    return {
        "origin_story": origin,
        "sustainability_rating": sustainability
    }