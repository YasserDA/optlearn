import numpy as np

from optlearn import graph_utils


class buildFeatures():
    def __init__(self, function_names):
        self.function_names = function_names
        self.get_funcs()

    def set_function_names(self, function_names):
        """ Set the names of the functions to be used """
        
        self.function_names = function_names
        self.get_funcs()

    def get_funcs(self):
        """ Get the functions from graph_utils.py """
        
        self._funcs = [graph_utils.functions[item] for item in function_names]
        
    def compute_feature(self, graph, func):
        """ Compute a specific feature for the graph """
        
        return func(graph)

    def compute_features(self, graph):
        """ Compute the feature vector for the graph """
        
        data = [self.compute_feature(graph, func) for func in self.funcs]
        return np.stack(data, axis=1)