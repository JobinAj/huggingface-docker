from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

MODEL_NAME = "distilgpt2"  # Change to your required model

class Model:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.logits.argmax().item()

model = Model()
