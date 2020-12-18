def comma_seperate_list(list_of_things):
    if len(list_of_things) == 0:
        # raise exception?
        return 'nothing'
    elif len(list_of_things) == 1:
        return f'{list_of_things[0]}'
    elif len(list_of_things) == 2:
        return f'{list_of_things[0]} and {list_of_things[1]}'
    else:
        return_string = ''
    for thing in list_of_things[:-1]:
        return_string += str(thing) + ', '
    return_string += f'and {list_of_things[-1]}'
    return return_string
