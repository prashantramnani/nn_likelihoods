import numpy as np
import pickle
import cddm_data_simulation as cd
import clba
import boundary_functions as bf
import os

temp = {
"lba_ndt":{
        "dgp":clba.rlba,
        "data_folder": "/users/afengler/data/kde/lba/train_test_data_ndt_20000",
        "data_folder_x7": "/media/data_cifs/afengler/data/kde/lba/train_test_data_ndt_20000",
        "output_folder": "/users/afengler/data/kde/lba/method_comparison/",
        "output_folder_x7": "/media/data_cifs/afengler/data/kde/lba/method_comparison/",
        "model_folder": "/users/afengler/data/kde/lba/keras_models/",
        "model_folder_x7": "/media/data_cifs/afengler/data/kde/lba/keras_models/",
        "param_names": ['v_0', 'v_1', 'A', 'b', 's', 'ndt'],
        "boundary_param_names": [],
        "param_bounds_network": [[1.0, 2.0], [1.0, 2.0], [0.0, 1.0], [1.5, 3.0], [0.1, 0.2], [0.0, 1.0]],
        "param_bounds_sampler": [[1.25, 1.75], [1.25, 1.75], [0.2, 0.8], [1.75, 2.75], [0.11, 0.19], [0.1, 0.9]], 
        "boundary_param_bounds": []
       },
"lba_analytic":{
        "dgp":clba.rlba,
        "data_folder": "/users/afengler/data/analytic/lba/train_test_data_kde_imit",
        "data_folder_x7": "/media/data_cifs/afengler/data/analytic/lba/train_test_data_kde_imit",
        "output_folder": "/users/afengler/data/analytic/lba/method_comparison/",
        "output_folder_x7": "/media/data_cifs/afengler/data/analytic/lba/method_comparison/",
        "model_folder": "/users/afengler/data/analytic/lba/keras_models/",
        "model_folder_x7": "/media/data_cifs/afengler/data/analytic/lba/keras_models/",
        "param_names": ['v_0', 'v_1', 'A', 'b', 's', 'ndt'],
        "boundary_param_names": [],
        "param_bounds_network": [[1.0, 2.0], [1.0, 2.0], [0.0, 1.0], [1.5, 3.0], [0.1, 0.2], [0.0, 1.0]],
        "param_bounds_sampler": [[1.25, 1.75], [1.25, 1.75], [0.2, 0.8], [1.75, 2.75], [0.11, 0.19], [0.1, 0.9]], 
        "boundary_param_bounds": []
       },
"ddm_ndt":{
    "dgp": cd.ddm_flexbound,
    "boundary": bf.constant,
    "boundary_multiplicative": True,
    "data_folder": "/users/afengler/data/kde/ddm/train_test_data_ndt_20000",
    "data_folder_x7": "/media/data_cifs/afengler/data/kde/ddm/train_test_data_ndt_20000",
    "data_folder_fcn": "/users/afengler/data/analytic/ddm/fcn_train_test_data_2000",
    "data_folder_fcn_x7": "/media/data_cifs/afengler/data/analytic/ddm/fcn_train_test_data_2000",
    #"custom_objects": {"huber_loss": tf.losses.huber_loss},
    #"fcn_custom_objects": {"heteroscedastic_loss": tf.losses.huber_loss},
    "output_folder": "/users/afengler/data/kde/ddm/method_comparison/",
    "output_folder_x7": "/media/data_cifs/afengler/data/kde/ddm/method_comparison/",
    "model_folder": "/users/afengler/data/kde/ddm/keras_models/",
    "model_folder_x7": "/media/data_cifs/afengler/data/kde/ddm/keras_models/",
    "param_names": ['v', 'a', 'w', 'ndt'],
    "boundary_param_names": [],
    "param_bounds_network": [[-2.0, 2.0], [0.5, 1.5], [0.3, 0.7], [0.0, 1.0]],   
    "param_bounds_sampler": [[-1.9, 1.9], [0.6, 1.4], [0.31, 0.69], [0.1, 0.9]],
    "boundary_param_bounds": []
    },
"ddm_analytic":{
    "dgp": cd.ddm_flexbound,
    "boundary": bf.constant,
    "boundary_multiplicative": True,
    "data_folder": "/users/afengler/data/analytic/ddm/train_test_data_20000",
    "data_folder_x7": "/media/data_cifs/afengler/data/analytic/ddm/train_test_data_20000",
    "output_folder": "/users/afengler/data/analytic/ddm/method_comparison/",
    "output_folder_x7": "/media/data_cifs/afengler/data/analytic/ddm/method_comparison/",
    "param_names": ['v', 'a', 'w', 'ndt'],
    "boundary_param_names": [],
    "boundary_param_bounds": [],
    "boundary_param_names": [],
    "param_bounds_network": [[-2.0, 2.0], [0.5, 1.5], [0.3, 0.7], [0.0, 1.0]],
    "param_bounds_sampler": [[-2.0, 2.0], [0.6, 1.5], [0.30, 0.70], [0.0, 1.0]],
    "boundary_param_bounds": []
    },
"angle_ndt":{
    "dgp": cd.ddm_flexbound,
    "boundary": bf.angle,
    "boundary_multiplicative": False,
    "data_folder": "/users/afengler/data/kde/angle/train_test_data_ndt_20000",
    "data_folder_x7": "/media/data_cifs/afengler/data/kde/angle/train_test_data_ndt_20000",
    "output_folder": "/users/afengler/data/kde/angle/method_comparison/",
    "output_folder_x7": "/media/data_cifs/afengler/data/kde/angle/method_comparison/",
    "model_folder": "/users/afengler/data/kde/angle/keras_models/",
    "model_folder_x7": "/media/data_cifs/afengler/data/kde/angle/keras_models/",
    "param_names": ["v", "a", "w", "ndt"],
    "boundary_param_names": ["theta"],
    "param_bounds_network": [[-1.5, 1.5], [0.6, 1.5], [0.3, 0.7], [0, 1]],
    "param_bounds_sampler": [[-1.51, 1.49], [0.6, 1.4], [0.31, 0.69], [0.1, 0.9]],
    "boundary_param_bounds_network": [[0, np.pi / 2 - .2]],
    "boundary_param_bounds_sampler": [[0.05, np.pi / 2 - .3]]
    },
"ornstein":{
    "dgp": cd.ornstein_uhlenbeck,
    "boundary": bf.constant,
    "boundary_multiplicative": True,
    "data_folder": "/users/afengler/data/kde/ornstein_uhlenbeck/train_test_data_20000",
    "output_folder": "/users/afengler/data/kde/ornstein_uhlenbeck/method_comparison/",
    "output_folder_x7": "/media/data_cifs/afengler/data/kde/ornstein_uhlenbeck/method_comparison/",
    "param_names": ["v", "a", "w", "g", "ndt"],
    "param_bounds_network": [[-2.0, 2.0], [0.5, 1.5], [0.3, 0.7], [-1.0, 1.0], [0.0, 1.0]],
    "param_bounds_sampler": [[-1.9, 1.9], [0.6, 1.4], [0.31, 0.69], [-0.9, 0.9], [0.1, 0.9]],
    "boundary_param_names": [],
    "boundary_param_bounds_network": [],
    "boundary_param_bounds_sampler": []
    },
"ddm_full":{
    "dgp": cd.full_ddm,
    "boundary": bf.constant,
    "boundary_multiplicative": True,
    "data_folder": "/users/afengler/data/kde/full_ddm/train_test_data_20000",
    "data_folder_x7": "/media/data_cifs/afengler/data/kde/full_ddm/train_test_data_20000",
    "output_folder": "/users/afengler/data/kde/full_ddm/method_comparison/",
    "output_folder_x7": "/media/data_cifs/afengler/data/kde/full_ddm/method_comparison/",
    "param_names": ["v", "a", "w", "ndt", "dw", "sdv", "dndt"],
    "boundary_param_names": [],
    "param_bounds_network": [[-2, 2], [0.6, 1.5], [0.3, 0.7], [0.25, 1.25], [0, 0.5], [0, 0.5], [0, 0.5]],
    "param_bounds_sampler": [[-1.9, 1.9], [0.6, 1.4], [0.31, 0.69], [0.3, 1.2], [0.05, 0.45], [0.05, 0.45], [0.05, 0.45]],
    "boundary_param_bounds_network": [],
    "boundary_param_bounds_sampler": []
    },
"ddm_fcn":{
    "dgp": cd.ddm_flexbound,
    "boundary": bf.constant,
    "boundary_multiplicative": True,
    "data_folder": "/users/afengler/data/tony/kde/ddm/train_test_data_fcn",
    "output_folder": "/users/afengler/data/kde/ddm/method_comparison_fcn/",
    "output_folder_x7": "/media/data_cifs/afengler/data/kde/ddm/method_comparison_fcn/",
    "param_names": ["v", "a", "w"],
    "boundary_param_names": [],
    "param_bounds": [[-2, 2], [0.6, 1.5], [0.3, 0.7]],
    "boundary_param_bounds": []
    }
}

pickle.dump(temp, open(os.getcwd() + "/kde_stats.pickle", "wb"))

# "ddm":{
#     "dgp": cd.ddm_flexbound,
#     "boundary": bf.constant,
#     "boundary_multiplicative": True,
#     "data_folder": "/users/afengler/data/kde/ddm/train_test_data_20000",
# #     custom_objects: {"huber_loss": tf.losses.huber_loss}
# #     fcn_path: "/users/afengler/data/tony/kde/ddm/keras_models/\
# # deep_inference08_12_19_11_15_06/model.h5"
# #    fcn_custom_objects: {"heteroscedastic_loss": tf.losses.huber_loss}
#     "output_folder": "/users/afengler/data/kde/ddm/method_comparison/",
#     "output_folder_x7": "/media/data_cifs/afengler/data/kde/ddm/method_comparison/",
#     "param_names": ['v', 'a', 'w'],
#     "boundary_param_names": [],
#     "param_bounds_network": [[-2.0, 2.0], [0.5, 1.5], [0.3, 0.7]],
#     "param_bounds": [[-1.9, 1.9], [0.6, 1.4], [0.31, 0.69]],
#     "boundary_param_bounds": []
#     },

# "lba":{
#         "dgp":clba.rlba,
#         "data_folder": "/users/afengler/data/kde/lba/train_test_data_20000",
#         "data_folder_x7": "/media/data_cifs/afengler/data/kde/lba/train_test_data_20000",
#         "output_folder": "/users/afengler/data/kde/lba/method_comparison/",
#         "output_folder_x7": "/media/data_cifs/afengler/data/kde/lba/method_comparison/",
#         "model_folder": "/users/afengler/data/kde/lba/keras_models/",
#         "model_folder_x7": "/media/data_cifs/afengler/data/kde/lba/keras_models/",
#         "param_names": ['v_0', 'v_1', 'A', 'b', 's'],
#         "boundary_param_names": [],
#         "param_bounds_network": [[1.0, 2.0], [1.0, 2.0], [0.0, 1.0], [1.5, 3.0], [0.1, 0.2]],
#         "param_bounds_sampler": [[1.25, 1.75], [1.25, 1.75], [0.2, 0.8], [1.75, 2.75], [0.11, 0.19], [0.1, 0.9]], 
#         "boundary_param_bounds": []
#        },