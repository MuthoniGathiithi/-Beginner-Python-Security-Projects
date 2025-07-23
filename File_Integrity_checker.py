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


def check_current_fingerprint():
    """
    Reads stored fingerprints from 'fingerprints.txt', then calculates
    current fingerprints for files in a user-specified folder, and
    reports any changes (modified, new, or deleted files).
    """
    print("\n--- Checking Current Fingerprints ---")

    # --- Part 1: Read Stored Fingerprints ---
    stored_fingerprints = {} # This will be our box to hold old fingerprints
    try:
        # Step 1: Open the file where we saved the original fingerprints
        # 'r' mode means read: we want to look at what's inside.
        with open('fingerprints.txt', 'r') as stored_fingerprints_file:
            # Step 2: Read all lines from the file into a list
            # Each item in the list will be one line from the file, including the '\n' at the end
            lines = stored_fingerprints_file.readlines()

            # Step 3: Go through each line and separate the filename from the hash
            for line in lines:
                # .strip() removes any extra spaces or the '\n' (new line) character
                cleaned_line = line.strip()
                if ':' in cleaned_line: # Make sure the line contains a colon
                    # .split(':') breaks the string into a list wherever it sees a ':'
                    # Example: "document.txt:hash" becomes ["document.txt", "hash"]
                    filename, stored_hash = cleaned_line.split(':', 1) # split only on the first colon
                    # Store it in our dictionary: filename is the key, hash is the value
                    stored_fingerprints[filename] = stored_hash
        print(f"Loaded {len(stored_fingerprints)} stored fingerprints.")

    except FileNotFoundError:
        print("Error: 'fingerprints.txt' not found. Please create fingerprints first using 'create_fingerprints()'.")
        return
    except Exception as e:
        print(f"Error reading 'fingerprints.txt': {e}")
        return

    # --- Part 2: Get Current Fingerprints ---
    current_folderpath = input("Enter the folder path to check: ")

    # Check if the provided path exists and is a directory
    if not os.path.isdir(current_folderpath):
        print(f"Error: The path '{current_folderpath}' does not exist or is not a directory.")
        return

    current_fingerprints = {} # This will be our box to hold current fingerprints
    files_in_current_folder = os.listdir(current_folderpath)

    for item_name in files_in_current_folder:
        full_item_path = os.path.join(current_folderpath, item_name)

        if os.path.isfile(full_item_path):
            try:
                with open(full_item_path, 'rb') as f:
                    content = f.read()
                    current_hash = hashlib.sha256(content).hexdigest()
                    current_fingerprints[item_name] = current_hash
            except Exception as e:
                print(f"  Error calculating hash for '{item_name}': {e}")

    # --- Part 3: Compare Fingerprints and Report Changes ---
    print("\n--- Fingerprint Comparison Results ---")
    modified_count = 0
    new_count = 0
    deleted_count = 0

    # Check for modified and deleted files
    for filename, stored_hash in stored_fingerprints.items():
        if filename in current_fingerprints:
            # File exists in both, compare hashes
            if stored_fingerprints[filename] != current_fingerprints[filename]:
                print(f"  MODIFIED: '{filename}' (Hash changed)")
                modified_count += 1
        else:
            # File was in stored, but not in current folder
            print(f"  DELETED: '{filename}'")
            deleted_count += 1

    # Check for new files
    for filename, current_hash in current_fingerprints.items():
        if filename not in stored_fingerprints:
            # File is in current folder, but not in stored
            print(f"  NEW: '{filename}'")
            new_count += 1

    if modified_count == 0 and new_count == 0 and deleted_count == 0:
        print("  No changes detected. All files match stored fingerprints.")
    else:
        print(f"\nSummary: {modified_count} modified, {new_count} new, {deleted_count} deleted.")

# --- Main part to run the functions ---
if __name__ == "__main__":
    while True:
        print("\n--- File Fingerprint Tool ---")
        print("1. Create Fingerprints (saves to fingerprints.txt)")
        print("2. Check Current Fingerprints")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            create_fingerprints()
        elif choice == '2':
            check_current_fingerprint()
        elif choice == '3':
            print("Exiting tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    