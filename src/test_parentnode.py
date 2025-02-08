import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    

    def test_nested_parent(self):
      node = ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
      )
      parent_node =  ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
              node
          ],
      )
      self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")


    def test_with_props(self):
      node = ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
      )
      parent_node =  ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
              node
          ],
          {
             "href": "ayyooo.com"
          }
      )
      self.assertEqual(parent_node.to_html(), '<p href= "ayyooo.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')
       
if __name__ == "__main__":
    unittest.main()
