import sys
import glob
    
def find_files(path, extension):
# Define the folder path and the extension you're interested in
    folder_path = path
    try:
        extension = '*'+extension
    except:
        print('please provide a string in the extension field')
        exit()
    
    files = glob.glob(folder_path + '/' + extension)
    return files

def update_file_names(file_path, new_file_name, new_file_name_bis):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    
        found_file_writer = False
        for i, line in enumerate(lines):
            if "[FileWriter]" in line:
                found_file_writer = True
            if "file_name" in line:
                if found_file_writer: #after [FileWriter]
                    lines[i] = f'file_name="{new_file_name_bis}"\n'
                else:
                    lines[i] = f'file_name="{new_file_name}"\n'
        with open(file_path, 'w') as file:
            file.writelines(lines)
            print("File names updated successfully.")

    except Exception as e:
        print(f"Somethig went wrong: {e}")
        
if __name__=="__main__":
#    print(find_files("../",".conf"))
    if len(sys.argv) != 4:
        print("Usage for this script is python3 change_filename.py path_to_configs new_raw_filename new_tracks_filename") 
        print("Please provide the right arguments. Aborting")
        exit()
    conf_files = find_files(str(sys.argv[1]), "*.conf")
    for file in conf_files:
        update_file_names(str(file),str(sys.argv[2]),str(sys.argv[3]))
