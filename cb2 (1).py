# -*- coding: utf-8 -*-
"""CB2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vmzpRK64TFaxjY-766OwI72kiqZjejXO
"""

!pip install huggingface_hub transformers

from huggingface_hub import snapshot_download
snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.1", local_dir="mistral_model")

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1", device_map="auto", torch_dtype="auto")

import torch
print("CUDA Available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "mistralai/Mistral-7B-Instruct-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use FP16 to reduce memory usage
    device_map="auto"           # Auto-distributes model to GPU
)

print("Model loaded successfully!")

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "mistralai/Mistral-7B-Instruct-v0.1"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model with 8-bit quantization (reduces memory usage)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    load_in_8bit=True,  # Load in 8-bit mode to reduce memory
    device_map="auto"   # Automatically map model to GPU/CPU
)

print("✅ Model loaded successfully in 8-bit mode!")

prompt = "Tell me an interesting fact about space."
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))

pip install transformers torch

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "/content/mistral_model"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load model with optimized settings
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,  # Use float16 to reduce memory usage
    device_map="auto"           # Automatically selects GPU if available
)

print("Model loaded successfully!")

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Define model name
model_name = "/content/mistral_model"  # Change this if needed

# Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"

# Use BitsAndBytesConfig for 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Use 4-bit quantization
    bnb_4bit_compute_dtype=torch.float16,  # Compute in 16-bit for speed
    llm_int8_enable_fp32_cpu_offload=True,  # Enable CPU offloading
)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,  # Use updated quantization method
    device_map="auto",
)

# System prompt to guide responses
system_prompt = (
    "You are a compassionate AI therapist. "
    "Your goal is to provide kind, thoughtful, and supportive responses. "
    "Always encourage the user and offer helpful advice while being empathetic."
)

print("🧠 AI Mental Health Chatbot Ready! Type 'exit' to end the session.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n🧘 Thank you for talking. Remember, you're not alone. 💙 Take care!\n")
        break

    # Format input with system prompt
    prompt = f"{system_prompt}\nUser: {user_input}\nTherapist AI:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.5,  # Less randomness
            top_p=0.85,  # More focused response
            repetition_penalty=1.2,  # Prevents repetition
        )

    bot_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove unnecessary repetitions
    bot_response = bot_response.replace(prompt, "").strip()

    print("\nTherapist AI: " + bot_response + "\n")

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Define model name
model_name = "/content/mistral_model"  # Change if needed

# Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"

# Use BitsAndBytesConfig for efficient quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    llm_int8_enable_fp32_cpu_offload=True,
)

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
)

# System prompt to guide behavior
system_prompt = (
    "You are a compassionate AI therapist. "
    "Your goal is to provide kind, thoughtful, and supportive responses. "
    "Always encourage the user and offer helpful advice while being empathetic."
)

# Store chat history (context-aware)
chat_history = []

print("🧠 AI Mental Health Chatbot Ready! Type 'exit' to end the session.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n🧘 Thank you for talking. Remember, you're not alone. 💙 Take care!\n")
        break

    # Append user input to history
    chat_history.append(f"User: {user_input}")

    # Keep only recent messages to fit token limit
    max_history_length = 5  # Adjust based on model's capacity
    chat_history = chat_history[-max_history_length:]

    # Combine messages into a single formatted prompt
    conversation = "\n".join(chat_history)
    prompt = f"{system_prompt}\n{conversation}\nTherapist AI:"

    # Tokenize and generate response
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.5,  # Less randomness
            top_p=0.85,  # More focused response
            repetition_penalty=1.2,
        )

    bot_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove unnecessary repetitions
    bot_response = bot_response.replace(prompt, "").strip()

    # Append AI response to chat history
    chat_history.append(f"Therapist AI: {bot_response}")

    print("\nTherapist AI: " + bot_response + "\n")