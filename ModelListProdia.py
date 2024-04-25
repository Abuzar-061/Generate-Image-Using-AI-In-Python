from prodiapy import Prodia

prodia = Prodia(
    api_key="API_KEY_PLACEHOLDER"
                )

# Get the list of trained models
model_list = prodia.sd.models()

# Print the list of models
print("Available models:")
for model in model_list:
    print(model)
