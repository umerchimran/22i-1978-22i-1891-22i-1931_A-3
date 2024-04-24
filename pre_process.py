import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def clean_data(data):
    cleaned_data = []
    for entry in data:

        cleaned_entry = {
            'asin': entry['asin'],
            'title': entry['title'],
            'description': entry['description'],
            'price': entry['price'],
            'categories': entry['categories']
        }
        cleaned_data.append(cleaned_entry)
    return cleaned_data

def preprocess_data(input_file, output_file):
    data = load_data(input_file)
    cleaned_data = clean_data(data)
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(cleaned_data, file, ensure_ascii=False, indent
4)


if __name__ == "__main__":
    input_file = "Sampled_Amazon_Meta.json"
    output_file = "preprocessed_data.json"  
    preprocess_data(input_file, output_file)

