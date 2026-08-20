from statsmodels.stats.proportion import proportions_ztest

def compare_conversion(success_a, nobs_a, success_b, nobs_b):
    stat, pval = proportions_ztest(count=[success_a, success_b], nobs=[nobs_a, nobs_b])

    return pval


print(compare_conversion(50, 500, 52, 500))