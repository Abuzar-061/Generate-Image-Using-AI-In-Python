### Description 🖼️

This project implements a Flask API for generating images using the ProDia API. Users can submit a prompt through a form, and the API will use the prompt to generate an image using ProDia's image generation service. The generated image URL is then returned as a response.

### Usage ℹ️

1. Clone the repository:

    ```bash
    git clone https://github.com/Abuzar-061/Generate-Image-Using-AI-In-Python.git
    ```

2. Install dependencies:

    ```bash
    pip install Flask prodiapy
    ```

3. Set up your ProDia API key by replacing `"YOUR_API_KEY"` in `ProdiaImage.py` with your actual API key.

4. Get your Prodia API Key From [Here](https://app.prodia.com/api)

5. Run the Flask app:

    ```bash
    python ProdiaImage.py
    ```

6. Open your web browser and go to `http://localhost:5000`.

7. Enter a prompt in the form and click "Generate Image".

### Project Structure 📂

- `ProdiaImage.py`: Contains the Flask application code.
- `README.md`: Instructions and information about the project.

### Requirements 🛠️

- Python 3.x
- Flask
- ProDiapy

### Contributing 🤝

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

### License 📝

This project is licensed under the [MIT License](LICENSE).

### Support 📧

For any inquiries or support, please contact [notabuzar@gmail.com](mailto:notabuzar@gmail.com).
