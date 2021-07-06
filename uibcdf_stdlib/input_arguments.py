import pyunitwizard as puw
import numpy as np
from .lists_and_tuples import is_list_or_tuple

def check_input_argument(argument, argument_type, shape=None, dimensionality=None):

    if argument is 'ndarray':
        argument=np.ndarray

    if is_list_or_tuple(argument_type):

        output=False

        for aux_argument_type in argument_type:
            aux_output = _check_single_input_argument(argument, aux_argument_type, shape=shape,
                    dimensionality=dimensionality, value_type=value_type)
            if aux_output:
                output=True
                break

    else:

        output = _check_single_input_argument(argument, aux_argument_type, shape=shape,
                dimensionality=dimensionality, value_type=value_type)

    return output

def _check_single_input_argument(argument, argument_type, shape=None, dimensionality=None, value_type=None):

    if argument_type is 'quantity':

        output = local_puw.check(argument, dimensionality=dimensionality, value_type=value_type, shape=shape)

    else:

        output = (type(argument)==argument_type)

        if output:
            if shape is not None:
                output = (np.shape(argument)==shape)

    return output

