# import os

# # Path to the directory containing your HTML files
# html_dir = "./blogs"

# # Initialize an empty list to store node data
# nodes = []

# # Iterate through HTML files in the directory
# for filename in os.listdir(html_dir):
#     if filename.endswith(".html"):
#         node_id = "node_"
#         label = filename.replace(".html", "")

#         # Read the content of the HTML file

#         # Extract a preview text (you can customize this part)
#         preview_text = "Preview text for " + label

#         # Generate a JavaScript object for the node
#         node = {
#             "id": node_id,
#             "label": label,
#             "previewText": preview_text,
#             "url": filename,
#         }

#         nodes.append(node)

# with open("generated_nodes.js", "w") as output_file:
#     output_file.write("const generatedNodes = " + str(nodes) + ";")


# # Print the generated JavaScript array
# print("const generatedNodes =", nodes, ";")


# -------


import os
import json

html_dir = "./blogs"

nodes = []
start_number = 108  # Starting number for node IDs

for idx, filename in enumerate(sorted(os.listdir(html_dir))):
    if filename.endswith(".html"):
        label = filename.replace(".html", "")
        preview_text = f"{label}"

        node = {
            "id": f"node_{start_number + idx}",  # Generate node ID based on start_number and increment
            "label": f"Node {start_number + idx}",
            "previewText": preview_text,
            "url": filename,
        }

        nodes.append(node)

with open("generated_nodess.js", "w") as output_file:
    output_file.write("const generatedNodes = " + json.dumps(nodes, indent=2) + ";")
