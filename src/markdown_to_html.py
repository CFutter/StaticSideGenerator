from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
import re



def text_to_children(text):
    return


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []


    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type.name == "HEADING":
            hashtags = re.findall(r"^#+", block)
            number_of_hashtags = len(hashtags[0])
            
            html_nodes.append(LeafNode(f"h{number_of_hashtags}", block[number_of_hashtags + 1: ]))

        elif block_type.name == "CODE":

            code_block = "<code>" + block[3: -3] + "</code>"
            html_nodes.append(LeafNode("pre", code_block))   

        elif block_type.name == "QUOTE":
            html_nodes.append(LeafNode("blockquote", block[2:]))

        elif block_type.name == "UNORDERED_LIST":

            list_elements = block.split("- ")
            list_leaf_nodes = []

            for element in list_elements[1:]:
                list_leaf_nodes.append(LeafNode("li", element))

            html_nodes.append(ParentNode("ul", list_leaf_nodes))      

        elif block_type.name == "ORDERED_LIST":
            list_elements = re.split(r'\d+\.\s', block)
            list_leaf_nodes = []
            for element in list_elements[1:]:
                list_leaf_nodes.append(LeafNode("li", element))
                
            html_nodes.append(ParentNode("ol", list_leaf_nodes))      
        else:
            html_nodes.append(LeafNode("p", block))

    html_nodes_2 = []

    for node in html_nodes:
        html_nodes_2.append(node.to_html())

    return HTMLNode("div", None, html_nodes_2)


md = """
### This is **bolded** paragraph

###### This is **bolded** paragraph

# This is **bolded** paragraph

- text in a p - And other - and another


3. tag here 4. and here 78. maybe not here

This is another paragraph with _italic_ text and `code` here

```CODDEDDEDEDThis is another paragraph with _italic_ text and `code` here```

> This is another paragraph with _italic_ text and `code` here

This is another paragraph with _italic_ text and `code` here

"""

node = markdown_to_html_node(md)


print(node.to_html())