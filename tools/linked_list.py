class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "|".join([str(d) for d in self.data]) if isinstance(self.data, tuple) else self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        str_nodes = []
        for node in nodes:
            if isinstance(node, Node):
                str_nodes.append(node.data[0])
  
        return " -> ".join(str_nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def traverse(self):
        temp = self.head
        while temp:
            try:
                if temp.data.data:
                    print(temp.data.data[0], end='-->')
            except AttributeError:
                print(temp.data, end='-->')
            temp = temp.next

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
    
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
    
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
    
        raise Exception("Node with data '%s' not found" % target_node_data)

class Graph:
    def __init__(self, vertices, directed=True):
        self.vertices = vertices
        self.vertices_list = [LinkedList() for i in range(0, self.vertices)] #create a list to represent the graph
        self.directed = directed 
    
    #insert an edge in the graph
    def insert_edge(self, edge, index1, index2):
        vertex1, vertex2 = edge

        # add an edge from vertex1 to vertex2
        self.vertices_list[index2].add_first(Node(vertex1))
        print("vertices list:", self.vertices_list)
        if not self.directed: #if the graph is undirected, add an edge from vertex2 to vertex1 as well
            self.vertices_list[index1].add_first(Node(vertex2))

    # display the graph
    def display_graph(self, names=None):
        for i in range(0, self.vertices):
            try:
                print(names[i], end="\t")
                self.vertices_list[i].traverse()
                print('none')

            except TypeError:
                print(i, end="\t")
                self.vertices_list[i].traverse()
                print('none')

          
