#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

import node as N

def sumnc(node_chain):
    """
    Purpose:
    Given a node chain with numeric data values, calculate
    the sum of the data values.

    Pre-conditions:
    :param node_chain: a node-chain, possibly empty, containing
                       numeric data values

    Post-condition:
    None

    Return:
    :return: the sum of the data values in the node chain
    """
    # initialize total to 0
    total = 0
    # set curr to first node of the chain
    curr = node_chain
    # loop over the chain
    while curr is not None:
        total += curr.get_data() # add the value of curr to total
        curr = curr.get_next() # move curr to next node

    return total

def count_in(node_chain, value):
    """
    Purpose:
    Counts the number of times a value appears in a node chain

    Pre-conditions:
    :param node_chain: a node chain, possibly empty
    :param value: a data value

    Return:
    :return: The number of times the value appears in the node chain
    """
    if node_chain is None:
        return 0
    elif node_chain['data'] == value:
        return 1 + count_in(node_chain['next'], value)
    else:
        return count_in(node_chain['next'], value)

def replace_in(node_chain, target, replacement):
    """
    Purpose:
    Replaces each occurrence of the target value with the replacement

    Pre-conditions:
    :param node_chain: a node-chain, possibly empty
    :param target: a value that might appear in the node chain
    :param replacement: the value to replace the target

    Post-conditions:
    Each occurrence of the target value in the chain is replaced with
    the replacement value.

    Return:
    None
    """
    if node_chain is not None:
        if node_chain['data'] == target:
            node_chain['data'] = replacement
        replace_in(node_chain['next'], target, replacement)
