class Treenode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.childrens=[]
    def add_child(self,child):
        child.parent=self
        self.childrens.append(child)
    def print_tree(self,lvl):
        space=' ' * self.get_level() *3
        prefix=space+'|__' if self.parent else ''
        print(prefix+self.data)
        if self.childrens:
            for c in self.childrens:
                if lvl>self.get_level():
                    c.print_tree(lvl)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent

        return level

def build_tree():
    root=Treenode('Global')

    india=Treenode('india')
    root.add_child(india)

    gujarat=Treenode('gujarat')
    india.add_child(gujarat)

    gujarat.add_child(Treenode('Ahmedabad'))
    gujarat.add_child(Treenode('Baroda'))

    karnataka=Treenode('karnataka')
    india.add_child(karnataka)

    karnataka.add_child(Treenode('Bangluru'))
    karnataka.add_child(Treenode('Mysore'))

    usa=Treenode('USA')
    root.add_child(usa)

    new_jersey=Treenode('New Jersey')
    usa.add_child(new_jersey)
    new_jersey.add_child(Treenode('Princeton'))
    new_jersey.add_child(Treenode('Trenton'))

    california=Treenode('California')
    california.add_child(Treenode('san francisco'))
    california.add_child(Treenode('Mountain View'))
    california.add_child(Treenode('Palo Alto'))

    usa.add_child(california)

    return root


if __name__=='__main__':
    root=build_tree()
    root.print_tree(3)