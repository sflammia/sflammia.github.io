import arxiv
import sys

def generate_bibtex(arxiv_id):
    # Initialize client and fetch metadata from arXiv
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    paper = next(client.results(search), None)
    
    if paper is None:
        print(f"Error: No paper found with ID {arxiv_id}")
        return None
    
    # Extract and format fields with braces
    title = "{{" + paper.title.replace('\n', ' ') + "}}"
    abstract = "{" + paper.summary.replace('\n', ' ') + "}"
    authors = "{" + ' and '.join(author.name for author in paper.authors) + "}"
    
    # Format the BibTeX entry with braces
    bibtex_entry = (
        f"@misc{{{arxiv_id},\n"
        f"    abstract={abstract},\n"
        f"    archivePrefix={{arXiv}},\n"
        f"    author={authors},\n"
        f"    bibtex_show = {{1}},\n"
        f"    doi = {{10.48550/arXiv.{arxiv_id}}},\n"
        f"    eprint={{{arxiv_id}}},\n"
        f"    pdf = {{https://arxiv.org/pdf/{arxiv_id}}},\n"
        f"    preview={{{arxiv_id}.jpg}},\n"
        f"    title={title},\n"
        f"    year={{{paper.published.year}}},\n"
        "}\n"
    )
    return bibtex_entry

def output_bibtex(bibtex_entry, filename=None):
    if filename:
        # Read existing content from file
        try:
            with open(filename, 'r') as f:
                existing_content = f.read()
        except FileNotFoundError:
            existing_content = ""

        # Check if the file starts with the YAML front matter pattern
        yaml_pattern = "---\n---\n"
        if existing_content.startswith(yaml_pattern):
            # Insert bibtex entry directly after YAML pattern, followed by a blank line
            new_content = yaml_pattern + bibtex_entry + "\n" + existing_content[len(yaml_pattern):]
        else:
            # Prepend bibtex entry at the very top with a blank line after
            new_content = bibtex_entry + "\n" + existing_content
        
        # Write the modified content back to the file
        with open(filename, 'w') as f:
            f.write(new_content)
    else:
        # Print to stdout
        print(bibtex_entry)

# Main function to take arXiv ID and optional filename
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <arxiv_id> [output_file]")
    else:
        arxiv_id = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        bibtex_entry = generate_bibtex(arxiv_id)
        
        if bibtex_entry:
            output_bibtex(bibtex_entry, output_file)