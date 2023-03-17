def sort_dictionary(dict):
    def sort(key):
        return dict.get(key)[1]

    rlist = list(dict.keys())
    rlist.sort(key=sort) 
    newOutput = []
    for x in rlist: 
        appendTuple = (x, dict.get(x)[0])
        newOutput.append(appendTuple)

    return newOutput
