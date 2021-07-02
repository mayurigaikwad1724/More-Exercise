marks = [[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
counter1=0
while counter1 < len(marks):
    small_list_length=len(marks[counter1])
    largest = marks[0][0]
    counter2=0
    while counter2 < small_list_length:
        if marks[counter1][counter2]>largest:
            largest=marks[counter1][counter2]
        counter2 = counter2+1
    counter1 = counter1+1
    print(largest)