from flask import Flask, request, jsonify
from llm.llm_handler import fetch_brand_origin
from utils.response_formatter import format_origin_response
from llm.llm_handler import fetch_brand_info

app = Flask(__name__)
@app.route('/brand_origin', methods=['GET'])
def brand_origin():
    brand_name = request.args.get('brand')
    if not brand_name:
        return jsonify({"error": "Please provide a brand name."}), 400

    origin_story = fetch_brand_origin(brand_name)
    response = format_origin_response(brand_name, origin_story)
    return jsonify(response)

@app.route('/brand_info', methods=['GET'])
def brand_info():
    brand_name = request.args.get('brand')
    if not brand_name:
        return jsonify({"error": "Please provide a brand name."}), 400

    brand_data = fetch_brand_info(brand_name)
    return jsonify(brand_data)

if __name__ == '__main__':
    app.run(debug=True)