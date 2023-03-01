#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def to_string(node_chain):
    """ 
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        # print the data
        result = '[ {} |'.format(str(walker.get_data()))
        while walker.get_next() is not None:
            walker = walker.get_next()
            value = walker.get_data()
            # represent the next with an arrow-like figure
            result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' *-]-->[ {} | / ]'.format(str(walker.get_data()))

    return result
