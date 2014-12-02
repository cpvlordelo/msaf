"""Config for the OLDA algorithm."""
import os

# OLDA params
config = {
    #"transform": os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              #"EstBeats.npy")
    "transform": os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "caca_path", "EstBeats_data.pickle")
}

algo_id = "olda"
is_boundary_type = True
is_label_type = False
