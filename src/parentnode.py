from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if not self.tag:
      raise ValueError("tag missing")
    if not self.children:
      raise ValueError("children missing")
    res = f"<{self.tag}"
    if self.props:
      res += self.props_to_html()
    res += ">"
    for i in self.children:
      res += i.to_html()
    res += f"</{self.tag}>"
    return res