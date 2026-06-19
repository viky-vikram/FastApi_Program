from transformers import pipeline

model_id = "./Models/Qwen2.5-0.5B-Instruct"

generator = pipeline(
    "text-generation",
    model=model_id,
    device_map="auto"
)

result = generator(
    "Explain API testing in simple words:",
    max_new_tokens=80
)

print(result[0]["generated_text"])