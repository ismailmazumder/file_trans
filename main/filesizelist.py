import os

def convert_bytes_to_gb(bytes):
    gb = bytes / (1024 ** 3)  # 1024 bytes = 1 kilobyte, 1024 kilobytes = 1 megabyte, 1024 megabytes = 1 gigabyte
    return gb

def list_files_by_size(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                filesize = os.path.getsize(filepath)
                files.append((filepath, filesize))

    files.sort(key=lambda x: x[1])
    return files

if __name__ == "__main__":
    c_drive_directory = "C:\\"
    files = list_files_by_size(c_drive_directory)

    print("Files on C drive sorted by size:")
    for file, size in files:
        size_gb = convert_bytes_to_gb(size)
        print(f"{file}: {size_gb:.2f} GB")
