import os

# Use 'r' before the string to make it a raw string
folder_path = r"/home/nova/Music/ Daily Mix 3"
prefix_to_remove = "[SPOTIFY-DOWNLOADER.COM] "

counter = 1
try:
  for filename in os.listdir(folder_path):
    if filename.startswith(prefix_to_remove):
      new_filename = os.path.join(folder_path, filename[len(prefix_to_remove):])
      os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
      print(f"{counter}. Renamed: {filename} to {new_filename}")
      counter += 1
except FileNotFoundError:
  print(f"Error: Folder '{folder_path}' not found.")
