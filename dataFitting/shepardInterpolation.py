def Shepard(vals, pts, p, mu = 2):
    """
    Shepard's interpolation method,
    Inverse Distance Weighting.
    pts - points array (2D, 3D)
    [[x1, y1, z1], [x2, y2, z2]...]
    p - point vector (2D, 3D)
    [x, y]
    """
    try:
        dim = len(p)
        # Define weight function
        def W(p, pi):
            r = 0
            for i in range(dim):
                r += (p[i]-pi[i])**2
            return r**-(mu/2)
        # Get denominator sum
        denom = 0
        for i, pi in enumerate(pts):
            if (any(p!=pi)):
                denom += W(p, pi)
            else:
                return vals[i]
        # Get numerator sum
        num = 0
        for i, pi in enumerate(pts):
            num += W(p, pi)*vals[i]
        return num/denom
    except:
        print("An error occured. Check input arrays.")