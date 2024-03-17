# Copy a file
shutil.copy('file1.txt', 'file2.txt')

# Move a file
shutil.move('file1.txt', 'new_directory')

# Remove a directory
shutil.rmtree('directory_to_remove')

# Copy a directory
shutil.copytree('directory_to_copy', 'new_directory')

# Copy a file preserving metadata
shutil.copy2('file1.txt', 'file2.txt')

# Copy file metadata
shutil.copystat('file1.txt', 'file2.txt')
