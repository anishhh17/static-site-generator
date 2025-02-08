from convert_text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
import unittest

class TestTextNode(unittest.TestCase):
    def test_node(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        self.assertEqual(str(leaf), "HTMLNode(b, This is a text node, None, None)")

    def test_hrefnode(self):
        node2 = TextNode("This is a href node", TextType.LINK, "https://www.google.com")
        leaf = text_node_to_html_node(node2)
        self.assertEqual(str(leaf), "HTMLNode(a, This is a href node, None, {'href': 'https://www.google.com'})")
    
    def test_image_node(self):
        node2 = TextNode("This is a image node", TextType.IMAGE, "https://www.google.com")
        leaf = text_node_to_html_node(node2)
        self.assertEqual(str(leaf), "HTMLNode(image, , None, {'src': 'https://www.google.com', 'alt': 'This is a image node'})")
    
if __name__ == "__main__":
    unittest.main()
