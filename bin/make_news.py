import arxiv
from datetime import datetime
import sys

def generate_announcement(arxiv_id):
    # Fetch paper metadata from arXiv
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    paper = next(client.results(search), None)
    
    if paper is None:
        print(f"Error: No paper found with ID {arxiv_id}")
        return None, None
    
    # Extract the publication date
    pub_date = paper.published.date()
    pub_date_str = pub_date.strftime("%Y-%m-%d")
    
    # Format title and authors
    title = paper.title.replace('\n', ' ')
    authors = ', '.join(author.name for author in paper.authors)
    
    # Generate filename in format newsYYMMDD.md
    filename = f"news{pub_date.strftime('%y%m%d')}.md"
    
    # Generate Markdown content
    markdown_content = f"""---
layout: post
date: {pub_date_str} 09:00:00-0700
inline: true
related_posts: false
---

###### New paper! 

*{title}*, {authors} [arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id}).
"""
    return filename, markdown_content

def save_announcement(filename, content):
    # Write the Markdown content to the file
    with open(filename, 'w') as f:
        f.write(content)

# Main function to take arXiv ID
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <arxiv_id>")
    else:
        arxiv_id = sys.argv[1]
        filename, markdown_content = generate_announcement(arxiv_id)
        
        if filename and markdown_content:
            save_announcement(filename, markdown_content)
            print(f"Announcement generated and saved to {filename}")