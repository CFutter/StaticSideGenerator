import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        node4 = TextNode("This is a different text node", TextType.ITALIC, url = None)     
        node5 = TextNode("This is a text node", TextType.ITALIC, url = None)
        node6 = TextNode("This is a text node", TextType.ITALIC, url = None)
        node7 = TextNode("This is a text node", TextType.ITALIC, url = "www.google.com")
        node8 = TextNode("This is a text node", TextType.ITALIC, url = None)


        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node6, node7)
        self.assertNotEqual(node4, node8)



class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")



if __name__ == "__main__":
    unittest.main()