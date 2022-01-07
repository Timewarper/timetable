from sympy.utilities.iterables import multiset_permutations

# Defining functions

def sumCombinatrics(sum, min, size):
    tuples = []
    if size <= 1:
        return [[sum]]
    for i in range(min, sum):
        partial = sumCombinatrics(sum-i, min, size-1)
        tuples += map(lambda t: [*sorted([i] + list(t))], partial)
    k = []
    for j in [list(i) for i in sorted(set([tuple(i) for i in tuples]))]:
        k += list(multiset_permutations(j))
    return k


def filter(array):
    added = sum(array[0])
    if added <= 5:
        for set in array:
            for value in set:
                if value >= 2:
                    set.remove(value)
    elif added > 5:
        for set in array:
            for value in set:
                if value >= 3:
                    set.remove(value)
    set = 0
    while set < len(array) - 1:
        if len(array[set]) != 5:
            array.pop(set)
        else:
            set += 1
    return array

# Start timetable creation code
def main():

    arTime = [[1, 0, 0, 0, 0]]
    csTime = [[0, 1, 0, 0, 0]]
    coTime = filter(sumCombinatrics(2, 0, 5))
    dt3dTime = filter(sumCombinatrics(2, 0, 5))
    dtTime = filter(sumCombinatrics(2, 0, 5))
    drTime = [[0, 0, 1, 0, 0]]
    frTime = filter(sumCombinatrics(3, 0, 5))
    ggTime = filter(sumCombinatrics(4, 0, 5))
    geTime = filter(sumCombinatrics(2, 0, 5))
    grTime = filter(sumCombinatrics(1, 0, 5))
    hiTime = filter(sumCombinatrics(3, 0, 5))
    # laTime = filter(sumCombinatrics(2, 0, 5))
    # muTime = [[0, 0, 0, 1, 0]]
    # peTime = filter(sumCombinatrics(2, 0, 5))
    # rsTime = filter(sumCombinatrics(2, 0, 5))
    # tripTime = filter(sumCombinatrics(6, 0, 5)))
    # spTime = filter(sumCombinatrics(3, 0, 5))

    solutions = []

    for ar in arTime:
        for cs in csTime:
            for co in coTime:
                for dt3d in dt3dTime:
                     for dt in dtTime:
                         for dr in drTime:
                             for fr in frTime:
                                 for gg in ggTime:
                                     for ge in geTime:
                                         for gr in grTime:
                                             for hi in hiTime:
                #                                 for la in laTime:
                #                                     for mu in muTime:
                #                                         for pe in peTime:
                #                                             for rs in rsTime:
                #                                                 for trip in tripTime:
                #                                                     for sp in spTime:
                                                                        possible = True
                                                                        for i in range(0,5):
                                                                            sumLessons = ar[i] + cs[i] + co[i] + dt3d[i] + dt[i] + dr[i] + fr[i] + gg[i] + ge[i] + gr[i] + hi[i] #+ la[i] + mu[i] + pe[i] + rs[i] + trip[i] + sp[i]
                                                                            if sumLessons > 5:
                                                                                possible = False
                                                                                break
                                                                        if possible:
                                                                            solutions += [ar, cs, co, dt3d, dt, dr, fr, gg, ge, gr, hi]#, la, mu, pe, rs, trip, sp]
    return solutions