import json
import os
from tqdm import tqdm

def sample_json(input_file, output_file, target_size_gb, 

filter_key = 'also_buy'):
	size_bytes = size_bytes * 1024**3
	curr_size_bytes = 0
	
	with open(input_file, 'r', encoding = 'utf-8') as infile, open(output_file, 'w', encoding = 'utf-8') as outfile:
		for line in tqdm(infile):
			record = json.loads(line)
			if record.get(filter_key):
				outfile.write(json.dumps(record) + '\n')
				current_size_bytes += len(line.encode('utf-8'))
				
			if curr_size_bytes >=size_bytes:
				break
				
	print(f"Finished Sampling. Output size: {current_size-bytyes / 1024**3:.2f} GB")
	
sample_json('All_Amazon_Meta.json','Sampled_Amazon_Meta.json',15)
