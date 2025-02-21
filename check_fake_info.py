from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model

model_name = "meta-llama/Llama-2-7b-chat-hf"  # Replace with the specific Llama model name if available
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Ensure the model is on the right device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to read input file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to detect misinformation
def assess_statement(text, tokenizer, model, device):
    prompt = (
        f"Evaluate the following statement for potential misinformation or falsehood. "
        f"Consider known facts and current understanding in your assessment. "
        f"Provide a brief explanation if the statement is misleading or false.\n\n"
        f"Statement: {text}\n\n"
        f"Assessment:"
    )
    inputs = tokenizer(prompt, return_tensors='pt').to(device)

    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], max_length=500, num_return_sequences=1, temperature=0.7, num_beams=5)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Read input text from file
input_file_path = './final/fake_input.txt'  # Replace with your input file path
input_text = read_input_file(input_file_path)

# Generate FQA pairs
summary = assess_statement(input_text.strip(), tokenizer, model, device)

# Save the result  to a file
output_file_path = 'results.txt'  # Replace with your output file path
with open(output_file_path, 'w') as file:
    file.write(f"Detect results:\n{summary}")

# Optionally display the generated FQA pairs
print(f"Results:\n{summary}")


