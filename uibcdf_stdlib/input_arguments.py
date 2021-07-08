import pyunitwizard as puw
import numpy as np
from .lists_and_tuples import is_list_or_tuple

def check_input_argument(argument, argument_type, shape=None, dtype_name=None, dimensionality=None,
                         value_type=None, unit=None):

    if argument is 'ndarray':
        argument=np.ndarray

    if is_list_or_tuple(argument_type):

        output=False

        for aux_argument_type in argument_type:
            aux_output = _check_single_input_argument(argument, aux_argument_type, shape=shape,
                    dtype_name=dtype_name, dimensionality=dimensionality, value_type=value_type, unit=unit)
            if aux_output:
                output=True
                break

    else:

        output = _check_single_input_argument(argument, aux_argument_type, shape=shape,
                dtype_name=dtype_name, dimensionality=dimensionality, value_type=value_type, unit=unit)

    return output

def _check_single_input_argument(argument, argument_type, shape=None, dtype_name=None,
                                 dimensionality=None, value_type=None, unit=None):

    if argument_type is 'quantity':

        output = local_puw.check(argument, dimensionality=dimensionality, value_type=value_type,
                                 shape=shape, dtype_name=dtype_name, unit=unit)

    else:

        output = (type(argument)==argument_type)

        if output:
            if shape is not None:
                output = (np.shape(argument)==tuple(shape))

        if output:
            if dtype_name is not None:
                try:
                    aux_dtype_name=argument.dtype.name
                    output = (aux_dtype_name==dtype_name)
                except:
                    output = False

    return output

