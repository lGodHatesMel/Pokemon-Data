import os

def rename_to_lowercase(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico')):
            lower_case_filename = filename.lower()
            source = os.path.join(directory, filename)
            destination = os.path.join(directory, lower_case_filename)
            
            # Renaming only if the filename is not already lowercase
            if source != destination:
                os.rename(source, destination)
                print(f'Renamed {source} to {destination}')
            else:
                print(f'{filename} is already in lowercase')

rename_to_lowercase(os.getcwd())
