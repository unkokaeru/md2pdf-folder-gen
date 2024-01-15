# md2pdf-folder-gen

## Overview
The `md2pdf-folder-gen` is a Python script designed to automate the process of generating markdown files for each PDF document in a specified directory. This script is particularly useful for organising and referencing PDF files in a markdown-friendly format, simplifying access to PDF documents through generated markdown files.

## Features
- **Automated Conversion:** Converts each PDF file in a specified directory into a markdown file.
- **Directory Management:** Automatically creates a directory for the markdown files if it doesn't exist.
- **Linking:** Each generated markdown file contains a direct link to the corresponding PDF file.

## Requirements
- Python 3.x
- Access to the file system (read/write permissions)

## Installation
To use the `md2pdf-folder-gen` script, clone or download this repository to your local machine.

## Usage
1. Place your PDF files in a directory named `pdfs` within the script's directory.
2. Run the script. It will generate markdown files in a directory named `mds`.
3. Each markdown file will be named after its corresponding PDF file and will contain a link to the PDF.

## How It Works
The script sets the working directory to a specified path, then creates two subdirectories: one for PDFs (`pdfs`) and one for markdown files (`mds`). For each PDF in the `pdfs` directory, the script creates a markdown file in the `mds` directory with the same name, providing a link to the original PDF file.

## Customisation
You can customise the script by changing the directory paths in the script according to your requirements.

## Limitations
- The script currently works only with PDF files.
- It does not recursively search through subdirectories.

## Contributing
Contributions to improve `md2pdf-folder-gen` are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
[MIT License](LICENSE)
