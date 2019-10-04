# Calculate a "sliding window" of system load averages.
# 1 min, 5 min, 15 min
import statistics

load_samples = [0.34, 0.93, 0.99, 1.04, 1.34, 2.34, 2.10, 1.21, 0.89, 0.12, 1.98, 1.00, 0.91, 0.32, 0.43, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00]
load_samples = [0.10, 80.10, 0.30, 0.40, 0.70, 1.00, 5.00, 2.00, 2.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00, 6.00]

#######################
# Scratch Pad
# Minute   1m    5m    15m
# 0        0.34  0.34  0.34
# 1        0.93  (0.93+0.34)/2 (0.93+0.34)/2
# 2        0.99  (0.93+0.34+0.99)/3 ...
# ...
# 6              sum(ls[1:7])/5     


def foo():
    pass


SPAN_MINS = len(load_samples) # mins to run

print("Minute \t\tCPU Load: 1m         5m         15m")
for minute in range(0, SPAN_MINS):
    win5_start = max(minute - 5, 0)
    win15_start = max(minute - 15, 0)
    win_end = minute + 1
    # This doesnt work because slicing is exclusive, and :None is needed to include the last
    la_1 = load_samples[minute]
    la_5 = statistics.mean(load_samples[win5_start:win_end])
    la_15 = statistics.mean(load_samples[win15_start:win_end])

    print(f"{minute}  \t\t    {la_1:10.2f} {la_5:10.2f} {la_15:10.2f}   >{win5_start}/{win15_start}")

