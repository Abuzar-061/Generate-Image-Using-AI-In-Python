from prodiapy import Prodia
from flask import Flask, request, jsonify

app = Flask(__name__)
prodia = Prodia(
    api_key= "YOUR_API_KEY" # Read Readme.md to get your own API KEY 
)

@app.route("/image-generation", methods=["POST"])  # Define a route for image generation endpoint
def image():
    try:
        command = request.form.get('prompt')  # Get prompt from form data
        
        # Generate image using ProDia API with specified model
        job = prodia.sd.generate(prompt=command, model="anything-v4.5-pruned.ckpt [65745d25]") # For Model Information Check the ModelListProdia.py File and get the model of your choice
        
        # Wait for the job to complete and get the result
        result = prodia.wait(job)

        # Return the generated image URL in JSON response
        return jsonify({"Image_Url": result.image_url}), 200
    except Exception as e:
        # Handle exceptions and return error message
        return jsonify({"Error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Run the Flask application
