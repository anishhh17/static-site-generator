import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        node = LeafNode("p", "This is a p tag")
        self.assertEqual(str(node), "HTMLNode(p, This is a p tag, None, None)")

    def test_to_html(self):
        p = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(p.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_children(self):
        a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(a.to_html(), '<a href= "https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
