ref = [1, 2, 3, 4, 2, 3, 1]
n = 3

memory = []
first = 0
hit = 0
miss = 0

print("Page   Frames        Result")
for p in ref:
    if p in memory:
        hit += 1
        result = "Hit"
    else:
        miss += 1
        result = "Fault"
        if len(memory) < n:
            memory.append(p)
        else:
            memory[first] = p
            first = (first + 1) % n
    print(" ", p, "   ", str(memory).ljust(12), result)

total = len(ref)
print()
print("Total Hits   :", hit)
print("Total Faults :", miss)
print("Hit Ratio    :", round(hit / total * 100, 2), "%")
print("Fault Ratio  :", round(miss / total * 100, 2), "%")
