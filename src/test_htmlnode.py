import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        
        
        node3 = LeafNode(None, "Hello, world!")



        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        with self.assertRaises(ValueError) as context:
            node1 = LeafNode("p", None)
        self.assertEqual(str(context.exception), "LeafNode must have a value.")

        
        with self.assertRaises(ValueError) as context:
             node2 = LeafNode(None, None)
        self.assertEqual(str(context.exception), "LeafNode must have a value.")
        

        self.assertEqual(node3.to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "the first grandchild")
        grandchild_node2 = LeafNode("i", "the second grandchild")
        grandchild_node3 = LeafNode(None, "the third grandchild")
        grandchild_node4 = LeafNode("b", "the fourth grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        child_node2 = ParentNode("span", [grandchild_node3, grandchild_node4])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>the first grandchild</b><i>the second grandchild</i></span><span>the third grandchild<b>the fourth grandchild</b></span></div>",
        )

    def test_to_html_with_no_child(self):
        parent_node = ParentNode("div", None)
        with self.assertRaisesRegex(ValueError, "ParentNode must have children"):
            parent_node.to_html()

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_no_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode(None, [child_node])

        with self.assertRaisesRegex(ValueError, "ParentNode must have a tag"):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()
