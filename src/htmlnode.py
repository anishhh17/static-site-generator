class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props 

  def to_html(self):
    raise NotImplemented()
  
  def props_to_html(self):
    return " " + " ".join(list(map(lambda i : i + '= "' + self.props[i] + '"', self.props)))

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"