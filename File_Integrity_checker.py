import os
import hashlib

def create_fingerprints():
    """
    Prompts the user for a folder path, then calculates and saves
    the SHA256 hash (fingerprint) for each file in that folder
    to a file named 'fingerprints.txt'.
    """
    folderpath = input("Enter the folder path to fingerprint: ")

    if not os.path.isdir(folderpath):
        print(f"Error: The path '{folderpath}' does not exist or is not a directory.")
        return

    files_and_dirs = os.listdir(folderpath)

    with open('fingerprints.txt', 'a') as output_file:
        for item_name in files_and_dirs:
            full_item_path = os.path.join(folderpath, item_name)

            if os.path.isfile(full_item_path):
                try:
                    with open(full_item_path, 'rb') as f:
                        content = f.read()
                        hash_value = hashlib.sha256(content).hexdigest()
                        line_to_write = f"{item_name}:{hash_value}\n"
                        output_file.write(line_to_write)

                except Exception as e:
                    print(f"Error processing file '{item_name}': {e}")

    print("\nFingerprint creation complete. Hashes saved to 'fingerprints.txt'")

# Example of how to call the function:
# if __name__ == "__main__":
#     create_fingerprints()
    