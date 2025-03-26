class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        #raise NotImplementedError(("to_html method not implemented"))
        children_string = "".join(self.children)
        return f"<{self.tag}>{children_string}</{self.tag}>"

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'

        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        if value is None:  # Enforce a valid value during initialization
            raise ValueError("LeafNode must have a value.")
    
    def to_html(self):
        if not self.tag:
            return str(self.value)
        
        return f"<{self.tag}{self.props_to_html()}>{str(self.value)}</{self.tag}>"

    def add_child(self, child):
        raise AttributeError("LeafNode cannot have children.")
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        

        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        elif self.children is None:
            raise ValueError("ParentNode must have children.")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        

    
