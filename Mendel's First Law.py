def dominant_probability(k, m, n):
    # Total number of organisms
    N = k + m + n


    p_DD = (k / N) * ((k - 1) / (N - 1))


    p_Dd = (m / N) * ((k) / (N - 1)) + (k / N) * ((m) / (N - 1)) + (m / N) * ((m - 1) / (N - 1)) * 0.75


    p_dd = (n / N) * ((k) / (N - 1)) + (k / N) * ((n) / (N - 1)) + (n / N) * ((m) / (N - 1)) * 0.5 + (m / N) * (
                (n) / (N - 1)) * 0.5


    return p_DD + p_Dd + p_dd


print(dominant_probability(30 ,21, 29))

