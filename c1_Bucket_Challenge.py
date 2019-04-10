
#        KHOA NGO
#   1. BUCKET CHALLENGE

def buckets_fill(bucket_sizes, target):
    bucket_sizes.sort()
    # Please first refer to the comments in single_check and multiple_check below to see how the functions work.
    bucket_list = multiple_check(bucket_sizes, target)
    # If the current sorted order of bucket_sizes yield a valid filling combinations, then fillable = True.
    # Otherwise, reverse order then try again.
    if sum(bucket_list) == target:
        fillable = True
        print('Target of %d can be filled (example: %s).' % (target, bucket_list))
    else:
        bucket_sizes.reverse()
        if sum(multiple_check(bucket_sizes, target)) == target:
            bucket_list = multiple_check(bucket_sizes, target)
        else:
            fillable = False
            print('Target of %d cannot be filled with only sizes %s available.' % (target, bucket_sizes))
    return fillable

def single_check(bucket, target):
    # Check if the specified bucket size can fill the target (remainder = 0), if so append it to a list.
    # Note that this is only for a single bucket size. This function will be used in multiple_check.
    temp_bucket_list = []
    if target % bucket == 0:
        for i in range(target // bucket):
            temp_bucket_list.append(bucket)
    return temp_bucket_list

def multiple_check(bucket_sizes, target):
    # Check if different combinations of buckets can fill the target.
    # First, perform a single_check(bucket, target) for cases when one bucket size can fill all.
    # If it doesn't work, perform the following:
    # STEP 1:   Subtract the current bucket size from the target, then append it to temp list.
    # STEP 2:   Check if any combinations of the remaining bucket sizes work by recalling the same function.
    #           If it works, then exit loop.
    #           If subtracting once doesn't work, keep subtracting again.
    #           If STEP 1:2 doesn't work, reset the target to the original value
    #           and move on to subtracting the next bucket size from the new target.
    #           Repeat STEP 1:2 until we run out of bucket sizes to try.
    # STEP 3:   If nothing works, empty list. This is necessary because we will be calling the same function inside the function.
    original_target = target
    temp_bucket_list = []

    for i in range(len(bucket_sizes)):
        target = original_target
        temp_bucket_list.extend(single_check(bucket_sizes[i], target)) # for cases when one bucket size can fill all.
        if sum(temp_bucket_list) != original_target:
            while target - bucket_sizes[i] > 0 and sum(temp_bucket_list) != original_target:
                target -= bucket_sizes[i]  # STEP 1
                temp_bucket_list.append(bucket_sizes[i])
                for next_index in range(i + 1, len(bucket_sizes)):  # STEP 2
                    temp_bucket_list.extend(multiple_check(bucket_sizes[next_index:], target))
                    if sum(temp_bucket_list) == original_target:
                        return temp_bucket_list
        else:
            return temp_bucket_list

    temp_bucket_list = []  # STEP 3
    return temp_bucket_list

print(buckets_fill([3, 7], 33))
print(buckets_fill([6, 3, 7], 17))
print(buckets_fill([6, 7], 19))
print(buckets_fill([6, 3, 7, 10, 3, 11], 22))
print(buckets_fill([4, 6, 7, 9], 26))
print(buckets_fill([55, 35, 54, 19, 9, 6, 5, 2, 9], 379))
print(buckets_fill([5, 3, 7], 4))

# REMARKS:  As instructed, function buckets_fill(bucket_sizes, target) returns boolean value
#           (e.g.: print(buckets_fill([5, 7], 33)) outputs True).
#           I tried to incorporate a way of showing sample combination so code is messy.
#           Please don't get heart attack.
#           Cases not considered: zero, negative, non-integers numbers.
