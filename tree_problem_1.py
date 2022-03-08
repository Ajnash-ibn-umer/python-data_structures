class Treenode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.childrens=[]
    def add_child(self,child):
        child.parent=self
        self.childrens.append(child)
    def print_tree(self,args):
        space=' ' * self.get_level() *3
        prefix=space+'|__' if self.parent else ''
        if args=='name':print(prefix+self.data[0])
        if args == 'designation': print(prefix + self.data[1] )
        if args == 'both': print(prefix + self.data[0] + " (" + self.data[1] + ")")

        if self.childrens:
            for c in self.childrens:
                c.print_tree(args)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent

        return level

def build_tree():
   root=Treenode(['Nilupul','CEO'])

   CTO=Treenode(['Chinmay','CTO'])
   Vishwa=Treenode(['Vishwa','Infrastracture Head'])
   CTO.add_child(Vishwa)

   Vishwa.add_child(Treenode(['Dhaval','Cloud Manager']))
   Vishwa.add_child(Treenode(['Abhijit','Application Head']))

   Aamir=Treenode(['Aamir','Application Head'])
   CTO.add_child(Aamir)

   Gels=Treenode(['Gels','HR manager'])
   Gels.add_child(Treenode(['Peter','Recruitment']))
   Gels.add_child(Treenode(['Waqas','Policy Manager']))

   root.add_child(CTO)
   root.add_child(Gels)
   return root






if __name__=='__main__':


    root =build_tree()
    root.print_tree('both')
