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