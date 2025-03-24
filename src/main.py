from textnode import *
from htmlnode import *


def main():
    node = TextNode("This is a text node", TextType.LINK, "www.google.com")
    html_node = node.text_node_to_html_node()
    print(html_node)

    """    
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)
    htmlnode = HTMLNode("a", "Hello World", None, {"href": "https://www.google.com", "target": "_blank",})
    print(htmlnode.props_to_html())
    print(htmlnode)
    leafnode = LeafNode("p", "Hello World")
    print(leafnode.to_html())

    parentnode = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)

    print(parentnode.to_html())
    """


main()
