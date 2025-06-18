import os

label_dirs = ['/home/edramos/Documents/MLOPS/ConvertDatasetYolo/foot-type-singleclass/train', '/home/edramos/Documents/MLOPS/ConvertDatasetYolo/foot-type-singleclass/valid']  # Add test if needed

def relabel_all_to_present(folder_path):    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5: continue  # skip malformed lines
                parts[0] = '0'  # overwrite class ID to 0 (present)
                new_lines.append(' '.join(parts))
            with open(file_path, 'w') as f:
                f.write('\n'.join(new_lines))

for d in label_dirs:
    relabel_all_to_present(d)
