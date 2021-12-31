from riskquant import pertloss

# pert = pertloss.PERTLoss(50, 1000, 0, 0.3, 0.1, 4)
pert = pertloss.PERTLoss(50, 1_000_000, 0, 0.3, 0.1, 4)

# n = 100
# lst = []
# for i in range(100):
#     losses = pert.simulate_losses_one_year()
#     print ("Year ", i, " - ", losses)

losses = pert.simulate_years(40000)

summary = pert.summarize_loss(losses)

# print(summary)


print(
    "minimum = ", f'{summary["minimum"]:,}', "\n", 
    "tenth_percentile = ", f'{summary["tenth_percentile"]:,}', "\n", 
    "mode = ", f'{summary["mode"]:,}', "\n", 
    "median = ", f'{summary["median"]:,}', "\n", 
    "ninetieth_percentile = ", f'{summary["ninetieth_percentile"]:,}' , "\n", 
    "maximum = ", f'{summary["maximum"]:,}'
)