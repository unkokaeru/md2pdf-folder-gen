"""A simple script to create markdown files for each PDF in a directory."""

# Imports
import os


def main() -> None:
    """
    Main function.
    :return: None
    """

    # Set the current working directory
    os.chdir("C:\\Users\\wills\\OneDrive\\Desktop")

    # Get the current working directory
    cwd = os.getcwd()

    # Get the directory of the PDFs
    pdf_dir = os.path.join(cwd, "pdfs")

    # Get the directory of the markdown files
    md_dir = os.path.join(cwd, "mds")

    # Create the markdown directory if it doesn't exist
    if not os.path.exists(md_dir):
        os.mkdir(md_dir)

    # Get the list of PDFs
    pdfs: list = os.listdir(pdf_dir)

    # Create a markdown file for each PDF
    for pdf in pdfs:
        # Get the name of the PDF
        pdf_name: str = pdf.split(".")[0]

        # Create the markdown file
        with open(os.path.join(md_dir, f"{pdf_name}.md"), "w") as f:
            f.write(f"# {pdf_name}\n\n")

            # Add the link to the PDF
            f.write(f"[{pdf_name}](../pdfs/{pdf})\n\n")


if __name__ == "__main__":
    main()
