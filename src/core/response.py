
```python
import json

def generate_response(dehumanizing_term, knowledge_graph_path="../../data/knowledge_graph.json"):
    try:
        # Note the adjusted path to the knowledge_graph.json file
        with open(knowledge_graph_path, 'r') as f:
            knowledge = json.load(f)
    except FileNotFoundError:
        return "Knowledge graph not found."

    if dehumanizing_term in knowledge:
        entry = knowledge[dehumanizing_term]
        counters = entry.get("counter_concepts", [])
        rights = entry.get("rights_violated", [])

        response_parts = [f"The term '{dehumanizing_term}' is often used to dehumanize individuals."]
        if counters:
            response_parts.append(f"These individuals are human beings, {', '.join(counters)}, with inherent worth.")
        if rights:
            response_parts.append(f"Such language can violate their fundamental human rights, including the right to {', '.join(rights)}.")
        return " ".join(response_parts)
    else:
        return f"No specific response found for '{dehumanizing_term}'."

if __name__ == "__main__":
    term = "vermin"
    response = generate_response(term)
    print(response)
```