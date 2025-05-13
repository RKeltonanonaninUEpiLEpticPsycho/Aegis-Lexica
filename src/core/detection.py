```python
dehumanizing_lexicon = [
    "animalistic", "vermin", "disease", "subhuman", "creature",
    # Add more terms as you identify them
]

def detect_dehumanization(text):
    text = text.lower()
    found_terms = [term for term in dehumanizing_lexicon if term in text]
    return found_terms

if __name__ == "__main__":
    example_text = "These people are like vermin infesting our city."
    detected = detect_dehumanization(example_text)
    if detected:
        print(f"Detected dehumanizing terms: {detected}")
    else:
        print("No dehumanizing terms detected.")
```