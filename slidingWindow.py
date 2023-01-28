"""
Learning to implement the sliding 
window algorithim to help retreive 
training sentence data instead of
just word data
"""

"""
Given an array as input, extract the pair of contiguous integers 
that have the highest sum of all pairs. Return the pair as an array.
"""

sampleArr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]
fixedPointer, slidingPointer = 0,1 

max_sum = 0
outputArr = []

for i in range(len(sampleArr)-1):
    current_sum = sampleArr[fixedPointer] + sampleArr[slidingPointer]
    if current_sum > max_sum:
        max_sum = current_sum
        outputArr = [sampleArr[fixedPointer], sampleArr[slidingPointer]]

        fixedPointer = slidingPointer
        slidingPointer = slidingPointer+1
    else:
        fixedPointer = slidingPointer
        slidingPointer = slidingPointer+1

print(outputArr)