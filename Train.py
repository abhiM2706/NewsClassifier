from datasets import load_dataset
from datasets import Dataset
import pandas as pd

from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
import evaluate
import numpy as np
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from transformers import pipeline 
import torch.nn.functional as F

from transformers import AutoTokenizer, AutoModelForCausalLM

model_name_or_path = r"C:\Users\abhi2\OneDrive\Documents\Github\DigitClassifier\my_awesome_model\checkpoint-2"
device = "cpu" # or "cuda" if you have a GPU

model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

test = """A Harris campaign video released Thursday featuring vice presidential candidate Tim Walz deadpanning that he eats "White guy tacos" is getting some blowback from critics on social media.  

Adding fuel to the fire was Vice President Kamala Harris’ snarky response in the video, with critics saying it "mocked" White people.  

"I have White guy tacos, and . . .," Walz says in the campaign video of him and Harris discussing some of their favorite foods.

"What does that mean? Like mayonnaise and tuna? What are you doing?" Harris quipped back."""

inputs = tokenizer.encode(test, return_tensors="pt").to(device)

print(inputs)
outputs = model(inputs)

print(outputs)
print(F.softmax(outputs.logits, dim=-1))
