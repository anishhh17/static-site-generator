import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        node = HTMLNode("p", "This is a p tag")
        self.assertEqual(str(node), "HTMLNode(p, This is a p tag, None, None)")

    def test_props_to_html(self):
        p = HTMLNode("p", "This is a p tag")
        h2 = HTMLNode("h2", "This is a h2 tag")
        div = HTMLNode("div", "This is a div tag")
        a = HTMLNode("a", "This is an a tag", None, { "href" : "www.google.com",  "target": "_blank" })
        h1 = HTMLNode("h1", "This is a h1 tag", [div, p])
        self.assertEqual(a.props_to_html(), ' href= "www.google.com" target= "_blank"')
        
    
    def test_children(self):
        p = HTMLNode("p", "This is a p tag")
        h2 = HTMLNode("h2", "This is a h2 tag")
        a = HTMLNode("a", "This is an a tag", None, { "href" : "www.google.com",  "target": "_blank" })
        h1 = HTMLNode("h1", "This is a h1 tag")
        div = HTMLNode("div", "This is a div tag", [p, h1, h2, a])
        self.assertEqual(str(div), "HTMLNode(div, This is a div tag, [HTMLNode(p, This is a p tag, None, None), HTMLNode(h1, This is a h1 tag, None, None), HTMLNode(h2, This is a h2 tag, None, None), HTMLNode(a, This is an a tag, None, {'href': 'www.google.com', 'target': '_blank'})], None)")
    
if __name__ == "__main__":
    unittest.main()
