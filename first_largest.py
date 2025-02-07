"""
Python program to find the largest element and its location.
"""

def largest_element(a,loc=False):
    """ Return the largest element of a sequence a."""

    try:
        maxval=a[0]
        maxloc=0
        for i in range(1,len(a)):
            if a[i] > maxval:
                    maxval = a[i]
                    maxloc = i
            if loc == True:
                return maxval,maxloc
        return maxval
    except TypeError:
            print("Error: Number / String mis-match")
    except:
        print("Undefined Error")
        raise

if __name__ == "__main__":

    a = [5,3,"words",1,2]
    print("Largest element is {:}".format(largest_element(a)))
