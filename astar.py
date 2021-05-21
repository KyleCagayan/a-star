import math


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x_coordinate = x
        self.y_coordinate = y


class Graph:
    vertices = {}
    edges = []  # this is your matrix
    edge_indices = {}
    children = [] # name, gscore

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            # print("Vertex added: " + vertex.name)
            return True
        else:
            return False

    def add_edge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def get_x(self, name):
        return self.vertices[name].x_coordinate

    def get_y(self, name):
        return self.vertices[name].y_coordinate

    def print_graph(self):
        for v, i in self.edge_indices.items():
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print("%5.1f" % (self.edges[i][j]), end='')
            print(' ')

    def print_vertices(self):
        for x in g.vertices:
            print(x)

    def print_vertex(self, name):
        print(g.vertices[name])

    def weight_calculator(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def fn_calculator(self, gn, hn):
        fn = gn + hn
        return fn

    def find_children(self, name_index_dict, current_key, current_g_score, index_name_dict, closedset, edges_and_weights):
        self.children.clear()
        indexNum = 0
        for index in g.edges[name_index_dict[current_key]]:  # finding neighbors of current
            if indexNum > len(g.edges[name_index_dict[current_key]]) - 1:
                return
            if index != 0:
                self.children.append((index_name_dict[indexNum], math.inf))
            indexNum = indexNum + 1
        for child in self.children:
            for i in closedset:
                if child == i[0]:
                    self.children.remove(child)

    def reconstruct_path(self, current_key, camefrom):
        node_path = []
        record = current_key
        while record in camefrom:
            node_path.insert(0, record)
            record = camefrom[record]
        node_path.insert(0, record)
        return node_path


    #   TODO IMPLEMENT A* ALGORITHM
    def a_star(self, edges_and_weights):

        heuristic = {
            'SS': 36.6742416417845,

            'A1': 36.71511950137164,
            'A2': 34.539832078341085,
            'A3': 21.400934559032695,
            'A4': 24.758836806279895,

            'B1': 34.48187929913333,
            'B2': 34.36568055487916,
            'B3': 28,
            'B4': 25.317977802344327,
            'B5': 29.154759474226502,

            'C1': 26.40075756488817,
            'C2': 22.360679774997898,
            'C3': 22.825424421026653,

            'D1': 20.8806130178211,
            'D2': 20,
            'D3': 16.0312195418814,
            'D4': 14.142135623730951,

            'E1': 21.93171219946131,
            'E2': 18.35755975068582,
            'E3': 17.029386365926403,

            'F1': 15.620499351813308,
            'F2': 12,
            'F3': 6,
            'F4': 11.661903789690601,

            'G1': 18.973665961010276,
            'G2': 19.235384061671343,
            'G3': 15.811388300841896,
            'G4': 12.083045973594572,
            'G5': 13.341664064126334,
            'G6': 17.26267650163207,

            'H1': 11.180339887498949,
            'H2': 5.385164807134504,
            'H3': 3,
            'H4': 3,

            'GG': 0}
        openset = {}  # holds my vertexes ("name": f(x), g(x))
        closedset = set()  # holds vertex.name : f(n)
        camefrom = {}  # every edge weight added until current

        name_index_dict = {}  # holds VERTEX NAME : INDEX
        index_name_dict = {}  # holds INDEX : VERTEX NAME

        openset['SS'] = (math.inf, 0)  # (name: f(x), g(x))




        i = 0
        for x in g.vertices:  # index each vertex name with a number
            name_index_dict[x] = i
            i = i + 1

        i = 0
        for x in g.vertices:  # index each number to a vertex name
            index_name_dict[i] = x
            i = i + 1


        # start A*
        while len(openset) != 0:

            current_key = min(openset, key=lambda t: openset[t][0])  # key string
            (current_f_score, current_g_score) = openset[current_key]  # (f score, g score)

            if current_key == 'GG':
                node_path = self.reconstruct_path(current_key, camefrom)
                print("The path is: ")
                for item in node_path:
                    print(item + " ", end='')
                break

            del openset[current_key]
            closedset.add(current_key)
            self.find_children(name_index_dict, current_key, current_g_score, index_name_dict, closedset, edges_and_weights)
            for child in self.children:
                if child[0] in closedset:
                    continue
                try:
                    tentative_g_score = current_g_score + edges_and_weights[current_key + child[0]]
                except KeyError:
                    tentative_g_score = current_g_score + edges_and_weights[child[0] + current_key]
                f_score = heuristic[child[0]] + tentative_g_score
                aaa = current_g_score
                bbb = child[1]
                try:
                    if tentative_g_score < child[1]:
                        f_score = heuristic[child[0]] + tentative_g_score
                        camefrom[child[0]] = current_key
                        del openset[child[0]]
                        openset[child[0]] = (f_score, tentative_g_score)
                except KeyError:
                    openset[child[0]] = (f_score, tentative_g_score)

# PROGRAM START
g = Graph()
edge_location = [
    'SSA1',  # 0
    'SSA2',  # 1
    'SSB1',  # 2
    'SSB2',  # 3
    'A1A2',  # 4
    'A1A4',  # 5
    'A2A3',
    'A2B1',
    'A2B5',
    'A2C1',
    'A2C3',  # 10
    'A3B5',
    'A3C1',
    'A3C2',
    'A3C3',
    'B1B2',
    'B1B3',
    'B2B3',
    'B3B4',
    'B3C2',  # 20
    'B4C2',
    'B4C1',
    'B4B5',
    'B5C2',
    'B5C1',  # 25
    'C1C2',
    'C1C3',
    'C2C3',
    'C3D1',
    'C3D4',
    'C3E2',
    'D1D2',
    'D1D4',
    'D1E1',
    'D1E2',
    'D1F1',
    'D2D3',
    'D3D4',
    'D3F2',
    'D4D2',
    'D4E2',
    'D4F1',
    'D4F2',
    'E1E2',
    'E1E3',
    'E1F4',
    'E1G3',
    'E1G4',
    'E1G1',
    'E1G2',
    'F1F2',
    'F1F3',
    'F1G3',
    'F1G4',
    'F1G3',
    'F1G4',
    'F1G3',
    'F1H1',
    'F2F3',
    'F3F4',
    'F3H2',
    'F3H3',
    'F4H2',
    'F4H1',
    'F4G3',
    'F4G4',
    'G1G2',
    'G1G6',
    'G2G3',
    'G3G4',
    'G4G5',
    'G4H1',
    'G4H2',
    'G5G6',
    'G5H1',
    'G5H2',
    'H1GG',
    'H1H2',
    'H3H2',
    'H3H4',
    'H3GG',
    'H4H1',
    'H4H3'
]  # TODO finish inputting the rest of the obstacle edges
complete_edge = {}

g.add_vertex(Vertex('SS', 1, 3))
g.add_vertex(Vertex('GG', 34, 19))

g.add_vertex(Vertex('A1', 2, 1))
g.add_vertex(Vertex('A2', 2, 6))
g.add_vertex(Vertex('A3', 17, 6))
g.add_vertex(Vertex('A4', 17, 1))

g.add_vertex(Vertex('B1', 1, 9))
g.add_vertex(Vertex('B2', 0, 14))
g.add_vertex(Vertex('B3', 6, 19))
g.add_vertex(Vertex('B4', 9, 15))
g.add_vertex(Vertex('B5', 7, 8))

g.add_vertex(Vertex('C1', 10, 8))
g.add_vertex(Vertex('C2', 12, 15))
g.add_vertex(Vertex('C3', 14, 8))

g.add_vertex(Vertex('D1', 14, 13))
g.add_vertex(Vertex('D2', 14, 19))
g.add_vertex(Vertex('D3', 18, 20))
g.add_vertex(Vertex('D4', 20, 17))

g.add_vertex(Vertex('E1', 19, 3))
g.add_vertex(Vertex('E2', 18, 10))
g.add_vertex(Vertex('E3', 23, 6))

g.add_vertex(Vertex('F1', 22, 9))
g.add_vertex(Vertex('F2', 22, 19))
g.add_vertex(Vertex('F3', 28, 19))
g.add_vertex(Vertex('F4', 28, 9))

g.add_vertex(Vertex('G1', 28, 1))
g.add_vertex(Vertex('G2', 25, 2))
g.add_vertex(Vertex('G3', 25, 6))
g.add_vertex(Vertex('G4', 29, 8))
g.add_vertex(Vertex('G5', 31, 6))
g.add_vertex(Vertex('G6', 31, 2))

g.add_vertex(Vertex('H1', 32, 8))
g.add_vertex(Vertex('H2', 29, 17))
g.add_vertex(Vertex('H3', 31, 19))
g.add_vertex(Vertex('H4', 34, 16))


# TODO ADD THE REST OF THE OBSTACLES

for edge in edge_location:  # appending edge weight + edges into 'complete_edge' as a tuple
    g.get_x(edge[:2])

    x1 = g.get_x(edge[:2])
    y1 = g.get_y(edge[:2])
    x2 = g.get_x(edge[2:])
    y2 = g.get_y(edge[2:])
    edge_weight = g.weight_calculator(x1, y1, x2, y2)
    g.add_edge(edge[:2], edge[2:], edge_weight)
    complete_edge[edge] = edge_weight

# for x in complete_edge:
    # print(x)
# print("      SS   GG   A1   A2   A3   A4   B1   B2   B3   B4   B5   C1   C2   C3")
# g.print_graph()

g.a_star(complete_edge)

# g.print_vertices()
# print(complete_edge[0][1])

# todo  calculate f(n) for all nodes         f(n) = g(n) + h(n)
#       g(n) = distance travelled
#       h(n) = straight line distance
#       compare nodes with current node      current = node with lowest f(n) value
#       fix print graph method
