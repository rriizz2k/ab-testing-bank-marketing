from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import confint_proportions_2indep

def conversion_diff_ci(success_a, nobs_a, success_b, nobs_b):
    low , high = confint_proportions_2indep(success_a, nobs_a, success_b, nobs_b)
    return float(low), float(high)


def compare_conversion(success_a, nobs_a, success_b, nobs_b):
    stat, pval = proportions_ztest(count=[success_a, success_b], nobs=[nobs_a, nobs_b])

    return pval



#print(type(conversion_diff_ci(50, 500, 52, 500)))
#print(compare_conversion(50, 500, 52, 500))