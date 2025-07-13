# llm/llm_handler.py

from services.brand_info import get_brand_origin, get_brand_ethics

def fetch_brand_origin(brand_name):
    return get_brand_origin(brand_name)

def fetch_brand_info(brand_name):
    return {
        "origin_story": get_brand_origin(brand_name),
        "ethical_practices": get_brand_ethics(brand_name)
    }
