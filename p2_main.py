import sys
from graph_gen import *
from p2 import p2_has_cycle


def main():
    p2_list = list()
    if len(sys.argv) <= 1:
        p1_list = get_p2('r07')
    else:
        p1_list = get_p2(sys.argv[1])
        
    p1_list_converted = convert_p2(p2_list)
    for i in range(len(p2_list)):
        graph = nx.DiGraph(p2_list[i])
        has_cycle = True
        try:
            res = nx.find_cycle(graph)
        except:
            has_cycle = False
        if p1_has_cycle(p2_list_converted[i]) != has_cycle:
            print('Bug in the {}th graph'.format(i))
    

if __name__ == '__main__':
    main()
