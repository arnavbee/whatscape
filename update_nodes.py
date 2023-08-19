# List of node information
node_data = [
    {
        "id": "node4",
        "label": "New Node 4",
        "content": "Content for New Node 4",
        "url": "new-node-4.html",
    },
    {
        "id": "node5",
        "label": "New Node 5",
        "content": "Content for New Node 5",
        "url": "new-node-5.html",
    },
    # Add more nodes as needed
]

# Read the content of script.js file
with open("script.js", "r") as js_file:
    script_content = js_file.read()

# Find the position to update graphData array
start_index = script_content.find("const graphData = [") + len("const graphData = [")
end_index = script_content.find("];", start_index)

# Generate JavaScript code for new nodes
js_code = "\n".join(
    [
        f"""{{
        id: "{node['id']}",
        label: "{node['label']}",
        content: `{node['content']}`,
        url: "{node['url']}"
    }},
    """
        for node in node_data
    ]
)

# Update the graphData array content in script.js
updated_script = script_content[:start_index] + js_code + script_content[end_index:]

# Write the updated script content back to script.js file
with open("script.js", "w") as js_file:
    js_file.write(updated_script)

print("graphData array updated in script.js")
