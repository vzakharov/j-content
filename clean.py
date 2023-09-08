import os
import argparse
from collections import defaultdict
import time

def find_files(extension, folder):
  file_dict = defaultdict(list)
  for root, dirs, files in os.walk(folder):
    for file in files:
      if file.endswith(extension):
        file_dict[root].append(os.path.join(root, file))
  return file_dict

def delete_files(file_dict):
  for dir_path, file_list in file_dict.items():
    if len(file_list) > 1:
      file_list.sort(key=lambda x: os.path.getmtime(x), reverse=True)
      for file in file_list[1:]:
        os.remove(file)
        print(f"Deleted file: {file}")

def main():
  parser = argparse.ArgumentParser(description='Delete all but the latest file of a given extension in each directory.')
  parser.add_argument('extension', type=str, help='The file extension to search for.')
  args = parser.parse_args()

  file_dict = find_files(args.extension, '.')
  delete_files(file_dict)

if __name__ == "__main__":
  main()