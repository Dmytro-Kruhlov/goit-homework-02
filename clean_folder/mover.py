import os
import shutil
from clean_folder import normalizer, utils, categorizer





def move_file(file_path: str, category: str, path_to_folder: str):
    filename = os.path.basename(file_path)
    name_without_extension = os.path.splitext(filename)[0]
    
    new_folder = os.path.join(path_to_folder, category)
    
    if  not (os.path.exists(new_folder) and os.path.isdir(new_folder)):
        os.makedirs(new_folder)
        
    new_file_name = normalizer.normalize(name_without_extension)
    
    destination = os.path.join(new_folder, f"{new_file_name}.{utils.get_extension(filename)}")
    
    counter = 1

    while os.path.exists(destination):
        new_file_name = f"{normalizer.normalize(name_without_extension)}_{counter}"
        destination = os.path.join(new_folder, f"{new_file_name}.{utils.get_extension(filename)}")
        counter += 1
    
    shutil.move(file_path, destination)


    
    
    
def move_archive(file_path: str, path_to_folder):
    filename = os.path.basename(file_path)
    name_without_extansion = os.path.splitext(filename)[0]
    category = categorizer.categorize(filename)

    category_folder = os.path.join(path_to_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    normalized_name = normalizer.normalize(name_without_extansion)
    extraction_folder = os.path.join(category_folder, normalized_name)

    folder_exists = os.path.exists(extraction_folder)
    counter = 1
    while folder_exists:
        new_folder_name = f"{normalized_name}_{counter}"
        extraction_folder = os.path.join(category_folder, new_folder_name)
        folder_exists = os.path.exists(extraction_folder)
        counter += 1
    os.makedirs(extraction_folder)    
        
    utils.extract_archive(file_path, extraction_folder)
    extracted_items = os.listdir(extraction_folder)

    for ext_item in extracted_items:
        ext_item_path = os.path.join(extraction_folder, ext_item)   
        item_name_whthout_ext, item_ext = os.path.splitext(ext_item)
        new_item_name = normalizer.normalize(item_name_whthout_ext) + item_ext
        new_item_path = os.path.join(extraction_folder, new_item_name)
        os.rename(ext_item_path, new_item_path)

        
    os.remove(file_path)


def move_files_from_subfolders(path: str) -> list:
    
    file_paths = utils.get_files_from_folder(path)
    moved_file = []
    
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        destination = os.path.join(path, filename)
        
        
        shutil.move(file_path, destination)
        moved_file.append(destination)
    return moved_file