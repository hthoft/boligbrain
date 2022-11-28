def singleListReducer(lst, featuresLength):
    """
    Takes a single list and reduces it dimensions. This function is meant to be used
    in conjuction with the function below called "tupleDimensionReducer".
    """
    reducedList = []
    for i in range(featuresLength - 1):
        appender = float(lst[i] * 2 / 3) + float(lst[i + 1] * 1 / 3)
        reducedList.append(appender)
    return reducedList


# print(singleListReducer(lstt, featureLength))

def tupleDimensionReducer(tupleInput, featuresLength):
    """
    This function takes a tuple and reduces its dimensionality by 1.
    It does this by taking a "weighted average" between 2 dimensions and then adding them together.
    The first element in the tuple weights 2/3 while the second element weights 1/3.
    That pattern will continue trickling down until the last dimension has been reached.
    """

    # First we change the tuples into variables of type list. This makes us able to edit elements in them.
    for i in range(len(tupleInput)):
        tupleInput[i] = list(tupleInput[i])

    for i in range(len(tupleInput)):
        tupleInput[i] = singleListReducer(tupleInput[i], featuresLength)
    for i in range(len(tupleInput)):
        tupleInput[i] = tuple(tupleInput[i])
    return tupleInput

def sequencerBM(propertyList):
    """
    This function takes a list of tuples, reffered to as "propertyList", sorts them
    and then arranges them to alternate between lowest and highest.
    This ensures that BM avoids putting two complex modules right after each other.
    """
    listSorted = sorted(propertyList)

    listRevSorted = []

    # The following code sorts the list of tuples alternating with the smallest value and then the higest value,
    # starting from the lowest value.
    rev = True
    for i in range(len(listSorted)):
        if (i % 2) == 0:
            # listRevSorted.append(2)
            listRevSorted.append(listSorted[-1])
            listSorted.pop(-1)
        elif (i % 2) == 1:
            # listRevSorted.append(1)
            listRevSorted.append(listSorted[0])
            listSorted.pop(0)

    for i in range(len(listRevSorted)):
        if "End" in listRevSorted[i]:
            print("End is nigh" + " in number" + str(i))
            listRevSorted.append(listRevSorted[i])
            listRevSorted.pop(i)

    return listRevSorted