# grabs everything in contents
# parses it into html
# organizes it sequentially
# outputs it to a file
#
#

import markdown2
import os
import time
from datetime import datetime


def parse_markdown(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        html = markdown2.markdown(content)
        return html


def parse_all():
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="styles.css">
        <title>b(attle)log</title>
    </head>
    <body>
        $CONTENT
    </body>
    </html>
    """
    # Get number of files in contents
    # Parse each file
    # Organize them sequentially
    # Output to a file
    output = ""

    # One-liner to get the number of files in contents
    num_files = len(
        [
            name
            for name in os.listdir("contents")
            if os.path.isfile(os.path.join("contents", name))
        ]
    )

    # Start from the highest number and work down
    for i in range(num_files, 0, -1):
        file_path = f"contents/{i}.md"
        # Add a custom anchor
        output += f'<a href="#{i}" class="page-anchor" name="{i}">{i}</a>'
        # Add last modified date
        modified_date = datetime.fromtimestamp(os.path.getmtime(file_path)).date()
        output += f'<div class="date">Updated: {modified_date}</div>'
        # Add created date
        # creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).date()
        # output += f'<div class="date">Created: {creation_date}</div>'
        # Add the parsed markdown
        output += parse_markdown(file_path)

    # Replace $CONTENT with the output
    template = template.replace("$CONTENT", output)

    # Write the output to a file
    with open("index.html", "w") as file:
        file.write(template)


def main():
    parse_all()


if __name__ == "__main__":
    main()
