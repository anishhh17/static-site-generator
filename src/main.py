from textnode import TextNode, TextType

def main():
	dummy1  = TextNode("This is a text Node", TextType.BOLD, "https://www.boot.dev")
	dummy2  = TextNode("This is a text Node", TextType.BOLD, "https://www.boot.dev")
	print(dummy1 == dummy2)
main()
