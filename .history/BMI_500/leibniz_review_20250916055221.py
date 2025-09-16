def leibniz_pi (n:int):
    """
    n : Number of terms to include (n >= 1, int)

    Returns: Approximate pi (float)
    """
    if n <= 0:
        return 0.0
    
    pi = 0.0
    for k in range(n):
        pi += ((-1.0)**k) / (2.0 * k + 1.0)

    print(pi * 4)
    return pi * 4