from prodiapy import Prodia
from flask import Flask, request, jsonify

app = Flask(__name__)
prodia = Prodia(
    api_key= "YOUR_API_KEY"
)

@app.route("/image-generation", methods=["POST"])
def image():
    try:
        command = request.form.get('prompt')
        job = prodia.sd.generate(prompt=command)
        result = prodia.wait(job)

        return jsonify({"Image_Url": result.image_url}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)