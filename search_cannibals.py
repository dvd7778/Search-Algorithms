import search

# Get Function that returns the dictionary used to create the graph for the cannibals and missionaries problem
# Each vertex in the graph is a tupple with two tupples. The first of the two tupples represents the left while the other tupple represents the right side of the river.
# Inside the tupples are integers indicating the number of missionaries, number of cannibals, and if the boat is in that location or not, represented by 1 if true and 
# 0 if false.
def get_graph_dict():
    graph_dict = {
        # Left        Right
        #(M, C, B), (M, C, B)
        ((3, 3, 1), (0, 0, 0)) : {
            ((2, 3, 0), (1, 0, 1)) : 1, #
            ((1, 3, 0), (2, 0, 1)) : 1, #
            ((3, 2, 0), (0, 1, 1)) : 1, #
            ((3, 1, 0), (0, 2, 1)) : 1, #
            ((2, 2, 0), (1, 1, 1)) : 1 #
        },
        ((1, 3, 0), (2, 0, 1)) : {
            ((2, 3, 1), (1, 0, 0)) : 1 #
        },
        ((3, 1, 0), (0, 2, 1)) : {
            ((3, 2, 1), (0, 1, 0)) : 1 #
        },
        ((2, 2, 0), (1, 1, 1)) : {
            ((3, 2, 1), (0, 1, 0)) : 1, #
            ((2, 3, 1), (1, 0, 0)) : 1 #
        }, 
        ((2, 3, 1), (1, 0, 0)) : {
            ((0, 3, 0), (3, 0, 1)) : 1, #
            ((2, 1, 0), (1, 2, 1)) : 1, #
            ((1, 2, 0), (2, 1, 1)) : 1 #
        },
        ((3, 2, 1), (0, 1, 0)) : {
            ((1, 2, 0), (2, 1, 1)) : 1, #
            ((3, 0, 0), (0, 3, 1)) : 1, #
            ((2, 1, 0), (1, 2, 1)) : 1 #
        },
        ((0, 3, 0), (3, 0, 1)) : {
            ((1, 3, 1), (2, 0, 0)) : 1 #
        },
        ((2, 1, 0), (1, 2, 1)) : {
            ((3, 1, 1), (0, 2, 0)) : 1, #
            ((2, 2, 1), (1, 1, 0)) : 1 #
        },
        ((1, 2, 0), (2, 1, 1)) : {
            ((2, 2, 1), (1, 1, 0)) : 1, #
            ((1, 3, 1), (2, 0, 0)) : 1 #
        },
        ((3, 0, 0), (0, 3, 1)) : {
            ((3, 1, 1), (0, 2, 0)) : 1 #
        },
        ((1, 3, 1), (2, 0, 0)) : {
            ((1, 1, 0), (2, 2, 1)) : 1, #
            ((0, 2, 0), (3, 1, 1)) : 1 #
        },
        ((3, 1, 1), (0, 2, 0)) : {
            ((1, 1, 0), (2, 2, 1)) : 1, #
            ((2, 0, 0), (1, 3, 1)) : 1 #
        },
        ((2, 2, 1), (1, 1, 0)) : {
            ((0, 2, 0), (3, 1, 1)) : 1, #
            ((2, 0, 0), (1, 3, 1)) : 1, #
            ((1, 1, 0), (2, 2, 1)) : 1 #
        },
        ((1, 1, 0), (2, 2, 1)) : {
            ((2, 1, 1), (1, 2, 0)) : 1, #
            ((1, 2, 1), (2, 1, 0)) : 1 #
        },
        ((0, 2, 0), (3, 1, 1)) : {
            ((1, 2, 1), (2, 1, 0)) : 1, #
            ((0, 3, 1), (3, 0, 0)) : 1 #
        },
        ((2, 0, 0), (1, 3, 1)) : {
            ((3, 0, 1), (0, 3, 0)) : 1, #
            ((2, 1, 1), (1, 2, 0)) : 1 #
        },
        ((2, 1, 1), (1, 2, 0)) : {
            ((0, 1, 0), (3, 2, 1)) : 1, #
            ((1, 0, 0), (2, 3, 1)) : 1 #
        },
        ((1, 2, 1), (2, 1, 0)) : {
            ((1, 0, 0), (2, 3, 1)) : 1, #
            ((0, 1, 0), (3, 2, 1)) : 1 #
        },
        ((0, 3, 1), (3, 0, 0)) : {
            ((0, 1, 0), (3, 2, 1)) : 1 #
        },
        ((3, 0, 1), (0, 3, 0)) : {
            ((1, 0, 0), (2, 3, 1)) : 1 #
        }, 
        ((0, 1, 0), (3, 2, 1)) : {
            ((1, 1, 1), (2, 2, 0)) : 1, #
            ((0, 2, 1), (3, 1, 0)) : 1 #
        },
        ((1, 0, 0), (2, 3, 1)) : {
            ((2, 0, 1), (1, 3, 0)) : 1, #
            ((1, 1, 1), (2, 2, 0)) : 1 #
        },
        ((1, 1, 1), (2, 2, 0)) : {
            ((0, 0, 0), (3, 3, 1)) : 1
        }, 
        ((0, 2, 1), (3, 1, 0)) : {
            ((0, 0, 0), (3, 3, 1)) : 1
        },
        ((2, 0, 1), (1, 3, 0)) : {
            ((0, 0, 0), (3, 3, 1)) : 1
        },
        ((0, 0, 0), (3, 3, 1)) : {
            ((1, 0, 1), (2, 3, 0)) : 1,
            ((0, 1, 1), (3, 2, 0)) : 1
        }
    }
    return graph_dict


# Graph class taken from the aimacode repository
class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
# Graph Problem class to create the problem from a given graph and solve it
class GraphProblem(search.Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph
        
   # Function that takes a vertex as input and returns a list of the vertices connected to it
    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or search.np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = search.np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

   # Heuristic function using the straight-line distance
    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(search.distance(locs[node], locs[self.goal]))

            return int(search.distance(locs[node.state], locs[self.goal]))
        else:
            return search.np.inf
        
# Breadth first search method from the Aimacode repository, modified to calculate the amount of steps found from the initial to the goal,
# the total number of visited vertices and to not permit moves where there are more cannibals than missionaries in either side of the river.
# Returns the Goal node, the amount of steps from the taken path, the number of vertices visited in total, and the path taken to reach the goal.
def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """
    node = search.Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = search.deque([(node, 0, [])])
    explored = set()
    while frontier:
        q_pop = frontier.popleft()
        node = q_pop[0]
        q_pop[2].append(node)
        if node.state in explored:
           continue
        explored.add(node.state)
      #   print("Now in Node:", q_pop)
        for child in node.expand(problem):
            child_str = str(child.state)
            if child.state not in explored:
                if int(child_str[2]) == 0 or int(child_str[13]) == 0 or (int(child_str[2]) >= int(child_str[5]) and int(child_str[13]) >= int(child_str[16])):
                    if problem.goal_test(child.state):
                        return (child, q_pop[1] + 1, q_pop[2]), len(explored)
                    frontier.append((child, q_pop[1] + 1, q_pop[2][::]))
    return None

# Start and goal states of the problem    
start_state = ((3, 3, 1), (0, 0, 0))
goal_state = ((0, 0, 0), (3, 3, 1))        

# Creating graph and problem objects 
graph = Graph(get_graph_dict(), False)
problem_3_11 = GraphProblem(start_state, goal_state, graph)

# Using Breadth first search to reach the goal
bfs = breadth_first_graph_search(problem_3_11)

# Printing results from the Breadth first search
print("\nBreadth First Search:\nGoal: " + str(bfs[0][0].state) + "\nVertices in Path: " + str(bfs[0][1]) + 
      "\nTotal Visited Vertices: " + str(bfs[1]) + "\nPath: " + str(bfs[0][2]))