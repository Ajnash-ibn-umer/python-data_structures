class Treenode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.childrens=[]
    def add_child(self,child):
        child.parent=self
        self.childrens.append(child)
    def print_tree(self):
        space=' ' * self.get_level() *3
        prefix=space+'|__' if self.parent else ''
        print(prefix+self.data)
        if self.childrens:
            for c in self.childrens:
                c.print_tree()
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent

        return level
def build_tree():
    root=Treenode('electronics')

    laptop=Treenode('laptop')
    laptop.add_child(Treenode('asus'))
    laptop.add_child(Treenode('mac'))
    laptop.add_child(Treenode('omen'))

    mobile=Treenode('mobile')
    mobile.add_child(Treenode('iphone'))
    mobile.add_child(Treenode('nokia'))
    mobile.add_child(Treenode('s22'))


    root.add_child(laptop)
    root.add_child(mobile)

    return root

if __name__=='__main__':
    root= build_tree()
    root.print_tree()
    # print(root.get_level())
    pass
